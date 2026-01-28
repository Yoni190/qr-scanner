import cv2
import webbrowser
import numpy as np
import win32gui, win32con

cap = cv2.VideoCapture(0)
detector = cv2.QRCodeDetector()
bg = np.full((512, 512, 3), (0,0,0), np.uint8)

while(True):
    ret, frame = cap.read()

    data, bboc, _ = detector.detectAndDecode(frame)

    if data:
        a = str(data)
        break

    cv2.imshow("Scanner", frame)
    hwnd = win32gui.FindWindow(None, "Scanner")
    icon_path = 'images/qr.ico'
    win32gui.SendMessage(hwnd, win32con.WM_SETICON, win32con.ICON_BIG, win32gui.LoadImage(None, icon_path, win32con.IMAGE_ICON, 0, 0, win32con.LR_LOADFROMFILE | win32con.LR_DEFAULTSIZE))


    if cv2.waitKey(1) == ord("q"):
        break
    
if data:
    webbrowser.open(a)
cap.release()
cv2.destroyAllWindows()