import threading
import time
import wx
from win10toast import ToastNotifier


class LogWindow(wx.Dialog):
    """A basic dialog for logging out current processes and info

    """
    def __init__(self, parent):
        pass


class GUI(wx.Frame):
    """ Basic GUI to run different pomodoro settings

    """
    def __init__(self, parent, title):
        super(GUI, self).__init__(parent, title=title,
                                  size=(350, 250))
        self.Center()
        self.InitUI()

    def InitUI(self):
        # Layout config
        self.mainPanel = wx.Panel(self)
        self.mainPanel.SetBackgroundColour("#d8bfd8")
        self.mainBox = wx.BoxSizer(wx.HORIZONTAL)

        # Work But
        self.workButton = wx.Button(self.mainPanel,
                                    label="Work", size=(70, 30))
        self.workButton.Bind(wx.EVT_BUTTON, lambda EVT: work())

        self.restButton = wx.Button(self.mainPanel,
                                    label="Rest", size=(70, 30))
        self.restButton.Bind(wx.EVT_BUTTON, lambda EVT: rest())

        self.mainBox.Add(self.workButton)
        self.mainBox.Add(self.restButton)

        self.mainPanel.SetSizer(self.mainBox)


def baseTimer(counter: int) -> bool:
    """Basic Timer Seperate of GUI."""
    toast = ToastNotifier()
    i = None
    i = counter
    toast.show_toast("Basic Timer",
                     "{} second timer".format(str(counter)),
                     duration=4,
                     threaded=True)

    while i:
        print("Countdown: {}".format(i))
        time.sleep(1)
        i -= 1
    print("Countdown finished")

    toast.show_toast("Basic Timer",
                     "Timer has ended!",
                     duration=4,
                     threaded=True)

    return True


def timeThreader(counter: int) -> bool:
    """Calls baseTimer with specified time."""
    t = threading.Thread(target=baseTimer, args=(counter,), daemon=True)
    try:
        t.start()
    except BaseException as err:
        raise(err)


def rest():
    timeThreader(5)


def work():
    timeThreader(15)


app = wx.App()
ex = GUI(None, title="AHAHA")
ex.Show()
app.MainLoop()
