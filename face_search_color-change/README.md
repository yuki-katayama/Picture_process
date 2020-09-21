# 日本語
## 初めに
これは、モザイク加工や、顔を認識するチュートリアルのようなものです。

### 用意する物
1. 正面を向いた人の顔の写真

2. 顔の認識モデル
 + ここからダウンロードした物を使用する。
https://github.com/opencv/opencv/tree/master/data/haarcascades

 + 今回は、正面を向いた顔を判定するモデル(haarcascade_frontalface_alt.xml）をダウンロード   
>*用途に合わせたモデルをダウンロードして使用しても良い*


### face-detect.py
顔を認識した箇所を四角で囲む

### mosaic-test.py
mosaic.pyにモザイク処理の関数を用意しているのでそれを使用し、mosaic-test.pyでモザイクをかける箇所を指定する。

### face-mosaic.py
顔と認識した箇所をモザイク処理を行う

### rotate-test.py
haarcascade_front_alt.xmlモデルがどれだけ正面画像を認識できるかを、角度を変えてテストする。

# English
## Introduction.
This is like a mosaic or face recognition tutorial.

### What you'll need.
1. a picture of a person's face facing the front

2. face recognition model
 + download from here.
https://github.com/opencv/opencv/tree/master/data/haarcascades ...

 + Download the model (harcascade_frontalface_alt.xml) to determine the frontal face this time.   
>* You can download and use the model that suits your needs*.


### face-detect.py
Encloses a square around the recognized face

### mosaic-test.py
You can use mosaic.py to create mosaic functions, and then use mosaic-test.py to specify where to place the mosaic.

### face-mosaic.py
mosaic test.py will mosaic the area recognized as a face

### rotor-test.py
Test how well the haarcascade_front_alt.xml model recognizes the frontal image by changing the angle.

