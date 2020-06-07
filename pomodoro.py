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
                                   wx.TE_MULTILINE |
                                   wx.HSCROLL)

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
        self.mainBox = wx.BoxSizer(wx.VERTICAL)
        self.customBox = wx.BoxSizer(wx.VERTICAL)

        # Menubar Config
        menubar = wx.MenuBar()
        logMenu = wx.Menu()
        logItem = logMenu.Append(wx.ID_ANY, "Show Log",
                                 "Show's the Logging Window")
        menubar.Append(logMenu, "&Log")

        self.Bind(wx.EVT_MENU, lambda EVT: self.initLog(), logItem)

        # Work But
        workButton = wx.Button(self.mainPanel,
                               label="Work", size=(100, 30))
        workButton.Bind(wx.EVT_BUTTON, lambda EVT: self.work())

        # Rest But
        restButton = wx.Button(self.mainPanel,
                               label="Rest", size=(100, 30))
        restButton.Bind(wx.EVT_BUTTON, lambda EVT: self.rest())

        # Log Spawn; Will put these into menubar soon
        logBut = wx.Button(self.mainPanel,
                           label="Log", size=(100, 30))
        logBut.Bind(wx.EVT_BUTTON, lambda EVT: self.initLog())

        customBut = wx.Button(self.mainPanel,
                              label="Custom Timer", size=(100, 30))
        customBut.Bind(wx.EVT_BUTTON, lambda EVT: self.customTimer())

        self.customText = wx.TextCtrl(self.mainPanel, size=(100, 30))

        # Add buttons to sizers
        self.mainBox.Add(workButton, wx.EXPAND | wx.ALL)
        self.mainBox.Add(restButton, wx.EXPAND | wx.ALL)
        self.mainBox.Add(logBut, wx.EXPAND | wx.ALL)
        # self.mainBox.Add(logTest, wx.EXPAND | wx.ALL)

        self.customBox.Add(customBut, wx.EXPAND | wx.ALL)
        self.customBox.Add(self.customText, wx.EXPAND | wx.ALL)

        self.mainBox.Add(self.customBox)

        self.mainPanel.SetSizer(self.mainBox)
        self.SetMenuBar(menubar)

    def initLog(self):
        """Will initialize the info dialog."""
        if self.logClass:
            self.logClass.Show()
        else:
            self.logClass = LogWindow(self, "Log Window")
            self.logClass.Show()

    def customTimer(self):
        """Custom Timer"""
        num = self.customText.GetValue()
        try:
            num = int(self.customText.GetValue())
        except BaseException as err:
            if not num:
                self.logClass.log("[-] TextCtrl is null\n")
                raise(err)
            wx.MessageBox("Please input a number", "Info",
                          wx.OK | wx.ICON_INFORMATION)
            raise(err)

        timeThreader(sndtoMin(num), self.logClass)

    def rest(self):
        timeThreader(sndtoMin(0.5), self.logClass)

    def work(self):
        timeThreader(sndtoMin(1.5), self.logClass)

    def selfLog(self, string: str) -> bool:
        if self.logClass:
            self.logClass.logInfo.AppendText(string)
            return True
        else:
            return False


def sndtoMin(seconds: int) -> int:
    return seconds * 60


# Does not display time proportional to base 60
def baseTimer(counter: int, logClass=None) -> bool:
    """Basic Timer Seperate of GUI."""
    toast = ToastNotifier()
    i = None
    i = counter
    toast.show_toast("Basic Timer",
                     "{} minute timer".format(str(counter / 60)),
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
            print("[+] Countdown: {}\n".format(i))
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
