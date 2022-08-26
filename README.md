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

- PaddleOCR R&D team would like to share the key points of PP-OCRv2, at 20:15 pm on September 8th, [Live Address](https://live.bilibili.com/21689802).
- 2021.9.7 release PaddleOCR v2.3, [PP-OCRv2](#PP-OCRv2) is proposed. The inference speed of PP-OCRv2 is 220% higher than that of PP-OCR server in CPU device. The F-score of PP-OCRv2 is 7% higher than that of PP-OCR mobile. ([arxiv paper](https://arxiv.org/abs/2109.03144))
- 2021.8.3 released PaddleOCR v2.2, add a new structured documents analysis toolkit, i.e., [PP-Structure](https://github.com/PaddlePaddle/PaddleOCR/blob/release/2.2/ppstructure/README.md), support layout analysis and table recognition (One-key to export chart images to Excel files).
- 2021.4.8 release end-to-end text recognition algorithm [PGNet](https://www.aaai.org/AAAI21Papers/AAAI-2885.WangP.pdf) which is published in AAAI 2021. Find tutorial [here](https://github.com/PaddlePaddle/PaddleOCR/blob/release/2.1/doc/doc_en/pgnet_en.md)；release multi language recognition [models](https://github.com/PaddlePaddle/PaddleOCR/blob/release/2.1/doc/doc_en/multi_languages_en.md), support more than 80 languages recognition; especically, the performance of [English recognition model](https://github.com/PaddlePaddle/PaddleOCR/blob/release/2.1/doc/doc_en/models_list_en.md#English) is Optimized.

- [more](./doc/doc_en/update_en.md)

## Features
- PP-OCR series of high-quality pre-trained models, comparable to commercial effects
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
