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
        # self.btn = wx.Button(self.panel, wx.ID_OK,
        #                      label="ok", size=(50, 20), pos=(75, 50))
        hbox = wx.BoxSizer(wx.HORIZONTAL)

        self.logInfo = wx.TextCtrl(panel,
                                   style=wx.TE_READONLY |
                                   wx.HSCROLL |
                                   wx.TE_MULTILINE)

        hbox.Add(self.logInfo, proportion=1, flag=wx.EXPAND)

        panel.SetSizer(hbox)


class GUI(wx.Frame):
    """ Basic GUI to run different pomodoro settings

    """
    def __init__(self, parent, title):
        super(GUI, self).__init__(parent, title=title,
                                  size=(350, 250))
        self.currState = False
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

        self.mainBox.Add(workButton)
        self.mainBox.Add(restButton)
        self.mainBox.Add(logBut)

        self.mainPanel.SetSizer(self.mainBox)

    def initLog(self):
        """Will initialize the info dialog."""
        log = LogWindow(self, "Log Window")
        log.Show()

    def initCustom(self):
        """Will initialize the custom menu."""
        pass

    def rest(self):
        timeThreader(5)

    def work(self):
        timeThreader(15)


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




app = wx.App()
ex = GUI(None, title="AHAHA")
ex.Show()
app.MainLoop()
