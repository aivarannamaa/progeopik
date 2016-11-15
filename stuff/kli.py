import socket

serveri_aadress=("localhost", 7842)
suhtlemise_pistik = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
suhtlemise_pistik.connect(serveri_aadress)
vastus = b""
while True:
    suhtlemise_pistik.sendall(b"kalamees")
    v = suhtlemise_pistik.recv(2048)
    if len(v) == 0:
        break
    else:
        vastus += v
print("Sain serverilt sellise vastuse:", vastus.decode("UTF-8"))
