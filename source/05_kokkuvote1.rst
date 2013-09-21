******************
5. I osa kokkuvõte
******************

.. attention::

    Selle peatüki materjali veel täiendatakse



.. todo::

    * counting digits (algul anna vigane variant (töötab vigaselt 0 ja -x puhul))
    * märgi ära or'i ja and'i shortcut evaluation
    * ülesanded kombineeritavuse kohta (sh. tõeväärtusavaldised, samaväärsused)
    * conditional vs alternative execution ???
    * chained & nested conditionals (st. keele poolt pakutavad mugavus-alternatiivid)
    * if-harudes toimingu kordamine eri argumendiga vs. muutujasse salvestamine ja pärast toimingu tegemine muutujaga
    * Harjutus loogiliste avaldiste samaväärsuse kontrollimiseks (õpeta ka testima)
    * Harjutus "wrap this code in a function"
    * tabelite genereerimine
    * kilpkonnaga rooma numbrite joonistamine
    * kalendri printimine
    * etteantud 2-3 muutujaga tõeväärtustabeli põhjal avaldise kirjutamine
    * Kuidas Python paneb sulge rohkem kui 1 operatsiooni korral
    * fact defineerimine rekursiivselt (ilma rekursiooni mainimata?)
    


Kood vs. runtime
================

igal tüübil on literaali süntaks ja operatsioonid/tähendus
code vs. data

kas 2 + 3 *on* 5?

Arvutamine vs. tegemine --> avaldised vs. laused
Mõtlemine vs. ütlemine !!!
Toetu mingile näitele eelmisest ptkst selle duaalsuse kirjutamisel!!!



Süntaks
=======

Operaatorid
-----------
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
---------------------------

Laused vs. avaldised
====================

Arvutusmudel
============

Avaldised vs. väärtused
-----------------------
väärtused e. objektid

igalpool kus kasutad muutujat/literaali võib kasutada ka teisi avaldise vorme, sest lõppkokkuvõttes muudetakse kõik väärtuseks.

Mälu ja muutujad
----------------
.. _milleks-muutujad:
    
Milleks muutujad?
-----------------
.. _operatsioonid-muutujatega:
    

 

Moodulid
--------

Sisend ja väljund
-----------------

Funktsioonide tööpõhimõte
-------------------------

TODO: Intuitsioon vs. mehhanism -- ka peale arvutile asjade õpetamist jäävad tema teadmised ikkagi mehhaaniliseks. Loll masin.

On vaja mõista, et arvuti/Python tegutsevad vaid etteantud reeglite järgi, neil pole initsiatiivi ega mingisugust arukust. Kujuta ette kõige mõnda sinu arvates rumalat, tähenärijalikku aga agarat ja täpset inimest -- Python on temast palju rumalam, agaram ja täpsem. Üllataval kombel annab just Pythoni rumalus ja tähenärimine programmidele üheseltmõistetavuse ja konkreetsuse. Programmeerimise oskus on ühelt poolt tehniline (tuleb tunda teatud komplekti mõistetest ja konstruktsioonidest, mida Python mõistab), aga ennekõike on see oskus mõista lahendatava ülesande olemust ja panna lahendusidee kirja sellisel kujul, et ka sedavõrd rumal olevus nagu arvuti suudaks neid käske järgida. Programmeerimise protsess ei ole lineaarne -- probleemi parem mõistmine ja lahenduse kirjapanek käivad vaheldumisi. Alles siis, kui me peame oma teadmise või idee sõnadesse panema (nt. eesti keeles, aga eriti mõnes programmeerimiskeeles) avastame, et teatud kohad meie idees on jäänud häguseks. Kõige paremini õpib õpetades ja programmeerimine on arvuti õpetamine. 

Taoline detailne mõtlemine võib tunduda algul väga ebaloomulik, aga kui me soovime oma mõtteid täpselt ja ühetähenduslikult kirja panna, siis on see ainuke võimalus

Loogiliste avaldiste samaväärsus
--------------------------------
Tihti on teatud tähendusega tõeväärtusavaldist võimalik kirjutada mitmel erineval kujul, näiteks:

    * ``not (x or y)`` on sama, mis ``(not x) and (not y)``
    * ``not (x and y)`` on sama, mis ``(not x) or (not y)``

Samaväärsetest variantidest tuleks valida selline, mis toob avaldise mõtte paremini esile.



Tõeväärtusega funktsioonid
--------------------------
Kui programmis on mitmes kohas vaja kontrollida sarnast tingimust, siis võib selle tingimuse panna kirja funktsioonina, mis tagastab tõeväärtuse. Järgnev programm  demonstreeribki tõeväärtusega funktsiooni loomist ja kasutamist:

.. sourcecode:: py3

    def on_positiivne_paarisarv(x):
        return (x > 0) and (x % 2 == 0)

    arv = int(input("Sisesta arv: "))
    if on_positiivne_paarisarv(arv):
        print("Arv on positiivne ja paaris")
    else:
        print("Arv pole positiivne või pole paaris")

Harjutus 3. Liigaasta tuvastamine
---------------------------------
Kirjuta funktsioon ``on_liigaasta``, mis võtab argumendiks aastaarvu ning **tagastab tõeväärtuse** vastavalt sellele, kas antud aasta on liigaasta või mitte.

Kirjuta programm, mis küsib kasutajalt aastaarvu ning väljastab ekraanile info selle kohta, kas tegemist on liigaastaga või mitte. Liigaasta tuvastamiseks kasuta eelnevalt defineeritud funktsiooni.

.. hint::

    Liigaasta on selline, kus aastaarv jagub 4-ga, välja arvatud juhud, kus aastaarv jagub 100-ga, aga ei jagu 400-ga. Näiteks aastad 2004 ja 2000 on liigaastad aga 1900 mitte.

.. note::
    Kui programmis läheb mõni lause liiga pikaks, siis võid ta kirjutada mitmele reale, aga sel juhul tuleb rea "murdmise" koht märkida ära langkriipsuga (``\``):
    
    .. sourcecode:: py3
    
        tulemus = (see >= teine * math.pi) \
            and (niimoodi or naamoodi) \
            and (x > y or u != 1)
        

    Sellist rea murdmist võib kasutada suvaliste lausete korral. Murda ei saa vaid sõneliteraali ja kommentaaari sees.



Harjutus 4. Päevade arv kuus
----------------------------
Kirjuta funktsioon ``päevade_arv``, mis võtab argumendiks kuu numbri ja aastaarvu ning tagastab mitu päeva on selles kuus. Kasuta abifunktsioonina eelnevalt defineeritud funktsiooni ``on_liigaasta``. (Kirjuta need funktsioonid samasse faili).

Harjutus 5. Kuupäeva kontrollimine
----------------------------------
Kirjuta funktsioon ``on_legaalne_kuupäev``, mis võtab argumendiks päeva, kuu ja aasta (arvudena) ning tagastab tõeväärtuse vastavalt sellele, kas argumentidele vastav kuupäev on legaalne või mitte. Kasuta abifunktsioonidena eelmistes ülesannetes defineeritud funktsioone.

Testi loodud funktsiooni järgnevate avaldistega:

    - ``on_legaalne_kuupäev(31, 1, 2001)``
    - ``on_legaalne_kuupäev(29, 2, 2001)``
    - ``on_legaalne_kuupäev(29, 2, 2000)``

    



Kokkuvõte
=========


Funktsioonid vs. muutujad
=========================
TODO: Räägi siin ka importimisest

.. admonition:: Nimede tähtsus

    TODO: Tee näiteprogramm, kus muutujanimed on a,b,c,x,y,z ja lase lugejal arvata, mida see programm teeb, pärast näita nimedega varianti. peab olema meeldejääv, sest seda on tarvis tagasi viidata



Avaldiste kombineerimine
========================
Me oleme nüüdseks kasutanud mitut viisi Pythoni maailma "asjade" e. väärtuste kirjeldamiseks. Konkreetsed väärtused pannakse kirja *literaalina* (nt. ``2.5`` või ``"Tere!"``). Mõnikord on mugavam väärtusele viidata hoopis läbi *muutuja* (nt. ``x``). Enamasti aga on meil programmi kirjutamise ajal väärtuse asemel teada hoopis selle leidmise "valem", mille me paneme kirja Pythoni *tehte* e. *operatsioonina* (nt. ``sin(x) * 2 - 1`` või ``nimi.upper()``). Kõik need viisid kannavad ühist nimetust *avaldis*.

Kahtlemata on neist kolmest avaldise liigist kõige põnevam arvutustehe -- on ju arvutamine üks põhjus miks programme üldse kirjutatakse. Loodetavasti märkasid, et Pythoni arvutustehetel on üks oluline omadus, mis tõstab ta peajagu kõrgemale taskukalkulaatoritest -- tehete komponentideks võivad olla suvalist liiki avaldised, st. mitte ainult konkreetsed väärtused vaid ka muutujad või mingid muud tehted, mis võivad omakorda koosneda konkreetsetest väärtustest, muutujatest või tehetest, mis võivad omakorda ... jne. Seetõttu nimetatakse tehete komponente vahel üldistavalt *alamavaldisteks*.

Kokkuvõttes, **igal pool, kus saab kasutada mingit konkreetset väärtust, saab kasutada ka muutujat või mingit tehet**, või veel üldisemalt, **igal pool, kus saab kasutada ühte avaldise liiki, saab kasutada ka teisi**. Siit tuleb ka välja miks me literaale, muutujaid ja tehteid koos vaatasime ning miks neile on välja mõeldud ühine nimetus -- hoolimata nende erinevast iseloomust kuuluvad nad Pythoni jaoks ühte perekonda.

Toome järgnevalt mõned näited avaldistest mis koosnevad erinevatest alamavaldistest:

TODO: näide

Tehniliselt võttes ühendab erinevaid avaldise liike see, et neil kõigil on *väärtus* -- literaalide puhul on väärtus otseselt kirja pandud, muutuja kasutamisel vaatab Python järele selle defineerimisel antud väärtuse, tehete väärtuse leidmiseks tuleb teha vastavad arvutused. Asjaolu, et Python suudab genereerida igale avaldisele väärtuse ja et reaalne arvutamine (nt. liitmine) toimub justnimelt väärtustega, ongi see, mis võimaldab meil erinevat liiki avaldisi nii vabalt kombineerida.

Harjutus x
----------
TODO: sõne- ja arvavaldise kombineerimine


Abimuutujate kasutamine
-----------------------
See, et meil on võimalik kirjutada väga keerulisi arvutusi ühe avaldisena, ei tähenda, et seda tuleks tingimata teha -- tihti on lihtsam jagada arvutus *abimuutujate* abil mitmeks sammuks:

TODO: näide

Taoline sammukaupa arvutamine võimaldab ka kergemini leida üles viga, kui ilmneb, et arvutuse tulemus ei ole õige, selleks tuleb iga sammu järel kuvada vahetulemus ekraanile, mispeale peaks olema lihtne tuvastada, millises sammus viga sisse tuli.

Harjutus x
----------
TODO: kirjuta arvutus lahti mitmeks sammuks

Harjutus x
----------
TODO: kirjuta mitmesammuline arvutus üheks avaldiseks



Kontrollküsimus
---------------
TODO: lugemiskontroll (mingi ilma tähenduseta programm, mille tulemust peab ennustama, justkui eksamil)





Väärtused ja avaldised
----------------------
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
    * faili lugemiseks ja kirjutamiseks tuleb fail kõigepealt *avada* (``f = open("andmed.txt")`` või ``f2 = open("andmed2.txt", mode="w")``). Lugemiseks saab kasutada failimeetodit ``readline`` (nt ``print(f.readline())``), kirjutamiseks meetodit ``write`` (nt ``f2.write(nimi + "\n")``).
    
Importimine
-----------
Kuna Pythonis standardteegis (ja teiste arendajate teekides) eksisteerib väga palju funktsioone, on nad organiseeritud *moodulitesse*. Moodulis olevatele funktsioonidele ligipääsemiseks on vaja kasutada *import lauset*. Sellel lausel on 3 erinevat varianti:

    * ``from math import sin, cos`` -- üksikute funktsioonide importimine
    * ``from math import *`` -- kogu mooduli sisu importimine
    * ``import math`` -- mooduli enda importimine. Sel juhul tuleb funktsiooni nimi kirjutada koos mooduli nimega (``math.sin(0.5)``)

Avaldised vs. laused
--------------------
Selle peatüki programmide puhul saame programmi iga rida nimetada **lauseks**. Pythoni programm polegi muud, kui lausete jada. Avaldisi kasutatakse vaid lausete koosseisus. Need lauseliigid mida me kohtasime olid:

    * import-lause, nt. ``from math import sin``
    * omistuslause, nt. ``vanus = input("Sisesta nimi: ")``. Selle lauseliigi *komponentideks* on muutuja nimi, võrdusmärk ja suvaline avaldis.
    * "käsulause", nt. ``print("Tere!")`` (tehniline termin selle lauseliigi kohta on *avaldislause*, sest formaalselt loetakse Pythonis ka tegevust väljendav funktsiooni väljakutse avaldiseks)
    
Kuna nende lauseliikide korral kulub iga lause jaoks täpselt üks rida, nimetatakse neid *lihtlauseteks*. Keerulisematest lausetest tuleb juttu järgmises peatükis. 


TODO:
Nüüdseks oleme üle vaadanud peaaegu kõik olulisemad programmeerimise konstruktsioonid -- järjendite käsitlus jäi paraku liiga põgusaks, aga selle võtame peagi ette eraldi teemana.



Ülesanded
=========

2. Täisnurkne kolmnurk
----------------------
Kirjuta funktsioon, mis võtab argumentideks kolmnurga külgede pikkused ja tagastab ``True`` või ``False`` vastavalt sellele, kas tegemist oli täisnurkse kolmnurgaga või mitte.

.. note:: 

    Lihtsustamise mõttes võid esialgu eeldada, et pikim külg antakse alati kolmanda argumendina. Kui saad esialgse variandi tööle, siis muutke programmi selliselt, et küljepikkuseid võib anda suvalises järjekorras.

.. note::
    
    Ära unusta, et mitte igast küljepikkuste komplektist ei saa moodustada kolmnurka! Soovitame kirjutada abifunktsiooni, mis ütleb, kas antud küljepikkused üldse sobivad kolmnurgale.
    
.. note::

    Ära unusta, et ujukomaarvud on pisut ebatäpsed, seega võib olla vajalik võrdsuse kontrollimise asemel kontrollida sarnasust:
    
    .. sourcecode :: py3
    
        if abs(x - y) < 0.000001:      # x on peaaegu võrdne y-ga
            ...

.. hint::

    Tuleta jälle meelde see vana hea koolimatemaatika teoreem.


Kasuta loodud funktsiooni, küsides kasutajalt kolmnurga 3 külje pikkused ja väljastades info selle kohta, kas antud kolmnurk on täisnurkne või mitte. Kui küljepikkused ei sobi kolmnurgale, siis tuleks ka seda öelda.

3. Klaveri mahutamine
---------------------
Ülikool on ostnud endale uue klaveri peahoone aula tarbeks. Paraku unustati  kontrollida, kas see klaver üldse välisuksest sisse mahub. Kirjutada programm, mis küsib kasutajalt klaverit sisaldava kasti kolm mõõdet (pikkus, laius, kõrgus) ning ukse laiuse ja kõrguse ning vastab, kas klaver on võimalik aulasse sisse toimetada.

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

