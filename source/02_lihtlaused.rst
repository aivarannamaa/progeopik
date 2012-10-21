2. Avaldised ja lihtlaused
================================

Selles peatükis vaatame süstemaatilisemalt üle mõned programmeerimise põhiteemad, millega esimeses peatükis juba põgusalt kokku puutusite: operatsioonid *arvude* ja *tekstiga*, *muutujad* ning *sisendi* ja *väljundi* kasutamine. 

.. topic:: Soovitus:

    Näited lugege kõigepealt hoolikalt läbi, mõeldes, milline võiks olla tulemus ja alles seejärel katsetage. Soovitav on teha ka väikeseid muudatusi ning ennustada, kuidas need tulemust mõjutavad. 

Terminoloogia
-------------
.. note::

    NB! Kuigi allpool toodud terminid kõlavad tähtsalt, on sisuliselt tegemist küllalt lihtsate mõistetega -- neid tuleb lihtsalt teada, et programmeerijate kõnepruugist aru saada.

.. index::
    single: väärtus
    
**Väärtused** (ing.k. `values`) on andmed, mida programm kasutab või loob. Mõned näited väärtustest:

* arv *2*
* arv *2,3*
* tekst *Tartu*

Keeles Python pannakse need väärtused kirja järgmiselt:

* ``2``
* ``2.3`` NB! koma asemel kasutatakse punkti
* ``'Tartu'``

.. index::
    single: andmetüüp; tüüp
    single: tüüp
    
Kõikidel väärtustel on kindel **andmetüüp**, või lihtsalt **tüüp**. Meie näiteväärtuste tüübid on vastavalt *täisarv*, *ujukomaarv* ja *sõne*. Edaspidi vaatame ka Pythoni keerulisemaid andmetüüpe (*järjend*, *sõnastik* jt.)

.. index::
    single: tehe; operatsioon
    single: operatsioon
    
Andmetüübi mõiste on oluline, kuna eri tüüpi väärtustega saab kasutada erinevaid **operatsioone** (e. *tehteid*) -- nt. arve saab omavahel liita, sõnesid (e. teksti) saab teisendada suurtähtedesse jne.

Analüüsime järgmist näidet:

.. sourcecode:: py3

    >>> 2 + 3
    5

Antud juhul teostas Python liitmisoperatsiooni väärtustega ``2`` ja ``3``, mille tulemusena konstrueeriti uus väärtus ``5``. Programmeerimise terminoloogiat kasutades saame seda näidet kirjeldada järgnevalt:

.. index::
    single: operaator
    single: argumendid; operaatori argumendid
    single: operaator; operaatori argumendid
    single: avaldis; avaldise väärtustamine
    single: avaldis
    single: literaalid
    
    
*  ``+`` on **operaator**
* ``2`` ja ``3`` on selle operaatori **argumendid** (öeldakse ka `operandid`)
* ``2 + 3`` on **avaldis** (ing.k. `expression`)
* `5` on antud **avaldise väärtus**
* toiming, mille käigus ``2 + 3``-st saadakse `5`, on **avaldise väärtustamine** (ing.k. *evaluation*)
* väärtuseid, mis on programmi "sisse kirjutatud" (antud näite puhul ``2`` ja ``3``), nimetatakse **literaalideks**

Järgnevalt uurime lähemalt, milliseid operatsioone saab teha arvude ja sõnedega. 

Arvud
-----
Pythonis (nagu ka enamikes teistes programmeerimiskeeltes) on eraldi andmetüübid täis- ja reaalarvude esitamiseks.

.. index::
    single: täisarvud

Täisarvud
~~~~~~~~~
Pythoni **täisarvu** tüübi nimeks on `int` (lühend sõnast *integer*). Erinevalt paljudest teistest keeltest, ei ole Python 3-s piiratud, kui suuri (või väikseid) täisarve saab selle andmetüübiga esitada.

.. index::
    single: ujukomaarvud
    
Ujukomaarvud
~~~~~~~~~~~~
Reaalarvudele vastavad Pythonis (ja paljudes teistes keeltes) **ujukomaarvud** (ing. k. `floating point number`, lühemalt `float`). 

.. note::
    Nimetus `ujukomaarvud` tuleb nende esitusviisist arvuti mälus -- lihtsustatult võib öelda, et kõigepealt on toodud välja arvu numbrite jada (ing.k `significant digits`) ning eraldi on öeldud, millisele positsioonile käib koma (seega koma on numbrijadast sõltumatu, "ujuv").

Ujukomaarvude literaalid võivad esineda järgmistel kujudel:

* ``3.0``, ``1.165``, ``-4.25`` tavapärane kirjapilt. NB! koma asemel kasutatakse punkti
* ``6.1529e+18``, ``1.253e-12`` nn. `teaduslik notatsioon`

.. note::

    Viimast kirjapilti kasutatakse väga suurte või nullilähedaste arvude esitamiseks. Tavapärases matemaatilises notatsioonis võiks viimased näited kirjutada vastavalt 6.1529×10\ :sup:`18` ja 1.253×10\ :sup:`-12`.
    
.. topic:: Ujukomaarvude ligikaudsus

    Proovige läbi järgnev lihtne näide:

    .. sourcecode:: py3
        
        >>> 0.1 * 3.0
        0.30000000000000004

    Ootuspärane vastus oleks `0.3`, kuid Python tagastas midagi muud.

    Asi on selles, et arvutis esitatakse ujukomaarvud kahendkujul, kasutades piiratud arvu bitte ja seetõttu polegi võimalik teatud kümnendmurde (nende hulgas `0.1`) täpselt esitada (analoogiliselt pole kümnendmurruna võimalik täpselt esitada näiteks `10 / 3`). Taolistel juhtudel ümardatakse sisestatud arv lihtsalt lähima võimaliku kahendmurruni ja see ongi põhjus, miks antud näites oli tulemus ebatäpne. 

    Kui ujukomaarvu on tarvis esitada kümnendmurruna (nt. ekraanile kuvamisel), siis toimub jälle ümardamine -- see on põhjus, miks sisestades käsureale ``0.1`` antakse vastuseks tagasi ``0.1``, kuigi Python sisimas ei suuda seda arvu täpselt esitada. Kui korrutasime ``0.1`` 3-ga, siis muutus viga juba piisavalt suureks, et saadud tulemusele lähim võimalik kümnendmurd oli ``0.30000000000000004``, mitte ``0.3``

    Tegelikult tekitab ujukomaarvude ligikaudsus probleeme vaid siis, kui me eeldame reaalarvude absoluutselt täpset esitamist (nt. kümnendmurruna esitatud rahasummad, kus murdosa tähistatab sente). Ujukomaarve kasutatakse peamiselt kõikvõimalike mõõtmistulemuste esitamiseks ja selle jaoks on Pythoni `float` tüübi ulatus ning täpsus enam kui piisav.

    
Operatsioonid arvudega
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
    


.. topic:: Operatsioonid negatiivsete arvudega

    Mitmed operaatorid ja funksioonid annavad esmapilgul üllatava tulemuse, kui neid kasutada negatiivsete argumentidega. Proovige järgi, kuidas toimivad sel puhul ``//``, ``%``, ``int`` ja ``round``.

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
      
.. index::
    single: sõne
    single: string; sõne
    
Sõned
--------
Programmeerimine pole ainult arvudega manipuleerimine, paljudes programmides on palju tähtsamal kohal töö *tekstiga* (tuletage meelde näiteks esimese peatüki programmi, mis kuvas ekraanile teksti *Tere maailm!*). Selle tarvis on Pythonis olemas eraldi andmetüüp **sõne** (ing.k `string`, lühend `str`), mida kasutatakse justnimelt teksti esitamiseks.

Konkreetsed tekstijupid pannakse programmi tekstis kirja *sõneliteraalidena*. Enamasti piisab sõneliteraali kirjapanekuks sellest, kui soovitud tekst piiritletakse ülakomade või jutumärkidega, nt. ``'Tartu'`` või ``"Kauneim linn on Eestis Tartu"``.

Pange tähele, et tekst, mida antud sõneliteraalid esitavad on *Tartu* ja *Kauneim linn on Eestis Tartu*, st. piiritlejana kasutatud ülakomad/jutumärgid ei kuulu sõne sisu juurde. Demonstreerime seda ``print`` käsu abil, mis toob ekraanile alati sõne *tegeliku* sisu, hoolimata sellest, kuidas ta programmi tekstis kirja on pandud:

.. sourcecode:: py3

    >>> print("Tartu")
    Tartu


.. admonition:: NB!

    Kui unustate sõneliteraali kirjutades piiritlejaid kasutada, siis peab Python vastavat tekstijuppi muutuja nimeks (või kui tekstis oli tühik, siis ei oska ta sellest midagi arvata). Proovige järgi, millised veateated neil juhtudel antakse -- siis on edaspidi taolisi näpuvigu kergem tuvastada.


Loomulikult saab sõneliteraali (nagu iga teise literaaliliigi) väärtuse salvestada muutujasse, et seda hiljem kasutada. Igal pool, kus võib kasutada sõneliteraali, võib kasutada ka sõnemuutujat (ja vastupidi):

.. sourcecode:: py3

    >>> nimi = "Peeter"
    >>> print(nimi)
    Peeter
    >>> print("Peeter")
    Peeter




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


Operatsioonid sõnedega
~~~~~~~~~~~~~~~~~~~~~~
+-------------------------------------+--------------------+---------------------------------------------------------------------+
| Avaldis                             | Väärtus            | Kommentaar                                                          |
|                                     | (literaalina)      |                                                                     |
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
| ``'jäääär'.count('ä')``             | ``4``              |                                                                     |
+-------------------------------------+--------------------+---------------------------------------------------------------------+
| ``' tere '.strip()``                | ``'tere'``         | Annab sõne ilma alguses ja lõpus olevate tühikute ja reavahetusteta |
+-------------------------------------+--------------------+---------------------------------------------------------------------+
| ``'tere'.replace('e','ö').upper()`` | ``'TÖRÖ'``         | Käske saab kombineerida                                             |
+-------------------------------------+--------------------+---------------------------------------------------------------------+


.. note::
    Kõikide sõnemeetoditega saab tutvuda aadressil http://docs.python.org/py3k/library/stdtypes.html#string-methods

.. index::
    single: muutujad
    
.. _muutujad:    

Muutujad
--------
Kõik levinud programmeerimiskeeled võimaldavad konkreetsetele väärtustele või arvutuste tulemustele anda nime. Teisiti väljendudes: väärtusi saab salvestada **muutujatesse**. Järgnev käsurea näide demonstreerib muutuja (nimega `x`) defineerimist ja kasutamist:

.. sourcecode:: py3
    
    >>> x = 2 + 3
    >>> x
    5
    >>> 2 * x
    10
    >>> x * x
    25

Esimesel real teeb Python kaks erinevat toimingut: kõigepealt väärtustab avaldise ``2 + 3`` ning seejärel salvestab saadud tulemuse muutujasse ``x``. Programmeerijate kõnepruugis: muutujale ``x`` **omistatakse** avaldise ``2 + 3`` väärtus. Peale seda on võimalik muutuja nime kasutada vastava väärtuse asemel. 

.. note::

    Pange tähele, et Python salvestas muutujasse ``x`` justnimelt avaldise *väärtuse* (st. `5`), mitte avaldise ``2 + 3`` enda. See nüanss muutub oluliseks edaspidi, kui hakkame muutujate väärtusi muutma.

Programmi loetavuse huvides peaks muutuja nimi kirjeldama vastava väärtuse tähendust antud kontekstis (nt. ``brutopalk`` või ``isikukood``). Kui on tarvis kasutada mitmest sõnast koosnevat muutuja nime, siis tuleks kasutada tühikute asemel allkriipse, nt. ``laste_arv``. Muutuja nimes võib kasutada ka numbreid, aga esimene sümbol peab olema täht (või allkriips).

.. topic :: Etteruttavalt:

    Pythonis saab vajadusel muutuja väärtust ka uue väärtusega üle kirjutada -- selleks tuleb lihtsalt teha uus omistamine samale muutujale. Muutuja ülekirjutamist meil praegu siiski veel tarvis ei lähe.


.. _milleks-muutujad:
    
Milleks muutujad?
~~~~~~~~~~~~~~~~~
Vaatame ühte näiteprogrammi, mis väljastab 60.25cm raadiusega ringi diameetri, ümbermõõdu ja pindala. Esimese versiooni kirjutame ilma muutujaid kasutamata:

.. sourcecode:: py3

    from math import *
    
    print('Ringi diameeter on ' + str(2 * 60.25) + ' cm')
    print('Ümbermõõt on ' + str(pi * 2 * 60.25) + ' cm')
    print('Pindala on ' + str(pi * (60.25 ** 2)) + ' cm2')
    
.. topic:: Meeldetuletus: 
    
    Käsku ``str`` kasutame selleks, et arvutuse tulemust teisendada sõneks.

See programm arvutab, mida me soovisime, kuid kui me hiljem tahame selle programmiga arvutada mõne teise raadiusega ringi infot, siis peaksime tegema vastava muudatuse kolmes kohas. Sellise kompaktse programmi puhul ei ole see küll probleemiks, kuid reaalsetes programmides on taolisel juhul suur oht, et mõnes kohas ununeb muudatus tegemata. 

Kirjutame nüüd sama programmi ümber kasutades raadiuse hoidmiseks muutujat:

.. sourcecode:: py3

    from math import *
    
    raadius = 60.25
    print('Ringi diameeter on ' + str(2 * raadius) + ' cm')
    print('Ümbermõõt on ' + str(pi * 2 * raadius) + ' cm')
    print('Pindala on ' + str(pi * (raadius ** 2)) + ' cm2')

Siin on konkreetset raadiust mainitud vaid ühes kohas -- muutuja ``raadius`` defineerimisel. Edaspidi on valemites kasutatud muutuja nime. Programmi jooksutamisel asendab Python muutuja nimed muutuja väärtusega ja seetõttu annab see versioon sama tulemuse, mis eelminegi. Samas, kui meil on vaja programmi edaspidi kohandada mõne muu ringi jaoks, siis on vaja muudatus teha vaid ühes kohas. Seega, muutuja kasutamine aitas meil teha programmis olevad arvutused *üldisemaks*, konkreetsest väärtusest sõltumatuks.

.. topic :: Analoogia:

    Mõelge Eesti Vabariigi põhiseadusele -- kui seal räägitakse presidendi rollist, siis ei nimetata ühegi konkreetse presidendi nime vaid kasutatakse väljendit *Vabariigi President*. Seaduse rakendamisel tõlgendatakse seda väljendit vastavalt sellele, kes on antud hetkel presidendiks. Selline lähenemine teeb seaduse teksti üldisemaks, konkreetsetest isikutest sõltumatuks.

.. _operatsioonid-muutujatega:
    
Operatsioonid muutujatega
~~~~~~~~~~~~~~~~~~~~~~~~~~
Kõiki arvu- ja sõneoperatsioone, mida demonstreerisime eelnevalt kasutades literaale, saab kasutada ka vastavalt arv- ja sõnemuutujatega:

.. sourcecode:: py3

    >>> tervitus = 'Tere'
    >>> len(tervitus)
    4
    >>> tervitus.upper()
    'TERE'
    >>> n = 3
    >>> n * n
    9
    >>> n * tervitus
    'TereTereTere'

.. topic:: Tähtis!!!

    Kui arvu- või sõneoperatsioonides (e. tehetes) kasutada muutujaid (nt. ``n + 1`` või ``tekst.upper()``), siis võib avaldise kujust jääda mulje, et operatsiooni käigus muudetakse muutuja väärtust. Tegelikult genereeritakse tehte tulemusena hoopis *uus väärtus* ja kasutatud muutujaga midagi ei juhtu.
    
    Selles veendumiseks uurige järgmisi käsurea näiteid, kus kõigepealt omistatakse muutujale mingi väärtus, seejärel kasutatakse muutujat mingis tehtes (mis konstrueerib uue väärtuse), ning lõpuks demonstreeritakse, et see ei mõjutanud muutuja väärtust:
    
    .. sourcecode:: py3
    
        >>> n = 3
        >>> n + 2
        5
        >>> n
        3
        
    .. sourcecode:: py3
    
        >>> tervitus = '  tere  '
        >>> tervitus.strip()
        'tere'
        >>> tervitus
        '  tere  '
        
    .. sourcecode:: py3
    
        >>> tekst = '3'
        >>> int(tekst)
        3
        >>> tekst
        '3'


Funktsioonid
---------------
Funktsioonid on need Pythoni objektid, mille abil saab midagi arvutada või teha. Me oleme siiani näinud hulka erinevaid funktsioone, nt ``sin``, ``cos``, ``int``, ``input``, ``print``.

Funktsiooni kasutamiseks e. `rakendamiseks` tuleb kirjutada tema nimi ja selle järel sulud. Sulgudes võib olla 0 või rohkem `argumenti` so. miski, mida funktsioon oma töös kasutab. Näiteks lauses ``print("tere")`` tähistab ``print`` funktsiooni, ``"tere"`` on tema argument ja kõik see kokku on funktsiooni rakendamine (e. `funktsiooni applikatsiooni`).

Mõned funktsioonid (nt. ``sin`` ja ``int``) on olemuselt küllalt sarnased matemaatikast tuntud funktsioonidele, kuna nad "võtavad" ühe väärtuse ja "annavad vastu" mingi teise väärtuse. Nt ``int("3")`` võtab sõne tüüpi väärtuse ``"3"`` ning annab vastu täisarvu tüüpi väärtuse ``3``. See võimaldab nende funktsioonide kasutamist avaldistes.

Lisaks sellele, et funktsiooni rakendamist võib kasutada mingi avaldise komponendina, võib ka funktsiooni argument olla ükskõik kui keeruline avaldis, sh. funktsiooni rakendamine:

.. sourcecode:: py3

    >>> x = 4
    >>> round(cos(sin(float("0" + "." + str(x)) + 4)), 2)
    0.58



Funktsioonidest tuleb edaspidi veel palju juttu, seepärast me praegu nendel pikemalt ei peatu.

``import``-lause
--------------------
Pythoni `standardteegis` (so. funktsioonide ja teiste programmielementide kogum) on väga palju funktsioone (ja teisi Pythoni objekte). Nende paremaks organiseerimiseks on nad jaotatud gruppidesse, mida nimetatakse `mooduliteks`. ``import`` lause teeb moodulis oleva funktsioonid programmi jaoks kättesaadavaks. Meeldetuletuseks näide, kus me soovime kasutada ainult kahte funktsiooni moodulist ``math``:

.. sourcecode:: py3

    from math import sin, cos
    
    print(sin(0.3))
    print(cos(sin(0.3)))

Kui soovime moodulist kõiki funktsioone, siis võime kasutada import lauses funktsiooninime(de) asemel tärni:

.. sourcecode:: py3

    from turtle import *
    
    forward(100)
    left(90)
    forward(100)

    
Mõned funktsioonid, nagu näiteks ``int`` ja ``float``, on alati kättesaadavad, neid pole vaja importida.

.. note::

    Importida saab ka moodulit ennast, sel juhul tuleb soovitava funktsiooni nimi kirjutada koos mooduli nimega:
    
    .. sourcecode:: py3
    
        >>> import math
        >>> print(math.sin(0.5))
        0.479425538604203
        >>> print(math.cos(0.5))
        0.8775825618903728    

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


