import wx
import sys

class MainMenu(wx.Frame):
    def __init__(self, *args, **kw):
        super(MainMenu, self).__init__(*args, **kw) 
        self.initUI()
                
    def initUI(self):
        self.menuIdPassword = wx.NewId()
        self.menuIdUsername = wx.NewId()
        self.menuIdQuit = wx.NewId()
        
        self.panel1 = wx.Panel(self)
        menuBar = wx.MenuBar() 
        fileMenu = wx.Menu()
        itemPassword = fileMenu.Append(self.menuIdPassword, 'Password') 
        itemUsername = fileMenu.Append(self.menuIdUsername, 'Username') 
        itemQuit = fileMenu.Append(self.menuIdQuit, 'Quit')
        menuBar.Append(fileMenu, '&File')
        self.SetMenuBar(menuBar)

        self.Bind(wx.EVT_MENU, self.onFileMenu, itemPassword)
        self.Bind(wx.EVT_MENU, self.onFileMenu, itemUsername)
        self.Bind(wx.EVT_MENU, self.onFileMenu, itemQuit)

        self.SetTitle("Login Program")
        self.Centre()
        self.Show(True)

    def onFileMenu(self, evt):
        if evt.GetId() == self.menuIdPassword:
            print "Password Menu"
            import password
            password.main()
        elif evt.GetId() == self.menuIdUsername:
            print "Username Menu"
            import username
            username.main()
        elif evt.GetId() == self.menuIdQuit:
            sys.exit()

def main():
    ma = wx.App()
    MainMenu(None)
    ma.MainLoop()    

if __name__ == '__main__':
    main() 

   


