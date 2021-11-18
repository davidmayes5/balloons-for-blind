import win32api, win32con
import time

sleep_time = .1


def click(coordinate):
    win32api.SetCursorPos((coordinate["x"],coordinate["y"]))
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)