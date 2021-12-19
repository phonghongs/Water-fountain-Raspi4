from Utils.supportFunc import Script_support

LIST_595 = "./list_595.cfg"
LIST_DMX = "./list_dmx.cfg"
LIST_PUMPS = "./list_pumps.cfg"


class list_handler():
    def __init__(self):
        self._595 = Script_support(LIST_595)
        self._dmx = Script_support(LIST_DMX)
        self._pumps = Script_support(LIST_PUMPS)
