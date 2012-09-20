1. Sissejuhatus
===============
Esimese peatüki põhieesmärgiks on tutvustada Python põhilisi töövahendeid ning anda pealiskaudne ülevaade programmeerimise olemusest ja võimalustest. Uurime ka mõningaid keerulisemaid näiteprogramme, kuid need on mõeldud vaid andmaks aimu kursuse edasisest käigust -- täpsemad selgitused ning süstemaatilise harjutamise jätame järgmistesse peatükkidesse.


Programmeerimine ja Python
----------------------------
Selle õpiku põhieesmärk on õpetada `programmeerimise` universaalseid põhimõtteid, mis kehtivad kõigi populaarsete `programmeerimiskeelte` puhul. Konkreetne keel, mille abil seda tehakse, on `Python`. 

Mis on programm?
~~~~~~~~~~~~~~~~~~~~~~~~
`Programm`, nii nagu me seda selles õpikus mõistame, on mingi tegevuse kirjeldus. Selle poolest on programmi mõiste väga sarnane teatris ja kinos kasutatavale `käsikirja` e. `stsenaariumi` mõistele (inglise keeles saab kasutada mõlema mõiste kohta lausa sama sõna -- `script`).

Oluline erinevus teatri käsikirja ning programmi vahel on see, et programm pannakse kirja mingis `programmeerimiskeeles` (nt. `Python` või `Java`), mitte `loomulikus keeles` (nt. eesti või inglise keel). Programmeerimiskeeled on palju primitiivsemad ja rangemad, kui loomulikud keeled (seda nii sõnavara, kui reeglite poolest), seetõttu on võimalik neid keeli "õpetada" ka arvutile. See omakorda võimaldab meil lasta oma "käsikirja" (programmi) "etendada" (`käivitada` või `jooksutada`) arvutil.

Kuigi kaasaegses teatris kaasatakse mõnikord etendusse ka publikut, on etenduse kulg enamasti siiski ette teada. Programmidesse on seevastu peaaegu alati sisse kirjutatud ka "publikuga" (kasutajaga) suhtlemine, mis võib edasist programmi käiku väga oluliselt mõjutada. Lisaks kasutajalt saadud infole (mis on edastatud nt. hiire või klaviatuuri kaudu) võib programm hankida infot ka näiteks kõvakettalt või internetist.


Mis on programmeerimine?
~~~~~~~~~~~~~~~~~~~~~~~~~~~
Kõige lihtsam oleks öelda, et programmeerimine on programmi kirjapanemine. Tehniliselt võttes see nii ongi, aga mängu tulevad ka mõned olulised inimlikud aspektid.

Kuna lähteülesanne on alati püstitatud loomulikus keeles, võivad paljud olulised nüansid jääda esialgu tähelepanuta. Seetõttu ei õnnestu tavaliselt programmi oma peast lihtsalt "maha kirjutada" -- enamasti tuleb alustada mõnede fragmentidega, mille kirjapanek annab parema arusaamise ülesande olemusest. Parem arusaamine omakorda võimaldab näha, mida tuleks veel täpsustada, mida järgmisena kirja panna jne. Teisiti öeldes, programmeerija peab pidevalt ülesannet `analüüsima`. Analüüsi ja kirjutamise tsükkel kordub suuremate ülesannete juures palju kordi.

Teiseks, programmeerija on inimene ja inimene teeb vigu. Seetõttu loetakse üheks programmeerimise osaks ka programmi `silumist` st. juba kirjapandud programmist vigade otsimist ja nende parandamist. Suurem osa vigu avastatakse eespool kirjeldatud kirjutamise ja analüüsimise protsessis, aga tähelepanelik maksab olla ka siis, kui programm on teie arvates juba valmis.

Kokkuvõtteks võib öelda, et *programmeerimine on mitmekesine protsess*, kuhu on muuhulgas põimitud ülesande analüüsimine, lahenduse kirjapanek, selle kontrollimine ja parandamine.

Mis on Python?
~~~~~~~~~~~~~~
Python on programmeerimiskeel ning samas ka programm, mis `interpreteerib` keeles Python kirjutatud programme. Pythoni interpretaatori kasutamisest tuleb varsti juttu.

.. note::

    Mõnede programmeerimiskeelte puhul (nt. `C` või `C++`) `tõlgitakse` e. `kompileeritakse` programmid enne käivitamist `masinkoodi` (st. "arvuti keelde"). Selliselt ettevalmistatud programmide käivitamiseks pole eraldi interpretaatorprogrammi tarvis -- arvuti ise on interpretaator.
    
    Taolisel lähenemisel on omad eelised ja omad puudused, aga on leitud, et vähemalt programmeerimise õppimisel on interpreteeritava keele (nt. Python) kasutamine mugavam.
    


.. index::
    single: installeerimine

Pythoni installeerimine
--------------------------
Pythoni enda arvutisse installeerimiseks laadige alla vajalikud failid Pythoni ametlikult leheküljelt http://www.python.org/download/. Valige sealt versioon `3.2`, 32-bitine variant (see töötab igas arvutis, 64-bitise OP-süsteemi korral võite valida ka 64-bitise variandi).

Mac'is on tavaliselt Python küll olemas aga see on Python 2. Python 3 installimiseks Intel Mac'i jaoks valige Pythoni lehelt `Mac OS X 64-bit/32-bit x86-64/i386 Installer`.

Ka Linuxis on tõenäoliselt olemas Python 2. Python 3 tuleks installida paketihalduri abil. Vajaminevad paketid on populaarsemates distrotes nimedega `python3`, `python3-tk` ja `idle3`.

.. note::

    Pythoni versioon ei pea olema tingimata just 3.2, on oluline, et versiooni number algab 3-ga, olgu see `3.2`, `3.1` vms. Seevastu versioonid, mis algavad 2-ga, ei sobi meile, kuna seal töötavad mõned asjad pisut teisiti, kui on kirjeldatud selles õpikus.
    


.. index::
    single: IDLE

IDLE ja esimene programm
----------------------------
Alustuseks kirjutame ühe väga lihtsa programmi, mis ei tee muud, kui kirjutab ekraanile ``Tere maailm!`` (vt. ka http://en.wikipedia.org/wiki/Hello_world_program). 

Pythoni programme võiks vabalt kirjutada näiteks Notepad'i või mõne muu üldotstarbelise tekstiredaktoriga, kuid Pythoni standardvarustuses on olemas spetsiaalne redaktor nimega **IDLE**, mis on selle töö jaoks palju sobivam.

**IDLE käivitamiseks** Windowsis valige `Start -> All Programs -> Python 3.2 -> IDLE (Python GUI)`. Mac'is ja Linuxis tuleks sisestada terminalis käsk ``idle3``. Tõenäoliselt ilmub kõigepealt IDLE *käsurea* aken (pealkirjaga "Python shell"), mida kasutatakse juba käivitatud programmidega (või Pythoni endaga) suhtlemiseks.

.. note::

    Kuna arvutiklassides on installeeritud nii Python 2, kui Python 3, tuleb jälgida, et kasutate õiget versiooni. Käsurea aknas on Pythoni versioon näidatud esimesel real. Versiooni saab kontrollida ka menüüst `Help -> About IDLE`


**Uue programmi kirjutamiseks** valige `File` menüüst `New window`. Ilmub uus aken pealkirjaga "Untitled", kuhu saab hakata kirjutama Python programmi. Esimeseks katsetuseks kirjutage või kopeerige redaktorisse järgnev üherealine programmitekst:

.. sourcecode:: py3

    print("Tere maailm!")
    
Salvestage fail (`Ctrl+S`) kasutades failinime lõpus laiendit `py`, nt. `teremaailm.py`. (NB! soovitav on juba praegu teha enda programmeerimisharjutuste jaoks eraldi kaust.) Taolist Pythoni programmi sisaldavat tekstifaili nimetame edaspidi *skriptiks*.

**Programmi käivitamiseks** vajutage klaviatuuril `F5`. Ilmub uuesti IDLE käsurea aken, kuhu tekib uus rida tekstiga ``Tere maailm!``.

Selgitused:

    * nagu võite järeldada, tähendab ``print`` Pythoni jaoks teksti ekraanile kuvamist, mitte printerisse saatmist
    * selleks, et Python suudaks teha vahet käskudel ja tavalisel tekstil, kirjutatakse tekst jutumärkide vahele

.. note::

    Selles peatükis anname programmidele väga põgusad selgitused. Kõikide konstruktsioonide täpsed tähendused ja kasutusjuhised toome välja järgnevates peatükkides.

Kasutajaga suhtlemine
-----------------------------
Meie esimene programm polnud just kõige põnevam. Proovime nüüd programmi, mis suhtleb kasutajaga dialoogi, mitte monoloogi vormis. Tekitage `File -> New window` abil uus programmiaken ja kopeerige sinna järgnev programm. *NB! Ärge praegu veel oma nime kuhugi kirjutage!*

.. sourcecode:: py3

    nimi = input("Palun sisesta oma nimi ja vajuta ENTER: ")
    print("Tere " + nimi + "!")

Salvestage ja käivitage programm. Ilmub taas käsurea aken, palvega sisestada oma nimi. Enne oma nime kirjutamist (kooloni järele) proovige ennustada, milline tekst ilmub ekraanile, kui te olete nime sisestanud. Katsetage! Kui arvasite õigesti, siis vaadake programmi tekst uue pilguga üle ja mõelge, milline otstarve võiks olla igal programmielemendil.

Selgitused:

    * käsk ``input`` võimaldab kasutajal midagi sisestada ning edastab saadud teksti Pythonile
    * konstruktsioon ``nimi = ...`` salvestab selle teksti mällu. Edaspidi saab sellele tekstile viidata kirjutades lihtsalt ``nimi``
    * konstruktsioon ``Tere " + nimi + "!"`` kombineerib etteantud tekstijupid ja kasutaja nime uueks tekstiks

Harjutus 1. Programmi muutmine
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Tehke programmis mingeid muudatusi, salvestage ja käivitage. Katsetage ka selliseid muudatusi, mis võiksid teie arvates Pythoni segadusse ajada.

.. note:: 

    Ärge kartke teha vigu! Kui Python annab mingi veateate, siis kontrollige kõigepealt oma viimast muudatust -- võibolla on puudu lõpetav sulg vms. Veateadetest arusaamine on tavaliselt algajate jaoks küll raske, kuid sellega tuleb ennast harjutada -- vigadeta ei suuda töötada ükski programmeerija.



Arvutamine
----------------
Järgmine näiteprogramm demonstreerib, et Python tunneb aritmeetikat. Enne katsetamist uurige programmi hoolikalt ning mõelge, milline tähendus võiks igal programmikomponendil olla:

.. sourcecode:: py3

    a = float(input("Palun sisesta esimene arv: "))
    b = float(input("sisesta teine arv: "))
    
    print("Arvude summa:", a + b)
    print("Arvude korrutis:", a * b)
    print("Esimese ja teise jagatis:", a / b)
    print("25% esimesest arvust:", a * 0.25)
    
    if a == b:
        print("Arvud on võrdsed")
    else:
        print("Arvud on erinevad")
        if a > b:
            print("Esimene arv on suurem")
        else:
            print("Teine arv on suurem")
    
Selgitused: 

    * ``input``-i abil saab Python kätte kasutaja poolt sisestatud teksti (justnagu eelmises näites)
    * ``float`` teisendab saadud teksti arvuks
    * konstruktsioon ``a = ...`` salvestab saadud arvu mällu, edaspidi saab selle arvu kätte kirjutades lihtsalt ``a``
    * ``print`` käsule võib ette anda mitu asja korraga
    * konstruktsioon ``if-else`` valib täitmisele minevad käsud vastavalt etteantud tingimustele 

Matemaatilised funktsioonid
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Python tunneb ka matemaatilisi funktsioone ja konstante, nagu näiteks ``sin`` ja ``pi``. Kuna paljudes programmides neid vaja ei lähe, on nad esialgu "peidetud". Nende kasutamiseks tuleb neid ``import`` lause abil eraldi küsida:

.. sourcecode:: py3

    from math import sin, cos, pi
    
    print(pi)
    
    print(cos(0.5))
    
    x = sin(4) 
    print(x)
    print(round(x,2))

Harjutus 2. Puu läbimõõdu arvutamine
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Proovige kirjutada eelnevate näidete põhjal programm, mis küsib kasutaja käest puu ümbermõõdu ning teatab selle peale puu läbimõõdu.


.. note::
    Kui jääte veateadetega hätta, siis kontrollige kõigepealt, kas teil on sulud `balansis`, st. iga alustava sulu jaoks on õiges kohas ka lõpetav sulg.

.. index::
    single: turtle
    single: kilpkonn; turtle
    
Kilpkonn
--------
Programmeerimise puhul on etteantud käskude hulk piiratud – arvuti mõistab vaid üksikuid väga lihtsaid käske. Neid kombineerides ja õigesti järjestades on aga võimalik arvutit panna tegema väga keerulisi asju. 

Demonstreerimaks käskude kombineerimist, toome siinkohal sisse ühe pedagoogilise abimehe – nimelt kilpkonna. Meie virtuaalne kilpkonn oskab kõndida edasi ja tagasi ning ennast pöörata. Tal on hambus ka pliiats, millega ta ringi kõndides enda all olevale pinnale jälje jätab. Vajadusel võib ta seda pliiatsit paberilt tõsta ning siis taas langetada. Järgnevalt vaatame, kuidas kilpkonnale sobivas järjekorras käske andes saame joonistada huvitavaid kujundeid.

.. note:: 
    
    Selline kilpkonn mõeldi esmakordselt välja 1967.a. lastele programmeerimise õpetamise otstarbel Feurzeigi ja Paperti poolt programmeerimiskeele Logo jaoks. Praeguseks on kilpkonnast saanud programmeerimise õpetamise klassika.

Kilpkonn Pythonis
~~~~~~~~~~~~~~~~~
Kilpkonna juhtimiseks kasutame 6 erinevat käsku:

* ``forward(n)``, ``backward(n)`` – edasi või tagasi `n` sammu
* ``left(d)``, ``right(d)`` – vasakule või paremale `d` kraadi
* ``up()``, ``down()`` - pliiatsi üles tõstmine ja langetamine

Esimese käskluse andmisel avaneb uus aken, kus kilpkonna tähistab väike nooleke.

Justnagu matemaatilised funktsioonid, pole antud käsud kohe kättesaadavad. Nad on peidetud `moodulisse` ``turtle``. Nende kasutamiseks ütleme seekord Pythonile ``from turtle import *`` (see impordib kõik kilpkonna käsud korraga).

Proovige järgnevat näiteskripti, mis joonistab kilpkonna abil kolmnurga:

.. note::
    
    Ärge pange oma skripti nimeks `turtle.py` -- see ajab Pythoni `import` käsu segadusse.
    
.. sourcecode:: py3
    
    from turtle import *
    
    forward(100)
    left(120)
    forward(100)
    left(120)
    forward(100)
    left(120)
    
    exitonclick() # see võimaldab akna sulgemist hiireklõpsuga

Harjutus 3. Ruut
~~~~~~~~~~~~~~~~
Kirjutage skript, mis joonistab kilpkonnaga ruudu.


Harjutus 4. Ümbrik
~~~~~~~~~~~~~~~~~~
Kirjutage skript, mis joonistab kilpkonnaga mõne huvitava kujundi, näiteks ümbriku. 


.. image:: images/ymbrik.png

.. hint::
    
    Diagonaali pikkuse leidmiseks tuletage meelde üht tuntud koolimatemaatika teoreemi. Kui jääte sellega hätta, siis proovige leida paras pikkus katsetamise teel.

.. index::
    single: veaotsing



.. index::
    single: käsurida
    single: shell; käsurida

IDLE'i käsurida
----------------
Võibolla imestasite, miks tuleb IDLE käivitamisel kõigepelt ette käsurea aken. Põhjus on selles, et programmeerida saab ka käsureal, ilma, et programmi peaks skriptina salvestamata. Selline programmeerimise viis sobib väiksemate ülesanne lahendamiseks ning Pythoni võimaluste katsetamiseks. Kuna käske antakse ühekaupa ja tulemus näidatakse kohe järgmisel real, nimetatakse seda ka *interaktiivseks programmeerimiseks*. 

Kui teil on hetkel lahti vaid IDLE'i programmi aken, siis käsurea saate avada menüüvalikuga `Windows -> Python shell`. Käsuviip ``>>>`` näitab kohta, kuhu saab kirjutada Pythoni käsu, vajutades ENTER, see käsk täidetakse. Järgnev näide on kopeeritud IDLE'i käsurealt, kuhu sisestati 2 käsku ``print("Tere maailm!")`` ja ``print(23*454)``:

.. sourcecode:: py3

    >>> print("Tere maailm!")
    Tere maailm!
    >>> print(23*454)
    10442

.. note::

    Edaspidi tuleb meil näiteid nii käsurea, kui skriptide (st. faili salvestatud programmide) kohta. Kui näide algab käsuviibaga (``>>>``), siis esitab see käsurea dialoogi. Vastasel juhul on tegemist skriptiga.
    
    NB! Käsureal kasutatakse käsuviiba märki vaid selleks, et oleks kergem eristada, millistel ridadel on käsud ja millistel on vastused. Seda ei ole vaja kunagi ise kirjutada. Skiptis ei kasutata seda märki kunagi.

.. note::

    IDLE käsureal saab varasema käsu uuesti ette, kui liigute nooleklahvidega soovitud käsuni ja vajutate ENTER. Veidi kiirem variant on klahvikombinatsioon Alt+P (*P* nagu *previous*).




Harjutus 5. Interaktiivne programmeerimine
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Katsetage erinevaid siiani nähtud käske ka käsureal. Proovige muuhulgas ka Pythoni mälu kasutamist. (Paraku võib kilpkonna juhtimine käsurealt ebaõnnestuda, see sõltub IDLE'i seadetest.)

Python kui kalkulaator
~~~~~~~~~~~~~~~~~~~~~~
Nagu nägite, oskab Python arvutada, seega saaks Pythoni käsurida kasutada võimsa kalkulaatorina. Kuna ``print``-i kirjutamine iga arvutuse juures on liiga tüütu, näidatakse käsureal tulemust ka siis, kui avaldis kirjutada ilma ``print`` käsuta: 

.. sourcecode:: py3  
    
    >>> 3 / 2
    1.5
    >>> 5 * 5
    25
    >>> 4 + 9 - 1
    12
    >>> 10 / 3
    3.3333333333333335
    >>> round(10 / 3)
    3

.. note::
    
    Selline trikk toimib ainult käsureal. Kui soovite skriptis midagi ekraanil näidata, tuleb kasutada ikkagi ``print`` käsku.
    
.. note::
    
    Siin ja edaspidi on käsurea näidete juures soovitav ise järgi katsetada mõned sarnased, aga mitte samad näiteid (kui proovite täpselt samu näiteid, siis uskuge, te saate ka samad tulemused.) Üritage Pythonit (või iseennast) üllatada!


Arve saab "mällu" salvestada samamoodi nagu skriptis:

.. sourcecode:: py3

    >>> a = 2 * 3
    >>> b = 1
    >>> a + b + 2
    9

Ka matemaatiliste funktsioonide `importimine` toimib samal põhimõttel nagu skripti puhul:

.. sourcecode:: py3

    >>> from math import sin, pi
    >>> sin(1)
    0.8414709848078965
    >>> pi
    3.141592653589793


Harjutus 6. `math` moodul
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#. Uurige Pythoni matemaatikamooduli dokumentatsiooni aadressilt http://docs.python.org/py3k/library/math.html
#. Proovige saada aru, kuidas arvutatakse Pythonis ruutjuurt
#. Arvutage Pythoni käsureal, kui pikk on ristkülikukujulise maatüki diagonaal, mille mõõtmed on 50m x 75m.

.. hint::

    .. sourcecode:: py3
    
        >>> from math import sqrt
        >>> sqrt(4)
        2.0    

Vigadest
--------------------------------
Nagu te ehk eelnevaid ülesandeid lahendades juba märkasite, annab Pythoni märku, kui te tema arvates midagi valesti olete teinud. Veateateid võiks kõige üldisemalt jaotada kahte liiki:

**Süntaksivea** (ing. k *syntax error*) korral ei saa Python programmi tekstist aru ja seetõttu ei hakka ta programmi üldse käivitama. Veateate ütleb Python selle rea kohta, kus ta enam edasi lugeda ei osanud, tegelik vea põhjus on tihti hoopis eelneval real. Üks tüüpilisemaid süntaksivigu on puuduv lõpetav sulg -- kuigi iga programmeerija saab aru, mida on mõeldud lausega ``x = 3 + (4 * 5``, on see Pythoni jaoks täiesti mõttetu tekst, sest see ei vasta Pythoni reeglitele. Teisiti öeldes, Python (nagu ka iga teine programmeerimiskeel) on suur tähenärija ning sellega tuleb arvestada -- programmi kirjutamisel tuleb olla täpne!

**Täitmisaegse vea** (ing. k *runtime error*) puhul programm küll käivitati, aga mingi konkreetse käsu täitmine ebaõnnestus. Vigaseks käsuks võis olla näiteks nulliga jagamine, valesti kirjutatud funktsiooninime kasutamine, olematu faili lugemine vms. Kui te pole siiani ühtki täitmisaegset veateadet näinud, siis sisestage käsureal käsk ``prin("Tere!")``.

.. note::

    Täitmisaegses veateates on tavaliselt mitme rea jagu infot, mis on abiks kogenud programmeerijale, aga võivad algajal silme eest kirjuks võtta. Sellest ei tasu lasta ennast heidutada -- enamasti piisab vaid veateate viimase rea lugemisest. Lisaks probleemi kirjeldusele on veateates alati ka reanumber, mis viitab vea tekitanud reale programmi tekstis. (Käsureal töötades on aktiivse käsu reanumber alati 1).

    Paraku tuleb algajatel vahel ka veateate viimase rea üle pead murda -- hea näide on see, kui teile öeldakse käsu ``cos(pi)`` peale ``NameError: name "cos" not defined``. Sisuline põhjus pole siin mitte see, et käsk ``cos`` vale oleks, vaid see, et unustasite eelnevalt ``cos`` funktsiooni importida. (Ei, Python ei soovi segaste teadetega algajaid kiusata -- kui õpite tundma Pythoni peamiseid tööpõhimõtteid, siis paistab ka teile antud veateate sõnastus täiesti loomulik).

.. note::

    Veateate põhjust on kergem leida, kui te kirjutate programmi järk-järgult ja katsetate poolikut lahendust iga täienduse järel. Kui programm töötas korralikult enne viimase rea lisamist, siis tõenäoliselt on viga viimases reas ja te ei pea tervet programmi läbi vaatama.

Veateateid näete te oma programmeerimise karjääri jooksul väga palju, seega ei maksa neid karta. Lähtuge sellest, et iga veateade on mõeldud programmeerija abistamiseks -- lugege teate tekst alati hoolikalt läbi ja mõelge, milles võis probleem olla. Nii märkate varsti, et Pythoni veateadete "salakiri" on muutunud arusaadavaks informatsiooniks.

Semantilised vead
~~~~~~~~~~~~~~~~~~~~~~
Programmeerimises on veel üks liik vigasid, mis on kõige ohtlikumad ja mida nimetatakse **semantilisteks vigadeks** või ka lihtsalt **loogikavigadeks**. Nende vigade puhul võib kõik olla Pythoni seisukohast korrektne (st. mingit veateadet ei tule), aga programm ei tee seda, mis programmeerija silmas pidas.

Harjutus 7. Semantiline viga
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Leidke järgnevast näiteprogrammist semantiline viga:

.. sourcecode:: py3

    aeg = float(input("Mitu tundi kulus sõiduks? "))
    teepikkus = float(input("Mitu kilomeetrit sõitsid? "))
    kiirus = aeg / teepikkus
    
    print("Sinu kiirus oli " + str(kiirus) + " km/h")

Programmeerimise õppimine
------------------------------
Programmeerimist ei saa "ära õppida" selles mõttes nagu saab selgeks õppida teatud hulka võõrkeelseid väljendeid. Kuigi kõik Pythonis programmeerimise reeglid saaks mahutada ühele A4-le, ei piisa nende meeldejätmisest, sest võimalusi nende reeglite *kombineerimiseks* on lõputult. Lisaks reeglite teadmisele tuleb osata näha ülesande "sisse", märgata selle nüansse, kujutleda otsitavat lahendust ning lõpuks "tõlkida" oma nägemus programmeerimiskeelde. See on protsess, mis nõuab samaaegselt loovust ja täpsust, üldistusvõimet ja konkreetsust. 

Et suuta taolist protsessi oma peas läbi viia ka raskemate (st. huvitavamate) ülesannete puhul, on vaja harjutada järjest raskemate ülesannetega, ainult teooria lugemisest ja näiteülesannete läbiproovimisest ei piisa. Seetõttu on järgnevates peatükkides hulgaliselt ülesandeid, mis nõuavad äsja loetud materjali loomingulist kasutamist.

.. admonition:: NB!

    Eespool mainitud täpsuse ja konkreetsuse aspekt ütleb muuhulgas seda, et lahendus tuleks panna kirja ka siis, kui suudate selle oma peas valmis konstrueerida. Keel, mida me kasutame mõtlemiseks, on palju hägusam ja vähem range kui programmeerimiskeeled, seetõttu on alati võimalus, et pealtnäha korralik lahendus meie peas on tegelikult puudulik ja/või vigane.


Kui te tunnete, et mõne ülesande lahendamiseks pole antud piisavalt juhtnööre, siis teadke, et see on taotluslik -- need ülesanded õpetavad teile tehniliste probleemide lahendamist kõige üldisemal tasemel. Proovige taolist ülesannet enda jaoks ümber sõnastada, otsige seoseid ja sarnasusi teiste ülesannetega, lihtsustage ülesannet, otsige abi internetist, võtke väike puhkepaus, vaadake ülesannet värske pilguga ja proovige jälle. Läbi raskuste saavutatud kogemused ja oskused on teile edaspidi kõige rohkem abiks!

Programmeerimiseks vajalikku ettevalmistust on mõnel inimesel rohkem ja teisel vähem, aga harjutamisega on kõigil võimalik end selles osas arendada!


Programmeerimine vs. maagia
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Algajatel programmeerijaltel võib kergesti tekkida mulje, et programmeerimiseks tuleb teada mingit komplekti "loitse" (programmilõike), mille on välja mõelnud vanad ja targad mehed, ning neid tuleb rituaali korras "sõnuda" (oma programmi kopeerida), ja loota, et kokku sattusid õiged loitsud, mis annavad soovitud tulemuse. Taolist lähenemist nimetatakse inglise keeles `cargo cult programming` (vt. http://en.wikipedia.org/wiki/Cargo_cult) ja see lähenemine ei vii praktikas kuigi kaugele.

On täiesti loomulik, kui mõned selle peatüki näited või ülesanded jäid *praegu* teie jaoks segaseks või lausa "müstiliseks" -- peatüki eesmärk oli anda lihtsalt esimene ettekujutus programmeerimisest. Tegelikult pole programmeerimises aga midagi müstilist, iga programmilõigu tööpõhimõtet on võimalik alati täielikult ära seletada.

Keerulisemate programmide loomine, täiendamine ja muutmine on võimalik vaid siis, kui te saate programmist lõpuni aru. Seetõttu *on oluline, et järgmisest peatükist alates mõistaksite te enda kirjutatud programmides iga sümboli otstarvet ja tähendust*. Kui te lepite sellega, et mingi koht programmis jääb segaseks, siis tõenäoliselt raskendab see ka järgnevate teemade mõistmist. Vajaduselt küsige julgelt nõu kaaslaste või juhendajate käest, aga **ärge kirjutage oma programmidesse ühtegi rida, mille tähendust te täpselt ei mõista! Katse/eksitus meetodil programmeerimine on tupiktee!**



Kokkuvõte
-------------
See peatükk on oma eesmärgi täitnud kui:

    * te oskate IDLE abil Pythoni programme avada ja käivitada
    * te oskate IDLE käsureal aritmeetikat teha
    * teil on üldine ettekujutus, mida programmeerimine endast kujutab
    * te tahate programmeerimise õppimisega jätkata :)
    
Iga peatüki lõpus on soovitav teha iseenda jaoks mõttes (või kirjalikult) olulistest punktidest kokkuvõte, aga toome siinkohal välja ka selle, mis on tähtis õpiku autorite arvates:

    * Pythonis programmeerimiseks on kaks viisi -- skripti kirjutamine ning käsureal toimetamine
    * programmeerimiskeeled on ranged, seetõttu tuleb programmeerimisel olla täpne
    * programmeerimise õppimine nõuab harjutamist
    * vigade tegemist ei maksa karta
    * enda kirjutatud programmi tuleks lubada vaid neid lauseid, mille otstarbest saate te täielikult aru

Ülesanded
------------
.. note ::

    Peatükkide lõpus olevad ülesanded on mahukamad, kui teksti sees antud ülesanded ja õpetavad seega paremini probleemi lahendamise oskust. Praktikumide korralduses on eeldatud, et need ülesanded on lahendatud (või proovitud lahendada) enne praktikumi tulemist. Esimeses peatükis on soenduseks vaid üks ülesanne, edaspidi tuleb neid rohkem.
    
1. Kilpkonna joonistus
~~~~~~~~~~~~~~~~~~~~~~ 
Kirjutage programm, mis joonistab kilpkonnaga lihtsa otsevaates maja (võib olla ka "pseudo-3d" vaatega). 

.. hint::

    Vaja võib minna kilpkonna käske ``up()`` ja ``down()``. Vaadake nende tähendust ülaltpoolt.

Projekt
----------
Selle õpiku näited ja ülesanded on valdavalt fokuseeritud mingile kindlale teemale, mida vastavas peatükis käsitletakse. Reaalse elu programmeerimisülesannetel aga pole taolisi teemalipikuid küljes -- programmeerija peab ise selgusele jõudma, milliseid vahendeid antud ülesande lahendamiseks tarvis läheb.

Teine paratamatu puudus õpikunäidete ja ülesannete juures on see, et need ei pruugi olla kõigi lugejate jaoks ühtviisi huvitavad. Seetõttu on programmeerimise õppimisel väga kasulik valida endale mõni suuremat sorti huvipakkuv ülesanne -- nn. `projekt`, ning tegelda sellega paralleelselt uute teemade õppimisega. Tuleb välja, et õppimine on palju ladusam ja huvitavam, kui teil on iga uue teema jaoks juba valmis paras "auk" oma projektiidees, kus õpitut saab kohe rakendada!

Huvitavate ideede realiseerimiseks läheb aga tavaliselt vaja rohkem abivahendeid, kui õpikunäidete jaoks. Nende abivahendite tutvustamiseks ongi mõnede peatükkide lõpus plokk pealkirjaga `Projekt`. Erinevalt õpiku põhitekstist, mis keskendub Pythoni üldistele põhimõtetele, vaadeldakse edaspidistes projektiplokkides mingi spetsiifilisema `teegi` (ing.k. `library`) kasutamist, mille abil saaks luua midagi põnevat ja/või praktilist.

Selle peatüki projektiploki eesmärgiks on aidata ideede genereerimisel. Allpool tutvustame kolme küllalt erinevat programmi, mida oleks võimalik kirjutada antud õpiku materjali põhjal. Laadige need programmid oma arvutisse ja käivitage samamoodi nagu ülalpool toodud näiteprogrammid. 

.. note::

    Arvatavasti jääb nende programmide kood praegu arusaamatuks, kuid proovige siiski seda lugeda, kas või selleks, et saada aimu, mis teid ees ootab :)

"Mis toimub?"
~~~~~~~~~~~~~~~~~~~~~~~~~~~
:download:`mistoimub.py <downloads/mistoimub.py>`

See küllalt lihtne programm loeb ja esitab andmeid kahelt veebilehelt. Ühel juhul loetakse info sisse spetsiaalses XML formaadis (XML-i töötlemisest tuleb põgusalt juttu ühes hilisemas projektiplokis), teisel juhul otsitakse soovitud info üles Pythoni tekstitöötlusvahenditega (seda õpetab juba järgmine peatükk).

Eurokalkulaator
~~~~~~~~~~~~~~~~~~~~
:download:`eurokalkulaator.py <downloads/eurokalkulaator.py>`

See programm demonstreerib "standardse" graafilise kasutajaliidese loomise võimalusi Pythonis. Programmi loogika on siin väga lihtne, põhitöö on kulunud kasutajaliidese elementide paikasättimisele. Sellele teemale on pühendatud mitu järgnevat projektiplokki ning õpiku lisa `tkinter`.

Minesweeper
~~~~~~~~~~~~~~~~
Selle programmi katsetamiseks tuleb alla laadida 3 faili. Kõik need tuleks salvestada samasse kausta:

    * :download:`minesweeper.py <downloads/minesweeper/minesweeper.py>`
    * :download:`plain_cover.gif <downloads/minesweeper/plain_cover.gif>`
    * :download:`flagged_cover.gif <downloads/minesweeper/flagged_cover.gif>`
    

Siin on tegemist "vabas vormis" graafilise kasutajaliidesega, mis sobib hästi just mängude tegemiseks. Rohkem selgitusi tuleb järgnevates projektiplokkides ning lisas `tkinter`.

Teie enda projekt
~~~~~~~~~~~~~~~~~~~~~~~~~~
Valige välja mõned esialgsed programmiideed, mida te sooviksite Pythonis realiseerida. Uute teemade õppimisel mõelge, kas ja kuidas te saaksite antud teemat rakendada enda programmi juures.


Praktilisi näpunäiteid
-----------------------
    
Pythoni kasutamine süsteemi käsureal
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Nagu eespool mainitud, on Pythoni programmid tavalised tekstifailid ja nende käivitamiseks läheb vaja vaid Pythoni interpretaatorit. Selle demonstreerimiseks kirjutame oma esimese "Tere maailm!" programmi nüüd Notepad'is (Linuxi ja Mac-i puhul kasutage mõnd suvalist tekstiredaktorit) ning käivitame selle *süsteemi käsureal*.

.. note:: 
    Neile, kes pole arvutiga veel päris sinasõbrad, võib alljärgnev protseduur tunduda keeruline. Nagu eespool nägite, saab edukalt programmeerida ka ilma süsteemi käsurida puutumata (tõepoolest, selles kursuses me seda rohkem ei puutugi), aga kuna arvutispetsialistide jaoks on käsurea kasutamise oskus väga oluline, siis näitame siinkohal kiirelt ära, kuidas Python toimib OP-süsteemi "kapoti all".

Avage Notepad (või mõni muu tekstiredaktor, mis salvestab *plain text*-i). Kopeerige sinna meie esimese programmi tekst (``print("Tere maailm!")``) ja salvestage, nagu ikka, laiendiga ``.py``.
    
.. note::

    Notepad on laiendite osas kangekaelne -- kui te panete laiendiks ``.py``, siis lisatakse tõenäoliselt salvestamisel sinna otsa veel ``.txt``. Selle vältimiseks pange salvestusdialoogis failinime ümber veel jutumärgid, nt. ``"teremaailm.py"``. See annab Notepad'ile märku, et te tõesti soovite sellist failinime ja ei midagi muud.

Programmi käivitamiseks avame kõigepealt süsteemi käsurea ja liigume sellesse kausta, kus meie programm asub. Windows Vista ja Windows 7 puhul avage *Start-menüü*, sisestage otsingulahtrisse *cmd.exe* ja vajutage ENTER. Windows XP's tuleb Start-menüüst kõigepealt valida *Run* ja seejärel sisestada *cmd.exe* ja ENTER. Mac OS X's ja Linuxis tuleb avada *Terminal*.

Õigesse kausta liikumiseks sisestage ``cd``, tühik ja täielik kausta nimi. Näiteks, kui teie programmeerimise kaust asub teie kodukaustas, siis võiks kausta vahetamise käsk näha välja midagi sellist:

    * ``cd c:\Users\Peeter\Documents\progemine`` (Windows 7 ja Vista)
    * ``cd "c:\Documents and Settings\Peeter\My Documents\progemine"`` (Windows XP. Kui kausta nimes esineb tühikuid, tuleb see ümbritseda jutumärkidega)
    * ``cd ~/progemine`` (Mac ja Linux)

Programmi käivitamiseks tuleb pöörduda Pythoni interpretaatori poole, öeldes talle jooksutatava programmi nime: 

    * ``c:\python32\python teremaailm.py`` (Windowsis, eeldades, et teil on Python 3.2 ja see on paigaldatud vaikimisi määratud kausta)
    * ``python3 teremaailm.py`` (Mac ja Linux)

Kui kõik läks kenasti, siis ilmus ekraanile uus rida ``Tere maailm!`` ja selle järel uuesti süsteemi käsuviip. 

Mis selle käsu peale tegelikult toimus:

    * OP-süsteem käivitas Pythoni interpretaatori, andes talle *argumendiks* programmi failinime (*teremaailm.py*)
    * Pythoni interpretaator luges etteantud faili sisu mällu, vaatas teksti üle (kontrollides muuhulgas, et seal poleks süntaksivigu) ning hakkas käske ükshaaval täitma e. *interpreteerima*. 
    * Esimene käsk ütles, et ekraanile tuleb kirjutada tekst *Tere maailm!*. Seda interpretaator ka tegi
    * Kuna selles programmis rohkem käske polnud, siis interpretaator lõpetas töö ning käsurida läks tagasi OP-süsteemi kätte.
    
Kui käivitate Pythoni interpretaatori ilma programmi argumendita, siis avaneb Pythoni käsurida, mis on peaaegu identne IDLE'i käsureaga.

.. note::

    Kui soovite ka Windowsis käivitada Pythoni interpretaatorit ilma tema asukohta mainimata (olgu interaktiivselt või skripti jooksutamiseks), siis lugege edasisi juhiseid siit: http://docs.python.org/py3k/using/windows.html#configuring-python.
    
    Windowsis saab Pythoni skripte käivitada ka nagu tavalisi programme, nt. topeltklõpsuga `Windows Exploreris`.

Pythoni programmi pakendamine *exe-failiks*
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Nõue, et Pythoni programmide käivitamiseks peab süsteemi olema paigaldatud Pythoni interpretaator, võib olla mõnikord tülikas, näiteks, kui soovite oma programmi jagada mõne sõbraga, kes arvutitest palju ei taipa.

Õnneks on loodud vahendeid, mis pakendavad Pythoni programmi koos selle käivitamiseks vajaliku infrastruktuuriga ühte *jooksutatavasse* (ing. k. *executable*) faili (e. `exe-faili`). Taolist faili saab topeltklõpsuga käivitada ka süsteemides, kus Pythonit pole paigaldatud. Tuleb vaid arvestada, et saadud exe fail on mõne megabaidi suurune ka siis, kui programmiks on "Tere maailm!".

Taolistest pakendajatest tundub hetkel kõige parem *cx_Freeze*. Selle allalaadimiseks ja kasutusjuhiste lugemiseks minge aadressile http://cx-freeze.sourceforge.net/.

`Edit with IDLE`
~~~~~~~~~~~~~~~~~~~~
Üks mugav viis, kuidas Windowsis avada olemasolevaid Pythoni faile IDLE-s, on teha `Windows Explorer`-is soovitud failil paremklõps ning valida `Edit with IDLE`.
    
Kuna arvutiklassides on mitu Pythoni versiooni, siis ei pruugi fail avaneda õiges IDLE versioonis. Sel puhul võib olla abiks järgneval aadressil jagatav programm: http://defaultprogramseditor.com/. Sellega saab kasutaja määrata, millise programmiga peaks mingi failitüüp avanema. (Kui antud aadressilt ei õnnestu seda programmi laadida, siis kasuta aadressi http://courses.cs.ut.ee/2011/programmeerimine/uploads/DefaultProgramsEditor.zip)