import cv2
import numpy as np
gray = cv2.imread(r'C:\Users\liss\anaconda3\envs\opencv3_env\image\opencv_logo.jpg',cv2.IMREAD_GRAYSCALE)
# 阈值处理
_,binay = cv2.threshold(gray,200,255,cv2.THRESH_BINARY_INV)
# 定义一个操作
kernel = np.ones((5,5),np.uint8)
# 使用kernel腐蚀binay图像
erosion = cv2.erode(binay,kernel)
# 膨胀
dilation = cv2.dilate(binay,kernel)

cv2.imshow('binay',binay)
cv2.imshow('erosion',erosion)
cv2.imshow('dilation',dilation)
cv2.waitKey(0)