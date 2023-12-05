import cv2

img_file='c:/Users/user/Desktop/test.jpg'
img=cv2.imread(img_file)

if img is not None:
    cv2.imshow('IMG', img)
    cv2waitKey()
    cv2.destroyAllWindows()
else:
    print('No image file')
    
