import time
from win10toast import ToastNotifier

toaster = ToastNotifier()

def pomodoSwitch(lol) -> str:
    timeSwitch = {
        "0": pomodoroStart(25),
        "1": pomodoroRest(5),
        "2": pomodoroStop(0)
    }
    return switcher.get(lol, lambda: "[-] Invalid int %s" % timeSwitch)

def pomodoroStart(time: float):
    toaster.show_toast("Timer Start",
                       "Timer has started for: {} minutes!".format(time),
                       duration=3,
                       threaded=True)
    print("[+] Started timer")
    basicTimer(time, 1.0)

def pomodoroRest(time: float):
    print("[+] Started rest")
    toaster.show_toast("Rest time!",
                       "Resting for {} minutes!".format(int(time)),
                       duration="3")
    basicTimer(time, 1.0)


def pomodoroStop(time: float):
    print("[+] Stopped timer")
    toaster.show_toast("Timer Stopped!",
                       "",
                       duration="3")
    basicTimer(time, 1.0)

def basicTimer(loltime: float, interval: float):
    while not loltime == 0:
        print(int(loltime))
        loltime -= interval
        time.sleep(interval)
    toaster.show_toast("Timer is finished",
                       duration=3)

pomodoSwitch(int(input('Start: 0, Rest: 1, Stop: 2 ')))

