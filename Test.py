import win32gui


def callback(hwnd, extra):
    rect = win32gui.GetWindowRect("DeadByDaylight ")
    x = rect[0]
    y = rect[1]
    w = rect[2] - x
    h = rect[3] - y
    print("Window %s:" % win32gui.GetWindowText(hwnd))
    print("\Location: (%d, %d)" % (x, y))
    print("\    Size: (%d, %d)" % (w, h))


def main():
    win32gui.EnumWindows(callback, None)


if __name__ == '__main__':
    main()
