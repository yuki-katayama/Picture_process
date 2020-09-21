import matplotlib.pyplot as plt
import cv2

# 画像を読み込む
img = cv2.imread("test.jpg")
# 画像のエッジ検出
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = cv2.Canny(img, 100, 200)

# 画像を保存する
cv2.imwrite("out.png", img)
img = 255 - img
# 画像を表示
# plt.axis("off")
plt.imshow(img, cmap="gray")
plt.show()
