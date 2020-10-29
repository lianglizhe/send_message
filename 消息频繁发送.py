# @Time : 2020/10/25 20:48
# @Author : Lizhe
# @File 消息轰炸.py
# @software: {PyCharm}
import time   #导入时间库
from pynput.mouse import Button,Controller as mouse_cl #鼠标控制器
from pynput.keyboard import Key,Controller as key_cl  #键盘控制器

def send_question():
    #1.定位输入框的位置（鼠标左键点击来实现）
    mouse = mouse_cl()   #获取鼠标控制器的权限
    mouse.press(Button.left)    #模拟鼠标左键按下控制器
    mouse.release(Button.left)  #模拟鼠标左键的弹起

    for i in range(1,10):
        #2.在输入框中输入文字
        keybord=key_cl()               #获取键盘的控制权限
        keybord.type('%s.晚上好！！！'%i)     #设置发送文字的内容
        #3.按下回车键发送消息
        keybord.press(Key.enter)       #模拟键盘回车键的按下
        keybord.release(Key.enter)     #模拟键盘回车键的弹起
print('在此处设置程序将要执行的时间，这里3秒后执行')
time.sleep(3)  #在此处设置程序将要执行的时间
send_question() #调用发送函数

