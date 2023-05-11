# 导入 socket、sys 模块
from re import T
import socket
import sys
import time
import threading


MSG=['欢迎访问菜鸟教程！'+ "\r\n", '欢迎访问菜鸟教程！'+ "\r\n", '欢迎访问菜鸟教程！'+ "\r\n", '欢迎访问菜鸟教程！'+ "\r\n"]
def Sent():
    global MSG
    # 创建 socket 对象
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 获取本地主机名
    host = socket.gethostname()
    # 设置端口号
    port = 8880
    # 连接服务，指定主机和端口
    s.connect((host, port))
    while True:
        if len(MSG) !=0:
            for i in range(0, len(MSG)):
                s.send(MSG[0].encode('utf-8'))
                del MSG[0]
        time.sleep(1)


t = threading.Thread(target=Sent)
t.start()