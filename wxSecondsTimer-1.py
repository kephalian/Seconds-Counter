
import wx
import threading
import time
tit='Seconds Counter Dr Santhosh Kumar Rajamani APP'
class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title=tit)
        self.InitUI()
        self.count = 0
        self.start_thread()

    def InitUI(self):
        panel = wx.Panel(self)
        # Create a sizer for layout management
        sizer = wx.BoxSizer(wx.VERTICAL)
        self.label = wx.StaticText(panel, label="Count starting....", pos=(20, 20))
        sizer.Add(self.label, 0, wx.ALL | wx.EXPAND, 5)
        verdana_font = wx.Font(48, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_NORMAL, faceName="Verdana")
#        roboto_font = wx.Font(18, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, faceName="Roboto")

        # Set the font for the StaticText control
        self.label.SetFont(verdana_font)
        button1 = wx.Button(panel, label="Click Me to Reset to Zero!")
        button1.Bind(wx.EVT_BUTTON, self.on_button_click)
        sizer.Add(button1, 0, wx.ALL | wx.CENTER, 5)
        #self.SetSize((750, 150))
        self.Center()
        
        # Set sizer and size
        panel.SetSizer(sizer)
        sizer.Fit(self)
        self.SetSize(750, 200)
        
    def on_button_click(self, event):
        wx.MessageBox("Counter Reset to Zero", "Widget Status", wx.OK | wx.ICON_INFORMATION)
        self.count=0
        self.label.SetLabel("Count restarting....")
        
        
    def start_thread(self):
        thread = threading.Thread(target=self.update_label)
        thread.daemon = True
        thread.start()

    def update_label(self):
        while True:
            time.sleep(1)  # Wait for 20 seconds
            self.count += 1
            # Use wx.CallAfter to safely update the GUI from a non-main thread
            wx.CallAfter(self.update_label_safe)

    def update_label_safe(self):
        self.label.SetLabel(f"Count in Seconds: {self.count}")

class MyApp(wx.App):
    def OnInit(self):
        frame = MyFrame()
        frame.Show()
        return True

if __name__ == '__main__':
    app = MyApp()
    app.MainLoop()
