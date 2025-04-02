import cv2
import numpy as np

# 把扑克牌的菱形找出来
image = cv2.imread(r'C:\Users\liss\anaconda3\envs\opencv3_env\image\poker.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
template = gray[75:105,235:265]
match = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF_NORMED)
locations = np.where(match>0.8)

w, h = template.shape[::-1]
for p in zip(*locations[::-1]):
    x1,y1 = p[0], p[1]
    x2,y2 = x1 + w, y1 + h
    cv2.rectangle(image, (x1, y1), (x2, y2), (0,255,0), 2)
cv2.imshow('image', image)
cv2.waitKey(0)