from Utils.supportFunc import Script_support
from Utils.devices.base_device import BASE_DEVICE

List_Client_DIR = 'Utils/devices/list_devices/list_595.cfg'


class WF_595(BASE_DEVICE):
    def __init__(self):
        self._ClientList = Script_support.List2Dict(
                            Script_support.ReadScript(List_Client_DIR)
                            )

    def CheckRule(self, data):
        pass
