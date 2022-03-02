from socket import socket, AF_INET, SOCK_STREAM
from time import sleep


def selenium_health_check(hostname: str, port: int | str):
    s = socket(AF_INET, SOCK_STREAM)
    request = f'GET /wd/hub/status HTTP/1.1\r\nHost:{hostname}\r\n\r\n'
    while True:
        try:
            s.connect((hostname, int(port)))
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
