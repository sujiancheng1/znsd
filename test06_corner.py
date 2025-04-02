import cv2

image = cv2.imread(r'C:\Users\liss\anaconda3\envs\opencv3_env\image\opencv_logo.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# 获取图像的特征点
corners = cv2.goodFeaturesToTrack(gray, 500, 0.01, 10)
for corner in corners:
    x, y = corner.ravel()
    cv2.circle(image, (int(x), int(y)), 3, (0, 0, 255), -1)
cv2.imshow('image', image)
cv2.waitKey(0)