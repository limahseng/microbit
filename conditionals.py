# Conditionals in micro:bit MicroPython
'''
if something is True:
    # do one thing
elif some other thing is True:
    # do another thing
else:
    # do yet another thing.
'''

from microbit import *

while True:
    if button_a.is_pressed():
        display.show(Image.HAPPY)
    elif button_b.is_pressed():
        display.show(Image.SAD)
    else:
        display.scroll("Waiting")
