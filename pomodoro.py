import time


def pomodoSwitch(lol) -> str:
    timeSwitch = {
        0: pomodoroStart(25),
        1: pomodoroRest(5),
        2: pomodoroStop(0)
    }
    return switcher.get(lol, lambda: "[-] Invalid int %s" % timeSwitch)

def pomodoroStart(time: float):
    print("[+] Started timer")
    basicTimer(time, 1.0)

def pomodoroRest(time: float):
    print("[+] Started rest")
    basicTimer(time, 1.0)


def pomodoroStop(time: float):
    print("[+] Stopped tmier")
    basicTimer(time, 1.0)

def basicTimer(loltime: float, interval: float):
    while not loltime == 0:
        print(int(loltime))
        loltime -= interval
        time.sleep(interval)

pomodoSwitch(int(input('Start: 0)))
