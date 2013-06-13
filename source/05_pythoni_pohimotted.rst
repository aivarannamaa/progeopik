5. Pythoni põhimõtted
========================

TODO Ülesanded
* counting digits (algul anna vigane variant (töötab vigaselt 0 ja -x puhul))

Kood vs. runtime
--------------------

igal tüübil on literaali süntaks ja operatsioonid/tähendus
code vs. data

kas 2 + 3 *on* 5?

Arvutamine vs. tegemine --> avaldised vs. laused
Mõtlemine vs. ütlemine !!!
Toetu mingile näitele eelmisest ptkst selle duaalsuse kirjutamisel!!!



Süntaks
----------------------

Operaatorid
~~~~~~~~~~~~~~~~~
Järgnev loetelu võtab kokku tähtsamate tehete prioriteedid (kõrgema prioriteediga tehted on ülalpool, samal real olevad operaatorid on sama prioriteediga):

    * ``**``
    * ``-x`` (*unaarne* miinus)
    * ``*``, ``/``, ``//``, ``%``
    * ``+``, ``-``
    * ``==``, ``!=``, ``<``, ``<=``, ``>``, ``>=``, ``in``
    * ``not``
    * ``and``
    * ``or``

Kahtluse korral kasuta soovitud tehete järjekorra määramiseks sulge.




Python vs. Scratch vs. Java
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Laused vs. avaldised
-----------------------

Arvutusmudel
--------------

Avaldised vs. väärtused
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
väärtused e. objektid

igalpool kus kasutad muutujat/literaali võib kasutada ka teisi avaldise vorme, sest lõppkokkuvõttes muudetakse kõik väärtuseks.

Mälu ja muutujad
~~~~~~~~~~~~~~~~~~~~~~
.. _milleks-muutujad:
    
Milleks muutujad?
~~~~~~~~~~~~~~~~~
.. _operatsioonid-muutujatega:
    

 

Moodulid
~~~~~~~~~~~~

Sisend ja väljund
~~~~~~~~~~~~~~~~~~

Funktsioonide tööpõhimõte
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

TODO: Intuitsioon vs. mehhanism -- ka peale arvutile asjade õpetamist jäävad tema teadmised ikkagi mehhaaniliseks. Loll masin.

On vaja mõista, et arvuti/Python tegutsevad vaid etteantud reeglite järgi, neil pole initsiatiivi ega mingisugust arukust. Kujuta ette kõige mõnda sinu arvates rumalat, tähenärijalikku aga agarat ja täpset inimest -- Python on temast palju rumalam, agaram ja täpsem. Üllataval kombel annab just Pythoni rumalus ja tähenärimine programmidele üheseltmõistetavuse ja konkreetsuse. Programmeerimise oskus on ühelt poolt tehniline (tuleb tunda teatud komplekti mõistetest ja konstruktsioonidest, mida Python mõistab), aga ennekõike on see oskus mõista lahendatava ülesande olemust ja panna lahendusidee kirja sellisel kujul, et ka sedavõrd rumal olevus nagu arvuti suudaks neid käske järgida. Programmeerimise protsess ei ole lineaarne -- probleemi parem mõistmine ja lahenduse kirjapanek käivad vaheldumisi. Alles siis, kui me peame oma teadmise või idee sõnadesse panema (nt. eesti keeles, aga eriti mõnes programmeerimiskeeles) avastame, et teatud kohad meie idees on jäänud häguseks. Kõige paremini õpib õpetades ja programmeerimine on arvuti õpetamine. 

Taoline detailne mõtlemine võib tunduda algul väga ebaloomulik, aga kui me soovime oma mõtteid täpselt ja ühetähenduslikult kirja panna, siis on see ainuke võimalus

Kokkuvõte
---------------
Väärtused ja avaldised
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Selles peatükis keskendusime põhiliselt Pythoni programmide kõige väiksematele, aga samas ka kõige tähtsamatele elementidele, millest ei saa üle ega ümber. Tegemist on lihtsate mõistetega, aga nende abstraktne olemus võib tekitada segadust, seepärast vaatame nende tähendused veelkord üle:

    * **Väärtus** (nt. tekst `tere` või arv `3`) on mingi Pythoni maailma "asi", millega tehakse midagi (nt. kuvatakse ekraanile, kombineeritakse teiste väärtustega, võrreldakse, salvestatakse mällu vms). Väärtusi nimetatakse ka *andmeteks*.
    * Igal väärtusel on mingi **tüüp** (nt. ``int`` või ``str``), see määrab ära, mida selle väärtusega teha saab
    * **Literaal** (nt. ``"tere"`` või ``3``) on mingi *konkreetse* väärtuse esitusviis programmi tekstis
    * **Muutuja** (nt. ``laste_arv``) võimaldab esitada programmi tekstis mingit väärtust *kaudselt*, teisisõnu -- muutuja `viitab` mingile väärtusele. Muutuja loomiseks (või olemasoleva muutuja "sisu" uuendamiseks) on mõeldud `omistuslause` (nt. ``vanuse_alampiir = 21``). Muutujate abil saab programmis mainida ka väärtusi, mis selguvad alles programmi jooksutamisel (nt. ``nimi = input("Sisesta oma nimi: ")``).
    * **Funktsioon** (nt. ``print`` või ``sin``) on miski, mille abil saab midagi teha või arvutada. **Funktsiooni rakendamine e. väljakutse** (nt. ``print(nimi)`` või ``sin(0.5)``) tähistab mingit konkreetset tegevust või arvutust. Kui funktsioon on mõeldud millegi arvutamiseks, siis tema rakendamisel saame vastuseks mingi väärtuse. NB! arvutamise all mõtleme suvaliste väärtustega toimetamist, mitte ainult arvudega.
    * **Operaator** on olemuselt väga sarnane funktsioonile, aga erinevalt funktsioonist kirjutatakse operaator oma `argumentide` vahele (nt. ``2 + 3``). Ka operaatori rakendamise tulemuseks on mingi väärtus.
    * **Avaldis**: literaale, muutujaid ja väärtusega funktsioonide ning operaatorite rakendamisi võib omavahel kombineerida ükskõik kui keeruliselt (nt. ``x + 2 * 4`` või ``len("tere") + len(nimi.lower()) - 1``) -- taolist kombinatsiooni nimetatakse *avaldiseks*. Samas, ka üksik literaal või muutuja on avaldis -- *tegemist on üldise mõistega*, mis käib kõigi programmiosade kohta, millel on väärtus.
    * Avaldisele vastava väärtuse väljaarvutamist nimetatakse **avaldise väärtustamiseks**. Avaldiste väärtustamine on üks Pythoni põhilistest tööülesannetest programmide jooksutamisel.

Arvud ja sõned
~~~~~~~~~~~~~~
Konkreetsetest andmetüüpidest vaatlesime *täisarve*, *ujukomaarve* ja *sõnesid*:

    * Täisarvude suurus pole Pythonis piiratud
    * Ujukomaarvude juures tuleb arvestada, et kõiki kümnendmurde ei suuda Python täpselt esitada
    * Sõne kirjapanekuks on mitmeid erinevaid viise
    * Enamik sõneoperatsioone on Pythonis realiseeritud `meetoditena` (nt. ``nimi.lower()``)

Sisend ja väljund
~~~~~~~~~~~~~~~~~~~
Et programmi käivitamisel midagi üldse juhtuks, on vaja programmi kirjutada ka mingi *tegevus*, näiteks kasutajaga (või failisüsteemiga) suhtlemine:

    * ``print`` kuvab etteantud väärtuse ekraanile
    * ``input`` küsib kasutajalt mingi tekstijupi ja *tagastab selle*, seega ``input("Sisesta oma nimi: ")`` on avaldis
    * faili lugemiseks ja kirjutamiseks tuleb fail kõigepealt *avada* (``f = open("andmed.txt")`` või ``f2 = open("andmed2.txt", mode="w")``). Lugemiseks saab kasutada failimeetodit ``readline`` (nt ``print(f.readline())``), kirjutamiseks meetodit ``write`` (nt ``f2.write(nimi + "\n")``).
    
Importimine
~~~~~~~~~~~~
Kuna Pythonis standardteegis (ja teiste arendajate teekides) eksisteerib väga palju funktsioone, on nad organiseeritud *moodulitesse*. Moodulis olevatele funktsioonidele ligipääsemiseks on vaja kasutada *import lauset*. Sellel lausel on 3 erinevat varianti:

    * ``from math import sin, cos`` -- üksikute funktsioonide importimine
    * ``from math import *`` -- kogu mooduli sisu importimine
    * ``import math`` -- mooduli enda importimine. Sel juhul tuleb funktsiooni nimi kirjutada koos mooduli nimega (``math.sin(0.5)``)

Avaldised vs. laused
~~~~~~~~~~~~~~~~~~~~~~~~
Selle peatüki programmide puhul saame programmi iga rida nimetada **lauseks**. Pythoni programm polegi muud, kui lausete jada. Avaldisi kasutatakse vaid lausete koosseisus. Need lauseliigid mida me kohtasime olid:

    * import-lause, nt. ``from math import sin``
    * omistuslause, nt. ``vanus = input("Sisesta nimi: ")``. Selle lauseliigi *komponentideks* on muutuja nimi, võrdusmärk ja suvaline avaldis.
    * "käsulause", nt. ``print("Tere!")`` (tehniline termin selle lauseliigi kohta on *avaldislause*, sest formaalselt loetakse Pythonis ka tegevust väljendav funktsiooni väljakutse avaldiseks)
    
Kuna nende lauseliikide korral kulub iga lause jaoks täpselt üks rida, nimetatakse neid *lihtlauseteks*. Keerulisematest lausetest tuleb juttu järgmises peatükis. 




