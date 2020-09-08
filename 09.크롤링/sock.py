'''
소켓 :  연결된 네트워크의 양 끝단을 추상화 시킨 개념,   
        컴퓨터의 관점에서는 네트워크로 통하는 컴퓨터의 외부와 컴퓨터 내부의 프로그램을 이어주는 인터페이스
'''

import socket

'''
소켓 생성하기 : socket.socket(패밀리, 타입)
패밀리 :  IP4v -> socket.AF_INET, IP6v -> socket.AF_INET6
소켓 타입 : socket.SOCK_STREAM 혹은 socket.SOCK_DGRAM을 많이 사용함
클라이언트가 서버에 연결하기 : sock.connect()
'''
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

google_ip = socket.gethostbyname("google.com")
sock.connect((google_ip, 80)) #80 : 포트 넘버

#프로토콜에 맞게 정보를 요청함
sock.send("GET / HTTP/1.1 \n".encode())
sock.send("\n".encode())

'''
소켓으로부터 정보를 읽을 때 : sock.recv()  / 단위 : 바이트
소켓으로부터 정보를 보낼 때 : sock.sendall()
소켓을 닫을 때 : sock.close()
'''

buffer = sock.recv(4096) #4096 : 단위 Byte
buffer = buffer.decode().replace("\r\n","\n")
sock.close()

print(buffer)

'''
HTTP/1.1 200 OK
Date: Tue, 08 Sep 2020 15:27:51 GMT        
Expires: -1
Cache-Control: private, max-age=0
Content-Type: text/html; charset=ISO-8859-1
P3P: CP="This is not a P3P policy! See g.co/p3phelp for more info."
Server: gws
X-XSS-Protection: 0
X-Frame-Options: SAMEORIGIN
Set-Cookie: 1P_JAR=2020-09-08-15; expires=Thu, 08-Oct-2020 15:27:51 GMT; path=/; domain=.google.com; Secure
Set-Cookie: NID=204=k-b0umbwAUiC4DTlCZWeafesNNyeOh5Ui-gIPXpg_2v95Jz09j96byVm8OOYkjRiPxohBi_c6flLHFRA5eNuLFK9SiU_zb9bcMkSgoJ2yegxfr-LpAAyJhvjHmTWDb7YJdStFtm8jqR8aAaUEoN2APKN79KgC3TzGV79SiWvtjE; expires=Wed, 10-Mar-2021 15:27:51 GMT; path=/; domain=.google.com; HttpOnly
Accept-Ranges: none
Vary: Accept-Encoding
Transfer-Encoding: chunked

51b1
<!doctype html><html itemscope="" itemtype="http://schema.org/WebPage" lan ~~
'''
