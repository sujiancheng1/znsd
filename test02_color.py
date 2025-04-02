# 导入 OpenCV 库
import cv2
img = cv2.imread(r'C:\Users\liss\anaconda3\envs\opencv3_env\image\opencv_logo(1).png')
cv2.imshow("blue",img[:,:,0])
cv2.imshow("green",img[:,:,1])
cv2.imshow("red",img[:,:,2])

# 颜色空间转换代码  cv2.cvtColor() 是 OpenCV 里用于颜色空间转换的函数 cv2.COLOR_BGR2GRAY：这是一个颜色空间转换代码
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("gray",gray)

cv2.waitKey(0)