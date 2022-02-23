from socket import socket, AF_INET, SOCK_STREAM
from time import sleep


def selenium_health_check(db_name: str, db_port: int | str):
    s = socket(AF_INET, SOCK_STREAM)
    request = f'GET /wd/hub/status HTTP/1.1\r\nHost:{db_name}\r\n\r\n'
    while True:
        try:
            s.connect((db_name, int(db_port)))
            while True:
                s.send(request.encode())
                response = s.recv(145)
                if response.find(b'"ready": true', 131) != -1:
                    break
                sleep(1)
            break
        except:
            sleep(1)
    s.close()
