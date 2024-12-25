# Klasifikasi Tuberkulosis Menggunakan ResNet dan MobileNet pada Gambar Sinar-X Dada
-------------
Project ini bertujuan untuk mengembangkan model deep learning yang dapat secara otomatis mengklasifikasikan citra sinar-X dada untuk mendeteksi Tuberkulosis (TB). Model ini diharapkan dapat membantu tenaga medis dalam mendiagnosis TB secara lebih cepat dan akurat.

Project ini menggunakan dataset gambar sinar-X dada yang terdiri dari dua kelas: "Normal" dan "Tuberkulosis". Dataset tersebut dibagi menjadi set pelatihan, validasi, dan pengujian. Augmentasi data digunakan untuk meningkatkan ukuran dan variasi dataset pelatihan. Link dataset https://www.kaggle.com/datasets/tawsifurrahman/tuberculosis-tb-chest-xray-dataset/data

Dua model deep learning yang populer, ResNet dan MobileNet, digunakan dalam project ini. Model-model ini dilatih menggunakan dataset pelatihan dan dievaluasi menggunakan dataset validasi dan pengujian.

ResNet50 Architecture
![1_rPktw9-nz-dy9CFcddMBdQ.jpg](https://www.dropbox.com/scl/fi/obzvb51j8ng6sh67ysvpg/1_rPktw9-nz-dy9CFcddMBdQ.jpg?rlkey=ywu6l4u7lemisvktdop1wss6n&dl=0&raw=1)

MobileNetV2 Architecture
![The-proposed-MobileNetV2-network-architecture.png](https://www.dropbox.com/scl/fi/rxkkfspzpbb862h3jsd59/The-proposed-MobileNetV2-network-architecture.png?rlkey=y3icgqy4kz1c8wfgkau8twdyk&dl=0&raw=1)

## Overview Dataset
------
Dataset yang digunakan dalam project ini terdiri dari gambar sinar-X dada berlabel "Normal" dan "Tuberkulosis" yang bersumber dari direktori terpisah dan dilengkapi metadata dalam file Excel. Dataset dibagi menjadi set pelatihan (80%), validasi, dan pengujian (20%), dengan augmentasi data diterapkan pada set pelatihan menggunakan transformasi seperti RandomHorizontalFlip, RandomRotation, dan ColorJitter untuk meningkatkan kinerja model.

## Preprocessing & Modelling
---

##### Preprocessing
Preprocessing dilakukan 3 tahap yaitu
- Train Test validation sets prep
- randomizing the data
- Creating image augmentation

##### Modeling
###### RestNet50
![Screenshot 2024-12-25 210959.png](https://www.dropbox.com/scl/fi/n4u4u84j3e1bs1hj5drgh/Screenshot-2024-12-25-210959.png?rlkey=advrf22e43nqm3y4242jmcuf0&dl=0&raw=1)

###### MobileNetV2
![Screenshot 2024-12-25 172439.png](https://www.dropbox.com/scl/fi/8kxbm458juhw9keglxotd/Screenshot-2024-12-25-172439.png?rlkey=c9sjmo77umruoimoxa1jfe06f&dl=0&raw=1)

###### ROC Curve Comparison Betweeen RestNet50 vs MobileNetV2
![Screenshot 2024-12-25 172547.png](https://www.dropbox.com/scl/fi/fww5jw8irdgw1gecx84ql/Screenshot-2024-12-25-172547.png?rlkey=nyfyna79n1wh4lg67xnhyemzv&dl=0&raw=1)

## Local Web Deployement
---
##### Tampilan Awal
![Screenshot 2024-12-25 201142.png](https://www.dropbox.com/scl/fi/q7vlz89p6o131oj1kzpxn/Screenshot-2024-12-25-201142.png?rlkey=cnlglhjvmuqipb5nctf3s2hf2&dl=0&raw=1)

##### Tampilan Setelah Upload Image dan Prediksi Result
![Screenshot 2024-12-25 201510.png](https://www.dropbox.com/scl/fi/6l4jk3aj8rcbgzixbj7tj/Screenshot-2024-12-25-201510.png?rlkey=ilwoxj7e76itzmykvhlc6pixh&dl=0&raw=1)

# Author
---
Muhammad Abdi Harliansyah

