import cv2

img_file='c:/Users/user/Desktop/test.jpg'
save_file='c:/Users/user/Desktop/test_gray.jpg'

img=cv2.imread(img_file, cv2.IMREAD_GRAYSCALE)

#cv2.imshow(img_file, img)
cv2.imwrite(save_file, img)
cv2.waitKey()
cv2.destroyAllWindows()
