import cv2
import webbrowser

cap = cv2.VideoCapture(0)
detector = cv2.QRCodeDetector()

while(True):
    ret, frame = cap.read()

    data, bboc, _ = detector.detectAndDecode(frame)

    if data:
        a = data
        break

    cv2.imshow("Scanner", frame)


    if cv2.waitKey(1) == ord("q"):
        break
    
webbrowser.open(str(a))
cap.release()
cv2.destroyAllWindows()