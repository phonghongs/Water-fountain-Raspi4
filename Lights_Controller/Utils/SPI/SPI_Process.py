import threading
import time
from Utils.supportFunc import Singleton_Class


class SPI(metaclass=Singleton_Class.SingletonMeta):

    def __init__(self, PORT, CS):
        self._Test = 0
        self.queue = []
        self._SPIThread = threading.Thread(
                                    target=self.Start,
                                    args=(self.queue,)
                            )
        self._SPIThread.start()

    def Start(self, ):
        print(f"begin thread {self._Test}")
        self._Test += 1
        time.sleep(5)
        print(f"end thread {self._Test - 1}")
        print(
            "Task 1 assigned to thread: {}".format(
                threading.current_thread().name
                )
            )

    def Debug(self):
        print(self._Test)
