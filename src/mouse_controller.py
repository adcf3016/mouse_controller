import time
import sys
import os
import mouse
from termcolor import colored


def getMousePosition():
    return mouse.get_position()


while True:
    print(mouse.get_position())
    time.sleep(1)
    pass
