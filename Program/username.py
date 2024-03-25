import wx

class Username(wx.Frame):
    def __init__(self, *args, **kw):
        super(Username, self).__init__(*args, **kw) 
        self.initUI()

    def initUI(self):

        self.panel1 = wx.Panel(self)
        self.lbl = wx.StaticText(self.panel1,label="Username:", pos=(50, 20))
        self.txtBox = wx.TextCtrl(self.panel1,pos=(50, 50), size=(150, 20))
        self.btnCheck = wx.Button(self.panel1,wx.ID_ANY, "Check", pos=(50, 110))


        self.Bind(wx.EVT_BUTTON, self.onClick, id=self.btnCheck.GetId())

        self.SetTitle("Username Menu") 
        self.Centre() 
        self.Show(True)

  
        print ("Please enter username") 
        self.lbl.Show()
        self.txtBox.Show()
        self.btnCheck.Show()
        self.lbl.SetLabel("Enter your username: ")



    def onClick(self, event):
        ActualUsername = "18004097" 
        EnteredUsername = self.txtBox.GetValue()
        if EnteredUsername == ActualUsername:
            print ("Correct Username!") 
        else:
            print ("Wrong Username")


def main():
    us = wx.App()
    Username(None)
    us.MainLoop()

if __name__ == '__main__':
 main() 
