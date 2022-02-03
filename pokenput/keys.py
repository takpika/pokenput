import pyautogui
from time import sleep

from . import name as nm

class keys():
    def __init__(self, version=1):
        self.KEY_UP = "up"
        self.KEY_DOWN = "down"
        self.KEY_LEFT = "left"
        self.KEY_RIGHT = "right"
        self.KEY_START = "enter"
        self.KEY_A = "z"
        self.KEY_B = "x"
        self.mode = "kana"
        self.version = version
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
                self.keyPress(self.KEY_UP)
        elif (dsty > self.y):
            for i in range(dsty - self.y):
                self.keyPress(self.KEY_DOWN)
        if dsty != 6:
            if (dstx < self.x):
                if (self.x - dstx < (dstx+9) - self.x):
                    for i in range(self.x - dstx):
                        self.keyPress(self.KEY_LEFT)
                else:
                    for i in range(dstx+9 - self.x):
                        self.keyPress(self.KEY_RIGHT)
            elif (dstx > self.x):
                if (dstx - self.x < self.x - (dstx-9)):
                    for i in range(dstx - self.x):
                        self.keyPress(self.KEY_RIGHT)
                else:
                    for i in range(self.x - (dstx-9)):
                        self.keyPress(self.KEY_LEFT)
            self.x = dstx
        else:
            self.x = 0
        self.y = dsty
        self.keyPress(self.KEY_A)

    def inputName(self, name):
        self.mode = "kana"
        self.x = 0
        self.y = 0
        for i in range(len(name)):
            KanaHira = nm.checkKanaHira(name[i])
            if KanaHira == 'error':
                break
            if self.mode != KanaHira and (not name[i] in nm.same_chars):
                self.moveCursor(0, 6)
                self.mode = KanaHira
            Pos = nm.checkPos(name[i])
            if Pos == (-1, -1):
                break
            if Pos[0] < 9:
                self.moveCursor(Pos[0], Pos[1])
            else:
                if Pos[0] > 8 and Pos[0] < 12:
                    self.moveCursor(Pos[0] - 8, Pos[1])
                    if i == 4:
                        self.x = 8
                        self.y = 5
                    self.moveCursor(4, 5)
                elif Pos[0] == 12:
                    self.moveCursor(5, Pos[1])
                    if i == 4:
                        self.x = 8
                        self.y = 5
                    self.moveCursor(4, 5)
                elif Pos[0] == 13:
                    self.moveCursor(5, Pos[1])
                    if i == 4:
                        self.x = 8
                        self.y = 5
                    self.moveCursor(5, 5)
        self.keyPress(self.KEY_START)