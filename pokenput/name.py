from chars import *

def checkName(name):
    for char in name:
            available = False
            for i in range(len(kana_chars)):
                if char in kana_chars[i] or char in hira_chars[i]:
                    return False
    return True

def convertName(name):
    name = name.replace(" ", "　")
    name = name.replace("リ", "り")
    name = name.replace("ヘ", "へ")
    name = name.replace("ベ", "べ")
    name = name.replace("ペ", "ぺ")
    return name

def checkKanaHira(char):
    for i in range(len(kana_chars)):
        if char in kana_chars[i]:
            return 'kana'
        elif char in hira_chars[i]:
            return 'hira'
    return 'error'

def checkPos(char):
    for i in range(len(kana_chars)):
        for j in range(len(kana_chars[i])):
            if char == kana_chars[i][j] or char == hira_chars[i][j]:
                return (i, j)
    return (-1, -1)