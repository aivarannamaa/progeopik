******************
5. I osa kokkuvõte
******************

.. todo::

    * Maini, et siiani tutvustati kahte liiki asju: universaalsed ja spetsiifilised. Olulised on universaalsed. Ei ole vaja eraldi meetodit 3 arvu kokku liitmiseks, kui on meetod 2 arvu kokku liitmiseks ja avaldiste kombineerimiseks. St. Pythoni reeglid on kavalalt valitud, et asjad universaalsete asjadega saaks teha spetsiifilisi asju. 
    
    * Otsi üldistavat lähenemist Evansi "Introduction to Computing"-ust
    * Lisalugemine formaalsetest keeltest


Väärtused ja avaldised
----------------------
Teises peatükis keskendusime põhiliselt Pythoni programmide kõige väiksematele, aga samas ka kõige tähtsamatele elementidele, millest ei saa üle ega ümber. Tegemist on lihtsate mõistetega, aga nende abstraktne olemus võib tekitada segadust, seepärast vaatame nende tähendused veelkord üle.

* **Väärtus** (nt. tekst `tere` või arv `3`) on mingi Pythoni maailma "asi", millega tehakse midagi (nt. kuvatakse ekraanile, kombineeritakse teiste väärtustega, võrreldakse, salvestatakse mällu vms). Väärtusi nimetatakse ka *andmeteks*.
* Igal väärtusel on mingi **tüüp** (nt. ``int`` või ``str``), see määrab ära, mida selle väärtusega teha saab.
* **Literaal** (nt. ``"tere"`` või ``3``) on mingi *konkreetse* väärtuse esitusviis programmi tekstis
* **Muutuja** (nt. ``laste_arv``) võimaldab esitada programmi tekstis mingit väärtust *kaudselt*, teisisõnu -- muutuja `viitab` mingile väärtusele. Muutuja loomiseks (või olemasoleva muutuja "sisu" uuendamiseks) on mõeldud `omistuslause` (nt. ``vanuse_alampiir = 21``). Muutujate abil saab programmis mainida ka väärtusi, mis selguvad alles programmi jooksutamisel (nt. ``nimi = input("Sisesta oma nimi: ")``). 
* **Funktsioon** (nt. ``print`` või ``sin``) on miski, mille abil saab midagi teha või arvutada. **Funktsiooni rakendamine e. väljakutse** (nt. ``print(nimi)`` või ``sin(0.5)``) tähistab mingit konkreetset tegevust või arvutust. Kui funktsioon on mõeldud millegi arvutamiseks, siis tema rakendamisel saame vastuseks mingi väärtuse. NB! Arvutamise all mõtleme suvaliste väärtustega, mitte ainult arvudega toimetamist.
* **Operaator** on olemuselt väga sarnane funktsiooniga, aga erinevalt funktsioonist kirjutatakse operaator oma `argumentide` vahele (nt. ``2 + 3``). Ka operaatori rakendamise tulemus on mingi väärtus.
* **Avaldis**: literaale ja muutujaid, väärtusega funktsioonide ning operaatorite rakendamisi võib omavahel kombineerida ükskõik kui keeruliselt (nt. ``x + 2 * 4`` või ``len("tere") + len(nimi.lower()) - 1``) -- taolist kombinatsiooni nimetatakse *avaldiseks*. Samas, ka üksik literaal või muutuja on avaldis -- tegemist on üldise mõistega, mis käib kõigi programmiosade kohta, millel on väärtus.
* Avaldisele vastava väärtuse väljaarvutamist nimetatakse **avaldise väärtustamiseks**. Avaldiste väärtustamine on üks Pythoni põhilistest tööülesannetest programmide jooksutamisel.

.. todo::

    Omistuslause

Arvud ja sõned
--------------
Konkreetsetest andmetüüpidest vaatlesime *täisarve*, *ujukomaarve* ja *sõnesid*.

* Täisarvude suurus pole Pythonis piiratud.
* Ujukomaarvude juures tuleb arvestada, et kõiki kümnendmurde ei suuda Python täpselt esitada.
* Sõne kirjapanekuks on mitmeid erinevaid viise.
* Enamik sõneoperatsioone on Pythonis realiseeritud `meetoditena` (nt. ``nimi.lower()``).

Sisend ja väljund
-----------------
Et programmi käivitamisel midagi üldse juhtuks, on vaja programmi kirjutada ka mingi *tegevus*, näiteks kasutajaga (või failisüsteemiga) suhtlemine.

* ``print`` kuvab etteantud väärtuse ekraanile.
* ``input`` küsib kasutajalt mingi tekstijupi ja *tagastab selle*, seega ``input("Sisesta oma nimi: ")`` on avaldis.
* Faili lugemiseks ja kirjutamiseks tuleb fail kõigepealt *avada* (``f = open("andmed.txt")`` või ``f2 = open("andmed2.txt", mode="w")``). Lugemiseks saab kasutada failimeetodeid ``read`` või ``readline`` (nt ``print(f.readline())``), kirjutamiseks meetodit ``write`` (nt ``f2.write(nimi + "\n")``).
    
Importimine
-----------
Kuna Pythoni standardteegis (ja teiste arendajate teekides) eksisteerib väga palju funktsioone, on nad organiseeritud *moodulitesse*. Moodulis olevatele funktsioonidele ligipääsemiseks on vaja kasutada *import lauset*. Sellel lausel on 3 erinevat varianti:

* ``from math import sin, cos`` -- üksikute funktsioonide importimine;
* ``from math import *`` -- kogu mooduli sisu importimine;
* ``import math`` -- mooduli enda importimine. Sel juhul tuleb funktsiooni nimi kirjutada koos mooduli nimega (``math.sin(0.5)``).


Tingimus- ja korduslaused
-------------------------
Kolmandas peatükis nägime, et Pythoni programm ei pruugi olla vaid lihtsate käskude jada, mida täidetakse üksteise järel kuni jõutakse programmi lõppu. Vaatlesime kahte programmikonstruktsiooni, millel mõlemal on **päis** ja tühikutega veidi paremale nihutatud **keha**, kusjuures kehas olevate lausete täitmise viis on mõlemal juhul erinev.

* **Tingimuslause** e. ``if``-lause peaharus olevad laused täidetakse ainult siis, kui päises esitatud tingimus kehtib. Kui tingimuslauses on olemas ka ``else`` haru, siis seal olevad laused täidetakse siis, kui tingimus *ei* kehti. Sellise konstruktsiooniga saab muuta programmi paindlikumaks, pannes selle käituma üht- või teistmoodi vastavalt olukorrale. Lisavõimalustena on Pythonis võimalik kirjutada ka üheharulisi (st. ilma ``else``-ta) ning mitmeharulisi (``elif``-iga) tingimuslauseid. 
* **Korduslause** e. tsükli puhul täidetakse kehas olevad laused vastavalt päisele 0 või rohkem korda. ``while``-lause korral kontrollitakse enne kehas olevate lausete täitmist, kas päises antud tingimus kehtib, nii nagu tingimuslausegi puhul. Erinevalt tingimuslausest minnakse peale keha täitmist uuesti tingimust kontrollima ja kui see kehtib endiselt, siis täidetakse kehas olevad laused uuesti jne. Seda protsessi korratakse niikaua, kuni tingimus enam ei kehti. Korduslausega saame kirjeldada protsesse, kus sama toimingut tuleb teha mitu korda järjest (ja seejuures ei pruugi me korduste arvu programmi kirjutamisel ette teada).

``if``- ja ``while``-lauseid nimetatakse Pythonis **liitlauseteks**. Liitlausete kehas võib kasutada suvalist liiki lauseid -- see võimaldab näiteks tingimuslauses lisaks lihtlausetele kasutada ka korduslauset, mille kehas on omakorda kasutatud tingmuslauset, mille kehas on veel üks tingimuslause jne.

Taolist lausete üksteise sisse panemist esitatakse Pythonis **treppimisega** -- samasse kehasse (e. plokki) kuuluvate lausete vasakud servad joondatakse tühikute abil sama kaugele. Liitlausete puhul joondatakse eelnevate ja järgnevate lausetega vaadeldava lause päis, keha nihutatakse päisega võrreldes veel rohkem paremale.


Tõeväärtused
------------
Üks oluline punkt nii ``if``- kui ``while``-lause juures on lause päises antud tingimusavaldis. Nagu eelnevalt mainitud, on avaldiste moodustamiseks lõputult võimalusi -- võib kasutada konstante, muutujaid, tehteid, funktsiooni väljakutseid või kõigi nende kombinatsioone. Tingimuse juures on oluline, et avaldise tüüp oleks tõeväärtus, st. avaldise väärtustamisel saadakse kas ``True`` või ``False``. Mitme tingimuse kombineerimiseks saab kasutada operaatoreid ``and`` ja ``or``, tingimuse "ümberpööramiseks" on operaator ``not``. Tingimuses saab kasutada ka isetehtud funktsioone, aga need peavad sel juhul tagastama tõeväärtuse.



Kombineeritavus
---------------
Nii avaldiste kui ka lausete juures on oluline see, et neid saab panna üksteise sisse. Näiteks operaatori ``+`` kasutuse üldskeem on ``<avaldis1> + <avaldis2>``, kusjuures nii ``avaldis1`` kui ka ``avaldis2`` võib olla samuti mingi liitmistehe. 

``if``-lause põhiskeem on:

.. sourcecode:: none

    if <avaldis>:
        <laused1>
    else:
        <laused2>

kusjuures nii ``laused1`` kui ka ``laused2`` võivad sisaldada suvalisi lauseid, sh. ``if``-lauseid, mille sees võib omakorda olla suvalisi lauseid.


Funktsioonid
------------
**Funktsiooni definitsiooni** kehas olevad laused jäetakse esialgu lihtsalt meelde. Neid saab hiljem käivitada kirjutades definitsiooni päises antud nime koos sulgudega -- seda nimetatakse *funktsiooni väljakutseks* e. rakendamiseks. Funktsioonid võimaldavad keerulise programmilõigu panna kirja vaid ühekordselt, aga kasutada seda mitmes erinevas kohas.

Kui muutujad võimaldavad meil töötada abstraktsemal tasemel, st. ilma et me peaksime mõtlema mingile konkreetsele väärtusele, siis funktsioonid võimaldavad meil midagi teha või arvutada, ilma et me peaksime mõtlema, kuidas seda toimingut või arvutust täpselt tehakse. Viska pilk peale järgnevale programmile:

.. sourcecode:: py3

    def kolmest_suurim(a, b, c):
        if a >= b and a >= c:
            return a
        elif b >= a and b >= c:
            return b
        else:
            return c
    
    print(kolmest_suurim(4, 15, 2))

Tõenäoliselt oskad isegi ilma funktsiooni definitsiooni süvenemata arvata, mida taoline programm ekraanile prindib. Põhjus on selles, et antud funktsiooni olemus tuleb välja juba tema nimest ja üldjuhul võime me eeldada, et funktsiooni tegelik definitsioon on tema nimele vastav. Seetõttu, kui meil on sobivad funktsioonid juba defineeritud, siis saame me programmi põhiosas (või järgmiste funktsioonide defineerimisel) töötada "kõrgemal tasemel" ilma "pisiasjade" pärast muretsemata.
