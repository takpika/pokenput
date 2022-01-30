from time import sleep

from .chars import *
from .keys import *
from .name import *

if __name__ == "__main__":
    name = input("入力する名前を入力してください: ")
    name = convertName(name)
    if checkName(name):
        print("3秒後に入力を開始します")
        sleep(3)
        inputName(name)