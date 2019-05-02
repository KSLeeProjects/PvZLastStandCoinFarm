from PIL import ImageGrab
import os
import time
import win32gui
import win32con

x_pad = 0
y_pad = 0

def screenGrab():
    hwnd = win32gui.FindWindow(None, r'Plants vs. Zombies')
    win32gui.SetForegroundWindow(hwnd)
    time.sleep(1)
    dimensions = win32gui.GetWindowRect(hwnd)
    box = ()
    im = ImageGrab.grab(dimensions)
    im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) + '.png', 'PNG')
    win32gui.MoveWindow(hwnd, 0, 0, 806, 629, 1)

def main():
    screenGrab()

if __name__ == '__main__':
    main()
