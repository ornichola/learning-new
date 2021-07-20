import socket
import selectors


selector = selectors.DefaultSelector()


def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('localhost', 5000))
    server_socket.listen()

    selector.register(server_socket, selectors.EVENT_READ, accept_connection)


def accept_connection(serv_socket):
    client_socket, address = serv_socket.accept()
    print('Connection from', address)

    selector.register(client_socket, selectors.EVENT_READ, send_message)


def send_message(client_socket):
    request = client_socket.recv(4096)
    if request:
        response = 'hello world\n'.encode()
        client_socket.send(response)
    else:
        selector.unregister(client_socket)
        client_socket.close()


def event_loop():
    while True:
        events = selector.select()  # (key, events)
        for key, _ in events:
            callback = key.data
            callback(key.fileobj)


if __name__ == '__main__':
    server()
    event_loop()
