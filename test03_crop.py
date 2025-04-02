import cv2
img = cv2.imread(r'C:\Users\liss\anaconda3\envs\opencv3_env\image\opencv_logo(1).png')
# 用索引取出图像的一部分
crop=img[10:300,40:250]
cv2.imshow('crop',crop)
cv2.waitKey(0)