import socket
import threading
import hashlib

BUFF_SIZE = 1024
CONNECTION = ('127.0.0.1', 55555)

MY_NAME = input("Enter your name: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    # If first to establish connection, start as a server
    client.bind(('127.0.0.1', 55555))
    client.listen()
    client, addr = client.accept()
except Exception:
    # If a user is already the server, connect to them via TCP
    client.connect(('127.0.0.1', 55555))


def chat_rx() -> None:
    """
    This function will wait for input to arrive. Should run as a
    thread.
    :return:
    """
    print("RX Thread running...")
    while True:
        try:
            msg = client.recv(BUFF_SIZE).decode('ascii')
            print(msg)
        except Exception:
            client.close()


def chat_tx() -> None:
    """
    This function is will sit and wait for user input to be passed.
    Should run as a thread.
    :return: None
    """
    print("TX Thread running...")
    print(f'Connected as {MY_NAME}')
    while True:
        msg = f'{MY_NAME}: {input("> ")}'
        try:
            client.send(msg.encode('ascii'))
        except Exception:
            client.close()


# Create the threads and start them for the clients
rx_thread = threading.Thread(target=chat_rx)
tx_thread = threading.Thread(target=chat_tx)
rx_thread.start()
tx_thread.start()
