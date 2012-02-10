import os

kaust = input("Sisesta kausta nimi: ")

failinimed = os.listdir(kaust)

failide_arv = 0
for failinimi in failinimed:
    if failinimi[-4:] == ".mp3":
        print(failinimi)
        failide_arv = failide_arv + 1

print("Kokku oli " + str(failide_arv) + " faili")
