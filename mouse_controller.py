import time
import sys
import os
from termcolor import colored

try:
    import mouse
except ImportError:
    os.system('pip install mouse')



def Mouse_MoveXY(x, y):
    mouse.move(x, y)

while True:
    print(mouse.get_position())
    time.sleep(1)
    pass
