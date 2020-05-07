from PyQt5 import QtCore,QtWidgets
import win32gui, win32api, win32con

# 调用win32api的模拟点击功能实现ctrl+v粘贴快捷键   
def ctrlV():
    win32api.keybd_event(17,0,0,0)  #ctrl键位码是17
    win32api.keybd_event(86,0,0,0)  #v键位码是86
    win32api.keybd_event(86,0,win32con.KEYEVENTF_KEYUP,0) #释放按键
    win32api.keybd_event(17,0,win32con.KEYEVENTF_KEYUP,0)
    
# 调用win32api的模拟点击功能实现alt+s微信发送快捷键 （可以根据自己微信发送快捷键是什么来进行调整）
def altS(): 
    win32api.keybd_event(18, 0, 0, 0)    #Alt  
    win32api.keybd_event(83,0,0,0) #s
    win32api.keybd_event(83,0,win32con.KEYEVENTF_KEYUP,0) #释放按键
    win32api.keybd_event(18,0,win32con.KEYEVENTF_KEYUP,0)
    
    
# 调用win32gui调用桌面窗口，获取指定窗口句柄id,激活窗口  ，向函数传递窗口名称to_weixin 
def wx_send(to_weixin):
    hw = win32gui.FindWindow(None, to_weixin)  # 获取窗口句柄
    win32gui.GetClassName(hw)  # 获取窗口classname
    title = win32gui.GetWindowText(hw)  # 获取窗口标题
    win32gui.GetDlgCtrlID(hw)
    win32gui.SetForegroundWindow(hw) # 激活窗口

def main():
    app = QtWidgets.QApplication([])
    data = QtCore.QMimeData()
    url = QtCore.QUrl.fromLocalFile(r'C:\Users\92536\Desktop\周计划.png')
    data.setUrls([url])
    app.clipboard().setMimeData(data)
    clipboard = QtWidgets.QApplication.clipboard()
    wx_send('文件助手')
    ctrlV()
    altS()

if __name__ == "__main__":
    main()
