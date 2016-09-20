import cv2
import numpy as np
from PIL import Image, ImageGrab, ImageDraw, ImageFilter
import time


def find_templates_on_screen(template,screenshot):
    res = cv2.matchTemplate(screenshot, template, cv2.TM_SQDIFF_NORMED)
    loc = np.where(res <= 0.005)
    w, h = template.shape[1],template.shape[0]
    #print(loc)
    #print(type(loc))

    for pt in zip(*loc[::-1]):
        #print(pt)
     #   cv2.rectangle(screenshot, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)

    #cv2.imwrite('res.png', screenshot)

        return pt

#find_templates_on_screen(template=template,screenshot=screenshot)
def cards_on_screen(screenshotpath):
    """
    :param screenshotpath: path to the screenshot
    :return: the list of cards appearing on the table with their locations
    """
    values = "23456789TJQKA"
    suites = "CDHS"

    t0 = time.time()
    screenshot1 = Image.open(screenshotpath)
    screenshot = cv2.cvtColor(np.array(screenshot1), cv2.COLOR_BGR2RGB)
    cards =[]

    for i in values:
        for j in suites:

            template1 = Image.open('ps/'+i+j+".png")
            template= cv2.cvtColor(np.array(template1), cv2.COLOR_BGR2RGB)
            c = find_templates_on_screen(template=template, screenshot=screenshot)
            cards.append((i+j, c))
            #print("card: "+i+j,c)

    t1 = time.time()
    print('Cards found in %s Seconds' % (round((t1 - t0), 2)))
    #print( len(cards))
    #print(cards)

    return  [cards[a] for a in range(len(cards)) if cards[a][1] != None]


screen = "ps/screenshot w7.png"
cs = cards_on_screen(screen)

print(cs)