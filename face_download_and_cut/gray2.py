import matplotlib.pyplot as plt
import cv2

# 画像を読み込む
img = cv2.imread("test.jpg")
# 色空間をグレイスケールに変換
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 閾値を指定する
th = 90
img[img > th] = 255
img[img < th] = 0
# 画像を表示
plt.imshow(img, cmap="gray")
plt.show()
