2. Avaldised ja lihtlaused
================================
Esimeses peatükis nägite ja katsetasite mitmeid erinevaid Pythoni programme. Millest need programmid koosnesid? Millest koosnevad mõnes loomulikus keeles (nt. eesti keeles) kirjutatud tekstid? 

.. topic:: Õpinipp:

    Taolised mõtteharjutused on antud õpiku oluline osa, ärge libisege neist üle!

Tuleb välja, et just nagu eesti keeles, on ka programmeerimisel tähelepanu keskmes *laused*, mis koosnevad "sõnadest" ja "fraasidest". Selles peatüki ülesandeks ongi tutvustada kõige olulisemaid Pythoni sõnu ning fraaside ja lihtsamate lausete moodustamise reegleid. Esimese asjana, enne praktilise osa juurde minemist, paneme paika mõned terminid.
    

Avaldised ja väärtused
-------------------------
.. note::

    Kuigi allpool toodud terminid kõlavad tähtsalt, on sisuliselt tegemist lihtsate mõistetega – neid tuleb lihtsalt teada, et programmeerijate kõnepruugist aru saada. 
    
Pythoni tutvustuse juures käisid läbi Pythoni laused ``print("Tere maailm!")`` ja ``print(2 + 3)``. Saite teada, et ``print`` käsk kuvab sulgudes oleva "asja" ekraanile. Aga mis see "asi" ikkagi on? Milliseid "asju" veel on olemas, mida sinna sulgudesse võib panna? Siin ongi paras koht tutvustada mõningaid programmeerimise põhitermineid. 

Neid osi programmitekstist, mis tähistavad mingit "asja", nimetatakse **avaldisteks**. On olemas erinevat liiki avaldisi -- ühed tähistavad mingit konkreetset arvu või tekstijuppi (nt. ``9``, ``4.25`` või ``'Tere!'``), teised mingit arvutustehet (nt. ``2 + 3``), kolmandad viitavad mingile eespool antud *definitsioonile* (nt. ``pi`` või ``nimi``) jne. 

Nüüd võib tekkida kohe järgmine küsimus: miks ilmus lause ``print(2 + 3)`` käivitamisel ekraanile ``5`` mitte ``2 + 3``? Asi on selles, et arvutustehte kujul avaldiste kasutamisel arvutab Python ilma küsimata tulemuse välja ja kasutab siis seda esialgse avaldise asemel. Arvutuse tulemust nimetatakse **väärtuseks** (ing.k. `value`) ning arvutusprotsessi avaldise **väärtustamiseks** (ing.k. `evaluation`).

.. index::
    single: väärtus
    
Väärtused (nt. arv 4.25, arv *5*, arv *3.141592653589793*, tekst *Tere!*) on need reaalsed andmed, mida programm oma töö käigus kasutab, loob, arvutab, teisendab vms. Võib öelda, et avaldised *tähistavad* mingisuguseid asju programmi tekstis, aga väärtused *on* need asjad programmi jooksutamise ajal.

.. index::
    single: andmetüüp; tüüp
    single: tüüp
    
.. index::
    single: tehe; operatsioon
    single: operatsioon

Andmetüübid, literaalid ja tehted
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  
Eelnevatest näidetest tuli välja, et Python oskab kasutada erinevat liiki andmeid e. väärtusi, nagu näiteks teksti, täisarve ja murdarve. Andmete liiki nimetatakse programmeerimisel **andmetüübiks**, või lihtsalt **tüübiks**.

Iga andmetüübi juures on esimeseks küsimuseks, kuidas panna kirja selle andmetüübi konkreetseid väärtusi. Siin tuleb lihtsalt teada vastavaid reegleid, nt. murdarvu esitamisel tuleb koma asemel kasutada punkti ning tekst tuleb panna ülakomade vahele või jutumärkidesse. Sedasi programmi teksti "sisse kirjutatud" väärtusi nimetatakse **literaalideks**.

Teiseks küsimuseks on, mida antud tüüpi andmetega teha saab. Siin tuleb jällegi teada Pythoni võimalusi -- näiteks arve saab omavahel liita, teksti saab teisendada suurtähtedesse ning kõiki andmetüüpe saab ``print`` käsuga ekraanile kuvada. Selliseid toiminguid nimetatakse **teheteks** e. **operatsioonideks**. Allpool vaatame täpsemalt arvude ja tekstiga tehtavaid operatsioone.

Avaldiste väärtustamine käsureal
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Üldjuhul ei ole eraldiseisev avaldis (nt. ``2 + 3``) Pythoni jaoks mõistlik lause (justnagu eesti keeles ei saa üksikut fraasi, nt. "suur mets", pidada lauseks) -- avaldised on harilikult mingi lause komponendiks (nt. ``print(2 + 3)``). Pythoni käsurida aga võimaldab avaldisi väärtustada ka ilma neid mingi lause konteksti panemata -- see on mugav viis erinevate tehete katsetamiseks. Kuna antud peatüki esimeses pooles keskendumegi just avaldiste ja väärtuste teemale, siis eelistame skripti koostamise asemel kasutada käsurida.

Selle teema kokkuvõtteks analüüsime järgmist lihtsat käsurea näidet:

.. sourcecode:: py3

    >>> 2 + 3
    5

Antud juhul teostas Python liitmisoperatsiooni arvudega *2* ja *3*, mille tulemusena konstrueeriti uus väärtus *5*. Programmeerimise terminitega saame seda näidet kirjeldada järgnevalt:

.. index::
    single: operaator
    single: argumendid; operaatori argumendid
    single: operaator; operaatori argumendid
    single: avaldis; avaldise väärtustamine
    single: avaldis
    single: literaalid
    
    
* ``2 + 3`` on **avaldis**
*  ``+`` on **operaator**
* ``2`` ja ``3`` on selle operaatori **argumendid** (öeldakse ka `operandid`). Antud juhul on mõlemad argumendid **literaalid** (st. konkreetsed väärtused).
* `5` on antud **avaldise väärtus**
* toiming, mille käigus ``2 + 3``-st saadakse `5`, on **avaldise väärtustamine**

Järgnevalt uurime lähemalt, milliseid operatsioone saab teha arvude ja sõnedega. 

Arvud
-----
Pythonis (nagu ka enamikes teistes programmeerimiskeeltes) on eraldi andmetüübid täis- ja reaalarvude esitamiseks.

.. index::
    single: täisarvud

Täisarvud
~~~~~~~~~
Pythoni **täisarvu** tüübi nimeks on `int` (lühend ingliskeelsest sõnast *integer*). Erinevalt paljudest teistest keeltest, ei ole Python 3-s piiratud, kui suuri (või väikseid) täisarve saab selle andmetüübiga esitada.

.. index::
    single: ujukomaarvud
    
Ujukomaarvud
~~~~~~~~~~~~
Reaalarvudele vastavad Pythonis (ja paljudes teistes keeltes) nn. **ujukomaarvud** (ing. k. `floating point number`, lühemalt `float`). 

.. note::
    Nimetus `ujukomaarvud` tuleb nende esitusviisist arvuti mälus -- lihtsustatult võib öelda, et kõigepealt on toodud välja arvu numbrite jada (ing.k `significant digits`) ning eraldi on öeldud, millisele positsioonile käib koma (seega koma on numbrijadast sõltumatu, "ujuv").

Ujukomaarvude literaalid võivad esineda järgmistel kujudel:

* ``3.0``, ``1.165``, ``-4.25`` on näited tavapärasest kirjapildist. NB! koma asemel kasutatakse punkti!
* ``6.1529e+18``, ``1.253e-12`` on nn. `teadusliku notatsiooni` näited. Seda kirjapilti kasutatakse väga suurte või nullilähedaste arvude esitamiseks. Traditsioonilises matemaatilises notatsioonis võiks need arvud kirjutada vastavalt 6.1529×10\ :sup:`18` ja 1.253×10\ :sup:`-12`.
    
    
Tehted arvudega
~~~~~~~~~~~~~~~~~~~~~~
+--------------------+----------+---------------------------------------------------------+
| Avaldis            | Väärtus  | Kommentaar                                              |
+====================+==========+=========================================================+
| ``6 / 3``          | ``2.0``  | Tavalise jagamise tulemus on alati ujukomaarv           |
+--------------------+----------+---------------------------------------------------------+
| ``5 // 3``         | ``1``    | Täisarvuline jagamine                                   |
+--------------------+----------+---------------------------------------------------------+
| ``5 % 3``          | ``2``    | Jagamise jäägi leidmine                                 |
+--------------------+----------+---------------------------------------------------------+
| ``5 ** 3``         | ``125``  | Astendamine                                             |
+--------------------+----------+---------------------------------------------------------+
| ``4 ** 0.5``       | ``2.0``  | Juurimine astendamise kaudu                             |
+--------------------+----------+---------------------------------------------------------+
|``round(2.6375, 2)``| ``2.64`` | Ümardamine nõutud täpsusega                             |
+--------------------+----------+---------------------------------------------------------+
|``round(2.6375)``   | ``3``    | Ümardamine lähima täisarvuni                            |
+--------------------+----------+---------------------------------------------------------+
|``int(2.6375)``     | ``2``    | Täisarvuks teisendades ei ümardata                      |
+--------------------+----------+---------------------------------------------------------+
| ``3 + 5 * 2``      | ``13``   |                                                         |
+--------------------+----------+ Python arvestab tehete järjekorda                       |
| ``(3 + 5) * 2``    | ``16``   |                                                         |
+--------------------+----------+---------------------------------------------------------+
| ``6 - 3 - 1``      | ``2``    |                                                         |
+--------------------+----------+ Sama prioriteediga tehted tehakse vasakult paremale ... |
| ``6 - (3 - 1)``    | ``4``    |                                                         |
+--------------------+----------+---------------------------------------------------------+
| ``2 ** 3 ** 2``    | ``512``  |                                                         |
+--------------------+----------+ ... va. astendamised, mis tehakse paremalt vasakule     |
| ``(2 ** 3) ** 2``  | ``64``   |                                                         |
+--------------------+----------+---------------------------------------------------------+

.. note::
      Kui avaldis on keeruline, siis võiks kaaluda sulgude kasutamist ka seal, kus Python neid ei nõua, et teha lugemist lihtsamaks.

.. note::
    
    Siin ja edaspidistes näidetes on parema loetavuse huvides tehtemärkide ümber pandud tühikud, aga need võib ka ära jätta.

Moodul ``math``
~~~~~~~~~~~~~~~~~~~~     
Suur hulk matemaatilisi funktsioone ja konstante on kättesaadavad peale seda, kui need importida moodulist nimega ``math``:

.. sourcecode:: py3

    >>> from math import *
    >>> cos(pi * 1.5)
    -1.8369701987210297e-16
    >>> atan(0.5)   
    0.4636476090008061
    >>> radians(360)
    6.283185307179586
    >>> 2 * pi
    6.283185307179586
    >>> degrees(2*pi)
    360.0
    >>> log(10.0)
    2.302585092994046
    >>> log(e)      
    1.0
    >>> log(100,10)
    2.0
    >>> sqrt(9)     
    3.0

.. note::
    Nagu võibolla märkasite, töötavad Pythoni trigonomeetrilised funktsioonid radiaanide, mitte kraadidega. Kraadide teisendamisel radiaanideks on abiks funktsion ``radians``, vastupidises suunas ``degrees``.
    
.. note::
    Kõikide mooduli ``math`` võimalustega saate tutvuda vastaval Pythoni dokumentatsiooni leheküljel: http://docs.python.org/py3k/library/math.html.

Harjutus 1. Matemaatilised avaldised
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Väärtustage järgnevad aritmeetilised avaldised Pythoni käsureal:

.. centered::
    :math:`(2^{89} + 5^{70})^2`
    
.. centered::
    :math:`6 + \sqrt[4]{6 \times 5 + 12}`

.. centered::
    :math:`\ln(e^{27} + 2^{30}) + \sin(\arccos(\frac{3\pi}{4}))`

.. note::
    Teise ülesande vastus peaks olema ``8.54572989502183``.

    Kui viimase avaldisega tekib probleeme, siis mõelge, milliste argumentide korral on arkuskoosinus üldse defineeritud. Veateade ``math domain error`` tähendab, et funktsiooni kasutati ebasobiva argumendiga. Muutke avaldist nii, et ``acos`` saab sobiva argumendi ja proovige uuesti.

Ujukomaarvude ligikaudsus
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Proovige läbi järgnev lihtne näide:

.. sourcecode:: py3
    
    >>> 0.1 * 3.0
    0.30000000000000004

Ootuspärane vastus oleks `0.3`, kuid Python tagastas midagi muud.

Asi on selles, et arvutis esitatakse ujukomaarvud kahendkujul, kasutades piiratud arvu bitte ja seetõttu polegi võimalik teatud kümnendmurde (nende hulgas `0.1`) täpselt esitada (analoogiliselt pole kümnendmurruna võimalik täpselt esitada näiteks `10 / 3`). Taolistel juhtudel ümardatakse sisestatud arv lihtsalt lähima võimaliku kahendmurruni ja see ongi põhjus, miks antud näites oli tulemus ebatäpne. 

Kui ujukomaarvu on tarvis esitada kümnendmurruna (nt. ekraanile kuvamisel), siis toimub jälle ümardamine -- see on põhjus, miks sisestades käsureale ``0.1`` antakse vastuseks tagasi ``0.1``, kuigi Python sisimas ei suuda seda arvu täpselt esitada. Kui korrutasime ``0.1`` 3-ga, siis muutus viga juba piisavalt suureks, et saadud tulemusele lähim võimalik kümnendmurd oli ``0.30000000000000004``, mitte ``0.3``

Tegelikult tekitab ujukomaarvude ligikaudsus probleeme vaid siis, kui me eeldame reaalarvude absoluutselt täpset esitamist (nt. kümnendmurruna esitatud rahasummad, kus murdosa tähistatab sente). Ujukomaarve kasutatakse peamiselt kõikvõimalike mõõtmistulemuste esitamiseks ja selle jaoks on Pythoni `float` tüübi ulatus ning täpsus enam kui piisav.



      
.. index::
    single: sõne
    single: string; sõne
    
Sõned
--------
Programmeerimine pole ainult arvudega manipuleerimine, paljudes programmides on tähtsamal kohal töö *tekstiga* (tuletage meelde näiteks esimese peatüki programmi, mis kuvas ekraanile teksti *Tere maailm!*). Selle tarvis on Pythonis olemas eraldi andmetüüp **sõne** (ing.k `string`, lühend `str`), mida kasutatakse justnimelt teksti esitamiseks.

Konkreetsed tekstijupid pannakse programmi tekstis kirja *sõneliteraalidena*. Enamasti piisab sõneliteraali kirjapanekuks sellest, kui soovitud tekst piiritletakse ülakomade või jutumärkidega, nt. ``'Tartu'`` või ``"Kauneim linn on Eestis Tartu"``.

Pange tähele, et tekst, mida antud sõneliteraalid esitavad on *Tartu* ja *Kauneim linn on Eestis Tartu*, st. piiritlejana kasutatud ülakomad/jutumärgid ei kuulu sõne sisu juurde. Demonstreerime seda ``print`` käsu abil, mis toob ekraanile alati sõne *tegeliku* sisu, hoolimata sellest, kuidas ta programmi tekstis kirja on pandud:

.. sourcecode:: py3

    >>> print("Tartu")
    Tartu


.. admonition:: NB!

    Kui unustate sõneliteraali kirjutades piiritlejaid kasutada, siis peab Python vastavat tekstijuppi muutuja nimeks (või kui tekstis oli tühik, siis ei oska ta sellest midagi arvata). Proovige käivitada laused ``print(Tere)`` ja ``print(Tere maailm)`` ning uurige, millised veateated neil juhtudel antakse -- siis on edaspidi taolisi näpuvigu kergem tuvastada.
    

.. topic:: "Aga kui mu tekst sisaldab jutumärke või ülakomasid?"

    Asi läheb veidi keerulisemaks, kui sõne *sees* on vaja kasutada jutumärke, ülakomasid või muid erisümboleid. Järgnevalt demonstreerime erinevaid viise selle probleemi lahendamiseks:

        * Kui tekstis on ülakomasid, siis kõige lihtsam on kasutada piiritlejaks jutumärke ja vastupidi:
        
            .. sourcecode:: py3
            
                >>> print("Rock 'n' roll")
                Rock 'n' roll
                >>> print('Jim ütles vaid: "Siin see on."')
                Jim ütles vaid: "Siin see on."
                
        * Kui tekstis on vaja kasutada nii jutumärke kui ülakomasid, siis pole eelmisest soovitusest abi. Sellisel juhul tuleb üks neist (nt. jutumärk) ikkagi valida piiritlejaks, aga tema kasutamisel tekstis tuleb ta spetsiaalselt märgistada langkriipsuga (seda nimetatakse inglise keeles *escaping*) -- see annab Pythonile märku, et tegemist pole veel teksti lõpuga, vaid sooviti kirja panna piiritlejaks valitud sümbolit ennast:
        
            .. sourcecode:: py3
            
                >>> print("Jack vastas: \"Rock 'n' roll\".")
                Jack vastas: "Rock 'n' roll".
                >>> print('Jack vastas: "Rock \'n\' roll".')
                Jack vastas: "Rock 'n' roll".
                
        * Langkriipsu saab kasutada ka muul otstarbel, nt. reavahetusi saab esitada kombinatsiooniga ``\n`` (tavalist reavahetust Python siin ei lubaks):
        
            .. sourcecode:: py3
            
                >>> print("Seda kuupaistet!\nOh muutuksin sündides\nmänniks mäetipul!\n--Ryota")
                Seda kuupaistet!
                Oh muutuksin sündides
                männiks mäetipul!
                --Ryota
                
        * Nagu näha on langkriips tekstiliteraalis spetsiaalse tähendusega. Kuidas aga esitada langkriipsu ennast? Lihtne, see tuleb ära märgistada ... langkriipsuga!:
        
            .. sourcecode:: py3
            
                >>> print("C:\\kaustanimi\\failinimi.txt")
                C:\kaustanimi\failinimi.txt

                
        * Kui tekstis on vaja kasutada palju erisümboleid, siis võib tulemus muutuda langkriipsude tõttu väga kirjuks. Seetõttu on Pythonis veel üks sõne kirjapaneku viis -- kolmekordsete ülakomade või jutumärkide vahele. Sel juhul ei ole langkriipsul literaali sees enam mingit eritähendust -- iga täht ja sümbol seisab iseenda eest. Selle esitusviisiga saab teksti sees kasutada ka tavalist reavahetust:
        
            .. sourcecode:: py3
            
                >>> print("""Jack vastas: "Rock 'n' roll".""")
                Jack vastas: "Rock 'n' roll".
                >>> print('''Jack vastas: "Rock 'n' roll".''')
                Jack vastas: "Rock 'n' roll".
                >>> print("""Seda kuupaistet!
                Oh muutuksin sündides
                männiks mäetipul!
                --Ryota""")
                Seda kuupaistet!
                Oh muutuksin sündides
                männiks mäetipul!
                --Ryota
                >>> print("""
                   _____                                            
                  / ____|                                           
                 | |  __  __ _ _ __ ___   ___    _____   _____ _ __ 
                 | | |_ |/ _` | '_ ` _ \ / _ \  / _ \ \ / / _ \ '__|
                 | |__| | (_| | | | | | |  __/ | (_) \ V /  __/ |   
                  \_____|\__,_|_| |_| |_|\___|  \___/ \_/ \___|_|
                """)

                   _____                                            
                  / ____|                                           
                 | |  __  __ _ _ __ ___   ___    _____   _____ _ __ 
                 | | |_ |/ _` | '_ ` _ \ / _ \  / _ \ \ / / _ \ '__|
                 | |__| | (_| | | | | | |  __/ | (_) \ V /  __/ |   
                  \_____|\__,_|_| |_| |_|\___|  \___/ \_/ \___|_|
                  
                  

                
                
        * On oluline mõista, et piiritlejad ning langkriipsud on vaid selleks, et Python suudaks teksti õigesti sisse lugeda -- peale sisselugemist muutub ``'Rock\'n\'roll'`` tekstiks `Rock'n'roll`.

        * Neid sõneliteraale Pythoni käsureale sisestades (ilma ``print``-i kasutamata) saate piiritlejad ja mõnel juhul langkriipsud ka väljundis. See on tingitud sellest, et Pythoni käsurida näitab avaldise väärtust alati Pythoni süntaksile vastavalt. Kui soovite näha sõne tegelikku väärtust, siis kuvage see ``print`` käsuga ekraanile.


Tehted sõnedega
~~~~~~~~~~~~~~~~~~~~~~


+-------------------------------------+--------------------+---------------------------------------------------------------------+
| Avaldis                             | Väärtus            | Kommentaar                                                          |
+=====================================+====================+=====================================================================+
| ``'Tere' + 'Madis!'``               |``'TereMadis!'``    | ``+`` loob kahe sõne põhjal uue sõne                                |
+-------------------------------------+--------------------+---------------------------------------------------------------------+
| ``'Tere' + ' Madis!'``              |``'Tere Madis!'``   | Tühikud tuleb vajadusel ise vahele panna                            |
+-------------------------------------+--------------------+---------------------------------------------------------------------+
| ``'Tere' + ' ' + 'Mad' + 'is!'``    |``'Tere Madis!'``   | kokku võib liita ka mitu sõnet                                      |
+-------------------------------------+--------------------+---------------------------------------------------------------------+
| ``'nr.' + 1``                       | Viga!!!            | Sõnet ja arvu ei saa niisama ühendada                               |
+-------------------------------------+--------------------+---------------------------------------------------------------------+
| ``'nr.' + str(1)``                  | ``'nr.1'``         | ``str`` annab arvule vastava sõne                                   |
+-------------------------------------+--------------------+---------------------------------------------------------------------+
| ``'5' + '3'``                       | ``'53'``           | Sõnena esitatud arve ei käsitleta arvudena                          |
+-------------------------------------+--------------------+---------------------------------------------------------------------+
| ``int('5')``                        | ``5``              | Annab sõnele vastava täisarvu                                       |
+-------------------------------------+--------------------+---------------------------------------------------------------------+
| ``float('5.3')``                    | ``5.3``            | Annab sõnele vastava ujukomaarvu                                    |
+-------------------------------------+--------------------+---------------------------------------------------------------------+
| ``'xo' * 3``                        | ``'xoxoxo'``       | Sõne dubleerimine                                                   |
+-------------------------------------+--------------------+---------------------------------------------------------------------+
| ``len('tere')``                     | ``4``              | Sõne pikkuse (`length`) küsimine                                    |
+-------------------------------------+--------------------+---------------------------------------------------------------------+
| ``'tere'.upper()``                  | ``'TERE'``         | Mõnede käskude korral kirjutatakse sõne käsu ette.                  |
+-------------------------------------+--------------------+ Taolisi käske nimetatakse *meetoditeks*                             |
| ``'TeRe'.lower()``                  | ``'tere'``         |                                                                     |
+-------------------------------------+--------------------+                                                                     |
| ``'jäääär'.count('ä')``             | ``4``              |                                                                     |
+-------------------------------------+--------------------+---------------------------------------------------------------------+
| ``' tere '.strip()``                | ``'tere'``         | Meetod ``strip`` annab sõne ilma alguses ja lõpus olevate tühikute  |
+-------------------------------------+--------------------+ ja reavahetusteta                                                   +
| ``'tere'.strip()``                  | ``'tere'``         |                                                                     |
+-------------------------------------+--------------------+---------------------------------------------------------------------+
| ``'abc'[0]``                        | ``'a'``            | Kirjutades sõne järele kantsulgudesse mingi numbri, antakse         |
+-------------------------------------+--------------------+ vastuseks vastava järjekorranumbriga e. *indeksiga* täht.           +
| ``'abc'[1]``                        | ``'b'``            | NB! indeksid algavad 0-ga                                           |
+-------------------------------------+--------------------+                                                                     +
| ``'abc'[2]``                        | ``'c'``            |                                                                     |
+-------------------------------------+--------------------+---------------------------------------------------------------------+
| ``'tere'[0:3]``                     | ``'ter'``          | Kui kantsulgudesse kirjutada kooloniga eraldatult kaks indeksit,    |
+-------------------------------------+--------------------+ siis antakse sõnest lõik alates esimesest indeksist (kaasaarvatud)  +
| ``'tere'[2:4]``                     | ``'re'``           | kuni viimase indeksini (väljaarvatud)                               |
+-------------------------------------+--------------------+---------------------------------------------------------------------+
| ``'tere'.replace('e','ö').upper()`` | ``'TÖRÖ'``         | Käske saab kombineerida                                             |
+-------------------------------------+--------------------+---------------------------------------------------------------------+


.. note::
    Kõikide sõnemeetoditega saab tutvuda aadressil http://docs.python.org/py3k/library/stdtypes.html#string-methods


Muutujad
---------
Kõik levinud programmeerimiskeeled võimaldavad konkreetseid väärtusi või arvutuste tulemusi salvestada **muutujatesse**. Uurige järgnevat näiteskripti, mis demonstreerib muutujate defineerimist ja kasutamist. Proovige ennustada, mis ilmub ekraanile selle skripti käivitamisel! 

.. sourcecode:: py3
    
    x = 2 + 3
    y = 10
    print(x)
    print(y)
    print(x + y)
    print(x * 2 + y)
    print(x)
    print(y)
    
    z = "Peeter"
    print(z + " " + "Paan")
    print(z + " " + "Esimene")
    print(z.upper())
    print(z + z)
    print(z * x)
    print(z)

Selgitus: esimese rea käivitamisel teeb Python kaks erinevat toimingut -- kõigepealt väärtustab avaldise ``2 + 3`` ning seejärel salvestab saadud tulemuse muutujasse ``x``. Programmeerijate kõnepruugis: muutujale ``x`` **omistatakse** avaldise ``2 + 3`` väärtus. Peale seda on võimalik muutuja nime **kasutada** vastava väärtuse asemel. Seega, antud näiteprogrammis tähistavad kõik ``x`` esinemised alates teisest reast arvu `5`.

Muutuja defineerimist (nt. ``x = 2 + 3``, üldisemalt *<muutuja nimi> = <avaldis>*) nimetakse **omistuslauseks**. Kuna tegemist on lausega, siis kirjutatakse ta omaette reale. Seevastu muutuja kasutamine (nt. ``x`` lauses ``print(x)``) on avaldis, mis esineb mingi lause või suurema avaldise sees. 

.. note::
    Muutujaid on võimalik defineerida ja kasutada ka käsureal -- kuigi käsurida kasutatakse enamasti avaldiste katsetamiseks, aktsepteerib ta rõõmuga ka lauseid sh. omistuslauseid:
    
    .. sourcecode:: py3

        >>> eesnimi = "Peeter"
        >>> eesnimi * 3
        'PeeterPeeterPeeter'
        >>> eesnimi.upper()
        'PEETER'
        >>> eesnimi
        'Peeter'


Milleks muutujad?
~~~~~~~~~~~~~~~~~~~~~~ 
Programmeerimises kasutatakse muutujaid samal põhjusel, nagu loomuliku keele tekstides kasutakse mingite spetsiifiliste mõistete definitsioone -- see võimaldab mingi (potentsiaalselt keerulise) asja panna kirja ühekordselt ning viidata sellele edaspidi erinevates kohtades kasutades vaid ühte sõna. Oleks ju üpris tüütu kirjutada trigonomeetrilistes avaldistes alati ``3.141592653589793``. Selle asemel saame importida moodulist ``math`` muutuja ``pi``, (mille väärtuseks on mooduli loojad juhtumisi omistanud `3.141592653589793`) ning kasutada oma arvutustes seda.

Mõnikord on muutuja kasutamine lausa hädavajalik, näiteks programmides, mis küsivad kasutaja käest mingit infot ja kasutavad seda siis mitmes kohas:

.. sourcecode:: py3

    nimi = input('Palun ütle, mis on sinu nimi: ')
    print(nimi + '?!! Oo, milline ilus nimi!')
    print('Ma tahaksin seista mäetipul ja hüüda "' + nimi.upper() + '!!!!"')
    print('ning kuulda, kuidas kaja vastab: "' + ((nimi.lower() + ' ') * 3) + '..."')
    
Ilmselt nõustute, et sellise programmi puhul oleks maitsetu küsida kasutajalt tema nime mitu korda.

Muutujale nime valimine
~~~~~~~~~~~~~~~~~~~~~~~~ 
Pythoni jaoks on ükskõik, millise nime sa mingi muutuja jaoks valid, aga programmi loetavuse huvides peaks nimi kirjeldama muutuja tähendust antud ülesande kontekstis (nt. ``brutopalk`` või ``isikukood``). Kui on tarvis kasutada mitmest sõnast koosnevat muutuja nime, siis tuleks kasutada tühikute asemel allkriipse, nt. ``laste_arv``. Muutuja nimes võib kasutada ka numbreid, aga esimene sümbol peab olema täht (või allkriips).


Avaldiste kombineerimine
------------------------------
Me oleme nüüdseks kasutanud mitut viisi Pythoni maailma "asjade" e. väärtuste kirjeldamiseks. Konkreetse väärtuse puhul on kõige lihtsam see panna kirja *literaalina* (nt. ``2.5`` või ``"Tere!"``). Mõnikord on mugavam väärtusele viidata hoopis läbi *muutuja* (nt. ``x``). Enamasti aga on meil programmi kirjutamise ajal väärtuse asemel teada hoopis selle leidmise "valem", mille me paneme kirja Pythoni *tehte* e. *operatsioonina* (nt. ``sin(x) * 2 - 1`` või ``nimi.upper()``). Kõik need viisid kannavad ühist nimetust *avaldis*.

Kahtlemata on neist kolmest avaldise liigist kõige põnevam arvutustehe -- on ju arvutamine üks põhjus miks programme üldse kirjutatakse. Loodetavasti märkasite, et Pythoni arvutustehetel on üks oluline omadus, mis tõstab ta peajagu kõrgemale taskukalkulaatoritest -- tehete komponentideks võivad olla suvalist liiki avaldised, st. mitte ainult konkreetsed väärtused vaid ka muutujad või mingid muud tehted, mis võivad omakorda koosneda konkreetsetest väärtustest, muutujatest või tehetest, mis võivad omakorda ... jne. Seetõttu nimetatakse tehete komponente vahel üldistavalt *alamavaldisteks*.

Kokkuvõttes, **igal pool, kus saab kasutada mingit konkreetset väärtust, saab kasutada ka muutujat või mingit tehet**, või veel üldisemalt, **igal pool, kus saab kasutada ühte avaldise liiki, saab kasutada ka teisi**. Siit tuleb ka välja miks me literaale, muutujaid ja tehteid koos vaatasime ning miks neile on välja mõeldud ühine nimetus -- hoolimata nende erinevast iseloomust kuuluvad nad Pythoni jaoks ühte perekonda.

Toome järgnevalt mõned näited avaldistest mis koosnevad erinevatest alamavaldistest:

TODO: näide

Tehniliselt võttes ühendab erinevaid avaldise liike see, et neil kõigil on *väärtus* -- literaalide puhul on väärtus otseselt kirja pandud, muutuja kasutamisel vaatab Python järele selle defineerimisel antud väärtuse, tehete väärtuse leidmiseks tuleb teha vastavad arvutused. Asjaolu, et Python suudab leida iga avaldise väärtuse ja et reaalne arvutamine (nt. liitmine) toimub justnimelt väärtustega, ongi see, mis võimaldab meil erinevat liiki avaldisi nii vabalt kombineerida.

Harjutus x
~~~~~~~~~~~~~~
TODO: sõne- ja arvavaldise kombineerimine


Abimuutujate kasutamine
~~~~~~~~~~~~~~~~~~~~~~~~ 
See, et meil on võimalik kirjutada väga keerulisi arvutusi ühe avaldisena, ei tähenda, et seda tuleks tingimata teha -- tihti on lihtsam jagada arvutus *abimuutujate* abil mitmeks sammuks:

TODO: näide

Taoline sammukaupa arvutamine võimaldab ka kergemini leida üles viga, kui ilmneb, et arvutuse tulemus ei ole õige, selleks tuleb iga sammu järel kuvada vahetulemus ekraanile, mispeale peaks olema lihtne tuvastada, millises sammus viga sisse tuli.

Harjutus x
~~~~~~~~~~~~~~
TODO: kirjuta arvutus lahti mitmeks sammuks

Harjutus x
~~~~~~~~~~~~~~
TODO: kirjuta mitmesammuline arvutus üheks avaldiseks






Sisend ja väljund
-----------------
Pythoni käsureal toimub avaldiste sisestamine ning tulemuste väljastamine ilma, et sellele peaks eriti mõtlema. Kui soovime aga programmi käivitada skriptina, siis tuleb sisendi ja väljundiga eraldi tegeleda. 

.. index::
    single: väljund
    single: print
    
Käsk ``print``
~~~~~~~~~~~~~~
Skriptina esitatud programmis saab väärtusi kuvada ekraanile käsuga **print**. Salvesta järgnev näide faili ning käivita. (Vajadusel vaadake sellekohast juhendit eelmisest peatükist.)

.. sourcecode:: py3

    print(32 * 57)

Sulgudes olevat avaldist ``32 * 57`` nimetatakse siinkohal käsu ``print`` **argumendiks**. Kui kõik läheb ilusti, siis programm kuvab ekraanile ``1824`` ja lõpetab töö.

.. note:: 
    
    Kui skripti kirjutada lihtsalt ``32 * 57``, siis midagi ekraanile ei ilmu. Sel juhul Python küll arvutab antud avaldise väärtuse, aga saadud tulemusega midagi ette ei võta.

Käsule ``print`` võib anda ka mitu argumenti, sel juhul trükitakse samale reale mitu asja järjest, tühikutega eraldatuna. Järgnev näide demonstreerib kahte samaväärset viisi, kuidas trükkida ekraanile mitu infokildu korraga. Esimene variant kombineerib andmed üheks sõneks ja kasutab seega ``print``-i ühe argumendiga, teine variant annab kõik komponendid eraldi argumentidena:

.. sourcecode:: py3

    >>> eesnimi = "Peeter"
    >>> perenimi = "Paan"
    >>> vanus = 21
    >>> print(eesnimi + " " + perenimi + " vanus: " + str(vanus))
    Peeter Paan vanus: 21
    >>> print(eesnimi, perenimi, "vanus:", vanus)
    Peeter Paan vanus: 21

Eraldi argumentidega variant on küll lühem kirja panna, aga mõnikord see siiski ei sobi, näiteks kui me ei soovi väljundis argumentide vahele tühikut.
    
.. topic:: Lisainfo

    Vaikimisi lisab ``print`` väljundi lõppu alati ka reavahetuse. Kui te seda ei soovi, siis tuleks seda näidata lisaargumendiga ``end``:

    .. sourcecode:: py3

        print('Vastus on: ', end='')    
        print(32 * 57)                  
        

    ``end`` on "peidetud" argument, mis määrab, mida kuvatakse väljundi lõppu. Vaikimisi on selle argumendi väärtuseks reavahetus (``'\n'``), aga meie seadsime selle väärtuseks *tühja sõne*, seetõttu kuvatakse antud näite väljund ühel real (mis lõpeb siiski reavahetusega, sest teine ``print`` käsk toimib ikka tavapäraselt).
    
    Tegelikult oleks saanud sama tulemuse ka lihtsamalt:
    
    .. sourcecode:: py3

        print('Vastus on: ' + str(32 * 57))    

.. index::
    single: sisend
    single: input
    
Käsk ``input``
~~~~~~~~~~~~~~
Meie "ringi" programmi viimases versioonis mainisime konkreetset raadiust vaid ühes kohas, kuid me peame ikkagi programmi muutma, kui soovime arvutada mõne teise ringi näitajaid. Alternatiivina võiks programm küsida ringi raadiuse kasutajalt.

Kasutajalt andmete küsimiseks on kõige lihtsam viis käsk **input**, mis kõigepealt kuvab ekraanile teksti selle kohta, milliseid andmeid programm ootab ning seejärel võimaldab kasutajal sisestada vastavad andmed klaviatuurilt. Kolmas versioon ringi arvutuste programmist kasutabki käsku ``input`` raadiuse küsimiseks:

.. sourcecode:: py3

    from math import *
    
    raadius_tekstina = input('Sisesta ringi raadius: ')
    raadius = float(raadius_tekstina)
    
    print('Ringi diameeter on ' + str(2 * raadius) + ' cm')
    print('Ümbermõõt on ' + str(pi * 2 * raadius) + ' cm')
    print('Pindala on ' + str(pi * (raadius ** 2)) + ' cm2')

See versioon on väga sarnane eelmisele versioonile -- viimasel kolmel real ei pidanud me midagi muutma. Erinevus on vaid selles, kuidas saab muutuja ``raadius`` oma väärtuse. Abimuutuja ``raadius_tekstina`` viitab sellele, et ``input`` annab sisestatud info alati teksti kujul. Enne kui me saame sisestatud andmeid kasutada numbrilistes arvutustes, tuleb sisestatud tekst teisendada arvuks (antud juhul ujukomaarvuks, kasutades käsku ``float``).

Teema kinnistamiseks uurige veel ühte näidet muutujate, ``input``-i ja teksti teisendamise kohta. Selles näites soovime arvutustes kasutada täisarve, seetõttu kasutame teisendamiseks käsku ``int``:

.. sourcecode:: py3

    tekst1 = input('Palun sisesta esimene täisarv: ')
    arv1 = int(tekst1)
    
    tekst2 = input('Palun sisesta teine täisarv: ')
    arv2 = int(tekst2)
    
    summa = arv1 + arv2
    print('Nende arvude summa on: ' + str(summa))

.. topic:: Meeldetuletus:

    Ärge unustage, et avaldis ``int(tekst1)`` mitte ei muuda muutujat ``tekst1`` arvuks, vaid genereerib vastava *uue* arvulise väärtuse.


Harjutus 2. Kasutaja tervitamine
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Nüüd peaks olema täiesti arusaadav eelmises peatükis esitatud tervitamise programm:

.. sourcecode:: py3

    nimi = input("Palun sisesta oma nimi ja vajuta ENTER: ")
    print("Tere " + nimi + "!")

Muutke seda programmi nii, et see küsiks eraldi kasutaja eesnime ja perekonnanime, ning tervitaks teda tema täisnimega.


Harjutus 3. Celsius-Fahrenheit teisendus
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Kirjutage programm, mis küsib kraadide arvu Celsiuse järgi ja väljastab vastavate kraadide arvu Fahrenheiti skaalas.


.. index::
    single: failid; failist lugemine
    single: sisend; failist lugemine

.. _sisendi-lugemine-failist:

Failide lugemine
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  
TODO read meetod

Siinkohal õpime ära ka ühe viisi tekstifailidest sisendi lugemiseks. Alustuseks koostage ja salvestage tekstifail nimega `andmed.txt`, mille esimesel real on inimese nimi, teisel real vanus (täisarvuna) ning kolmandal real e-maili aadress (lihtsuse mõttes ärge praegu täpitähti kasutage). NB! see peab olema *plain-text* kujul, st. Wordi fail ei sobi. Seejärel salvestage loodud failiga *samasse kausta* järgnev skript, ning käivitage see. NB! tühikud ``print`` käskude ees on olulised!

.. sourcecode:: py3

    f = open('andmed.txt')
    
    nimi = f.readline()
    vanus = f.readline()
    aadress = f.readline()
    
    print("Nimi:", nimi)
    print("Vanus:", vanus, "aastat")
    print("Aadress:", aadress)
    
    f.close()

Selgituseks: 

* Käsk ``open`` otsib failisüsteemist üles soovitud faili ja tagastab viite sellele (antud näites salvestasime selle viite muutujasse ``f``). NB! kui on antud ainult failinimi, ilma teeta, siis otsitakse seda ainult sellest kaustast, kus asub skript.
* ``f.readline()`` loeb failist ühe rea, ning tagastab selle sõnena. See käsk liigutab edasi ka failist lugemise "järjehoidjat", st. järgmisel korral sama käsku kasutades loetakse järgmine rida.
* ``f.close()`` ütleb failisüsteemile, et me oleme selle faili kasutamise lõpetanud. 

Kui seda programmi katsetate, siis märkate, et väljundis tekib iga sisestatud andmejupi järele üks üleliigne tühi rida. Põhjus on just selles, et failist lugedes jäetakse iga rea lõppu alles ka reavahetuse sümbol (faili viimase rea puhul võib see puududa, vastavalt sellele, kas failis on viimase rea lõpus reavahetus või mitte). Käsk ``print`` lisab omaltpoolt veel ühe reavahetuse.

.. note::
    Kui Python ütleb teile (Windowsi arvutis), et ta ei leia faili, aga te olete veendunud, et fail on õiges kaustas olemas, siis tuleks kontrollida, ega failinimele pole saanud eksikombel kaks faililaiendit. Segadust võib tekitada asjaolu, et Windows Explorer vaikimisi varjab teatud faililaiendid.
    
    Kõige kindlam on muuta Windowsi seadeid nii, et alati näidataks kõik faililaiendid. Selleks tuleks Windows Exploreris valida menüüribalt `Tools -> Folder options...` (kui menüüriba pole näha, siis vajutada korraks klahvi `Alt`). Avanenud dialoogis valige lehekülg `View`, ning eemaldage linnuke valiku `Hide extensions for known file types` eest.

.. note::
    Kui proovite lugeda sisse täpitähtedega teksti, siis võib juhtuda, et saate veateate ``UnicodeDecodeError``. Sel juhul tuleks ``open`` käsu rakendamisel öelda, millises kodeeringus on teie tekst, nt. ``open('andmed.txt', encoding='UTF-8')``. ``'UTF-8'`` asemel võite proovida ka ``'cp1257'``.

Harjutus 4. Reavahetuste eemaldamine
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Tuletage meelde, mida tegi sõnemeetod ``strip()``. Modifitseerige eelnevat näiteprogrammi selliselt, et programmi väljundisse ei tekiks üleliigseid reavahetusi.

Failide kirjutamine
~~~~~~~~~~~~~~~~~~~~
Järgnev programm demonstreerib andmete kirjutamist tekstifaili:

.. sourcecode:: py3

    nimi = input("Palun sisesta oma nimi: ")
    vanus = input("vanus: ")
    aadress = input("aadress: ")
    
    f = open("andmed2.txt", "w")
    f.write(nimi + "\n")
    f.write(vanus + "\n")
    f.write(aadress + "\n")
    f.close()

Selgituseks:

* failide kirjutamiseks tuleb funktsioonile ``open`` anda ka teine argument väärtusega ``"w"`` (nagu `write`).
* kui antud fail juba eksisteerib, siis ``open(..., "w")`` teeb selle tühjaks.
* erinevalt ``print`` käsust, ei tekita faili meetod ``write`` automaatselt reavahetust. Selleks, et saada eri andmeid eri ridadele, lisasime reavahetuse sümboli käsitsi.


.. index::
    single: kommentaarid


    
Kommentaarid
------------
Lisaks Pythoni jaoks mõeldud käskudele, saab programmi kirjutada `kommentaare`, mis on mõeldud vaid programmi lugemise hõlbustamiseks:

.. sourcecode:: py3
    
    # Küsin kasutaja nime
    nimi = input('Kuidas on sinu nimi? ')
    
    # Tervitan kasutajat
    print('No tere ' + nimi)
    print('Kuidas läheb?')
    
Kommentaar esitatakse ``#`` sümboliga -- Python ignoreerib kogu teksti, mis kirjutatakse sellest sümbolist kuni rea lõpuni.

Kommenteerida tuleks neid kohti programmis, mis võivad jääda lugejale segaseks. 

.. note ::
    Programmi loetavuse seisukohast on tegelikult kõige olulisemad hästi valitud muutuja- ja funktsiooninimed. Kommentaaride põhiprobleem on see, et kuna Python nende vastu huvi ei tunne, siis võivad nad programmi arenedes "vananeda", st. programmeerija muudab programmi sisu aga unustab vastava kommentaari uuendada.

Lisaks kommentaaridele võib koodi loetavuse parandamiseks kasutada ka tühje ridu.

Suur näide
--------------
.. note::

    Siin ja edasipidi proovige kõigepealt ise lahenduseni jõuda. Mõnikord see õnnestub, mõnikord mitte, aga alati treenib see teie probleemilahendamise oskust.

TODO

Ülesanded
-------------
.. note::
    Kuigi mõned järgnevad ülesanded nõuavad programmi vormistamist koos kasutajalt sisendi küsimisega, on soovitav esialgu kirjutada ``input`` käskude asemele mingid konkreetsed väärtused -- sedasi läheb võimalike arvutusvalemite katsetamine kiiremini. Kui olete saanud kätte õige valemi, siis asendage need ajutised algandmed ``input`` käskudega.


1. Pythoni dokumentatsioon
~~~~~~~~~~~~~~~~~~~~~~~~~~
* Uurige jällegi Pythoni dokumentatsioonist ``math`` mooduli kohta käivat infot (http://docs.python.org/py3k/library/math.html). Otsige välja käskude ``floor`` ja ``ceil`` tähendus -- neid võib edaspidi ülesannete lahendamisel tarvis minna.
* Vaadake üle ka sõnemeetodite dokumentatsioon (http://docs.python.org/py3k/library/stdtypes.html#string-methods). 

.. note ::
    Nurksulud Pythoni funktsioonide dokumentatsioonis näitavad, et sellele parameetrile ei pea väljakutsel tingimata väärtust andma, sest tal on olemas vaikeväärtus. Nt. kui meetodi kirjeldus on kujul ``str.center(width[, fillchar])``, siis see tähendab, et seda võib kasutada kas 1 argumendiga (nt. ``kliendi_nimi.center(80)``) või 2 argumendiga (``kliendi_nimi.center(80, '~')``).



2. Pangaarve intress
~~~~~~~~~~~~~~~~~~~~~
Kirjutage programm, mis küsib kasutajalt tema pangaarvel olevat summat ning intressi protsenti, mida pank talle igal aastal maksab. Vastuseks peab programm väljastama pangaarvel oleva summa 5 aasta pärast.

**Testige** oma programmi erinevate summa ja intressi kombinatsioonidega!

.. topic:: Lisaülesanne

    Kui olete saanud õige valemi paika, siis modifitseerige oma programmi nii, et kasutajalt küsitakse vaid intressi protsent ja algsumma loetakse tekstifailist.

3. Küpsisetort
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Küpsisetordi tegemisel laotakse küpsised ristkülikukujulisele kandikule ja seda mitmes kihis, nii, et igas kihis on sama palju küpsiseid. Küsida kasutajalt, mitu küpsist mahub kandikule laiuses ja mitu pikkuses ning kui mitme kihilist torti ta teha soovib. Seejärel küsida, kui mitu küpsist on ühes pakis.

Lõpuks väljastada, mitu küpsisepakki tuleb sellise tordi tegemiseks osta. NB! Eeldame, et poolikut küpsisepakki osta ei saa.

**Testige** oma programmi! Valige vähemalt üks komplekt algandmeid nii, et küpsistest jätkub täpselt ja vähemalt üks komplekt nii, et osa ostetud küpsiseid jääb üle.

4. Nimede korrastamine
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Modifitseerige veelkord kasutaja tervitamise programmi, kus kasutaja sisestab eraldi ees- ja perenime ning programm tervitab teda täisnimega. 

Seekord peaks programm vastama alati selliselt, et nii eesnimi, kui perenimi algavad suure tähega ja ülejäänud tähed on väikesed, hoolimata sellest, kuidas nimi sisestati (olgu ainult väikeste tähtedega, ainult suurtega või segamini).

.. hint::

    .. sourcecode:: py3
    
        >>> "pEEteR".capitalize()
        'Peeter'
    
.. note::

    Praegu on aktsepteeritav, kui programm ei esita sidekriipsuga nimesid ootuspäraselt (nt. kui kasutaja sisestas eesnimeks `Mari-Liis`, siis on OK, kui programm muudab selle `Mari-liis`-iks).
    
.. admonition:: Väljakutse

    Kui see ülesanne oli teie jaoks liiga lihtne, siis proovige muuta programmi selliselt, et nt. `Mari-Liis`, `mari-liis` ja `mAri-liiS` muudetakse kõik `Mari-Liis`-iks.
    
    NB! selle jaoks läheb tarvis ühte Pythoni konstruktsiooni, mida pole selles peatükis tutvustatud! 
    
    .. hint::
    
        http://www.google.com
    
    .. hint::
    
        .. sourcecode :: py3
        
            >>> x = "tere"
            >>> x[0]
            't'
            >>> x[1]
            'e'
            >>> x[2]
            'r'
            >>> x.find("r")
            2
            >>> x[0:2]
            'te'
            >>> x[2:4]
            're'
        
        Kui te pole veendunud, et saite konstruktsiooni ``[...]`` tähendusest aru, siis lugege täpsemalt siit: http://docs.python.org/py3k/tutorial/introduction.html#strings. Antud õpikus käsitleme seda teemat alles järjendite peatükis.

5. Redeli pikkus
~~~~~~~~~~~~~~~~~~
Kirjutage programm, mis arvutab mitme pulgaga redelit läheb vaja mingile kõrgusele ronimiseks. Programm peaks küsima kasutajalt soovitud kõrguse ning väljastama minimaalse ja maksimaalse pulkade arvu, mis peaks sobival redelil olema. Arvestame, et:
 
    * redeli alumine ja ülemine pulk on redeli otstest 15cm kaugusel
    * redeli pulkade vahekaugus on 25cm
    * redeli ülemine ots peab toetuma etteantud kõrgusele
    * nurk redeli ja maapinna vahel peab olema vahemikus 50° - 80°

.. hint::

    Selleks, et arvutused ei läheks liiga keeruliseks, on soovitav vahetulemused salvestada abimuutujatesse.

Projekt
---------------
Kuna teie projektiidee jaoks võib minna vaja vahendeid, mille jaoks Pythoni standardteegis moodulit ei leidu, vaatame siinkohal järgi, kuidas võtta kasutusele internetist leitud mooduleid.

.. index::
    single: kolmanda osapoole moodulid
    single: moodulid; kolmanda osapoole moodulid

Kolmandate osapoolte moodulid
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Neid mooduleid, mis ei kuulu Pythoni standardteeki ja mida te pole ise kirjutanud, vaid internetist alla laadinud, nimetatakse tavaliselt *kolmandate osapoolte* mooduliteks (ing. k `third party modules`).  Siinkohal demonstreerime ühe lihtsa kolmanda osapoole mooduli kasutamist.

Laadige alla moodul :download:`bingtrans <downloads/bingtrans.py>`, mis võimaldab kasutada Microsoft Bing tõlketeenust (NB! salvestage ta nimega ``bingtrans.py``). Seejärel salvestage samasse kausta järgnev programm ja katsetage seda:

.. sourcecode:: py3
    
    from bingtrans import translate
    
    eesti_keeles = input("Palun sisesta eestikeelne sõna (või lause): ")
    ing_vaste = translate(eesti_keeles, 'et', 'en')
    print("Inglise keelne vaste: " + ing_vaste)

Me importisime moodulist ``bingtrans`` funktsiooni nimega ``translate``, mis võtab argumentideks tõlgitava teksti, lähtekeele koodi (eesti keele kood on ``'et'``) ning sihtkeele koodi. Proovige ka teisi keelekoode (nt. ``'ru'``, ``'fr'``, ``'ko'``).

.. admonition:: Harjutus

    Proovige nüüd kohandada antud näidet nii, et tõlgitav sõna või lause ning keelekood loetakse tekstifailist.

``bingtrans.py`` on lihtsustatud versioon Byung Gyu Ahn'i poolt kirjutatud moodulist, mis asub aadressil https://github.com/bahn/bingtrans. 

Selle näite moraal on see, et internetis on saadaval Pythoni mooduleid, mis võivad väga tehnilise programmeerimisülesande muuta väga lihtsaks. Selleks, et saada aimu, milliseid võimalusi veel leidub, soovitame külastada aadressi http://pypi.python.org/pypi.
    
Tavaliselt on kolmandate osapoolte moodulid pakendatud koos installeerimisskriptidega ja nende paigaldamine võib nõuda pisut tehnilist tööd. Vastavaid juhiseid saab huvi korral lugeda siit: http://docs.python.org/py3k/install/index.html.

.. admonition:: Väljakutse

    Proovige leida internetist Pythoni moodul (või moodulite kogum e. `pakett`, ing. k `package`), mille abil saab Twitteri sõnumeid kirjutada ja lugeda. Üritage selle abil midagi postitada.
    
    NB! varuge piisavalt aega ja kannatust, et võimalike tehniliste katsumustega hakkama saada. Võibolla peate valitud paketi installimiseks töötama ka käsureal (selle kohta leiab juhiseid eelmise peatüki lisalugemises). Samas, läbi taolise "mässamise" saab oma OP-süsteemi kõige paremini tundma õppida.


