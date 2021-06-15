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

import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(('0.0.0.0', 2222))
    s.listen(10)
    conn, addr = s.accept()
    while True:
        data = conn.recv(1024)
        if data.decode() == 'close':
            break
        conn.send(data)
