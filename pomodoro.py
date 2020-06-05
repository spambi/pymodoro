import threading
import time
import wx
from win10toast import ToastNotifier


class LogWindow(wx.Dialog):
    """A basic dialog for logging out current processes and info

    """
    def __init__(self, parent, title):
        super(LogWindow, self).__init__(parent, title=title)
        self.InitUI()

    def InitUI(self):
        """Init's UI for LogWindow Class"""
        panel = wx.Panel(self)
        hbox = wx.BoxSizer(wx.HORIZONTAL)

        self.logInfo = wx.TextCtrl(panel,
                                   style=wx.TE_READONLY |
                                   wx.HSCROLL |
                                   wx.TE_MULTILINE)

        hbox.Add(self.logInfo, proportion=1, flag=wx.EXPAND)

        panel.SetSizer(hbox)

    def log(self, info: str):
        self.logInfo.AppendText(info)


class GUI(wx.Frame):
    """ Basic GUI to run different pomodoro settings

    """
    def __init__(self, parent, title):
        super(GUI, self).__init__(parent, title=title,
                                  size=(350, 250))
        self.logClass = None

        self.Center()
        self.InitUI()

    def InitUI(self):
        """Init's UI for GUI Class"""

        # Layout config
        self.mainPanel = wx.Panel(self)
        self.mainPanel.SetBackgroundColour("#d8bfd8")
        self.mainBox = wx.BoxSizer(wx.HORIZONTAL)

        # Work But
        workButton = wx.Button(self.mainPanel,
                               label="Work", size=(70, 30))
        workButton.Bind(wx.EVT_BUTTON, lambda EVT: self.work())

        # Rest But
        restButton = wx.Button(self.mainPanel,
                               label="Rest", size=(70, 30))
        restButton.Bind(wx.EVT_BUTTON, lambda EVT: self.rest())

        # Log Spawn
        logBut = wx.Button(self.mainPanel,
                           label="Log", size=(70, 30))
        logBut.Bind(wx.EVT_BUTTON, lambda EVT: self.initLog())

        logTest = wx.Button(self.mainPanel,
                            label="Log Test!", size=(70, 30))
        logTest.Bind(wx.EVT_BUTTON,
                     lambda EVT: self.logClass.log("This is a test!"))

        self.mainBox.Add(workButton)
        self.mainBox.Add(restButton)
        self.mainBox.Add(logBut)
        self.mainBox.Add(logTest)

        self.mainPanel.SetSizer(self.mainBox)

    def initLog(self):
        """Will initialize the info dialog."""
        if self.logClass:
            self.logClass.Show()
        else:
            self.logClass = LogWindow(self, "Log Window")

    def initCustom(self):
        """Will initialize the custom menu."""
        pass

    def rest(self):
        timeThreader(5, self.logClass)

    def work(self):
        timeThreader(15, self.logClass)

    def selfLog(self, string: str) -> bool:
        if self.logClass:
            self.logClass.logInfo.AppendText(string)
            return True
        else:
            return False


def baseTimer(counter: int, logClass=None) -> bool:
    """Basic Timer Seperate of GUI."""
    toast = ToastNotifier()
    i = None
    i = counter
    toast.show_toast("Basic Timer",
                     "{} second timer".format(str(counter)),
                     duration=4,
                     threaded=True)

    if logClass:
        while i:
            logClass.log("[+] Countdown: {}\n".format(i))
            time.sleep(1)
            i -= 1
        logClass.log("[+] Countdown finished\n")
    elif not logClass:
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


def timeThreader(counter: int, logClass=None) -> bool:
    """Calls baseTimer with specified time."""
    t = threading.Thread(target=baseTimer,
                         args=(counter, logClass,), daemon=True)
    try:
        t.start()
    except BaseException as err:
        raise(err)


app = wx.App()
ex = GUI(None, title="AHAHA")
ex.Show()
app.MainLoop()
