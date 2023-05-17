import socket 

port = 5000
mensages = []
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', port))

while True:
    print("Aguardando conexão...")
    conn, addr = sock.recvfrom(64)
    mensages.append(addr)
    data = (f"Dados:{conn}\n"
            f"Origem:{addr}\n").encode("utf-8")


    for ip in mensages:
        sock.sendto(data, addr)

sock.close()