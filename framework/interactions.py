import win32api, win32con
import time, logging
import coordinates

sleep_time = .1

# Button coordinate variables
TITLE_BUTTONS = coordinates.title

class interactions():

    def __init__(self):
        self.log = logging.getLogger(__name__)


    def click(button):
        win32api.SetCursorPos((button["x"],button["y"]))
        time.sleep(.1)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
        time.sleep(.1)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)


    def click_title_button(self, button_name=None):

        if button_name == None:
            self.log.error("Please provide the name of the button to click in the click_title_button function.")
        elif not button_name in TITLE_BUTTONS:
            self.log.error(f"{str(button_name)} is not a valid button on the title screen.")

        self.click(TITLE_BUTTONS[button_name])
