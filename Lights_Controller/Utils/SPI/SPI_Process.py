import threading
import queue
from Utils.supportFunc import Singleton_Class
from Utils.supportFunc.Script_support import Switcher

"""
SPI TRANFER FRAME: {type, group, index, on/off, red, green, blue}
    - type: 1 - 595, 2 - DMX, 3 - PUMPER
    - group: device group index
    - index: what device in group
    - on/off: 0/1
    - red, green, blue: MIN[0, 0, 0], MAX[254, 254, 254]
"""


class SPI(metaclass=Singleton_Class.SingletonMeta):

    def __init__(self):
        self.runAvailable = False
        self.signalQueue = queue.Queue()
        self._SPIThread = threading.Thread(
                                    target=self.Start,
                            )
        self._SPIThread.start()

    def Start(self):
        self.runAvailable = True
        while self.runAvailable:
            if (not self.signalQueue.empty()):
                tranferData = [0, 0, 0, 0, 0, 0, 0]
                raw_data = self.signalQueue.get()

                tranferData[0] = int(Switcher(raw_data))
                temp = raw_data[0].split('.')[1].split('-')
                tranferData[1] = int(temp[0])
                tranferData[2] = int(temp[1])
                if (raw_data[1] == 'OFF'):
                    tranferData[3] = 0
                    tranferData[4] = 0
                    tranferData[5] = 0
                    tranferData[6] = 0
                else:
                    tranferData[3] = 1
                    temp = raw_data[2].split('.')
                    tranferData[4] = int(temp[0])
                    tranferData[5] = int(temp[1])
                    tranferData[6] = int(temp[2])

                print(tranferData)

    def PutSignal(self, data):
        self.signalQueue.put(data)

    def StopSPI(self):
        self.runAvailable = False
        self._SPIThread.join()
        while (not self.signalQueue.empty()):
            self.signalQueue.get()


spiHandler = SPI()
