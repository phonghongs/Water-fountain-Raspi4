from Utils.supportFunc import Script_support
from Utils.devices.wf_595_device import WF_595
from Utils.devices.wf_dmx_device import WF_DMX
from Utils.devices.wf_pumps_device import WF_PUMPS
from Utils.devices.base_device import spiHandler
import threading
import time

global status
status = {}

RGB_OBJ_595 = WF_595()
RGB_OBJ_DMX = WF_DMX()
RGB_OBJ_PUMPS = WF_PUMPS()


def DelayAction(delayTime, threadName):
    global status
    startTime = time.time()
    while (
        status[threadName]
        and (time.time() - startTime < float(delayTime))
    ):
        pass

    return 'Delay OK'


def Switcher(_cnt, threadName):
    global status
    case = _cnt[0].split('.')
    # print(_cnt)
    switch = {
        '595': lambda: RGB_OBJ_595.Action(_cnt),
        'DMX': lambda: RGB_OBJ_DMX.Action(_cnt),
        'PUMPS': lambda: RGB_OBJ_PUMPS.Action(_cnt),
        'DELAY': lambda: DelayAction(_cnt[1], threadName)
    }

    return switch.get(case[0], lambda: False)()


def run_Director(_FileDir, threadName):
    while status[threadName]:
        Script_Content = Script_support.ReadScript(_FileDir)
        # print(Script_Content)
        for index, cnt in enumerate(Script_Content):
            if status[threadName]:
                print(Switcher(cnt, threadName))
            else:
                break


if __name__ == "__main__":

    status['threadRun_595'] = True
    threadRun_595 = threading.Thread(
            target=run_Director,
            args=('L_Script.cfg', 'threadRun_595', )
        )

    status['threadRun_DMX'] = True
    threadRun_DMX = threading.Thread(
            target=run_Director,
            args=('L_Script_2.cfg', 'threadRun_DMX', )
        )

    threadRun_595.start()

    time.sleep(2)
    threadRun_DMX.start()

    time.sleep(10)
    status['threadRun_595'] = False
    threadRun_595.join()
    del status['threadRun_595']

    time.sleep(3)
    status['threadRun_DMX'] = False
    threadRun_DMX.join()
    del status['threadRun_DMX']
    print(status)

    spiHandler.StopSPI()
