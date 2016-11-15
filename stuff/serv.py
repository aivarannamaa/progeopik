import socket
import time

# Paneme serveri kuulama mingit kindlat porti
serveri_aadress=("localhost", 7842)
kuulamise_pistik = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
kuulamise_pistik.bind(serveri_aadress)
kuulamise_pistik.listen()

# Kliendi teenendamise kood on lõpmatus tsüklis,
# kuna me tahame teenendada lõpmatu arvu kliente
i = 1
while True:
    print("Hakkan klienti ootama")
    suhtlemise_pistik, kliendi_aadress = kuulamise_pistik.accept()
    print("Sain just ühenduse kliendiga nr.", i)
    teade = "Tere, klient nr. " + str(i) + "! Kell on " + time.strftime("%H:%M:%S")
    
    suhtlemise_pistik.sendall(("a"*1000).encode("UTF-8"))
    r = suhtlemise_pistik.recv(256)
    print(r)
    suhtlemise_pistik.sendall(teade.encode("UTF-8"))
    print("Saatsin talle sellise teate:", teade)
    suhtlemise_pistik.close()
    i += 1
    

