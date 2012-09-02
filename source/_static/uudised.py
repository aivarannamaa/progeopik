from urllib.request import urlopen
from xml.dom.minidom import parse
from time import strftime
import locale

# Nõuame süsteemi vaikeeelistusi nädalapäeva ja kuu esitamisel
locale.setlocale(locale.LC_ALL, '')
# Päis
print("Täna on", strftime('%A, %d. %B %Y'))
print("Kell on", strftime('%H:%M'))
print()


# Loeme sisse ERR uudiste ülevaate XML kujul ja nopime
# sealt välja ainult 10 värskema uudise pealkirjad
f = urlopen('http://uudised.err.ee/uudised_rss.php')
dom = parse(f) # parse annab lehekülje sisu struktuursel kujul
pealkirjad = dom.getElementsByTagName("title")
print("ERR uudised:")
loendur = 0
for pealkiri in pealkirjad:
    tekst = pealkiri.childNodes[0].data
    if tekst != "uudised.err.ee - online": 
        print('  *', tekst)
        
    loendur += 1
    if loendur == 10:
        break

f.close()
print()


# Kõigilt veebilehtedelt ei saa eriti kergelt kätte struktuurset infot.
# Selleks, et saada TÜ füüsikahoone ilmajaama kodulehelt kätte hetketemperatuuri,
# otsime vastava tekstijupi üles selle ees ja järel olevate kindlate
# tekstijuppide järgi
f = urlopen("http://meteo.physic.ut.ee/et/frontmain.php?m=2") 
sisu = str(f.read()) # loeme kogu lehekülje sisu sõnena sisse
f.close()

vasak_naaber = 'Temperatuur</A></TD><TD align="left" width="45%"><B>'
parem_naaber = ' &deg;C'
algus = sisu.find(vasak_naaber) + len(vasak_naaber)
lopp = sisu.find(parem_naaber)
temperatuur = float(sisu[algus:lopp])
hinnang = ""
if temperatuur < -20:
    hinnang = "pane ikka kindad ka kätte, kui välja lähed"
elif temperatuur > 35:
    hinnang = "otsi veekogu ja mine kaelani vette"
else:
    hinnang = "normaalne ilm"

print("Temperatuur Tartus:", temperatuur, "(" + hinnang + ")")



