import cv2
import numpy as np

def screenCompare(location):
#	hwnd = win32gui.FindWindow(None, r'Plants vs. Zombies')
#	dimensions = win32gui.GetWindowRect(hwnd)
#	im = ImageGrab.grab(dimensions)
    im = cv2.imread('big.png')
    imgSun = cv2.imread('Sun.png')

    w, h = imgSun.shape[0:2]
    #cv2.matchTemplate(im, imgSun, result, cv2.TM_CCOEFF_NORMED, 0)
    result = cv2.matchTemplate(im, imgSun, cv2.TM_CCOEFF_NORMED)
    threshold = .7
    loc = np.where(result >= threshold)
    for pt in zip(*loc[::-1]):
        cv2.rectangle(im, pt, (pt[0] + w, pt[1] + h), (0, 255, 255), 2)
        #mouseAndClick2((pt[0] + w, pt[1]+h))
    cv2.imwrite('result.png', im)

screenCompare('imgSun.png')
