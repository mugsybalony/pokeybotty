
from PIL import Image
import pygame
import cv2
import pyautogui
from pytesseract import image_to_string



#img = ImageGrab.grab(bbox=(260, 222, 300, 75))
#img.save('smallscreen.png')


#img = pyautogui.screenshot(region=(359,191,100,30))
#img.save('pot.png')

print image_to_string(Image.open('pot.png'))

#img = cv2.imread("screen.png")
#crop_img = img[222:295,260:560]
#cv2.imwrite('smallscreen.png',crop_img)
#cv2.imshow('crop_img', crop_img)
#cv2.waitKey(0)






