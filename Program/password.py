import wx

class Password(wx.Frame):
    def __init__(self, *args, **kw):
        super(Password, self).__init__(*args, **kw) 
        self.initUI()

    def initUI(self):

        self.panel1 = wx.Panel(self)
        self.lbl = wx.StaticText(self.panel1,label="Password:", pos=(50, 20))
        self.txtBox = wx.TextCtrl(self.panel1,pos=(50, 50), size=(150, 20))
        self.btnCheck = wx.Button(self.panel1,wx.ID_ANY, "Check", pos=(50, 110))


        self.Bind(wx.EVT_BUTTON, self.onClick, id=self.btnCheck.GetId())

        self.SetTitle("Password Menu") 
        self.Centre() 
        self.Show(True)

  
        print ("Please enter password") 
        self.lbl.Show()
        self.txtBox.Show()
        self.btnCheck.Show()
        self.lbl.SetLabel("Enter your Password: ")



    def onClick(self, event):
        Actualpassword = "pass1" 
        EnteredPassword = self.txtBox.GetValue()
        if EnteredPassword == Actualpassword:
            print ("Correct Password!") 
        else:
            print ("Wrong Password")


def main():
    pa = wx.App()
    Password(None)
    pa.MainLoop()

if __name__ == '__main__':
 main() 

