import cv2
i=0

cap = cv2.VideoCapture(0)
while True:
    ret, frame=cap.read()
    if ret :
        cv2.imshow('camera', frame)
        if cv2.waitKey(1) != -1:
            cv2.imwrite('photo%d.jpg' %i, frame)
            i=i+1

    else:
        print("no frame")
        break

cap.release()
cv2.destroyAllWindows()
