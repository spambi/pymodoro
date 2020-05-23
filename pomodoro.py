import time
import threading
import queue
from win10toast import ToastNotifier


toaster = ToastNotifier()

# append sleep to queue
# make it thread
# go on with life


class Pymodoro():
    mainThread = None
    mainQueue = None
    printLock = None

    def __init__(self, time: float, interval: float, state: str):
        # Set up threading
        # self.mainThread = threading.Thread(target=self.handleThreads)
        # self.mainThread.daemon = True
        # Init mainQueue
        self.printLock = threading.Lock()
        self.mainQueue = queue.Queue()
        # timerLock = threading.Lock()
        #test = input("Please Input You're State: ")
        #self.pomodoroSwitch(state)

    # def threader(self, *vars):
    #     """Runs main thread of class"""
    #     while True:
    #         vars()
    #         self.mainQueue.task_done()

    # def handleThreads(self, *vars):
    #     # for x in range(1):
    #     t = threading.Thread(target=vars)
    #     t.daemon = True
    #     t.start()

    #     for worker in range(20):
    #         self.mainQueue.put(worker)
    #     self.mainQueue.join()

    def pomodoroSwitch(self, lol: str) -> str:
        timeSwitch = {
            "0":     self.pomodoroStart(25),
            "1":     self.pomodoroRest(5),
            "2":     self.pomodoroStop(0),
            "Start": self.pomodoroStart(25),
            "Rest":  self.pomodoroRest(5),
            "Stop":  self.pomodoroStop(0)
        }
        # state = timeSwitch.get(lol, lambda: "[-] Invalid int %s" % timeSwitch)
        return timeSwitch.get(lol, lambda: "[-] Invalid int %s" % timeSwitch)
        # if state not in timeSwitch:
        #     return False

        # self.handleThreads(state)
        # time.sleep(5)
        # if self.mainThreads.isAlive():
        #     print('hihi')

    def pomodoroStart(self, time: float):
        toaster.show_toast("Timer Start",
                           "Timer has started for: {} minutes!".format(time),
                           duration=3,
                           threaded=True)
        print("[+] Started timer")

    def pomodoroRest(self, time: float):
        print("[+] Started rest")
        toaster.show_toast("Rest time!",
                           "Resting for {} minutes!".format(time),
                           duration=3)
        self.basicTimer(time, 1.0)

    def pomodoroStop(self, time: float):
        print("[+] Stopped timer")
        toaster.show_toast("Timer Stopped!",
                           "",
                           duration=3)
        self.basicTimer(time, 1.0)

    def basicTimer(self, loltime: float, interval: float) -> bool:
        print('HERE')
        while loltime:
            with self.printLock:
                print(int(loltime))
                loltime -= interval
                time.sleep(interval)
        toaster.show_toast("Timer is finished",
                           "you are a terrible person",
                           duration=3)
        return True


# DEV
basic = Pymodoro(10, 10, lambda: int(input("Put in state: ")))
basic.pomodoroSwitch(int(input('Start: 0, Rest: 1, Stop: 2 ')))
