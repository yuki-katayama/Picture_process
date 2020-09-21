# 画像のダウンロード
import cv2
import urllib.request as req

pic = ["https://s3-ap-northeast-1.amazonaws.com/cdn2.kurashi-no.jp/production/posts/eyecatches/000/014/457/original.jpg",
       "https://1.bp.blogspot.com/-4FM2qztrDbw/UYzcLgHuO3I/AAAAAAAAR8c/YirUuv-UxB0/s800/ski_man.png"]

for i, a in enumerate(pic):
    req.urlretrieve(a, "test" + str(i) + ".png")
    # OpenCVで読み込む
    img = cv2.imread("test" + str(i) + ".png")
    print(img)
