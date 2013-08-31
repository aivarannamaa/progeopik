******************
5. I osa kokkuvõte
******************

TODO Ülesanded
* counting digits (algul anna vigane variant (töötab vigaselt 0 ja -x puhul))
* märgi ära or'i ja and'i shortcut evaluation
* ülesanded kombineeritavuse kohta (sh. tõeväärtusavaldised, samaväärsused)


.. todo::

    * conditional vs alternative execution ???
    * chained & nested conditionals (st. keele poolt pakutavad mugavus-alternatiivid)
    * if-harudes toimingu kordamine eri argumendiga vs. muutujasse salvestamine ja pärast toimingu tegemine muutujaga
    * Harjutus loogiliste avaldiste samaväärsuse kontrollimiseks (õpeta ka testima)
    * Harjutus "wrap this code in a function"
    * tabelite genereerimine
    * kilpkonnaga rooma numbrite joonistamine
    * kalendri printimine
    * etteantud 2-3 muutujaga tõeväärtustabeli põhjal avaldise kirjutamine
    


Kood vs. runtime
========================================================================

igal tüübil on literaali süntaks ja operatsioonid/tähendus
code vs. data

kas 2 + 3 *on* 5?

Arvutamine vs. tegemine --> avaldised vs. laused
Mõtlemine vs. ütlemine !!!
Toetu mingile näitele eelmisest ptkst selle duaalsuse kirjutamisel!!!



Süntaks
========================================================================

Operaatorid
-------------------------------------------------------------------------------------------------------
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
-------------------------------------------------------------------------------------------------------

Laused vs. avaldised
========================================================================

Arvutusmudel
========================================================================

Avaldised vs. väärtused
-------------------------------------------------------------------------------------------------------
väärtused e. objektid

igalpool kus kasutad muutujat/literaali võib kasutada ka teisi avaldise vorme, sest lõppkokkuvõttes muudetakse kõik väärtuseks.

Mälu ja muutujad
-------------------------------------------------------------------------------------------------------
.. _milleks-muutujad:
    
Milleks muutujad?
-------------------------------------------------------------------------------------------------------
.. _operatsioonid-muutujatega:
    

 

Moodulid
-------------------------------------------------------------------------------------------------------

Sisend ja väljund
-------------------------------------------------------------------------------------------------------

Funktsioonide tööpõhimõte
-------------------------------------------------------------------------------------------------------

TODO: Intuitsioon vs. mehhanism -- ka peale arvutile asjade õpetamist jäävad tema teadmised ikkagi mehhaaniliseks. Loll masin.

On vaja mõista, et arvuti/Python tegutsevad vaid etteantud reeglite järgi, neil pole initsiatiivi ega mingisugust arukust. Kujuta ette kõige mõnda sinu arvates rumalat, tähenärijalikku aga agarat ja täpset inimest -- Python on temast palju rumalam, agaram ja täpsem. Üllataval kombel annab just Pythoni rumalus ja tähenärimine programmidele üheseltmõistetavuse ja konkreetsuse. Programmeerimise oskus on ühelt poolt tehniline (tuleb tunda teatud komplekti mõistetest ja konstruktsioonidest, mida Python mõistab), aga ennekõike on see oskus mõista lahendatava ülesande olemust ja panna lahendusidee kirja sellisel kujul, et ka sedavõrd rumal olevus nagu arvuti suudaks neid käske järgida. Programmeerimise protsess ei ole lineaarne -- probleemi parem mõistmine ja lahenduse kirjapanek käivad vaheldumisi. Alles siis, kui me peame oma teadmise või idee sõnadesse panema (nt. eesti keeles, aga eriti mõnes programmeerimiskeeles) avastame, et teatud kohad meie idees on jäänud häguseks. Kõige paremini õpib õpetades ja programmeerimine on arvuti õpetamine. 

Taoline detailne mõtlemine võib tunduda algul väga ebaloomulik, aga kui me soovime oma mõtteid täpselt ja ühetähenduslikult kirja panna, siis on see ainuke võimalus

Loogiliste avaldiste samaväärsus
-------------------------------------------------------------------------------------------------------
Tihti on teatud tähendusega tõeväärtusavaldist võimalik kirjutada mitmel erineval kujul, näiteks:

    * ``not (x or y)`` on sama, mis ``(not x) and (not y)``
    * ``not (x and y)`` on sama, mis ``(not x) or (not y)``

Samaväärsetest variantidest tuleks valida selline, mis toob avaldise mõtte paremini esile.



Tõeväärtusega funktsioonid
-------------------------------------------------------------------------------------------------------
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
-------------------------------------------------------------------------------------------------------
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
-------------------------------------------------------------------------------------------------------
Kirjuta funktsioon ``päevade_arv``, mis võtab argumendiks kuu numbri ja aastaarvu ning tagastab mitu päeva on selles kuus. Kasuta abifunktsioonina eelnevalt defineeritud funktsiooni ``on_liigaasta``. (Kirjuta need funktsioonid samasse faili).

Harjutus 5. Kuupäeva kontrollimine
-------------------------------------------------------------------------------------------------------
Kirjuta funktsioon ``on_legaalne_kuupäev``, mis võtab argumendiks päeva, kuu ja aasta (arvudena) ning tagastab tõeväärtuse vastavalt sellele, kas argumentidele vastav kuupäev on legaalne või mitte. Kasuta abifunktsioonidena eelmistes ülesannetes defineeritud funktsioone.

Testi loodud funktsiooni järgnevate avaldistega:

    - ``on_legaalne_kuupäev(31, 1, 2001)``
    - ``on_legaalne_kuupäev(29, 2, 2001)``
    - ``on_legaalne_kuupäev(29, 2, 2000)``

    



Kokkuvõte
========================================================================
Väärtused ja avaldised
-------------------------------------------------------------------------------------------------------
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
-------------------------------------------------------------------------------------------------------
Konkreetsetest andmetüüpidest vaatlesime *täisarve*, *ujukomaarve* ja *sõnesid*:

    * Täisarvude suurus pole Pythonis piiratud
    * Ujukomaarvude juures tuleb arvestada, et kõiki kümnendmurde ei suuda Python täpselt esitada
    * Sõne kirjapanekuks on mitmeid erinevaid viise
    * Enamik sõneoperatsioone on Pythonis realiseeritud `meetoditena` (nt. ``nimi.lower()``)

Sisend ja väljund
-------------------------------------------------------------------------------------------------------
Et programmi käivitamisel midagi üldse juhtuks, on vaja programmi kirjutada ka mingi *tegevus*, näiteks kasutajaga (või failisüsteemiga) suhtlemine:

    * ``print`` kuvab etteantud väärtuse ekraanile
    * ``input`` küsib kasutajalt mingi tekstijupi ja *tagastab selle*, seega ``input("Sisesta oma nimi: ")`` on avaldis
    * faili lugemiseks ja kirjutamiseks tuleb fail kõigepealt *avada* (``f = open("andmed.txt")`` või ``f2 = open("andmed2.txt", mode="w")``). Lugemiseks saab kasutada failimeetodit ``readline`` (nt ``print(f.readline())``), kirjutamiseks meetodit ``write`` (nt ``f2.write(nimi + "\n")``).
    
Importimine
-------------------------------------------------------------------------------------------------------
Kuna Pythonis standardteegis (ja teiste arendajate teekides) eksisteerib väga palju funktsioone, on nad organiseeritud *moodulitesse*. Moodulis olevatele funktsioonidele ligipääsemiseks on vaja kasutada *import lauset*. Sellel lausel on 3 erinevat varianti:

    * ``from math import sin, cos`` -- üksikute funktsioonide importimine
    * ``from math import *`` -- kogu mooduli sisu importimine
    * ``import math`` -- mooduli enda importimine. Sel juhul tuleb funktsiooni nimi kirjutada koos mooduli nimega (``math.sin(0.5)``)

Avaldised vs. laused
-------------------------------------------------------------------------------------------------------
Selle peatüki programmide puhul saame programmi iga rida nimetada **lauseks**. Pythoni programm polegi muud, kui lausete jada. Avaldisi kasutatakse vaid lausete koosseisus. Need lauseliigid mida me kohtasime olid:

    * import-lause, nt. ``from math import sin``
    * omistuslause, nt. ``vanus = input("Sisesta nimi: ")``. Selle lauseliigi *komponentideks* on muutuja nimi, võrdusmärk ja suvaline avaldis.
    * "käsulause", nt. ``print("Tere!")`` (tehniline termin selle lauseliigi kohta on *avaldislause*, sest formaalselt loetakse Pythonis ka tegevust väljendav funktsiooni väljakutse avaldiseks)
    
Kuna nende lauseliikide korral kulub iga lause jaoks täpselt üks rida, nimetatakse neid *lihtlauseteks*. Keerulisematest lausetest tuleb juttu järgmises peatükis. 


TODO:
Nüüdseks oleme üle vaadanud peaaegu kõik olulisemad programmeerimise konstruktsioonid -- järjendite käsitlus jäi paraku liiga põgusaks, aga selle võtame peagi ette eraldi teemana.



Ülesanded
========================================================================

1. Kuupäeva esitamine sõnena
-------------------------------------------------------------------------------------------------------
Kirjuta funktsioon ``kuupäev_sõnena``, mis võtab argumentideks päeva, kuu ja aasta (arvudena) ning tagastab sõne, mis esitab kuupäeva kujul *<päev>. <kuu nimi> <aasta>* (nt. *24. veebruar 1918*).

Seejärel kirjuta programm, mis küsib kasutajalt arvudena päeva, kuu ja aasta. Kui neile vastav kuupäev on legaalne, siis kuvada ekraanile vastav kuupäev sõnena, vastasel juhul kuvada ``'Viga: mittelegaalne kuupäev'``.

Kasuta abifunktsioonidena ülalpood loodud funktsioone (vt. harjutusi 3-6).

2. Täisnurkne kolmnurk
-------------------------------------------------------------------------------------------------------
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
-------------------------------------------------------------------------------------------------------
Ülikool on ostnud endale uue klaveri peahoone aula tarbeks. Paraku unustati  kontrollida, kas see klaver üldse välisuksest sisse mahub. Kirjutada programm, mis küsib kasutajalt klaverit sisaldava kasti kolm mõõdet (pikkus, laius, kõrgus) ning ukse laiuse ja kõrguse ning vastab, kas klaver on võimalik aulasse sisse toimetada.

4. Pitsapood
-------------------------------------------------------------------------------------------------------
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
========================================================================

Midagi programmeerimiskeelte kohta
-------------------------------------------------------------------------------------------------------
TODO


Python tutorial
-------------------------------------------------------------------------------------------------------
sh. tour of std library 