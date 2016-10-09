import os
import pyscreenshot as ImageGrab

img = ImageGrab.grab(bbox=(0,0,792,590))

print(type(img))
