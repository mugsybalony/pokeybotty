
from PIL import Image
import pygame
import cv2
import pyautogui


def init_window():
    global screen, background_colour

    pygame.init()
    (width, height) = (10, 10)
    background_colour = (200, 200, 255)

    screen = pygame.display.set_mode((width, height))
    screen.fill(background_colour)
    pygame.display.flip()
    pygame.display.set_caption('PokeyBotty')

    global running
    running = True
    global x
    x=1

init_window()

#img = ImageGrab.grab(bbox=(260, 222, 300, 75))
#img.save('smallscreen.png')


img = pyautogui.screenshot(region=(260,219,275,75))
img.save('smallscreen.png')
#img = cv2.imread("screen.png")
#crop_img = img[222:295,260:560]
#cv2.imwrite('smallscreen.png',crop_img)
#cv2.imshow('crop_img', crop_img)
#cv2.waitKey(0)






