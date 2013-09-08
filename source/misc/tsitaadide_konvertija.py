f = open("tsitaadid.txt", encoding="utf-8")

sisu = f.read()
f.close()


allikas = "???"
i = 1


def save_file(sisu):
    fnimi = "tsitaadid/" + str(i).rjust(3, "0") + ".txt"
    f = open(fnimi, mode="w", encoding="utf-8")
    f.write(sisu.strip() + "\n\n-- " + allikas + "\n")
    f.close()


jupid = sisu.splitlines()
#print(jupid)

for jupp in jupid:
    if jupp.strip() == "":
        pass
    elif jupp[0] == '"' and not jupp.startswith('"Hukkunud Alp'):
        save_file(jupp)
        i += 1
    else:
        allikas = jupp.strip().strip(":")
        
        
        
