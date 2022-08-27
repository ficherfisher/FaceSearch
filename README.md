English | [简体中文](README_ch.md)

<p align="center">
 <img src="./doc/img/index.jpg" align="middle" width = "600"/>
<p align="center">


------------------------------------------------------------------------------------------

<p align="left">
    <a href=""><img src="https://img.shields.io/badge/release-1.1.0-brightgreen"></a>
    <a href=""><img src="https://img.shields.io/badge/torch-1.12.1-yellowgreen"></a>
    <a href=""><img src="https://img.shields.io/badge/Pillow-9.2.0-blue"></a>
</p>

## 简介

FaceSearch旨在打造一套丰富、领先、且实用的人脸检测识别对比工具库，助力开发者训练出更好的模型，并应用落地。

**Recent updates**

- 将人脸探测出来，保存到指定文件路径中
- 将单张人脸进行编码，返回编码
- 对文件夹中的图片进行编码，返回编码矩阵(一行是一张人脸编码)
- 寻找最相似的人脸
- 已知id 求去重之后的人脸列表和人脸个数

## Features
- FaceSearch一个高质量预训练模型，准确的识别效果
    - Ultra lightweight PP-OCRv2 series models: detection (3.1M) + direction classifier (1.4M) + recognition 8.5M) = 13.0M
    - Ultra lightweight PP-OCR mobile series models: detection (3.0M) + direction classifier (1.4M) + recognition (5.0M) = 9.4M
    - General PP-OCR server series models: detection (47.1M) + direction classifier (1.4M) + recognition (94.9M) = 143.4M
    - Support Chinese, English, and digit recognition, vertical text recognition, and long text recognition
    - Support multi-language recognition: Korean, Japanese, German, French
- Rich toolkits related to the OCR areas
    - Semi-automatic data annotation tool, i.e., PPOCRLabel: support fast and efficient data annotation
    - Data synthesis tool, i.e., Style-Text: easy to synthesize a large number of images which are similar to the target scene image
- Support user-defined training, provides rich predictive inference deployment solutions
- Support PIP installation, easy to use
- Support Linux, Windows, MacOS and other systems

## Visualization

<div align="center">
    <img src="doc/imgs_results/ch_ppocr_mobile_v2.0/test_add_91.jpg" width="800">
    <img src="doc/imgs_results/multi_lang/img_01.jpg" width="800">
    <img src="doc/imgs_results/multi_lang/img_02.jpg" width="800">
</div>
  