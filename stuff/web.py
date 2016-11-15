# serverprogramm
import socket
import time

# Paneme serveri kuulama porti 7482 (loodame, et see pole juba kasutuses).
# "localhost" tähendab, et esialgu aktsepteerime vaid samast arvutist
# tulevaid ühendusi.
serveri_aadress=("localhost", 7482)
kuulamise_pistik = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
kuulamise_pistik.bind(serveri_aadress)
kuulamise_pistik.listen()

# Kliendi teenindamise kood on lõpmatus tsüklis, kuna me tahame 
# peale ühe kliendiga lõpetamist olla valmis järgmise kliendi jaoks.
i = 1
while True:
    print("Hakkan klienti ootama")
    suhtlemise_pistik, kliendi_aadress = kuulamise_pistik.accept()
    print("Sain just ühenduse kliendiga nr.", i)

    # Uurime kliendi käest, mida ta tahtis ...
    päring = b""
    while b"\r\n\r\n" not in päring: # kuni päringu (päise) lõpp pole veel loetud
        ports = suhtlemise_pistik.recv(1024)
        if len(ports) > 0:
            päring += ports
        else:
            break
    päringu_päis = päring.split(b"\r\n\r\n")[0].decode("ASCII")
    print("Päringu päis oli selline: \n" + päringu_päis)

    # Lihtsuse mõttes praegu me vastuse koostamisel päringut veel ei arvesta
    vastuse_päis = """HTTP/1.0 200 OK
Content-Type: text/html; charset=utf-8"""
    
    vastuse_sisu = """
    <html>
        <head>
            <title>Tere!</title>
        </head>
        <body>
            <h1>Tere, klient nr. {}!</h1>
            <p>Kell on {}</p>
        </body>
    </html>""".format(i, time.strftime("%H:%M:%S"))
    
    vastus = vastuse_päis + "\r\n\r\n" + vastuse_sisu
    suhtlemise_pistik.sendall(vastus.encode("UTF-8"))
    print("Saatsin talle sellise teate:", vastus)
    suhtlemise_pistik.close()
    i += 1
