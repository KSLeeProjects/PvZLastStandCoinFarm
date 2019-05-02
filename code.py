from PIL import ImageGrab
import keyboard
import os
import time
import win32gui
import win32con
import win32api
import pyls
import time
import msvcrt
import cv2
import numpy as np
from sys import exit
endOfGame = False;
def checkAndPlace():
	endOfFlag = False;
	endOfGame = False;
	GarlicBoi = (425, 66)
	Pumpkin = (475, 66)
	Continue = (399, 603)

	while (not endOfGame):
		if (not endOfFlag):
			check(GarlicBoi, (643, 241))
			time.sleep(0.1)
			check(GarlicBoi, (719, 241))
			time.sleep(0.1)
			check(GarlicBoi, (643, 501))
			time.sleep(0.1)
			check(GarlicBoi, (719, 501))
			time.sleep(0.1)
			check(Pumpkin, (325, 159))
			time.sleep(0.1)
			check(Pumpkin, (325, 582))
			time.sleep(0.1)
			mouseandClick3(Continue)
			time.sleep(0.1)
			screenCompare('Sun.png')

	time.sleep(10)
	startGame()

def check(first, second):
	mousePos(first)
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
	time.sleep(0.01)
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
	mousePos(second)
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
	time.sleep(0.01)
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
	win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0)
	time.sleep(0.01)
	win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0)

def leftclick():
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
	time.sleep(0.01)
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
	print ("Click")

def leftDown():
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
	time.sleep(0.1)

def leftUp():
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
	time.sleep(0.1)

def mousePos(cord):
	win32api.SetCursorPos(cord)

def get_cords():
	x, y = win32api.GetCursorPos()
	x = x - x_pad
	y = y - y_pad
	print (x, y)


x_pad = 0
y_pad = 0

def screenGrab():
	hwnd = win32gui.FindWindow(None, r'Plants vs. Zombies')
	win32gui.SetForegroundWindow(hwnd)
	time.sleep(1)
	dimensions = win32gui.GetWindowRect(hwnd)
	box = ()
	im = ImageGrab.grab(dimensions)
	win32gui.MoveWindow(hwnd, 0, 0, 806, 629, 1)

def screenCompare(location):
	hwnd = win32gui.FindWindow(None, r'Plants vs. Zombies')
	dimensions = win32gui.GetWindowRect(hwnd)
	im = ImageGrab.grab(dimensions)
	im.save('Kamehama.png')
	im = cv2.imread('Kamehama.png')
	imgSun = cv2.imread('Sun.png')
	w, h = imgSun.shape[0:2]
	#cv2.matchTemplate(im, imgSun, result, cv2.TM_CCOEFF_NORMED, 0)
	result = cv2.matchTemplate(im, imgSun, cv2.TM_CCOEFF_NORMED)
	threshold = .5
	loc = np.where(result >= threshold)
	count = 0
	for pt in zip(*loc[::-1]):
		if count%2==0:
		#cv2.rectangle(im, pt, (pt[0] + w, pt[1] + h), (0, 255, 255), 2)
			mouseAndClick2((pt[0] + w, pt[1]+h-10))
		count+=1
		#cv2.imwrite('result.png', im)
	imgSun = cv2.imread('SunB.png')
	w, h = imgSun.shape[0:2]
	result = cv2.matchTemplate(im, imgSun, cv2.TM_CCOEFF_NORMED)
	threshold = .5
	loc = np.where(result >= threshold)
	for pt in zip(*loc[::-1]):
		mouseAndClick2((pt[0] + w, pt[1]+h-10))
	imgSun = cv2.imread('Moneybag.png')
	w, h = imgSun.shape[0:2]
	result = cv2.matchTemplate(im, imgSun, cv2.TM_CCOEFF_NORMED)
	threshold = .75
	loc = np.where(result >= threshold)
	for pt in zip(*loc[::-1]):
		endOfGame = True;
		endOfFlag = True;
		mouseAndClick2((pt[0] + w, pt[1]+h))

def getPlantCood():
	Marigold = (376, 458)
	Lilypad = (46, 324)
	FumeShroom = (156, 259)
	GloomShroom = (171, 522)
	MagnetShroom = (421, 402)
	GoldMagnet = (315, 536)
	GarlicBoi = (257, 463)
	Pumpkin = (373, 397)
	CoffeeBean = (205, 457)
	StartButton = (283, 592)

	mouseAndClick2(Marigold)
	mouseAndClick2(Lilypad)
	mouseAndClick2(FumeShroom)
	mouseAndClick2(GloomShroom)
	mouseAndClick2(MagnetShroom)
	mouseAndClick2(GoldMagnet)
	mouseAndClick2(GarlicBoi)
	mouseAndClick2(Pumpkin)
	mouseAndClick2(CoffeeBean)
	mouseandClick3(StartButton)
	time.sleep(5)

def placePlants():
	Marigold = (118, 66)
	Lilypad = (173, 67)
	FumeShroom = (221, 66)
	GloomShroom = (275, 66)
	MagnetShroom = (325, 66)
	GoldMagnet = (375, 66)
	GarlicBoi = (425, 66)
	Pumpkin = (475, 66)
	CoffeeBean = (525, 66)

	Continue = (402, 608)

	xarr = [83, 158, 238, 325, 397, 485, 564, 643, 719]
	yarr = [159, 241, 341, 426, 501, 582]

	mouseAndClick2(Marigold)
	mouseAndClick2((xarr[0], yarr[0]))
	mouseAndClick2(Marigold)
	mouseAndClick2((xarr[1], yarr[0]))
	mouseAndClick2(Marigold)
	mouseAndClick2((xarr[2], yarr[0]))
	mouseAndClick2(Marigold)
	mouseAndClick2((xarr[3], yarr[0]))
	mouseAndClick2(Pumpkin)
	mouseAndClick2((xarr[3], yarr[0]))
	mouseAndClick2(Marigold)
	mouseAndClick2((xarr[0], yarr[1]))
	mouseAndClick2(Marigold)
	mouseAndClick2((xarr[1], yarr[1]))
	mouseAndClick2(Marigold)
	mouseAndClick2((xarr[2], yarr[1]))
	mouseAndClick2(MagnetShroom)
	mouseAndClick2((xarr[3], yarr[1]))
	mouseAndClick2(GoldMagnet)
	mouseAndClick2((xarr[3], yarr[1]))

	mouseAndClick2(Marigold)
	mouseAndClick2((xarr[0], yarr[4]))
	mouseAndClick2(Marigold)
	mouseAndClick2((xarr[1], yarr[4]))
	mouseAndClick2(Marigold)
	mouseAndClick2((xarr[2], yarr[4]))
	mouseAndClick2(MagnetShroom)
	mouseAndClick2((xarr[3], yarr[4]))
	mouseAndClick2(GoldMagnet)
	mouseAndClick2((xarr[3], yarr[4]))
	mouseAndClick2(Marigold)
	mouseAndClick2((xarr[0], yarr[5]))
	mouseAndClick2(Marigold)
	mouseAndClick2((xarr[1], yarr[5]))
	mouseAndClick2(Marigold)
	mouseAndClick2((xarr[2], yarr[5]))
	mouseAndClick2(Marigold)
	mouseAndClick2((xarr[3], yarr[5]))
	mouseAndClick2(Pumpkin)
	mouseAndClick2((xarr[3], yarr[5]))

	mouseAndClick2(Lilypad)
	mouseAndClick2((xarr[0], yarr[2]))
	mouseAndClick2(Lilypad)
	mouseAndClick2((xarr[1], yarr[2]))
	mouseAndClick2(Lilypad)
	mouseAndClick2((xarr[2], yarr[2]))
	mouseAndClick2(Lilypad)
	mouseAndClick2((xarr[3], yarr[2]))
	mouseAndClick2(Lilypad)
	mouseAndClick2((xarr[4], yarr[2]))

	mouseAndClick2(Lilypad)
	mouseAndClick2((xarr[0], yarr[3]))
	mouseAndClick2(Lilypad)
	mouseAndClick2((xarr[1], yarr[3]))
	mouseAndClick2(Lilypad)
	mouseAndClick2((xarr[2], yarr[3]))
	mouseAndClick2(Lilypad)
	mouseAndClick2((xarr[3], yarr[3]))
	mouseAndClick2(Lilypad)
	mouseAndClick2((xarr[4], yarr[3]))

	mouseAndClick2(Marigold)
	mouseAndClick2((xarr[0], yarr[2]))
	mouseAndClick2(Marigold)
	mouseAndClick2((xarr[1], yarr[2]))
	mouseAndClick2(Marigold)
	mouseAndClick2((xarr[2], yarr[2]))
	mouseAndClick2(Marigold)
	mouseAndClick2((xarr[3], yarr[2]))
	mouseAndClick2(Pumpkin)
	mouseAndClick2((xarr[3], yarr[2]))
	mouseAndClick2(GarlicBoi)
	mouseAndClick2((xarr[4], yarr[2]))

	mouseAndClick2(Marigold)
	mouseAndClick2((xarr[0], yarr[3]))
	mouseAndClick2(Marigold)
	mouseAndClick2((xarr[1], yarr[3]))
	mouseAndClick2(Marigold)
	mouseAndClick2((xarr[2], yarr[3]))
	mouseAndClick2(Marigold)
	mouseAndClick2((xarr[3], yarr[3]))
	mouseAndClick2(Pumpkin)
	mouseAndClick2((xarr[3], yarr[3]))
	mouseAndClick2(GarlicBoi)
	mouseAndClick2((xarr[4], yarr[3]))

	mouseAndClick2(FumeShroom)
	mouseAndClick2((xarr[4], yarr[1]))
	mouseAndClick2(GloomShroom)
	mouseAndClick2((xarr[4], yarr[1]))
	mouseAndClick2(CoffeeBean)
	mouseAndClick2((xarr[4], yarr[1]))

	mouseAndClick2(FumeShroom)
	mouseAndClick2((xarr[5], yarr[1]))
	mouseAndClick2(GloomShroom)
	mouseAndClick2((xarr[5], yarr[1]))
	mouseAndClick2(CoffeeBean)
	mouseAndClick2((xarr[5], yarr[1]))

	mouseAndClick2(FumeShroom)
	mouseAndClick2((xarr[6], yarr[1]))
	mouseAndClick2(GloomShroom)
	mouseAndClick2((xarr[6], yarr[1]))
	mouseAndClick2(CoffeeBean)
	mouseAndClick2((xarr[6], yarr[1]))
	mouseAndClick2(Pumpkin)
	mouseAndClick2((xarr[6], yarr[1]))

	mouseAndClick2(GarlicBoi)
	mouseAndClick2((xarr[7], yarr[1]))
	mouseAndClick2(GarlicBoi)
	mouseAndClick2((xarr[8], yarr[1]))

	mouseAndClick2(FumeShroom)
	mouseAndClick2((xarr[4], yarr[4]))
	mouseAndClick2(GloomShroom)
	mouseAndClick2((xarr[4], yarr[4]))
	mouseAndClick2(CoffeeBean)
	mouseAndClick2((xarr[4], yarr[4]))

	mouseAndClick2(FumeShroom)
	mouseAndClick2((xarr[5], yarr[4]))
	mouseAndClick2(GloomShroom)
	mouseAndClick2((xarr[5], yarr[4]))
	mouseAndClick2(CoffeeBean)
	mouseAndClick2((xarr[5], yarr[4]))

	mouseAndClick2(FumeShroom)
	mouseAndClick2((xarr[6], yarr[4]))
	mouseAndClick2(GloomShroom)
	mouseAndClick2((xarr[6], yarr[4]))
	mouseAndClick2(CoffeeBean)
	mouseAndClick2((xarr[6], yarr[4]))
	mouseAndClick2(Pumpkin)
	mouseAndClick2((xarr[6], yarr[4]))

	mouseAndClick2(GarlicBoi)
	mouseAndClick2((xarr[7], yarr[4]))
	mouseAndClick2(GarlicBoi)
	mouseAndClick2((xarr[8], yarr[4]))

	mouseandClick3(Continue)
	checkAndPlace()

def mouseAndClick(x, y):
	mousePos((x, y))
	leftclick()

def mouseAndClick2(x):
	mousePos(x)
	leftclick()

def mouseandClick3(x):
	mousePos(x)
	time.sleep(0.5)
	leftclick()
	leftclick()
	leftclick()

def startGame():
	time.sleep(0.5)
	mouseAndClick(107, 528)
	time.sleep(5)
	getPlantCood()
	placePlants()


def main():
	screenGrab()

def killer():
	os._exit(1)

keyboard.add_hotkey('esc', killer)

if __name__ == '__main__':
	screenGrab()
	time.sleep(0.5)
	mouseAndClick(577, 274)
	startGame()
