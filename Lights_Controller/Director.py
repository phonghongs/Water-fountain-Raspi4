# from Utils.RGB.RGB_595 import RGB_595, RGB_Control
from Utils.SPI import SPI_Process
from Utils.supportFunc import Script_support
from Utils.devices.wf_595_device import WF_595
from Utils.devices.wf_dmx_device import WF_DMX
from Utils.devices.wf_pumps_device import WF_PUMPS
import time

RGB_OBJ_595 = WF_595()
RGB_OBJ_DMX = WF_DMX()
RGB_OBJ_PUMPS = WF_PUMPS()


def Switcher(_cnt):
    case = _cnt[0].split('.')
    switch = {
        '595': lambda: print('595'),
        'DMX': lambda: print("DMX"),
        'DELAY': lambda: print("DELAY")
    }

    return switch.get(case[0], lambda: 'Invalid')()


def main_Director(_FileDir, status):
    Script_Content = Script_support.ReadScript(_FileDir)
    print(Script_Content)
    for index, cnt in enumerate(Script_Content):
        if status:
            Switcher(cnt)


if __name__ == "__main__":
    main_Director('L_Script.cfg', True)
