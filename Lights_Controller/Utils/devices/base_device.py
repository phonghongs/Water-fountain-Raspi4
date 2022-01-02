from abc import abstractmethod
from Utils.supportFunc import Singleton_Class
from Utils.SPI.SPI_Process import spiHandler


class BASE_DEVICE(metaclass=Singleton_Class.SingletonMeta):
    def __init__(self):
        self._ClientList = {}

    def AddSlave(self, iD, numCP):
        self._ClientList[iD] = numCP

    def DelSlave(self, iD):
        del self._ClientList[iD]

    def getinfo(self):
        return self._ClientList

    @abstractmethod
    def CheckRule(self, data):
        pass

    def Action(self, data):
        if (self.CheckRule(data) is False):
            return False

        spiHandler.PutSignal(data)
        return True
