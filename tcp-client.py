import socket
import threading

nickname = input("Choose a nickname: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("10.0.111.176", 55555))

def recieve():
    while True:
        try:
            message = client.recv(1024).decode("utf-8")

            if message == "NICK":
                client.send(nickname.encode("utf-8"))
            else:
                print(message)
        except:
            print("An error occurred! Leaving the chat...")
            client.close()
            break

def send():
    while True:
        message = f"{nickname}: {input()}"
        client.send(message.encode("utf-8"))

recv_thread = threading.Thread(target=recieve)
recv_thread.start()

send_thread = threading.Thread(target=send)
send_thread.start()