import os

kaust= input("Sisesta kausta nimi: ")
laiend = input("Sisesta laiend: ")

failinimed = os.listdir(kaust)
print(len(failinimed))

failide_arv = 0
kogumaht = 0

for failinimi in failinimed:
    if failinimi[-(len(laiend)+1):] == "." + laiend:

        täisnimi = kaust + "\\"+ failinimi
        
        suurus = os.stat(täisnimi).st_size
        suurus_mb = round(suurus / 1024 / 1024, 1)
        
        print(failinimi + ", " + str(suurus_mb) + "MB")
        
        failide_arv = failide_arv + 1
        kogumaht = kogumaht + suurus

kogu_mb = round(kogumaht / 1024 / 1024, 1)
print("Kokku oli " + str(failide_arv) + " faili, kogumahuga " + str(kogu_mb) + "MB")