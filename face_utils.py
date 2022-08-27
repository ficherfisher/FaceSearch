import os
import torch
from torchvision import utils as vutils
from PIL import Image
import numpy as np


class face_utils:

    def __init__(self):
        self.device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
        # self.device = torch.device('cpu')
        print('Running on device: {}'.format(self.device))
        workers = 0 if os.name == 'nt' else 4
        if self.device == torch.device('cpu'):
            self.face_detacher = torch.load("face_detacher_cpu.pt")
            self.face_embeddinger = torch.load("face_embedding_cpu.pt")
            self.count = 100
        else:
            self.face_detacher = torch.load("face_detacher.pt")
            self.face_embeddinger = torch.load("face_embedding.pt")
            init_gpu_memory = torch.cuda.get_device_properties(self.device).total_memory
            default_gpu_memory = 4294967295  # 默认4G显存大小
            if init_gpu_memory < default_gpu_memory:
                self.count = (init_gpu_memory // default_gpu_memory) * 500
            else:
                self.count = 100

    def get_img_file(self, file_name):
        imagelist = []
        for parent, dirnames, filenames in os.walk(file_name):
            for filename in filenames:
                if filename.lower().endswith(
                        ('.bmp', '.dib', '.png', '.jpg', '.jpeg', '.pbm', '.pgm', '.ppm', '.tif', '.tiff')):
                    imagelist.append(os.path.join(parent, filename))
            return imagelist

    def get_similar_matrix(self, v1, v2):
        num = np.dot(np.array(v1), np.array(v2).T)  # 向量点乘
        denom = np.linalg.norm(v1, axis=1).reshape(-1, 1) * np.linalg.norm(v2, axis=1)  # 求模长的乘积
        res = num / denom
        res[np.isneginf(res)] = 0
        return res

    """
    用于在将人脸探测出来，保存到指定文件路径中
    input: img_path -> 输入图片(PIL图片格式)
           file_path -> 保存文件路径
    
    output: prob -> 探测人脸的概率
    """
    def detach(self, img, file_save_path):
        x_aligned, prob = self.face_detacher(img, return_prob=True)
        if x_aligned is None:
            return 0
        vutils.save_image(x_aligned, file_save_path)
        return prob

    '''
    将单张人脸进行编码，返回编码
    imput: img -> 输入图片(PIL图片格式)
    
    output: embedding -> 人脸的编码向量
    '''
    def face_embedding(self, img):
        x_aligned = self.face_detacher(img, return_prob=False)
        aligned = torch.stack([x_aligned]).to(self.device)
        embeddings = self.face_embeddinger(aligned).detach().cpu()
        return embeddings

    '''
    对文件夹中的图片进行编码，返回编码矩阵(一行是一张人脸编码)
    imput: img -> folder
    output: embeddings -> 人脸的编码向量(多张)
    '''
    def face_embedding_folder(self, img_folder):
        all_images = self.get_img_file(img_folder)
        if len(all_images) == 0:
            print("there is not image files in the path:{}".format(img_folder))
            return
        with torch.no_grad():
            temp_aligned = []
            temp_result = np.zeros([1, 512])
            for index, i in enumerate(all_images):
                image_inf = Image.open(i)
                image_inf = image_inf.convert("RGB")
                x_aligned, prob = self.face_detacher(image_inf, return_prob=True)
                if x_aligned is None:
                    continue
                temp_aligned.append(x_aligned)
                if index % self.count == 1:
                    aligned = torch.stack(temp_aligned).to(self.device)
                    embeddings = self.face_embeddinger(aligned).detach().cpu()
                    temp_result = np.append(temp_result, embeddings.numpy(), axis=0)
                    temp_aligned.clear()
                    print("batch size:{}".format(index // self.count))
            if len(temp_aligned) != 0:
                aligned = torch.stack(temp_aligned).to(self.device)
                embeddings = self.face_embeddinger(aligned).detach().cpu()
                temp_result = np.append(temp_result, embeddings.numpy(), axis=0)
            user_embeddings = np.delete(temp_result, 0, axis=0)
        return user_embeddings

    '''
    寻找最相似的人脸
    input: base_embeddings -> 通过face_embedding_folder得到的所有的人脸编码
           img_embedding -> 通过face_embedding得到的单张的人脸编码
           k -> 在base_embeddings中查找前k个相似度高人脸索引
    output: idx_prob -> 一个字典，形式为{index :prob}
    '''
    def find_topk(self, base_embeddings, img_embedding, k=5):  # 前k个相似度
        dicts = {}
        cos_sim_matrix = self.get_similar_matrix(img_embedding, base_embeddings)
        for index, i in enumerate(cos_sim_matrix):
            sort_index = i.argsort()[-k:][::-1]
            for j in sort_index:
                dicts[j] = cos_sim_matrix[index][j]
        return dicts

    '''
    已知id 求去重之后的人脸列表和人脸个数
    input: embedding_matrix, 通过id搜寻到的人脸，将其向量取出来得到矩阵
    output: person_list count, 人脸列表，不同的人脸个数
    similar_matrix 人脸相似矩阵 
    '''
    def id2face_count(self, embedding_matrix):
        similar_matrix = self.get_similar_matrix(embedding_matrix, embedding_matrix)
        data = similar_matrix - 0.8
        data[data > 0] = 1
        data[data < 0] = 0
        list = []
        n = data.shape[0]
        person = []
        for i in range(n):
            if i in list:
                continue
            temp = []
            list.append(i)
            for j in range(n):
                if data[i][j] == 1:
                    temp.append(j)
                    list.append(j)
            person.append(temp)
            count = len(person)
        return person, count

    '''
    增加
    input: embedding_matrix 库中的人脸向量矩阵， embedding 单次需要增加的人脸向量
    output: embedding_matrix 增加了embedding的人脸向量人脸向量矩阵
    '''

    def add_person(self, embedding_matrix, embedding):
        embedding_matrix = np.append(embedding_matrix, embedding.numpy(), axis=0)
        return embedding_matrix

    '''
    删除
    input: embedding_matrix 库中的人脸向量矩阵， inx 需要删除的人脸的索引
    output: embedding_matrix 删除了inx人脸向量的人脸向量矩阵
    '''
    def delete_person(self, embedding_matrix, idx):
        embedding_matrix = np.delete(embedding_matrix, idx, axis = 0)
        return embedding_matrix


if __name__ == "__main__":
    print(torch.__version__)

    bs = face_utils()

    # 检测人脸并保存
    images = Image.open(r"./test_dataset/test_folder/QQ截图20211216205822.png")
    bs.face_detacher(images.convert("RGB"), r"./test_dataset/test_folder/cut.jpg")

    # 计算人脸相似度
    img1 = Image.open("test_dataset/4_1.png")
    img1_embedding = bs.face_embedding(img1.convert("RGB"))
    img2 = Image.open("test_dataset/4.jpg")
    img2_embedding = bs.face_embedding(img2.convert("RGB"))
    print(bs.get_similar_matrix(img1_embedding, img2_embedding)[0][0])

    # 编码文件夹中的人脸
    images_path = "test_dataset/test_folder"
    images_embedding_matrix = bs.face_embedding_folder(images_path)
    np.save("test_matrix.npy", images_embedding_matrix)

    # 查找最相似的top k个人脸
    load_matrix = np.load("test_matrix.npy")
    img3 = Image.open("test_dataset/1_1.jpg")
    img3_embedding = bs.face_embedding(img3.convert("RGB"))
    print(bs.find_topk(load_matrix, img3_embedding))

    # 已知id 求去重之后的人脸列表和人脸个数
    load_matrix = np.load("test_matrix.npy")
    face_list, count = bs.id2face_count(load_matrix)
    print(face_list)
    print(count)

    # 添加人脸，删除人脸
    load_matrix = np.load("test_matrix.npy")
    temp = bs.add_person(load_matrix, img1_embedding)
    print(temp.shape)
    temp1 = bs.delete_person(load_matrix, 0)
    print(temp1.shape)


















