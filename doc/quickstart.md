## 1. 人脸检索软件便捷使用
人脸检索软件是一款能够进行人脸探测、人脸对比、人脸检索的软件。通过使用神经网络从一张图片中提取出人脸图片，对人脸图片进行编码，最后能在人脸库中完成人脸检索的功能。包装工具类都放在face_utils下，使用只需要调用face_utils类下的方法即可
  - FaceSearch提供了一系列测试图片，在终端中切换到相应目录
  
```
cd test_dataset/
ls
```

如果不使用提供的测试图片，可以替换为相应的测试图片路径

### 1.1 face_utils.py 详解
1.初始化方法， 指定两个模型的位置，默认值如代码中所示
```python
init(self, face_detacher_path="face_detacher.pt", face_embeddinger_path="face_embedding.pt")
```


2.用于在将人脸探测出来，保存到指定文件路径中
```python
detach(self, img, file_save_path)
```
    input: img_path -> 输入图片(PIL图片格式)
           file_path -> 保存文件路径
    output: prob -> 探测人脸的概率
<img src="./doc/img/show1.png" width="600">


3.将单张人脸进行编码，返回编码    
```python
face_embedding(self, img)
```
    imput: img -> 输入图片(PIL图片格式)
    output: embedding -> 人脸的编码向量



4.对文件夹中的图片进行编码，返回编码矩阵(一行是一张人脸编码)
```python
face_embedding_folder(self, img_folder)
```
    imput: img -> folder
    output: embeddings -> 人脸的编码向量(多张)

5.寻找最相似的人脸
```python
find_topk(self, base_embeddings, img_embedding, k=5)
```
    input: base_embeddings -> 通过face_embedding_folder得到的所有的人脸编码,
           img_embedding -> 通过face_embedding得到的单张的人脸编码,
           k -> 在base_embeddings中查找前k个相似度高人脸索引,
    output: idx_prob -> 一个字典，形式为{index :prob},
<img src="./doc/img/show2.png" width="600"><br>
<img src="./doc/img/show3.png" width="600">


6.已知id 求去重之后的人脸个数
```python
id2face_count(self, embedding_matrix)
```
    input: embedding_matrix, 通过id搜寻到的人脸，将其向量取出来得到矩阵,
    output: prob_matrix, 返回相似矩阵,
<img src="./doc/img/show4.png" width="600">
