import pyautogui
from time import sleep

KEY_UP = "up"
KEY_DOWN = "down"
KEY_LEFT = "left"
KEY_RIGHT = "right"
KEY_A = "z"
KEY_B = "x"

kana_chars = [
    ['ア', 'イ', 'ウ', 'エ', 'オ', 'ャ'],
    ['カ', 'キ', 'ク', 'ケ', 'コ', 'ュ'],
    ['サ', 'シ', 'ス', 'セ', 'ソ', 'ョ'],
    ['タ', 'チ', 'ツ', 'テ', 'ト', 'ッ'],
    ['ナ', 'ニ', 'ヌ', 'ネ', 'ノ'],
    ['ハ', 'ヒ', 'フ', 'へ', 'ホ'],
    ['マ', 'ミ', 'ム', 'メ', 'モ', 'ー'],
    ['ヤ', 'ユ', 'ヨ', 'ワ', 'ン', '　'],
    ['ラ', 'り', 'ル', 'レ', 'ロ'],
    ['ガ', 'ギ', 'グ', 'ゲ', 'ゴ'],
    ['ザ', 'ジ', 'ズ', 'ゼ', 'ゾ'],
    ['ダ', 'ヂ', 'ヅ', 'デ', 'ド'],
    ['バ', 'ビ', 'ブ', 'ぺ', 'ボ'],
    ['パ', 'ピ', 'プ', 'べ', 'ポ']
]

hira_chars = [
    ['あ', 'い', 'う', 'え', 'お', 'ゃ'],
    ['か', 'き', 'く', 'け', 'こ', 'ゅ'],
    ['さ', 'し', 'す', 'せ', 'そ', 'ょ'],
    ['た', 'ち', 'つ', 'て', 'と', 'っ'],
    ['な', 'に', 'ぬ', 'ね', 'の'],
    ['は', 'ひ', 'ふ', 'へ', 'ほ'],
    ['ま', 'み', 'む', 'め', 'も', 'ー'],
    ['や', 'ゆ', 'よ', 'わ', 'ん', '　'],
    ['ら', 'り', 'る', 'れ', 'ろ'],
    ['が', 'ぎ', 'ぐ', 'げ', 'ご'],
    ['ざ', 'じ', 'ず', 'ぜ', 'ぞ'],
    ['だ', 'ぢ', 'づ', 'で', 'ど'],
    ['ば', 'び', 'ぶ', 'べ', 'ぼ'],
    ['ぱ', 'ぴ', 'ぷ', 'ぺ', 'ぽ']
]

same_chars = ['ー', 'り', 'へ', 'べ', 'ぺ', '　']

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

if __name__ == "__main__":
    name = input("入力する名前を入力してください: ")
    name = name.replace(" ", "　")
    name = name.replace("リ", "り")
    name = name.replace("ヘ", "へ")
    name = name.replace("ベ", "べ")
    name = name.replace("ペ", "ぺ")
    for char in name:
        available = False
        for i in range(len(kana_chars)):
            if char in kana_chars[i] or char in hira_chars[i]:
                available = True
                break
        if not available:
            print("名前に使用できない文字が含まれています", char)
            exit()

    mode = 'kana'
    x = 0
    y = 0
    print("3秒後に入力を開始します")
    sleep(3)
    inputName(name)