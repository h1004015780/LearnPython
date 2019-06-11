import win32con
import win32api
import time
with open('D:/123.txt','r') as s:
    str = s.readlines()
    s.close()
#list获取到文本的参数
list = [int(x) for x in str]
a1,a2,a3,a4 = list[0],list[1],list[2],list[3]
a = 420
b = a//60
while True:
#设置鼠标位置
    time.sleep(3)
    win32api.SetCursorPos((a1,a2))
#发送消息
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0,0)
#点击确定
    print("等待{}分钟".format(b))
    time.sleep(a)
    win32api.SetCursorPos((a3,a4))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0,0)
