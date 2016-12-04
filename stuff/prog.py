f = open("../source/downloads/sonad.txt", encoding="UTF-8")

j = {}

for sõna in f.read().splitlines():
        for i in range(len(sõna)-1):
            if sõna[i] == "i":
                järgm = sõna[i+1]
                j[järgm] = j.get(järgm, 0) + 1
                if järgm in "aeouõäöü" and len(sõna) < 6:
                    print(sõna)
    

f.close()
print(j)
