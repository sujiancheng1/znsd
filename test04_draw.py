import cv2
# 引用numpy工具包
import numpy as np
img = np.zeros((300,300,3), np.uint8)

# 绘制线段
cv2.line(img,(100,200),(130,250),(255,255,255),2)
# 绘制矩形
cv2.rectangle(img,(30,100),(100,150),(255,255,255),2)
# 绘制园形
cv2.circle(img,(50,50),20,(0,0,255),3)
# 绘制字符串
cv2.putText(img,"hello",(150,150),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)


cv2.imshow('img',img)
cv2.waitKey(0)
#img = cv2.imread(r'C:\Users\liss\anaconda3\envs\opencv3_env\image\opencv_logo(1).png')