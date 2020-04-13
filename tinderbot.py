#!/usr/bin/env python3
import time
from pynput.keyboard import Key, Controller

keyboard = Controller()
with keyboard.pressed(Key.cmd):
        keyboard.press(Key.space)
        keyboard.release(Key.space)
time.sleep(0.3)
keyboard.type('terminal')
time.sleep(0.3)
keyboard.press(Key.enter)
keyboard.release(Key.enter)
time.sleep(0.3)
keyboard.type('open http://www.tinder.com')
time.sleep(0.3)
keyboard.press(Key.enter)
keyboard.release(Key.enter)

time.sleep(3)

for i in range(0,200):
    time.sleep(1)
    keyboard.press(Key.right)
    keyboard.release(Key.right)


