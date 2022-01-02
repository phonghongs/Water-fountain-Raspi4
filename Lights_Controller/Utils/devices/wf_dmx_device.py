from Utils.supportFunc import Script_support
from Utils.devices.base_device import BASE_DEVICE
from Utils.SPI.SPI_Process import SPI

spiHandler = SPI()

List_Client_DIR = 'Utils/devices/list_devices/list_dmx.cfg'


class WF_DMX(BASE_DEVICE):
    def __init__(self):
        self._ClientList = Script_support.List2Dict(
                            Script_support.ReadScript(List_Client_DIR)
                            )

    def CheckRule(self, data=""):
        deviceCheck = data[0].split('-')
        try:
            if (int(self._ClientList[deviceCheck[0]]) <= int(deviceCheck[1])):
                return False
        except:
            print('loi nhe')
            return False

        if (data[1] not in ('ON', 'OFF')):
            return False
        elif (data[1] == 'ON'):
            colorCheck = data[2].split('.')
            if (
                int(colorCheck[0]) > 255
                or int(colorCheck[1]) > 255
                or int(colorCheck[2]) > 255
            ):
                return False
        return True

