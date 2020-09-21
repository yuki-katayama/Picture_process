import matplotlib.pyplot as plt
import cv2
# 画像を読み込む
img = cv2.imread("test.jpg")
# 元画像を左側に表示
plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
# 画像を上下左右反転
plt.subplot(1, 2, 2)
img2 = cv2.flip(img, 0)
plt.imshow(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB))
plt.show()
