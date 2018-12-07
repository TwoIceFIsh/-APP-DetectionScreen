import cv2
import mss
import numpy
import win32gui
import win32con
import os
from tkinter import *
from tkinter import messagebox


# 목표
# 데바데 핸들을 구한다(o)
# 데바데 창 크기를 구한다(0)
# 현재 이미지와 비교해야할 이미지를 비교한다
# 로직에 맞으면 이미지 파일 하나를 상단에 계속 띄운다(0)

count = 0


def img_always_on_top(image_path, pos_x, pos_y, image_size_x, image_size_y):
    original = cv2.imread(image_path, cv2.IMREAD_COLOR)

    cv2.namedWindow(image_path)
    cv2.moveWindow(image_path, pos_x, pos_y)

    win32gui.SetWindowPos(win32gui.FindWindow(None, image_path), win32con.HWND_TOPMOST, pos_x, pos_y, 0, 0,
                          win32con.SWP_SHOWWINDOW)
    cv2.imshow(image_path, original)

gameName = "DeadByDaylight "
hwnd = win32gui.FindWindow(None, gameName)

if hwnd <= 0:
    messagebox.showinfo("에러", "데바데를 찾을수 없습니다.")

elif hwnd > 0:

    # button click event
    def button_click():

        if count == 1:
            exit(1)
        app.destroy()

    # create window
    app = Tk()
    app.title("데바데 커튼 v1.0   by kokonut111")
    app.geometry('500x400+200+100')
    app.resizable(False, False)

    # load file path
    label = Label(app, text="로비화면 player",  width=20, height=1, fg="black", relief="groove")
    label.pack()
    if len(os.listdir('lobby')) == 0:
        label2 = Label(app, text="파일이 없습니다", width=20, height=1, fg="red")
        count = 1
        label2.pack()
    elif len(os.listdir('lobby')) < 4:
        label2 = Label(app, text="[파일 갯수 부족 총5개]", width=150, height=1, fg="black")
        count = 1
        label2.pack()
    else:
        lobby_player = os.listdir('lobby')
        label2 = Label(app, text=os.listdir('lobby'), width=150, height=1, fg="black")
        label2.pack()
        count = 0

    label = Label(app, text="인게임화면 player", width=20, height=1, fg="black", relief="groove")
    label.pack()
    if len(os.listdir('in_game')) == 0:
        label2 = Label(app, text="파일이 없습니다", width=20, height=1, fg="red")
        label2.pack()
        count = 1
    elif len(os.listdir('in_game')) < 4:
        label2 = Label(app, text="[파일 갯수 부족 총5개]", width=150, height=1, fg="black")
        label2.pack()
        count = 1
    else:
        in_game_player = os.listdir('in_game')
        label2 = Label(app, text=os.listdir('in_game'), width=150, height=1, fg="black")
        label2.pack()
        count = 0

    label = Label(app, text="결과화면 player", width=20, height=1, fg="black", relief="groove")
    label.pack()
    if len(os.listdir('result')) == 0:
        label2 = Label(app, text="파일이 없습니다", width=20, height=1, fg="red")
        label2.pack()
        count = 1
    elif len(os.listdir('result')) < 3:
        label2 = Label(app, text="[파일 갯수 부족 총4개]", width=150, height=1, fg="black")
        label2.pack()
        count = 1
    else:
        result_player = os.listdir('result')
        label2 = Label(app, text=os.listdir('result'), width=150, height=1, fg="black")
        label2.pack()
        count = 0
    # make buttons
    b = Button(app, text="적용하기", width=15, command=button_click)
    b.pack(padx=10, pady=10)

    label22 = Label(app, text="모든 파일명은 [영문,숫자]만 가능하며 순서대로 읽어 들입니다", width=150, height=1, fg="black")
    label22.pack()
    label224 = Label(app, text="파일 총 갯수를 맞추어 주십시오 [그림파일만]", width=150, height=1, fg="black")
    label224.pack()
    label224 = Label(app, text="폴더명 변경시 작동 불가", width=150, height=1, fg="black")
    label224.pack()

    # window execution
    app.mainloop()

    # show image
    print('DeadByDaylight process Detected')

    img_always_on_top("in_game/"+in_game_player[0], 778, 243, 250, 250)

    img_always_on_top("in_game/"+in_game_player[1], 980, 221, 250, 250)

    img_always_on_top("in_game/"+in_game_player[2], 1256, 182, 250, 250)

    img_always_on_top("in_game/"+in_game_player[3], 107, 937, 250, 250)

    img_always_on_top("result/"+result_player[0], 190, 275, 150, 25)
    img_always_on_top("result/"+result_player[1], 190, 389, 250, 25)
    img_always_on_top("result/"+result_player[2], 190, 494, 250, 25)
    img_always_on_top("result/"+result_player[3], 190, 601, 250, 25)


    with mss.mss() as sct:
        while 'Capturing':

            # get window position
            size = win32gui.GetWindowRect(hwnd)
            x = size[0]
            y = size[1]
            w = size[2] - x
            h = size[3] - y
            monitor = {'top': x, 'left': y, 'width': w, 'height': h}
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

