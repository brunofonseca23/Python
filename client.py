import socket 

SERVER = input("Digite o endereço IP do servidor: ")
PORT = 5000

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    msg = input("Escreva a mensagem: ").encode("utf-8")
    if msg != "":
        sock.sendto(msg,(SERVER, PORT))
    
    data, addr = sock.recvfrom(64)
    print(data.decode("utf-8"))

sock.close()
