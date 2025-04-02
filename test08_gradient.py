import cv2

gray = cv2.imread(r'C:\Users\liss\anaconda3\envs\opencv3_env\image\opencv_logo.jpg',cv2.IMREAD_GRAYSCALE)

loplaction = cv2.Laplacian(gray,cv2.CV_64F)
canny = cv2.Canny(gray,100,200)

cv2.imshow('gray',gray)
cv2.imshow('loplaction',loplaction)
cv2.imshow('canny',canny)

cv2.waitKey(0)