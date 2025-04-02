# 导入 OpenCV 库
import cv2
# 打印版本号
print(cv2.getVersionString())
# 读取图片
img = cv2.imread(r'C:\Users\liss\anaconda3\envs\opencv3_env\image\2(1).jpg')
# 打印图片的维度
print(img.shape)
# 创建图像窗口
cv2.imshow('img',img)
# waikey函数会让窗口暂停并等待键盘输入
cv2.waitKey(0)
