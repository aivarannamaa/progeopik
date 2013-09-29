******************
5. I osa kokkuvõte
******************


Väärtused ja avaldised
----------------------
Teises peatükis keskendusime põhiliselt Pythoni programmide kõige väiksematele, aga samas ka kõige tähtsamatele elementidele, millest ei saa üle ega ümber. Tegemist on lihtsate mõistetega, aga nende abstraktne olemus võib tekitada segadust, seepärast vaatame nende tähendused veelkord üle:

    * **Väärtus** (nt. tekst `tere` või arv `3`) on mingi Pythoni maailma "asi", millega tehakse midagi (nt. kuvatakse ekraanile, kombineeritakse teiste väärtustega, võrreldakse, salvestatakse mällu vms). Väärtusi nimetatakse ka *andmeteks*.
    * Igal väärtusel on mingi **tüüp** (nt. ``int`` või ``str``), see määrab ära, mida selle väärtusega teha saab
    * **Literaal** (nt. ``"tere"`` või ``3``) on mingi *konkreetse* väärtuse esitusviis programmi tekstis
    * **Muutuja** (nt. ``laste_arv``) võimaldab esitada programmi tekstis mingit väärtust *kaudselt*, teisisõnu -- muutuja `viitab` mingile väärtusele. Muutuja loomiseks (või olemasoleva muutuja "sisu" uuendamiseks) on mõeldud `omistuslause` (nt. ``vanuse_alampiir = 21``). Muutujate abil saab programmis mainida ka väärtusi, mis selguvad alles programmi jooksutamisel (nt. ``nimi = input("Sisesta oma nimi: ")``). 
    * **Funktsioon** (nt. ``print`` või ``sin``) on miski, mille abil saab midagi teha või arvutada. **Funktsiooni rakendamine e. väljakutse** (nt. ``print(nimi)`` või ``sin(0.5)``) tähistab mingit konkreetset tegevust või arvutust. Kui funktsioon on mõeldud millegi arvutamiseks, siis tema rakendamisel saame vastuseks mingi väärtuse. NB! arvutamise all mõtleme suvaliste väärtustega toimetamist, mitte ainult arvudega.
    * **Operaator** on olemuselt väga sarnane funktsioonile, aga erinevalt funktsioonist kirjutatakse operaator oma `argumentide` vahele (nt. ``2 + 3``). Ka operaatori rakendamise tulemuseks on mingi väärtus.
    * **Avaldis**: literaale, muutujaid ja väärtusega funktsioonide ning operaatorite rakendamisi võib omavahel kombineerida ükskõik kui keeruliselt (nt. ``x + 2 * 4`` või ``len("tere") + len(nimi.lower()) - 1``) -- taolist kombinatsiooni nimetatakse *avaldiseks*. Samas, ka üksik literaal või muutuja on avaldis -- *tegemist on üldise mõistega*, mis käib kõigi programmiosade kohta, millel on väärtus.
    * Avaldisele vastava väärtuse väljaarvutamist nimetatakse **avaldise väärtustamiseks**. Avaldiste väärtustamine on üks Pythoni põhilistest tööülesannetest programmide jooksutamisel.

.. todo::

    Omistuslause

Arvud ja sõned
--------------
Konkreetsetest andmetüüpidest vaatlesime *täisarve*, *ujukomaarve* ja *sõnesid*:

    * Täisarvude suurus pole Pythonis piiratud
    * Ujukomaarvude juures tuleb arvestada, et kõiki kümnendmurde ei suuda Python täpselt esitada
    * Sõne kirjapanekuks on mitmeid erinevaid viise
    * Enamik sõneoperatsioone on Pythonis realiseeritud `meetoditena` (nt. ``nimi.lower()``)

Sisend ja väljund
-----------------
Et programmi käivitamisel midagi üldse juhtuks, on vaja programmi kirjutada ka mingi *tegevus*, näiteks kasutajaga (või failisüsteemiga) suhtlemine:

    * ``print`` kuvab etteantud väärtuse ekraanile
    * ``input`` küsib kasutajalt mingi tekstijupi ja *tagastab selle*, seega ``input("Sisesta oma nimi: ")`` on avaldis
    * faili lugemiseks ja kirjutamiseks tuleb fail kõigepealt *avada* (``f = open("andmed.txt")`` või ``f2 = open("andmed2.txt", mode="w")``). Lugemiseks saab kasutada failimeetodeid ``read`` või ``readline`` (nt ``print(f.readline())``), kirjutamiseks meetodit ``write`` (nt ``f2.write(nimi + "\n")``).
    
Importimine
-----------
Kuna Pythonis standardteegis (ja teiste arendajate teekides) eksisteerib väga palju funktsioone, on nad organiseeritud *moodulitesse*. Moodulis olevatele funktsioonidele ligipääsemiseks on vaja kasutada *import lauset*. Sellel lausel on 3 erinevat varianti:

    * ``from math import sin, cos`` -- üksikute funktsioonide importimine
    * ``from math import *`` -- kogu mooduli sisu importimine
    * ``import math`` -- mooduli enda importimine. Sel juhul tuleb funktsiooni nimi kirjutada koos mooduli nimega (``math.sin(0.5)``)


Tingimus- ja korduslaused
-------------------------
Kolmandas peatükis nägime, et Pythoni programm ei pruugi olla vaid lihtsate käskude jada, mida täidetakse üksteise järel kuni jõutakse programmi lõppu. Vaatlesime kolme programmikonstruktsiooni, millel kõigil on **päis** ja tühikutega veidi paremale nihutatud **keha**, kusjuures kehas olevate lausete täitmise viis on kõigil kolmel juhul erinev:

    * **Tingimuslause** e. ``if``-lause peaharus olevad laused täidetakse ainult siis, kui päises esitatud tingimus kehtib. Kui tingimuslauses on olemas ka ``else`` haru, siis seal olevad laused täidetakse siis, kui tingimus *ei* kehti. Sellise konstruktsiooniga saab muuta programme paindlikumaks, pannes selle käituma üht- või teistmoodi vastavalt olukorrale. Lisavõimalustena on Pythonis võimalik kirjutada ka üheharulisi tingimuslauseid (st. ilma ``else``-ta) ning mitmeharulisi (``elif``-iga). 
    * **Korduslause** e. tsükli puhul täidetakse kehas olevad laused 0 või rohkem korda, vastavalt päisele. ``while``-lause korral kontrollitakse enne kehas olevate lausete täitmist, kas päises antud tingimus kehtib, justnagu tingimuslausegi puhul. Erinevalt tingimuslausest, minnakse peale keha täitmist uuesti tingimust kontrollima ja kui see kehtib endiselt, siis täidetakse kehas olevad laused uuesti jne. Seda protsessi korratakse niikaua, kuni tingimus enam ei kehti. Korduslausega saame kirjeldada protsesse, kus sama toimingut tuleb teha mitu korda järjest (ja seejuures ei pruugi me korduste arvu programmi kirjutamisel ette teada).
    * **Andmetüüp bool** - Üks oluline punkt nii ``if``- kui ``while``-lause juures on lause päises antud tingimusavaldis. Nagu eelnevalt mainitud, on avaldiste moodustamiseks lõputult võimalusi -- võib kasutada konstante, muutujaid, tehteid, funktsiooni väljakutseid, või kõigi nende kombinatsioone. ingimusavaldise juures on oluline, et avaldise tüüp oleks tõeväärtus, st. avaldise väärtustamisel saadakse kas ``True`` või ``False``. Mitme tingimuse kombineerimiseks saab kasutada operaatoreid ``and`` ja ``or``, tingimuse "ümberpööramiseks" on operaator ``not``. Tingimuses saab kasutada ka isetehtud funktsioone, aga need peavad sel juhul tagastama tõeväärtuse.


``if``- ja ``while``-lauseid nimetatakse Pythonis **liitlauseteks**. Liitlausete kehas võib kasutada suvalist liiki lauseid -- see võimaldab näiteks tingimuslauses lisaks lihtlausetele kasutada ka korduslauset, mille kehas on omakorda kasutatud tingmuslauset, mille kehas on veel üks tingimuslause jne.

Taolist lausete üksteise sisse panemist esitatakse Pythonis **treppimisega** -- samasse kehasse (e. plokki) kuuluvate lausete vasakud servad joondatakse tühikute abil sama kaugele. Liitlausete puhul joondatakse eelnevate ja järgnevate lausetega vaadeldava lause päis, keha nihutatakse päisega võrreldes veel rohkem paremale.


Kombineeritavus
---------------
Nii avaldiste, kui lausete juures on oluline see, et neid saab panna üksteise sisse. Näiteks operaatori ``+`` kasutuse üldskeem on ``<avaldis1> + <avaldis2>``, kusjuures nii ``avaldis1`` kui ``avaldis2`` võib olla samuti mingi liitmistehe. 

``if``-lause põhiskeem on:

.. sourcecode:: none

    if <avaldis>:
        <laused1>
    else:
        <laused2>

kusjuures nii ``laused1``, kui ``laused2`` võivad sisaldada suvalisi lauseid, sh. ``if``-lauseid, mille sees võib olla omakorda suvalisi lauseid.


Funktsioonid
------------
**Funktsiooni definitsiooni** kehas olevad laused jäetakse esialgu lihtsalt meelde. Neid saab hiljem käivitada kirjutades definitsiooni päises antud nime koos sulgudega -- seda nimetatakse *funktsiooni väljakutseks* e. rakendamiseks. Funktsioonid võimaldavad keerulise programmilõigu panna kirja vaid ühekordselt, aga kasutada seda mitmes erinevas kohas.

Kui muutujad võimaldavad meil töötada abstraktsemal tasemel, st. ilma, et me peaksime mõtlema mingile konkreetsele väärtusele, siis funktsioonid võimaldavad meil midagi teha või arvutada ilma, et me peaksime mõtlema kuidas see toiming või arvutus täpselt tehakse. Viska pilk peale järgnevale programmile:

.. sourcecode:: py3

    def kolmest_suurim(a, b, c):
        if a > b and a > c:
            return a
        elif b > a and b > c:
            return b
        else:
            return c
    
    print(kolmest_suurim(4, 15, 2))

Tõenäoliselt oskad isegi ilma funktsiooni definitsiooni süvenemata arvata, mida taoline programm ekraanile prindib. Põhjus on selles, et antud funktsiooni olemus tuleb välja juba tema nimest ja üldjuhul võime me eeldada, et funktsiooni tegelik definitsioon on tema nimele vastav. Seetõttu, kui meil on sobivad funktsioonid juba defineeritud, siis saame me programmi põhiosas (või järgmiste funktsioonide defineerimisel) töötada "kõrgemal tasemel", ilma "pisiasjade" pärast muretsemata.


Ülesanded
=========


2. Kuupäeva kontrollimine
-------------------------
Täienda oma eelmise peatüki kuupäeva kuvamise programmi lisades sinna kuupäeva kontrollimise. Kirjuta selleks funktsioon ``on_legaalne_kuupäev``, mis võtab argumentideks päeva, kuu ja aasta numbrid ja tagastab ``True`` või ``False`` vastavalt sellele, kas antud komponentidest saab moodustada kuupäeva või mitte. 

Soovitav on luua ka kaks abifunktsiooni: 1) ``on_liigaasta``, mis tagastab ``True``, kui etteantud aasta on liigaasta ja ``False`` muudel juhtudel, ning 2) ``päevade_arv``, mis etteantud kuu ja aasta numbri kohta ütleb, mitu päeva selles kuus on.

Lõpuks muuda funktsiooni ``kuupäev_sõnena`` nii, et kui ette antakse mittelegaalsed kuupäeva komponendid (nt. ``kuupäev_sõnena(29, 2, 2013)`` või ``kuupäev_sõnena(14, 13, 2000)``), siis tagastatakse vastav veateade.

Loodud funktsioone peaks saama kasutada näiteks nii:

.. sourcecode:: py3

    >>> on_liigaasta(1900)
    False
    >>> on_liigaasta(1904)
    True
    >>> on_liigaasta(2000)
    True
    >>> on_liigaasta(2013)
    False
    >>> päevade_arv(1, 2012)
    31
    >>> päevade_arv(2, 2012)
    29
    >>> päevade_arv(2, 2013)
    28
    >>> on_legaalne_kuupäev(29, 2, 2013)
    False
    >>> on_legaalne_kuupäev(22, 2, 2013)
    True
    >>> kuupäev_sõnena(29, 2, 2013)
    'Vigane kuupäev'
    >>> kuupäev_sõnena(14, 13, 2000)
    'Vigane kuupäev'
    >>> kuupäev_sõnena(14, 10, 2013)
    '14. Oktoober 2013'



3. Klaveri mahutamine
---------------------
Ülikool on ostnud endale uue klaveri peahoone aula tarbeks. Paraku unustati  kontrollida, kas see klaver üldse välisuksest sisse mahub. Kirjutada programm, mis küsib kasutajalt klaverit sisaldava kasti kolm mõõdet (pikkus, laius, kõrgus) ning ukse laiuse ja kõrguse ning vastab, kas klaver on võimalik aulasse sisse toimetada. 

.. note::

    üeldame, et klaverikasti võib ükskõik kuidas keerata, st. ükskõik milline kasti tahk võib jääda peale. Samas võib eeldada, et kasti ei üritata põigiti uksest läbi mahutada.

4. Pitsapood
------------
Kirjuta programm, mis küsib kasutajalt infot tellitava pitsa suuruse, komponentide ja kättetoimetamise detailide kohta. Igal sammul tuleks esitada kasutajale võimalikud valikud koos vastavate koodidega, nt:

.. sourcecode:: none

    ...
    ...
    Millise suurusega pitsat soovid? Valikud on:
      1 - väike (18cm)
      2 - keskmine (25cm)
      3 - suur (35cm)
    Palun sisesta oma valik: 2
    ...
    ...
    Mida lisada pitsa peale? 
      0 - rohkem mitte midagi
      1 - juust
      2 - vorst
      3 - ...   
      4 - ...   
    ...
    ...
    Kuidas pitsa kohale toimetada? 
      1 - tulen ise järele
      2 - sisestan aadressi ja telefoninumbri
    ...
    
Pitsakatte komponente peaks saama valida ükskõik kui palju. Aadressi küsida ainult siis, kui kasutaja ei soovi ise järele tulla. Kogutud andmed salvestada tekstifaili.


Lisalugemine
============

Midagi programmeerimiskeelte kohta
----------------------------------
TODO


Python tutorial
---------------
sh. tour of std library 

Moodulite loomine
-----------------
Kõikide selle õpiku ülesannete puhul piisab, kui terve su programm koosneb ainult ühest failist. Samas, suuremate programmide juures on mõistlik organiseerida programmi jaoks loodud funktsioonid teemade kaupa eraldi *moodulitesse*, samamoodi nagu Pythoniga kaasatulevad funktsioonid on jaotatud eraldi moodulitesse. 

Uue mooduli loomine on Pythonis imelihtne -- funktsioonide (või muutujate) definitsioonid tuleb lihtsalt salvestada tavalisse *.py*-laiendiga faili. Mooduli nimeks saab seejuures tema failinimi ilma *.py*-laiendita. Selleks, et neid funktsioone saaks kasutada teistes failides, tuleb seal teha sobiv ``import``, just nagu sa tegid ``math`` või ``turtle`` mooduli kasutamiseks. 

.. note::
 
    Siit tuleb ka välja, miks esimese peatüki kilpkonna ülesannete juures märgiti, et oma faili nimeks ei tohiks panna `turtle.py` -- sellega varjaks sa ära Pythoni enda mooduli nimega ``turtle``.



Eelneva jutu demonstreerimiseks loome ühe lihtsa mooduli (nimega ``minumoodul``) ja ühe skripti, kus me seda moodulit kasutame.

.. sourcecode:: py3

    # eeldan, et see kood asub failis nimega minumoodul.py
    
    def suramura(x):
        return x * 34 - 123
    
    nipitiri = 888776


.. sourcecode:: py3

    # See on peaskript, e. see, mida käivitatakse
    # Selle faili nimi pole tähtis, aga oletame, et see on minuskript.py
    
    from minumoodul import suramura, nipitiri
    
    spunk = suramura(45) 
    print(nipitiri)
    print(spunk)


Kui need failid on salvestatud samasse kausta, siis peaskripti käivitamisel (täpsemalt lause ``from minumoodul import suramura, nipitiri`` täitmisel) otsib Python üles ka faili ``minumoodul.py``, käivitab selle ja teeb seal defineeritud funktsiooni ``suramura`` ja muutuja ``nipitiri`` programmi põhiosas kättesaadavaks.

.. admonition:: Lisavõimalus

    Kui sa oled loonud mingi üldise otstarbega mooduli ja soovid seda kasutada erinevate programmide juures, siis sa võibolla ei viitsi seda alati iga uue programmi kausta kopeerida. Sel juhul tuleks moodul kopeerida ühte spetsiaalsesse kausta, kuhu Python alati vaatab, kui ``import`` lauses mainitud moodulit programmi kaustas pole. Vaata täpsemalt siit: http://docs.python.org/3/tutorial/modules.html#the-module-search-path.



Näide: Tõeväärtusfunktsioonid
-----------------------------
TODO:

