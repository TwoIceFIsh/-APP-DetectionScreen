import cv2
import mss
import numpy
import win32gui
from tkinter import messagebox

gameName = "DeadByDaylight "

# 목표
# 데바데 핸들을 구한다(o)
# 데바데 창 크기를 구한다
# 현재 이미지와 비교해야할 이미지를 비교한다
# 로직에 맞으면 이미지 파일 하나를 상단에 계속 띄운다

window = win32gui.FindWindow(None, gameName)

if window <= 0:
    messagebox.showinfo("에러", "데바데를 찾을수 없습니다.")

elif window > 0:

    # Capture the DBD windows size
    print('DeadByDaylight process Detected')
    size = win32gui.GetWindowRect(window)
    x = size[0]
    y = size[1]
    w = size[2] - x
    h = size[3] - y

    with mss.mss() as sct:
        # Part of the screen to capture
        # I need to change program scale
        monitor = {'top': x, 'left': y, 'width': w, 'height': h}

        while 'Capturing':

            sct.save()

            # Get raw pixels from the screen, save it to a Numpy array
            img = numpy.array(sct.grab(monitor))

        # Display the picture
            cv2.namedWindow('DeadByDaylight Recognizer', cv2.WINDOW_NORMAL)
            cv2.resizeWindow('DeadByDaylight Recognizer', 600, 400)
            cv2.imshow('DeadByDaylight Recognizer', img)

        # Press "q" to quit
            if cv2.waitKey(25) & 0xFF == ord('q'):
                cv2.destroyAllWindows()
                exit(1)

