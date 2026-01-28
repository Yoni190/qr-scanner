import cv2

cap = cv2.VideoCapture(0)
detector = cv2.QRCodeDetector()

while(True):
    ret, frame = cap.read()

    cv2.imshow("Scanner", frame)


    if cv2.waitKey(1) == ord("q"):
        break
    
cap.release()
cv2.destroyAllWindows()