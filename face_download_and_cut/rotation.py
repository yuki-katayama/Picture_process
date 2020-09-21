import matplotlib.pyplot as plt
import cv2
# 画像を読み込む
img = cv2.imread("test.jpg")
# 画像サイズの取得
h, w, colors = img.shape
size = (w, h)
# 画像の中心位置を取得
center = (w // 2, h // 2)
print(size, center)

# 回転変換行列の取得
angle = 45
scale = 1.0
matrix = cv2.getRotationMatrix2D(center, angle, scale)
# アフィン変換
img2 = cv2.warpAffine(img, matrix, size)

# 元画像を左側に表示
plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
# 回転画像を右側に表示
plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB))
plt.show()
