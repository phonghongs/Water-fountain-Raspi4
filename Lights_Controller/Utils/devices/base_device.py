from abc import abstractmethod
from Utils.supportFunc import Singleton_Class


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
