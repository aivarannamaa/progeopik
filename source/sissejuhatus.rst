I. Sissejuhatus
===============
Esimese peatüki esmärgiks on tutvustada programmeerimise olemust ja võimalusi ning keele Python põhilisi töövahendeid. Uurime ka mõningaid näiteprogramme, kuid need on mõeldud vaid andmaks aimu kursuse edasisest käigust -- täpsemad selgitused ning süstemaatilise harjutamise jätame järgmistesse praktikumidesse.

.. index::
    single: käsurida
    single: shell; käsurida


Programmeerimine ja Python
----------------------------
TODO

    * Miks Python?
    * Selles kursuses programmeerimise universaalsed põhimõtted
    * keskendume sellele osale programmeerimisest, mis jääb inputi ja outputi vahele
    * Põhiülesanne: näidata lahedaid asju, mida on võimalik programmeerida ja veenda, et need on varsti jõukohased ka lugejale.
    * liiguta osa Kilpkonna asju siit järgmisesse peatükki ja too siia lihtsad if/while/for näited
    * maini, et programmeerimine peab olema täpne

.. todo::
    skeem: python, programm, klaver, hiir jms.


.. index::
    single: installeerimine

Pythoni installeerimine
--------------------------
Pythoni enda arvutisse installeerimiseks laadige alla vajalikud failid Pythoni ametlikult leheküljelt http://www.python.org/download/. Valige sealt versioon `3.2`, 32-bitine variant (see töötab igas arvutis, 64-bitise OP-süsteemi korral võite valida ka 64-bitise variandi).

Mac'is on tavaliselt Python küll olemas aga see on Python 2. Python 3 installimiseks Intel Mac'i jaoks valige Pythoni lehelt `Mac OS X 64-bit/32-bit x86-64/i386 Installer`.

Ka Linuxis on tõenäoliselt olemas Python 2. Python 3 tuleks installida paketihalduri abil. Vajaminevad paketid on populaarsemates distrotes nimedega `python3`, `python3-tk` ja `idle3`.

.. note::

    Pythoni versioon ei pea olema tingimata just 3.2, on oluline, et versiooni number algab 3-ga, olgu see `3.2`, `3.1` vms. Versioonid, mis algavad 2-ga, ei sobi meile, kuna seal töötavad mõned asjad pisut teisiti, kui on kirjeldatud selles õpikus.
    


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

**Programmi käivitamiseks** vajutage klaviatuuril `F5`. Ilmub uuesti IDLE käsurea aken, kuhu tekib uus rida tekstiga ``Tere maailm!``. (Nagu võite järeldada, tähendab ``print`` Pythoni jaoks teksti ekraanile kuvamist, mitte printerisse saatmist.)

.. note::

    Üks mugav viis, kuidas Windowsis avada olemasolevaid Pythoni faile IDLE-s, on teha `Windows Explorer`-is soovitud failil paremklõps ning valida `Edit with IDLE`.
    
    Kuna arvutiklassides on mitu Pythoni versiooni, siis ei pruugi fail avaneda õiges IDLE versioonis. Sel puhul võib olla abiks järgneval aadressil jagatav programm: http://defaultprogramseditor.com/. Sellega saab kasutaja määrata, millise programmiga peaks mingi failitüüp avanema. (Kui antud aadressilt ei õnnestu seda programmi laadida, siis kasuta aadressi http://courses.cs.ut.ee/2011/programmeerimine/uploads/DefaultProgramsEditor.zip)



Interaktiivsed programmid
-----------------------------
Meie esimene program polnud just kõige põnevam. Proovime nüüd programmi, mis suhtleb dialoogi, mitte monoloogi vormis. Tekitage `File -> New window` abil uus programmiaken ja kopeerige sinna järgnev programm. *NB! Ärge praegu veel oma nime kuhugi kirjutage!*

.. sourcecode:: py3

    nimi = input("Palun sisesta oma nimi ja vajuta ENTER: ")
    print("Tere " + nimi + "!")

Salvestage ja käivitage programm. Ilmub taas käsurea aken, palvega sisestada oma nimi. Enne oma nime kirjutamist kooloni järele proovige ennustada, milline tekst ilmub ekraanile, kui te olete nime sisestanud. Katsetage!

Ülesanne 1. Programmi muutmine
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Tehke programmis mingeid muudatusi, salvestage ja käivitage. Katsetage ka selliseid muudatusi, mis võiksid teie arvates Pythoni segadusse ajada.

.. note:: 

    Ärge kartke teha vigu! Kui Python annab mingi veateate, siis kontrollige kõigepealt oma viimast muudatust -- võibolla on puudu lõpetav sulg vms. Veateadetest arusaamine on tavaliselt algajate jaoks küll raske, kuid sellega tuleb ennast harjutada -- vigadeta ei suuda töötada ükski programmeerija.



Näide. Kalkulaator
~~~~~~~~~~~~~~~~~~~~~~
Järgmine näiteprogramm demonstreerib, et Python tunneb aritmeetikat:

.. todo:: math, import

.. note::
    
    Siin ja edaspidistes näidetes on parema loetavuse huvides tehtemärkide ümber pandud tühikud, aga need võib ka ära jätta.
    





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

Antud käsud pole kohe kättesaadavad, sest nad on peidetud `moodulisse` ``turtle``. Nende kasutamiseks peame kõigepealt ütlema Pythonile ``from turtle import *``. (Analoogselt talitasime eespool ``math`` mooduliga).

Proovige järgnevat näiteskripti, mis joonistab kilpkonna abil kolmnurga:

.. note::
    
    Ärge pange oma skripti nimeks `turtle.py` -- see ajab Pythoni `import` käsu segadusse. Üldisemalt: vältige skripti nimedes Pythoni moodulite nimesid (vähemalt neid, mida te ise impordite).
    
.. sourcecode:: py3
    
    from turtle import *
    
    forward(100)
    left(120)
    forward(100)
    left(120)
    forward(100)
    left(120)
    
    exitonclick() # see võimaldab akna sulgemist hiireklõpsuga

Ülesanne 2. Ruut
~~~~~~~~~~~~~~~~
Joonistage kilpkonnaga ruut.


Ülesanne 3. Ümbrik
~~~~~~~~~~~~~~~~~~
Kirjutage skript, mis joonistab kilpkonnaga mõne huvitava kujundi, näiteks ümbriku. NB! Ärge unustage lisamast skripti algusesse `import`-lauset.


.. image:: _static/ymbrik.png

.. hint::
    
    Diagonaali pikkuse leidmiseks tuletage meelde üht tuntud koolimatemaatika teoreemi. Kui jääte sellega hätta, siis proovige leida paras pikkus katsetamise teel.

.. index::
    single: veaotsing



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

    Edaspidi tuleb meil näiteid nii käsurea, kui skriptide (st. faili salvestatud programmide) kohta. Kui näide algab käsuviibaga (``>>>``), siis sisaldab see käsurea dialoogi. Vastasel juhul on tegemist skriptiga.
    
    NB! Käsureal kasutatakse käsuviiba märki vaid selleks, et oleks kergem eristada, millistel ridadel on käsud ja millistel on vastused. Seda ei ole vaja kunagi ise kirjutada. Skiptis ei kasutata seda märki kunagi.

.. note::

    IDLE käsureal saab varasema käsu uuesti ette, kui liigute nooleklahvidega soovitud käsuni ja vajutate ENTER. Veidi kiirem variant on klahvikombinatsioon Alt+P (*P* nagu *previous*).




Ülesanne. Interaktiivne programmeerimine
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
    
    Siin ja edaspidi on käsurea näidete juures soovitav ise järgi katsetada mõned sarnased, aga mitte samad näiteid (kui proovite täpselt samu näiteid, siis uskuge, te saate ka samad tulemused.) Üritage Pythonit (või iseennast) üllatada!

.. note::
    
    Selline trikk toimib ainult käsureal. Kui soovite skriptis midagi ekraanil näidata, tuleb kasutada ikkagi ``print`` käsku.

Samamoodi nagu mõnede taskukalkulaatorite puhul, saab ka Pythonis arve "mällu" salvestada:

.. sourcecode:: py3

    >>> a = 2 * 3
    >>> b = 1
    >>> a + b + 2
    9

Kui soovite kasutada trigonomeetrilisi funktsioone või matemaatilisi konstante, siis tuleb kõigepealt öelda Pythonile ``from math import *``, nt:

.. sourcecode:: py3

    >>> from math import *
    >>> sin(1)
    0.8414709848078965
    >>> pi
    3.141592653589793

.. hint::

    Varem antud käsu saab uuesti ette, vajutades klaviatuuril `üles` ja `alla` nooleklahve.
    

Ülesanne 1. Puu läbimõõt
~~~~~~~~~~~~~~~~~~~~~~~~
Arvutage Pythonis, kui suur on puu läbimõõt, kui ümbermõõt on 75cm.

Harjutus
~~~~~~~~
Proovige sisestada ka keerulisemaid avaldisi. Soovi korral saab tehete järjekorda muuta sulgudega. Katsetage ka "mälu" kasutamist.






Vigadest
--------------------------------
Nagu ehk eelnevaid ülesandeid lahendades juba märkasite, annab Pythoni märku, kui te tema arvates midagi valesti olete teinud. Veateateid võiks kõige üldisemalt jaotada kahte liiki:

**Süntaksivea** (ing. k *syntax error*) korral ei saa Python programmi tekstist aru ja seetõttu ei hakka ta programmi üldse käivitama. Veateate ütleb Python selle rea kohta, kus ta enam edasi lugeda ei osanud, tegelik vea põhjus on tihti hoopis eelneval real. Üks tüüpilisemaid süntaksivigu on puuduv lõpetav sulg -- kuigi iga programmeerija saab aru, mida on mõeldud lausega ``x = 3 + (4 * 5``, on see Pythoni jaoks täiesti mõttetu tekst, sest see ei vasta Pythoni reeglitele. Teisiti öeldes, Python (nagu ka iga teine programmeerimiskeel) on suur tähenärija ning sellega tuleb arvestada -- programmi kirjutamisel tuleb olla täpne!

**Täitmisaegse vea** (ing. k *runtime error*) puhul programm küll käivitati, aga mingi konkreetse käsu täitmine ebaõnnestus. Vigaseks käsuks võis olla näiteks nulliga jagamine, valesti kirjutatud funktsiooninime kasutamine, olematu faili lugemine vms. Kui te pole siiani ühtki täitmisaegset veateadet näinud, siis sisestage käsureal käsk ``prin("Tere!")``.

.. note::

    Täitmisaegses veateates on tavaliselt mitme rea jagu infot, mis on abiks kogenud programmeerijale, aga võivad algajal silme eest kirjuks võtta. Sellest ei tasu lasta ennest heidutada -- enamasti piisab vaid veateate viimase rea lugemisest. Lisaks probleemi kirjeldusele on veateates alati ka reanumber, mis viitab vea tekitanud reale programmi tekstis. (Käsureal töötades on aktiivse käsu reanumber alati 1).

    Paraku tuleb algajatel vahel ka veateate viimase rea üle pead murda -- hea näide on see, kui teile öeldakse käsu ``cos(pi)`` peale ``NameError: name "cos" not defined``. Sisuline põhjus pole siin mitte see, et käsk ``cos`` vale oleks, vaid see, et unustasite eelnevalt ``cos`` funktsiooni importida. (Ei, Python ei soovi segaste teadetega algajaid kiusata -- kui õpite ära Pythoni peamised tööpõhimõtted, siis paistab ka teile antud veateate sõnastus täiesti loomulik).

Veateateid näete te oma programeerimise karjääri jooksul väga palju, seega ei maksa neid karta. Lähtuge sellest, et iga veateade on mõeldud programmeerija abistamiseks -- lugege teate tekst alati hoolikalt läbi ja mõelge, milles võis probleem olla. Nii märkate varsti, et Pythoni veateadete "salakiri" on muutunud arusaadavaks informatsiooniks.

Programmeerimises on veel üks liik vigasid, mis on kõige ohtlikumad ja mida nimetatakse **semantilisteks vigadeks** või ka lihtsalt **loogikavigadeks**. Nende vigade puhul võib kõik olla Pythoni seisukohast korrektne (st. mingit veateadet ei tule), aga programm ei tee seda, mis programmeerija silmas pidas.

Ülesanne X. Semantiline viga
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Leidke järgnevast näiteprogrammist semantiline viga:

.. sourcecode:: py3

    aeg = float(input("Mitu tundi kulus sõiduks? "))
    teepikkus = float(input("Mitu kilomeetrit sõitsid? "))
    kiirus = aeg / teepikkus
    
    print("Sinu kiirus oli " + str(kiirus) + " km/h")

Programmeerimine ja maagia
-----------------------------------
.. todo:: selgita Cargo cult-i ja et siitmaalt edasi vaja on saada oma programmide igast detailist aru


Efektiivne õppimine
--------------------
.. todo:: selgita ülesannete lahendamise olulisust. Miks on kasulik mõelda välja oma projekt.

kirjuta natuke ja katseta, paranda vead ja kirjuta järgmine asi

Programmeerima pole võimalik õppida vaid loenguid kuulates – tegemist on praktilise oskusega, mis nõuab eelkõige harjutamist. Reeglina ei piisa vaid praktikumides tehtud ülesannetest ning harjutada tuleks kindlasti ka kodus.



Mis edasi?
--------------
TODO

Kokkuvõte
-------------
TODO

Sõnastik
~~~~~~~~~~~~~~
TODO

(Kodu?)Ülesanded
-----------------

Mingi kilpkonna joonistus
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
TODO

Projekti teema osas mõtisklemine
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
TODO

Lisalugemine
------------

blaa, blaa
~~~~~~~~~~~~~~~~~~~~~~~~
TODO

    * Näited, mida kõike on võimalik programmeerida
    * programmeerimine ja juhtimine
    * Head näited progammeerimise olemusest: http://www.nrg.tartu.ee/algkursus/Teema1.htm
    * Korda seda, et sellel kursuse fookus on inputi ja outputi vahel oleval alal
    * Too programeerimise näiteks Ruby Goldbergi masin vms!!
    * teleka programmeerimine

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

Õnneks on loodud vahendeid, mis pakendavad Pythoni programmi koos selle käivitamiseks vajaliku infrastruktuuriga ühte *jooksutatavasse* (ing. k. *executable*) faili. (Kuna Windowsis on nende failide laiendiks *.exe*, siis nimetatakse neid tihti *exe-failideks*.) Taolist faili saab topeltklõpsuga käivitada ka süsteemides, kus Pythonit pole paigaldatud. Tuleb vaid arvestada, et saadud exe fail on mõne megabaidi suurune ka siis, kui programmiks on "Tere maailm!".

Taolistest pakendajatest tundub hetkel kõige parem *cx_Freeze*. Selle allalaadimiseks ja kasutamisjuhiste lugemiseks minge aadressile http://cx-freeze.sourceforge.net/.