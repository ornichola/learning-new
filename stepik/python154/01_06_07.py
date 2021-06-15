"""
[STEPIK]
Web-технологии https://stepik.org/course/154
01_06_06 Сетевые протоколы

Разработать простейший TCP echo сервер.

Требования

Запускается на IP адресе 0.0.0.0 и TCP порту 2222
Получает сообщения длинной не более 1024 байт и отправляет обратно клиенту
Закрывает соединение при получении сообщения с текстом close.
"""

import os
import socket
import sys


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0', 2222))
server_socket.listen(10)

while True:
    conn, addr = server_socket.accept()
    child_pid = os.fork()
    if child_pid == 0:
        request = conn.recv(1024)
        conn.send(request)
        conn.close()
        sys.exit()
    else:
        conn.close()
