import pyautogui
from time import sleep

from name import *

KEY_UP = "up"
KEY_DOWN = "down"
KEY_LEFT = "left"
KEY_RIGHT = "right"
KEY_A = "z"
KEY_B = "x"

mode = 'kana'
x = 0
y = 0

def keyPress(key):
    pyautogui.keyDown(key)
    sleep(0.01)
    pyautogui.keyUp(key)
    sleep(0.01)

def moveCursor(dstx, dsty):
    if dstx < 0:
        dstx = 0
    elif dstx > 8:
        dstx = 8
    if dsty < 0:
        dsty = 0
    elif dsty > 6:
        dsty = 6
    global x
    global y
    if (dsty < y):
        for i in range(y - dsty):
            keyPress(KEY_UP)
    elif (dsty > y):
        for i in range(dsty - y):
            keyPress(KEY_DOWN)
    if dsty != 6:
        if (dstx < x):
            for i in range(x - dstx):
                keyPress(KEY_LEFT)
        elif (dstx > x):
            for i in range(dstx - x):
                keyPress(KEY_RIGHT)
        x = dstx
    else:
        x = 0
    y = dsty
    keyPress(KEY_A)

def inputName(name):
    for i in range(len(name)):
        KanaHira = checkKanaHira(name[i])
        if KanaHira == 'error':
            break
        if mode != KanaHira and (not name[i] in same_chars):
            moveCursor(0, 6)
            mode = KanaHira
        Pos = checkPos(name[i])
        if Pos == (-1, -1):
            break
        if Pos[0] < 9:
            moveCursor(Pos[0], Pos[1])
        else:
            if Pos[0] > 8 and Pos[0] < 12:
                moveCursor(Pos[0] - 8, Pos[1])
                if i == 4:
                    x = 8
                    y = 5
                moveCursor(4, 5)
            elif Pos[0] == 12:
                moveCursor(5, Pos[1])
                if i == 4:
                    x = 8
                    y = 5
                moveCursor(4, 5)
            elif Pos[0] == 13:
                moveCursor(5, Pos[1])
                if i == 4:
                    x = 8
                    y = 5
                moveCursor(5, 5)
    keyPress('enter')