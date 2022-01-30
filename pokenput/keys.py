import pyautogui
from time import sleep

from .name import *

class keys():
    def __init__(self):
        self.KEY_UP = "up"
        self.KEY_DOWN = "down"
        self.KEY_LEFT = "left"
        self.KEY_RIGHT = "right"
        self.START = "enter"
        self.KEY_A = "z"
        self.KEY_B = "x"
        self.mode = "kana"
        self.x = 0
        self.y = 0

    def keyPress(self, key):
        pyautogui.keyDown(key)
        sleep(0.01)
        pyautogui.keyUp(key)
        sleep(0.01)

    def moveCursor(self, dstx, dsty):
        if dstx < 0:
            dstx = 0
        elif dstx > 8:
            dstx = 8
        if dsty < 0:
            dsty = 0
        elif dsty > 6:
            dsty = 6
        if (dsty < self.y):
            for i in range(self.y - dsty):
                keyPress(self.KEY_UP)
        elif (dsty > self.y):
            for i in range(dsty - self.y):
                keyPress(self.KEY_DOWN)
        if dsty != 6:
            if (dstx < self.x):
                for i in range(self.x - dstx):
                    keyPress(self.KEY_LEFT)
            elif (dstx > self.x):
                for i in range(dstx - self.x):
                    keyPress(self.KEY_RIGHT)
            self.x = dstx
        else:
            self.x = 0
        self.y = dsty
        keyPress(self.KEY_A)

    def inputName(self, name):
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
        keyPress(self.START)