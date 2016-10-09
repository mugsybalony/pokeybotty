import time
import cv2


def find_stuff():
    no_players = 0
    hand = []

    return no_players, hand


def update_gui(prob):
    pass

def calc_odds():
    odds = 0
    return odds



while True:
    time.sleep(0.5)
    no_players, hand = find_stuff()
    prob = calc_odds()
    update_gui(prob)
    print 'looped'


