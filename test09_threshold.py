import cv2

gray = cv2.imread(r'C:\Users\liss\anaconda3\envs\opencv3_env\image\bookpage.jpg',cv2.IMREAD_GRAYSCALE)
# 定义一个固定阈值，阈值为10，最大灰度255
ret,thresh = cv2.threshold(gray,10,255,cv2.THRESH_BINARY)
# 自适应阈值算法
thresh_adaptive = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,115,1)
# 常用的阈值算法
#ret2_adaptive_otsu = cv2.threshold(gray,0,255,cv2.THRESH_BINARY + cv2.THRESH_OTSU)
_, ret2_adaptive_otsu = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

cv2.imshow('adaptive_otsu', ret2_adaptive_otsu)
cv2.imshow('gray',gray)
cv2.imshow('thresh',thresh)
cv2.imshow('adaptive',thresh_adaptive)
cv2.imshow('adaptive_otsu', ret2_adaptive_otsu)
cv2.waitKey(0)