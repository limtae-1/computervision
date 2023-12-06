import cv2
import numpy as np

img = np.full((500,500,3), 255, dtype=np.uint8)
cv2.imwrite('C:/Users/user/Desktop/blank_500.jpg',img)

img=cv2.imread('C:/Users/user/Desktop/blank_500.jpg')


#cv2.rectangle(img, start, end, color, thickness, lineType)
#img:그림 그릴 대상 이미지
#start:사각형 시작 꼭지점(x,y)
#end: 사각형 긑 꼭짓점(x,y)
#color: 색상(BGR)
#thickness: 선 두께 => -1을 하면 면을 채우기
#LineType: 선타입

cv2.rectangle(img, (50,50), (150,150), (255,0,0))
cv2.rectangle(img, (300,300), (100,100), (0,255,0), 10)
cv2.rectangle(img, (450,200), (200,450), (0,0,255), -1)

cv2.imshow('recktangle', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
