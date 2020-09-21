import matplotlib.pyplot as plt
import cv2
from mosaic import mosaic as mosaic

# 画像を読み込んでモザイクをかける
img = cv2.imread("tidori.jpg")
mos = mosaic(img, (10, 10, 480, 250), 10)

# モザイクをかけた画像を出力
cv2.imwrite("tidori-mosaic.png", mos)
plt.imshow(cv2.cvtColor(mos, cv2.COLOR_BGR2RGB))
plt.show()
