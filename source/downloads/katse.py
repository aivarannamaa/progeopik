f = open('andmed2.txt')

nimi = f.readline()
vanus = f.readline()
aadress = f.readline()

print("Nimi:", nimi)
print("Vanus:", vanus, "aastat")
print("Aadress:", aadress)

f.close()