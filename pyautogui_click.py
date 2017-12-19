from pyautogui import position
import time
from random import randint
from random import random

upperLeft = list(position())
lowerRight = list(position())

while True:
    pauseMax = randint(90,110)
    pauseTime = randint(8,12)
    for item in range(0,pauseMax):
        r = random()
        x = randint(upperLeft[0],lowerRight[0])
        y = randint(upperLeft[1],lowerRight[1])
        pag.click(x,y)
        time.sleep(r)
    time.sleep(pauseTime)
