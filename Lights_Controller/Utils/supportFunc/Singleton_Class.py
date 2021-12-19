import threading


class SingletonMeta(type):

    _instances = {}
    _lock = threading.Lock()

    def __call__(cls, *args, **kwds):
        with cls._lock:
            if cls not in cls._instances:
                isinstance = super().__call__(*args, **kwds)
                cls._instances[cls] = isinstance
        return cls._instances[cls]
