from Utils.RGB.RGB_595 import RGB_595, RGB_Control
from Utils.SPI import SPI_Process
from Utils import Script_support
import time

RGB_OBJ = RGB_595()


def Switcher(_cnt):
    switch = {
        '595': lambda: RGB_Control(_cnt[1:], RGB_OBJ),
        'DMX': lambda: print("DMX"),
        'Delay': lambda: time.sleep(float(_cnt[1]))
    }

    print(_cnt[0])

    return switch.get(_cnt[0], lambda: 'Invalid')()


def main_Director(_FileDir, status):
    Script_Content = Script_support.ReadScript(_FileDir)
    print(Script_Content)
    # for index, cnt in enumerate(Script_Content):
    #     if status:
    #         print(cnt[0].split('.'))
    #         # Switcher(cnt)


if __name__ == "__main__":
    main_Director('L_Script.txt', True)
