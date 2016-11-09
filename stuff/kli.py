import socket

serveri_aadress=("localhost", 7842)
suhtlemise_pistik = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
suhtlemise_pistik.connect(serveri_aadress)
vastus = suhtlemise_pistik.recv(1024)
print("Sain serverilt sellise vastuse:", vastus.decode("UTF-8"))
