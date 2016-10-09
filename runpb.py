import time
import pygame
import os
import cv2


def find_stuff():
    no_players = 0
    hand = []
    """
    os.system("screencapture screen.png")
    cardpath = 'ps/backofcards2.png'

    screenshot1 = Image.open(screen)
    screenshot = cv2.cvtColor(np.array(screenshot1), cv2.COLOR_BGR2RGB)

    card = Image.open(cardpath)
    coveredcard = cv2.cvtColor(np.array(card), cv2.COLOR_BGR2RGB)

    """
    return no_players, hand


def update_gui(prob):
    #screen.fill(background_colour) #use this if you need to wipe the whole background
    font = pygame.font.Font(None,36)


    text1 = font.render("Number of players %s" %x, 1, (0,0,0),(255,255,255))
    textpos = text1.get_rect()
    screen.blit(text1,textpos)

    text2 = font.render("My cards %s" % x, 1, (50, 50, 50),(255,255,255))
    textpos = text2.get_rect()
    screen.blit(text2, (0,font.get_height()))

    text3 = font.render("Probability of winning is: %s" % x, 1, (50, 50, 50), (255, 255, 255))
    textpos = text3.get_rect()
    screen.blit(text3, (0, font.get_height()*2))

    pygame.display.flip()


def calc_odds():
    odds = 0
    return odds

def init_window():
    global screen, background_colour

    pygame.init()
    (width, height) = (350, 200)
    background_colour = (200, 200, 255)

    screen = pygame.display.set_mode((width, height))
    screen.fill(background_colour)
    pygame.display.flip()
    pygame.display.set_caption('PokeyBotty')

    global running
    running = True
    global x
    x=1



#initialise the window for rendering output
init_window()

while running:
    #event handling section of the while loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    time.sleep(0.3)
    x+=1
    no_players, hand = find_stuff()
    prob = calc_odds()
    update_gui(prob)

    print 'looped'


