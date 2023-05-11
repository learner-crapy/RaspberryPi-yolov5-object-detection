# 导入 socket、sys 模块
import socket
import sys

# 创建 socket 对象
serversocket = socket.socket(
            socket.AF_INET, socket.SOCK_STREAM)

# 获取本地主机名
host = socket.gethostname()

port = 8880

# 绑定端口号
serversocket.bind((host, port))

# 设置最大连接数，超过后排队
serversocket.listen(5)
# 建立客户端连接
clientsocket,addr = serversocket.accept()
while True:
    msg1 = clientsocket.recv(1024)
    print ((msg1.decode('utf-8')))
