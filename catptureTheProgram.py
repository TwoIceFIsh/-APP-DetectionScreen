import cv2
import mss
import numpy
import win32gui
import win32con
from tkinter import *
from tkinter import messagebox


# 목표
# 데바데 핸들을 구한다(o)
# 데바데 창 크기를 구한다
# 현재 이미지와 비교해야할 이미지를 비교한다
# 로직에 맞으면 이미지 파일 하나를 상단에 계속 띄운다


def img_always_on_top(image_path, pos_x, pos_y):

    original = cv2.imread(image_path, cv2.IMREAD_COLOR)
    cv2.namedWindow(image_path, cv2.WINDOW_NORMAL)
    cv2.setWindowProperty(image_path, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    win32gui.SetWindowPos(win32gui.FindWindow(None, image_path), win32con.HWND_TOPMOST, 0, 1080, pos_x, pos_y, win32con.SWP_SHOWWINDOW)
    cv2.resizeWindow(image_path, 500, 400)
    cv2.imshow(image_path, original)


gameName = "DeadByDaylight "
hwnd = win32gui.FindWindow(None, gameName)

if hwnd <= 0:
    messagebox.showinfo("에러", "데바데를 찾을수 없습니다.")

elif hwnd > 0:

    def button_click():
        print("button clicked")


    # create window
    app = Tk()
    app.title("방송 세팅하기")
    app.geometry('300x100+200+100')

    # make label
    label = Label(app)
    label.pack()

    # make input field
    entry = Entry(app)
    entry.bind("<Return>", button_click())
    entry.pack()

    # make buttons
    b = Button(app, text="Click on me!", width=15, command=button_click)
    b.pack(padx=10, pady=10)

    app.mainloop()

    # Capture the DBD windows size
    print('DeadByDaylight process Detected')
    img_always_on_top('sample.jpg', 0, 1080)

    with mss.mss() as sct:
        # Part of the screen to capture
        # I need to change program scale

        while 'Capturing':

            size = win32gui.GetWindowRect(hwnd)
            x = size[0]
            y = size[1]
            w = size[2] - x
            h = size[3] - y

            monitor = {'top': x, 'left': y, 'width': w, 'height': h}
            # print(monitor)
            sct.save()

            # Get raw pixels from the screen, save it to a Numpy array
            img = numpy.array(sct.grab(monitor))

            # Display the picture
            cv2.namedWindow('DeadByDaylight Recognizer', cv2.WINDOW_NORMAL)
            cv2.resizeWindow('DeadByDaylight Recognizer', 600, 400)
            # cv2.setWindowProperty("DeadByDaylight Recognizer", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
            cv2.imshow('DeadByDaylight Recognizer', img)



        # Press "q" to quit
            if cv2.waitKey(25) & 0xFF == ord('q'):
                cv2.destroyAllWindows()
                exit(1)

