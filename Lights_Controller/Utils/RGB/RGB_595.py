from Utils import Script_support, Singleton_Class


List_Client_DIR = 'List_Client_RGB.txt'


class RGB_595(metaclass=Singleton_Class.SingletonMeta):

    def __init__(self):
        self.__ClientList = Script_support.List2Dict(
                            Script_support.ReadScript(List_Client_DIR)
                            )

    def AddSlave(self, iD, numCP):
        self.__ClientList[iD] = numCP

    def DelSlave(self, iD):
        del self.__ClientList[iD]

    def CheckRule(self, data):
        # data structure : [ID][index][message][color]
        if data[0] in self.__ClientList:
            if data[1] > self.__ClientList[data[0]]:
                return 0
        else:
            return 0

        if (int(data[2]) > 254) or (int(data[3]) > 7):
            return 0

        return 1


def RGB_Control(data, rgb_obj=RGB_595()):
    if rgb_obj.CheckRule(data):
        print("Oke chuyen duoc")
