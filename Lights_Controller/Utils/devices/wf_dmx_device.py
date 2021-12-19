from Utils.supportFunc import Script_support
from Utils.devices.base_device import BASE_DEVICE

List_Client_DIR = 'Utils/devices/list_devices/list_dmx.cfg'


class WF_DMX(BASE_DEVICE):
    def __init__(self):
        self._ClientList = Script_support.List2Dict(
                            Script_support.ReadScript(List_Client_DIR)
                            )

    def CheckRule(self, data):
        # data structure : [ID][index][message][color]
        if data[0] in self._ClientList:
            if data[1] > self._ClientList[data[0]]:
                return 0
        else:
            return 0

        if (int(data[2]) > 254) or (int(data[3]) > 7):
            return 0

        return 1
