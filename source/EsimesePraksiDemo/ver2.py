import os

kaust= input("Sisesta kausta nimi: ")
laiend = input("Sisesta laiend: ")

failinimed = os.listdir(kaust)
# print(len(failinimed))

failide_arv = 0
for failinimi in failinimed:
    if failinimi[-(len(laiend)+1):] == "." + laiend:
        print(failinimi)
        failide_arv = failide_arv + 1

print("Kokku oli " + str(failide_arv) + " faili")
