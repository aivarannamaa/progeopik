4. Funktsioonid
====================================



.. todo::
    
    * lisa kombinatoorika ülesandeid
    * lisa samaväärsuse küsimusi


    * omistamise += kuju üle korrata?
    * TODO: muutujate juurde: Pange tähele, et Python salvestas muutujasse ``x`` justnimelt avaldise *väärtuse* (st. `5`), mitte avaldise ``2 + 3`` enda. See nüanss muutub oluliseks edaspidi, kui hakkame muutujate väärtusi muutma.
    * TODO: Wikipedia sirvimise näide funktsiooni väljakutsete mõistmiseks
    * TODO: **näited** selle kohta, et ühte funktsiooni saab välja kutsuda mitu korda
    * TODO: väljakutse, meetod, argument
    * TODO: Kontrollküsimus: funktsioon, mis teeb midagi n korda kutsutakse välja m korda. Mitu korda tehakse midagi?
    * "Let's wrap it in a function to make it easier to use" -- tee selle kohta näide
    * calling a function *generates* a value
    * funktsioonide komponeerimine avaldises & funktsioonid, mis kutsuvad välja teisi funktsioone
    * bool funktsioonid
    * Ülesanded, kus ühe ülesande lahenduses on vaja teise ülesande funktsiooni
    * paaris, paaritu defineerimine vastastikuselt
    * Definitsioonide laadimine käsureale, harjutused, kus on näidatud käsurea sessioon, aga puudu on definitsioonid, Lõpuks Docstringi ja doctest'i tutvustamine
    * üldistamise harjutus: vt. ex2 http://www.openbookproject.net/thinkcs/python/english2e/ch07.html#exercises
    * roles of variables
    * roles of functions: utility functions, reuse, division, documentation, encapsulation
    * paralleelid muutujate ja funktsioonide vahel -> tadaa
    

Eelmises peatükis vaatasime, kuidas lasta Pythonil teha mingit tegevust mitu korda järjest. Kuidas käituda aga siis, kui mingit keerulist tegevust on vaja teha mitu korda, aga mitte järjest, vaid erinenevates programmi osades ja võibolla ka teatud variatsioonidega?

Selles peatükis uurimegi, kuidas pakendada mingi programmijupp *funktsiooniks* ja kuidas seda hiljem erinevates kohtades kasutada saab. Teisiti öeldes, me hakkame looma uusi Pythoni käske. Alustuseks aga vaatame üle mida me Pythoni käskude kohta juba teame.

Mis on funktsioon?
-------------------
Siiani olnud juttu mitmetest erinevatest Pythoni "käskudest", nagu näiteks ``input``, ``sin``, ``right``, ``is_wall``, ``int``, ``readline``, ``upper``, ``print``. Tegelikult on korrektsem termin nende kohta *funktsioon*.

Kuigi paljudel juhtudel saab tõmmata paralleelid Pythoni funktsioonide ja matemaatikast tuntud funktsioonide vahele, on Pythoni jaoks funktsiooni mõiste siiski veidi avaram. Alustuseks ütleme lihtsalt, et funktsioon (e. mitteformaalselt *käsk*) on mingi Pythoni maailma "tegelane", millel on (tavaliselt) nimi ja mis oskab midagi arvutada või teha. 


Funktsioonide kasutamine
-----------------------------
Toome meeldetuletuseks mõned näited programmifragmentidest, kus on kasutatud funktsioone:

* ``nimi = input("Sisesta oma nimi: ")``
* ``vanus_arvuna = int(sisestatud_vanus)``
* ``if is_wall(): ...``
* ``print(sqrt(sin(0.5)))``

Esimene tähelepanek on see, et funktsiooni kasutamiseks tuleb kirjutada tema nimi ja selle järel sulud. Sulgudes võib olla 0 või rohkem **argumenti** so. miski, millega me saame funktsiooni tööd kuidagi mõjutada. Näiteks lauses ``print("tere")`` tähistab ``print`` funktsiooni, ``"tere"`` on tema argument ja kõik see kokku on funktsiooni **rakendamine** (e. *väljakutse* või *aplikatsioon*). Argumendid võivad olla mingid konkreetsed väärtused, muutujad või mingid muud avaldised (sh. funktsioonide rakendused).

Teatud funktsioonide (nt. ``upper``) rakendamiseks tuleb kirjutada üks argument funktsiooni nime ette (nt. ``'tere'.upper()``) -- selliseid funktsioone nimetatakse **meetoditeks**. Sedalaadi funktsioonide defineerimist me ei vaata, aga oma olemuselt ei erine need väga palju tavalistest funktsioonidest.

Arvutamine vs. "tegemine"
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  
Siiani oli meil kombeks uusi Pythoni konstruktsioone lahterdada avaldiste või lausete hulka. Nüüd tekib küsimus, kas mingi funktsiooni rakendus (nt. ``sqrt(sin(x))`` või ``print('Tere!')``) on avaldis või lause?

Mõned funktsioonid (nt. ``sin``, ``sqrt`` ja ``int``) on olemuselt küllalt sarnased matemaatilistele funktsioonidele, kuna nad "võtavad" ühe väärtuse, arvutavad natuke ja "annavad vastu" e. *tagastavad* mingi teise väärtuse (nt. avaldisega ``sqrt(4)`` anname funktsioonile ``sqrt`` argumendiks väärtuse ``4`` ning funktsioon annab meile vastu väärtuse ``2.0``). Selliste funktsioonide rakendused on oma olemuselt avaldised, mis tähendab, et me võime neid kasutada igal pool, kus avaldised on lubatud, näiteks omistuslauses või mõne teise funktsiooni argumendina. 

Siia gruppi loeme ka need funktsioonid, mille rakendus võib anda igal korral erineva väärtuse, näiteks ``input("Sisesta midagi: ")`` või Pykkari ``is_wall()``. Kuigi need pole funktsioonid matemaatilises mõttes, kasutatakse ka neid avaldistes.

Teiste funktsioonide rakendamisel (nt. ``print('Tere')``, ``right(90)``, ``step()``) huvitab meid see, mida nad *teevad* -- me tahame, et midagi *juhtuks* (nt. et ekraanile ilmuks uus tekstijupp või robot liigutaks ennast). Selliste funktsioonide rakendusi loeme me lauseteks ja seetõttu esinevad nad programmides omaette real. Funktsioonide defineerimise õppimist alustame just seda tüüpi funktsioonidega.


.. note::

    Mõnedes keeltes kasutatakse tegevusele orienteeritud funktsioonide jaoks eraldi terminit *protseduur*.



Funktsioonide defineerimine
-----------------------------------------
Enne, kui funktsiooni saab kasutada, tuleb ta *defineerida*. Meile tuttavad funktsioonid on defineeritud Pythoni loojate poolt, seepärast ei pidanud me siiani selle peale mõtlema. Paraku pole alati võimalik ette ennustada, milliseid funktsioone võiks programmeerijatel vaja minna, seepärast lubab Pythonis neid ka programmeerijatel ise defineerida.

Oletame, et meil on vaja joonistada kilpkonnaga 3 ruutu, kõik küljepikkusega 30, aga nad peavad olema erinevates kohtades: esimene ruut ekraani keskel, teine üleval-paremal, kolmas üleval-vasakul ja teisest natuke allpool. 

Kui see programm kirjutada "jõumeetodil", siis sisalduks programmis ruudu joonistamise kood kolmes kohas:

.. sourcecode:: py3

    # "Jõuga" programmeeritud variant
    from turtle import *

    joonistatud_külgi = 0
    while joonistatud_külgi < 4:
        forward(30)
        left(90)
        joonistatud_külgi += 1 

    up()
    forward(100)
    left(90)
    forward(100)
    down()

    joonistatud_külgi = 0
    while joonistatud_külgi < 4:
        forward(30)
        left(90)
        joonistatud_külgi += 1 

    up()
    left(90)
    forward(200)
    down()

    joonistatud_külgi = 0
    while joonistatud_külgi < 4:
        forward(30)
        left(90)
        joonistatud_külgi += 1 

    exitonclick()    

Lahendus oleks palju lihtsam, kui ruudu joonistamiseks oleks olemas eraldi funktsioon. ``turtle`` moodulis sellist ei leidu, aga me võime selle ise *defineerida* ja seejärel kasutada justkui iga teist Pythoni funktsiooni:

.. sourcecode:: py3
    :emphasize-lines: 4-9,11,19,26    
    
    # Kavalam variant
    from turtle import *
    
    def ruut():
        joonistatud_kylgi = 0               
        while joonistatud_kylgi < 4:
            forward(30)
            left(90)
            joonistatud_kylgi += 1
    
    ruut()
    
    up()
    forward(100)
    left(90)
    forward(100)
    down()
    
    ruut()
    
    up()
    left(90)
    forward(200)
    down()
    
    ruut()
    
    exitonclick()


Ilmselt juba taipasid, et funktsioonide defineerimisega on seotud konstruktsioon, mis algab võtmesõnaga ``def``. Selle konstruktsiooni päises antakse funktsioonile nimi ja kehas näidatakse need laused, mida tuleks käivitada funktsiooni rakendamisel. Antud juhul kopeerisime funktsiooni kehasse algsest programmist ruudu joonistamise koodi. Seejuures pidime muidugi selle pisut paremale nihutama, et oleks aru saada, et see kuulub ``def`` lause alla. Pärast ``def`` lause käivitamist on Pythonil üks käsk juures, mida saab rakendada samal põhimõttel nagu sisseehitatud funktsioone. (Erinevus on selles, et uus funktsioon kehtib ainult sama programmi piires -- kui tahad seda kasutada ka järgmistes programmides, siis tuleb see uuesti defineerida.)

.. admonition:: NB!

    ``def`` konstruktsioon jätab enda kehas olevad laused lihtsalt meelde, need käivitatakse alles siis, kui defineeritud funktsiooni rakendatakse.
    

Kontrollküsimus: Mitu kala?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
Mitu korda kirjutab järgnev programm ekraanile sõna "kala"? NB! proovi vastata ilma programmi käivitamata! Kui oled vastanud, siis kontrolli oma vastust Pythoni abil.

.. sourcecode:: py3

    def a():
        print("kala")
        print("kala")
    
    def b():
        a()
        print("kala")
        a()

    b()
    b()

Funktsiooni defineerimine ja kasutamine
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Jätame hetkeks kilpkonna kõrvale ja vaatleme ühte väga lihtsat näidet funktsioonide defineerimisest. Järgnevas näiteprogrammis defineeritakse funktsioon nimega ``tere``:

.. sourcecode:: python

    def tere():
        print("Tere")
        print("Kuidas läheb?")

Esimest rida, mis algab ``def``-iga, nimetame funktsiooni **päiseks**, järgnevad read, mis on tühikutega paremale nihutatud, moodustavad funktsiooni **keha**. 

Proovi seda kolmerealist programmi käivitada. Kui kõik läks õigesti, ei ilmu ekraanile midagi. Nimelt on programmis antud juhul toodud vaid teatud tegevuse kirjeldus, kuid seal pole käsku seda (ega ühtegi teist) tegevust täita.

Sisuliselt me defineerisime uue käsu ``tere``, mille rakendamisel peab Python käivitama laused ``print("Tere")`` ja ``print("Kuidas läheb?")``. Kõik need "käsud", mida oled siiani kasutanud (nt. ``print`` ja ``sin``) on samuti kuskil funktsioonidena defineeritud. Edaspidi kasutame sõna `käsk` asemel põhiliselt sõna `funktsioon`. 

Nagu ikka, tuleb funktsiooni (käsu) kasutamiseks kirjutada selle nimi koos sulgudega e. programmeerijate kõnepruugis: funktsioon tuleb **välja kutsuda** (või *rakendada*). Proovi järgmist, täiendatud programmi:

.. sourcecode:: python

    def tere():
        print("Tere")
        print("Kuidas läheb?")
    
    # funktsiooni defineerimise ja väljakutse vahel võib olla
    # ükskõik kui palju muid lauseid
    print("blaa, blaa, blaa")
    # ...
    
    tere() # funktsiooni väljakutse e. rakendamine

.. note::

    Antud näites on nii funktsiooni definitsioonis, kui ka väljakutses kirjutatud *tühjad* sulud, kuna see funktsioon *ei võta argumente*. Argumentidega funktsioonidest tuleb juttu alamprogrammide peatükis.

    
Tavaliselt pannakse funktsioonidesse need laused, mida on vaja käivitada rohkem, kui ühel korral. Proovi programmi, kus funktsiooni ``tere`` on kaks korda välja kutsutud. Programmi käivitamisel peaks nüüd tulema kaks järjestikust tervitust.

.. note:: 

    Samamoodi nagu ``if`` ja ``while`` lausete puhul, on ka funktsiooni kehas ridade ees olevad tühikud olulised -- selle järgi saab Python aru, kus lõpeb funktsiooni definitsioon ja algavad järgmised laused. Selles veendumiseks kustuta ``print("Kuidas läheb?")`` rea eest tühikud ära ning proovi siis programmi uuesti käivitada. Miks ilmusid laused ekraanile sellises järjekorras?

Harjutus 11. Ruudu joonistamine
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Nüüd on paras aeg tulla tagasi selle teema alguses käsitletud probleemi juurde.
Kirjuta funktsioon ``ruut``, mis joonistaks kilpkonna abil ruudu (küljepikkusega 30).  Kasuta seda funktsiooni mitu korda, joonistades ruute erinevatesse kohtadesse.

.. note::

    Justnagu tsükli või tingimuslause kehas, saab ka funktsiooni kehas kasutada ükskõik kui keerulisi ``if``- või ``while`` lauseid (ja nende kombinatsioone):
    
    .. sourcecode:: py3
    
        def mitu_teret():
            n = 0
            
            while n < 10:
                print("Tere!")
                n += 1
        
        mitu_teret()

.. note::

    Kui kilpkonna rahulik tempo sind ärritab, siis anna talle käsk ``speed(10)``.




.. _lokaalsed-muutujad:
 
Lokaalsed muutujad
---------------------
Funktsiooni kehas võib võtta kasutusele abimuutujaid, justnagu me oleme siiani neid kasutanud funktsioonidest väljaspool. Toome siinkohal uuesti ära 3. peatükist tuttava ruudu joonistamise funktsiooni:

.. sourcecode:: py3
    
    from turtle import *
    
    def ruut():
        # selle muutuja abil peame arvet, mitu külge on juba joonistatud
        joonistatud_kylgi = 0               
        
        while joonistatud_kylgi < 4:
            forward(100)
            left(90)
            joonistatud_kylgi = joonistatud_kylgi + 1   # suurendame muutuja väärtust
    
    ruut()
    exitonclick()


Kuidas oleks, kui me üritaksime peale funktsiooni ``ruut`` väljakutsumist kontrollida, milline oli ikkagi muutuja ``joonistatud_kylgi`` viimane väärtus? Proovi järgmist, veidi muudetud programmi:

.. sourcecode:: py3
    :emphasize-lines: 13
    
    from turtle import *
    
    def ruut():
        # selle muutuja abil peame arvet, mitu külge on juba joonistatud
        joonistatud_kylgi = 0               
        
        while joonistatud_kylgi < 4:
            forward(100)
            left(90)
            joonistatud_kylgi = joonistatud_kylgi + 1   # suurendame muutuja väärtust
    
    ruut()
    print(joonistatud_kylgi)
    exitonclick()


Ilmselt said programmi käivitamisel Pythonilt veateate (``"NameError: name 'joonistatud_kylgi' is not defined"``). Asi on selles, et funktsiooni kehas kasutusele võetud muutujad on *lokaalsed*, st nad "elavad" täielikult funktsiooni sees. Lokaalsed muutujad luuakse funktsiooni käivitamisel ja nad kaovad, kui funktsioon oma tööga lõpetab. Nende olemasolu on funktsiooni siseasi, see ei paista kuidagimoodi väljapoole. See asjaolu võimaldab meil lokaalsetele muutujatele vabalt nimesid valida, ilma muretsemata, kas mõnda neist nimedest on juba programmi põhiosas või mõnes teises funktsioonis kasutatud. 

Eelneva jutu kinnituseks demonstreerib järgnev programm, et funktsiooni sees defineeritud muutuja ``x`` ei mõjuta kuidagi programmi põhiosas defineeritud samanimelist muutujat, tegemist on kahe eraldi muutujaga, millele on juhtumisi sama nimi (justnagu kahel erineval inimesel võib olla sama nimi):

.. sourcecode:: py3

    x = 1

    def f():
        x = 2
        print(x)
    
    print(x) # ekraanile kuvatakse 1
    f()      # ekraanile kuvatakse 2
    print(x) # ekraanile kuvatakse 1
        

.. note::

    Programmi põhiosa muutujate (neid nimetakse ka *globaalseteks muutujateks*) ning funktsiooni kehas defineeritud muutujate (e. lokaalsete muutujate) eraldatus ei ole päris samaväärne -- kuigi programmi põhiosal pole ligipääsu funktsiooni muutujatele, saab funktsioonis vajadusel siiski kasutada programmi põhiosa muutujaid. Sellest võimalusest tuleb täpsemalt juttu ühes hilisemas peatükis.



    
Parameetrid
-----------
Täpselt sama tegevuse kordamist on tegelikult vaja siiski üpris harva. Tavaliselt on tarvis igal korral teha midagi sarnast, kuid mingi väikese nüansiga. Sellise nüansi väljatoomiseks kasutatakse programmeerimisel **parameetreid**. Järgnevas näiteprogrammis on defineeritud funktsioon kasutaja tervitamiseks. Selleks muutuvaks nüansiks on siinkohal kasutaja nimi:

.. sourcecode:: python

    def tere(nimi):
        print("Tere " + nimi)
        print("Kuidas läheb?")
        
    tere("Kalle")
    tere("Malle")
    
Funktsiooni ``tere`` definitsiooni päises on lisaks funktsiooni nimele näidatud ära ka üks *parameeter* nimega "nimi". Parameetri näol on sisuliselt tegu spetsiaalse *lokaalse muutujaga*, millele Python annab konkreetse väärtuse funktsiooni väljakutsel. Konkreetsed väärtused (nt. ``"Kalle"``) kirjutatakse väljakutsel funktsiooni nime järel olevatesse sulgudesse. Antud juhul on parameetri ``nimi`` väärtuseks esimesel väljakutsel "Kalle" ning teisel väljakutsel "Malle". Funktsioon töötab aga mõlemal juhul samamoodi – ta võtab parameetri väärtuse ning lisab selle tervitusele. Kuna aga väärtused on kahel juhul erinevad, on ka tulemus erinev.


.. index::
    single: funktsioon; argumendid
    single: argumendid; funktsiooni argumendid

.. admonition:: Terminoloogia: Parameetrid ja argumendid

    Koos parameetritega räägitakse enamasti ka **argumentidest**. Argumendiks nimetakse funktsiooni väljakutses sulgudes antud avaldise väärtust, millest saab vastava parameetri väärtus. Parameetrid on seotud funktsiooni definitsiooniga, argumendid on seotud funktsiooni väljakutsega. Meie viimases näites on ``nimi`` funktsiooni ``tere`` `parameeter`, aga sõneliteraal ``"Kalle"`` on vastav `argument` funktsiooni väljakutses.

    
    `Parameetri` vs. `argumendi` asemel võid mõnikord kohata ka väljendeid `formaalne parameeter` vs. `tegelik parameeter`.  

Harjutus 2. Parameetriseeritud ``ruut``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Täiusta 3. peatükis mainitud ruudu joonistamise funktsiooni nii, et ruudu küljepikkuse saab määrata funktsiooni väljakutsel. Kasuta loodud funktsiooni, joonistades mitu erineva suurusega ruutu.

.. note::

    Järgnevas vihjes on antud harjutuse näitelahendus, ära seda enne vaata, kui oled ise proovinud!

.. hint::
    
    .. sourcecode:: py3
    
        from turtle import *
        
        def ruut(kylg):
            i = 0
            while i < 4:
                forward(kylg)
                left(90)
                i += 1
        
        ruut(100)
        
        # liigume kuskile mujale
        up()
        forward(200)
        down()
        
        # väiksem ruut
        ruut(20)
        
        exitonclick()


.. _param-vs-input:
.. topic:: Parameetrid vs. ``input``

    Parameetritega funktsioon meenutab oma olemuselt programmi, kus on kasutatud ``input`` käsku -- mõlemal juhul on konkreetsed sisendandmed teadmata. Erinevus on selles, et kui ``input`` puhul on teada, et sisendandmed küsitakse kasutajalt, siis parameetrite kasutamisel jäetakse (funktsiooni seisukohast vaadatuna) sisendi saamise viis lahtiseks. Eelnevas näites andsime funktsiooni väljakutsel parameetri väärtuseks sõneliteraalid, kuid seal oleks võinud kasutada ka muutujat:

    .. sourcecode:: py3

        def tere(nimi):
            print("Tere " + nimi)
            print("Kuidas läheb?")
            
        sisestatud_nimi = input("Kuidas on sinu nimi? ")
        tere(sisestatud_nimi)

    See näide demonstreerib parameetritega funktsioonide universaalsust -- vastavalt vajadusele võime taolist funktsiooni kasutada literaaliga või mõne muutujaga (mille väärtus võib olla saadud ``input``-ist) või ka mingil keerulisemal kujul oleva avaldisega.

    .. note::

        Pange tähele, et eelviimasel real defineeritud muutuja nimeks oleksime võinud panna ka lihtsalt ``nimi``:
        
        .. sourcecode:: py3

            def tere(nimi):
                print("Tere " + nimi)
                print("Kuidas läheb?")
                
            nimi = input("Kuidas on sinu nimi? ")
            tere(nimi)
            
        See, et funktsiooni ``tere`` parameeter on samuti ``nimi``, ei aja Pythonit segadusse, kuna funktsiooni sisemus (sh. tema parameetrid) on ülejäänud programmist eraldatud. Kõlab sarnaselt sektsioonile "Lokaalsed muutujad"? Tegemist ongi sama teemaga -- nagu juba korra mainitud, käsitletakse ka parameetreid justkui (lokaalseid) muutujaid.
        
        Taoline nimede "taaskasutamine" erinevates kontekstides on küllalt levinud, aga kui leiate, et see ajab sind ennast segadusse, siis võid kasutada alati erinevaid muutujanimesid.




Mitu parameetrit
~~~~~~~~~~~~~~~~
Parameetreid (ja vastavaid argumente) võib olla ka rohkem kui üks. Proovi näiteks järgmist programmi:

.. sourcecode:: python

    def tere(nimi, aeg):
        print("Tere, " + nimi)
        print("Pole sind juba " + str(aeg) + " päeva näinud")
	
    tere("Kalle", 3)

Nagu näed, tuleb funktsiooni väljakutsel argumendid anda samas järjekorras nagu on vastavad  parameetrid funktsiooni definitsioonis. Teisisõnu, argumendi *positsioon* määrab, millisele parameetrile tema väärtus omistatakse.

.. note::

    Mõnede funktsioonide puhul on ühe parameetri väärtus tavaliselt sama ja seda on vaja vaid harvadel juhtudel muuta. Sellisel juhul on võimalik see "tavaline" väärtus funktsiooni definitsioonis ära mainida. Kui funktsiooni väljakutsel sellele parameetrile väärtust ei anta, kasutatakse lihtsalt seda vaikeväärtust. Seda võimalust demonstreerime eelmise näite modifikatsiooniga:

    .. sourcecode:: python

        def tere(nimi, aeg = "mitu"):
            print("Tere, " + nimi)
            print("Pole sind juba " + str(aeg) + " päeva näinud")
        
        tere("Kalle", 3)
        tere("Malle")
    
    Eespool juba nägime, et funktsioonil ``print`` on lisaks põhiparameetrile veel parameeter nimega `end`, millele on antud vaikeväärtus ``"\n"`` (so. reavahetus). See on põhjus, miks ``print`` vaikimisi kuvab teksti koos reavahetusega. Kuna selle funktsiooni definitsioonis kasutatakse Pythoni keerulisemaid võimalusi, siis ``print``-i väljakutsel ei olegi võimalik `end` väärtust määrata ilma parameetri nime mainimata, st. seda ei saa anda positsiooniliselt.

Harjutus 3. Värviline ruut
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Kilpkonna "pliiatsi" värvi saab muuta funktsiooniga ``color``, andes sellele argumendiks sõne ingliskeelse värvinimega, nt. ``color('red')``. Peale seda teeb kilpkonn järgmised jooned nõutud värviga. 

.. note::

    Soovi korral vaata täpsemat infot siit:
    http://docs.python.org/py3k/library/turtle.html#turtle.color

Lisa funktsioonile ``ruut`` uus parameeter joone värvi määramiseks. Katseta.

.. index::
    single: funktsioon; tagastamine
    single: väärtusega funktsioon
    single: return
    
Väärtuse tagastamine
-----------------------
.. admonition:: Probleem

    Kolmanda peatüki pere sissetuleku ülesandes kordasite tõenäoliselt netopalga arvutamise valemit kahes kohas -- ema ja isa netopalga arvutamisel. (Kui sul jäi see ülesanne tegemata, siis on väga soovitav see praegu, enne edasi lugemist ära teha). 
    
    Siin polnud õnneks tegemist eriti keerulise valemiga ning copy-paste'ga oli võimalik topelt tippimise vaeva vältida. Aga kui netopalga arvutamise valem peaks muutuma, siis peab olema meeles programmi muuta kõigis kohtades, kus seda valemit on kasutatud. 

    Ilmselt juba aimate, et taolise kordamise vältimiseks on jälle abiks funktsioonid -- netopalga arvutamiseks tuleb defineerida uus funktsioon (nt. nimega ``neto``), valem tuleb kirja panna selle funktsiooni kehas, ning edaspidi tuleb netopalga arvutamiseks kasutada uut funktsiooni. Kuidas aga saada funktsiooni käest vastust kätte? Võib proovida muutujatega, aga kuna antud programmi puhul tuleb ühel juhul salvestatakse tulemus muutujasse ``isa_sissetulek`` ja teisel juhul muutujasse ``ema_sissetulek``, siis pole selge, millist muutujat kasutada. Mis teha siis, kui mõnikord on tarvis tulemus kohe ekraanile näidata ja muutujat polegi tarvis?



Funktsioone ``ruut`` ja ``print`` kasutame käskudena -- meid huvitab see **tegevus**, mida see funktsioon teeb (kilpkonna liigutamine või ekraanile kirjutamine). Seevastu funktsioonide ``sin`` ning ``sqrt`` kasutusviis on hoopis erinev -- meid huvitab hoopis vastava funktsiooni rakendamisel saadav **väärtus**.

Nii ``sin`` kui ``sqrt`` teevad argumentidega mingi arvutuse, ning **tagastavad** saadud väärtuse, mida võime nt. kasutada avaldises, salvestada muutujasse või vaadata käsureal. Taolisi funktsioone nimetame **väärtusega funktsioonideks**.

Järgnev näide defineerib funktsiooni, mis arvutab ja tagastab ristküliku pindala. Seejärel kasutatakse seda funktsiooni konkreetsete argumentidega:

.. sourcecode:: python

    def ristkyliku_pindala(laius, korgus):
        return laius * korgus
        
    pindala = ristkyliku_pindala(4, 5)
    print("Pindala on: " + str(pindala))
    print("Pool pindalast on: " + str(pindala / 2))

Väärtusega funktsioonide puhul on oluline *võtmesõna* ``return`` -- sellele sõnale järgnev avaldis määrab funktsiooni väljakutse väärtuse.

Harjutus 4. Topelt
~~~~~~~~~~~~~~~~~~~~~~
Kirjuta funktsioon, mis võtab argumendiks ühe arvu ning tagastab selle arvu kahega korrutatuna.

Demonstreeri loodud funktsiooni tööd, kirjutades programmi ka mõned funktsiooni väljakutsed erinevate argumentidega. NB! tulemuse ekraanile kuvamine tuleks korraldada funktsiooni väljakutse juures, mitte funktsiooni definitsioonis!

.. topic:: ``return`` lõpetab funktsiooni töö

    Eelmises näites oli ``return`` lause funktsiooni kehas kõige viimane asi. Tegelikult ei pea ``return`` olema tingimata funktsiooni lõpus. Järgnevas absoluutväärtuse arvutamise funktsiooni näites kasutatakse ``return``-i kahes kohas -- funktsiooni lõpus ja tingimuslause sees:

    .. sourcecode:: py3

        def absoluut(x):
            if x < 0:
                return -x
            
            return x

    Kumb neist ``return``-idest siis ikkagi kehtib? Sellele vastamiseks peame teadma, et ``return`` lause käivitamine lõpetab alati funktsiooni töö. Seega, kui kutsume antud funktsiooni välja negatiivse argumendiga, siis käivitub esimene ``return`` ja ``if``-lausele järgnevat rida üldse ei vaadatagi. Kui aga ``if`` lause tingimus osutub vääraks, siis ``if``-lause keha ei vaadata ja Python jätkab sellega, mis tuleb peale ``if``-lauset (so. teine ``return```).
    
    See võimalus kasutada ``return``-i funktsiooni keskel ei ole tegelikult eriti oluline -- alati saab funktsiooni panna kirja nii, et seal on täpselt üks ``return`` lause ja see paikneb funktsiooni lõpus.



.. _return-vs-print:

.. topic:: ``return`` vs. ``print``

    TODO: mingi absurdne näide, nt. "Selle arvu siinus on .."

    Eelnevalt märkisime, et nii funktsiooni parameetrid kui ``input`` on olemuselt sarnased, kuna mõlemad on seotud sisendi saamisega, kuid parameetrid on paindlikumad, kuna täpne sisendi saamise viis jäetakse lahtiseks.

    Analoogselt võime võrrelda ``print`` ja ``return`` käsku -- mõlemad on seotud väljundi andmisega, kuid ``return`` on paindlikum, kuna *täpne tulemuse kasutamise viis jäetakse lahtiseks*. Kuigi ristküliku pindala näites me lõpuks ikkagi ``print``-isime saadud tulemuse, siis tänu ``return``-ile jäi meie funktsiooni definitsioon universaalseks ja see võimaldas meil tulemust kasutada ka teistes arvutustes.

    Kui me oleks ``print``-imise teinud juba funktsiooni sees ...

    .. sourcecode:: python

        # NB! Ebasoovitav!
        def ristkyliku_pindala(laius, korgus):
            print(laius * korgus)

    ... siis see funktsioon oleks sobinud vaid neil juhtudel, kui me soovime arvutuse tulemust ainult ekraanil näidata, teistes arvutustes poleks me tulemust enam kasutada saanud.

    .. note::
        
        Kuigi ka funktsioon ``print`` näib "tagastavat" oma argumendi (kuvades selle ekraanile), ei ole see siiski ``print`` funktsiooni tagastusväärtus: nt. kirjutades ``x = print("Tere")`` ei jõua sõne ``"Tere"`` muutujasse ``x``.
        
        Sarnane segadus võib tekkida ka Pythoni käsurea kasutamisel -- kui kirjutada sinna avaldis ``sqrt(2)``, siis tulemus ilmub ikkagi ekraanile, kuigi me ei kasutanud ``print`` käsku. Kas see tähendab, et ka "funktsioon" ``sqrt`` kuvab vastuse ekraanile? Ei, tegelikult Pythoni käsurida kuvab ``sqrt`` käest saadud vastuse ekraanile omal algatusel, ``sqrt`` ei tea sellest midagi.

        Kui päris täpne olla, siis tegelikult kõik Pythoni funktsioonid tagastavad midagi, isegi ``print`` ja ``ruut``. Need funktsioonid, mille eesmärk on vaid mingi tegevus, tagastavad alati ühe spetsiifilise (ja suhteliselt ebahuvitava) väärtuse ``None``. Selle väärtusega ei ole üldjuhul midagi peale hakata ning seepärast Python'i käsurida ka ei näita seda automaatselt.


Harjutus 5. Tollid ja sentimeetrid
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. note::
    Selle ülesandega saad harjutada ühte levinud võtet uute funktsioonide loomiseks

#. Kirjuta funktsioon, mis võtab argumendiks pikkuse tollides ning tagastab pikkuse sentimeetrites. Salvesta esialgu faili vaid funktsiooni definitsioon, ilma väljakutseta.
#. Testi loodud funktsiooni käsureal (käivita programm IDLE-ga, ning kirjuta mõned väljakutsed). Kui funktsioon ei tööta õigesti, siis korrigeeri definitsiooni ja proovi uuesti.
#. Lõpuks kasuta funktsiooni programmis, mis küsib kasutajalt tema pikkuse tollides ja väljastab ekraanile vastava pikkuse sentimeetrites ning tema nn. "ideaalkaalu" (so. pikkus sentimeetrites - 100, nt. kui pikkus on 185cm, siis ideaalkaal on 85kg).

Harjutus 6. Sõne dubleerimine
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Kirjuta funktsioon ``dubleeri`` , mis võtab argumendiks sõne ning tagastab selle sõne dubleerituna niimitu korda, kui mitu tähte on esialgses sõnes:

.. sourcecode:: py3

    >>> dubleeri('xo')
    'xoxo'
    >>> dubleeri('Tere')
    'TereTereTereTere'

.. hint::

    Abiks on funktsioon ``len`` ja operaator ``*``




"Mugavusfunktsioonid"
~~~~~~~~~~~~~~~~~~~~~
Python'i ``math`` mooduli ``log`` funktsioon arvutab vaikimisi naturaallogaritmi. Selleks, et arvutada logaritmi mõne teise alusega, tuleb alus anda teiseks argumendiks, nt. ``log(8, 2)``. Kui meil on tihti tarvis arvutada just kahendlogaritmi, siis võime defineerida selle jaoks uue funktsiooni, mis kasutab oma definitsioonis tavalist ``log`` funktsiooni:

.. sourcecode:: py3

    from math import *

    def log2(x):
        return log(x, 2)

Nüüd on meil eraldi kahendlogaritmi arvutamise funktsioon, millele peame andma vaid ühe argumendi, nt. ``log2(8)``. Antud näites ei võitnud me sellega just palju, kuid keerulisemate funktsioonide väljakutsete puhul võib taoline trikk teha koodi märgatavalt lühemaks ja selgemaks.



Funktsiooni keha sisu
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Nagu juba 3. peatükis mainitud, võib funktsiooni definitsioonis (olgu väärtusega või ilma) kasutada ükskõik milliseid lausetüüpe (sh. tingimuslaused ja tsükleid). Järgnev näide esitab absoluutväärtuse arvutamise funktsiooni:

.. sourcecode:: py3

    def abs_vaartus(arv):
        if arv < 0:
            tulemus = -arv
        else:
            tulemus = arv
        
        return tulemus

Kui võrdlete seda funktsiooni kolmandas peatükis näidatud absoluutväärtuse arvutamise programmiga, siis märkate, et erinevus on vaid sisendandmete saamises (parameeter vs. ``input``) ning tulemuse esitamises (``return`` vs. ``print``).

.. note:: 

    Tingimuslausega funktsioonis on mõnikord mugavam kasutada mitut ``return`` lauset. Sama funktsiooni saaksime panna kirja ka järgnevalt:
    
    .. sourcecode:: py3

        def abs_vaartus(arv):
            if arv < 0:
                return -arv
            else:
                return arv


Harjutus 7. Kahest arvust suurim
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Kirjuta funktsioon, mis saab parameetritena kaks arvu ning tagastab neist suurima.


.. _milleks-funktsioonid:

Milleks funktsioonid?
---------------------
Vaatame üle peamised põhjused, miks on funktsioonid kasulikud.

.. index::
    single: DRY-printsiip
    
*DRY*-printsiip
~~~~~~~~~~~~~~~
Kolmandas peatükis oli ülesanne pere sissetuleku arvutamiseks. Tõenäoliselt kasutasite programmis netopalga arvutamise valemit kahes kohas (vastavalt isa ja ema palga jaoks).

Kui taoline programm oleks reaalses kasutuses, siis nt. tulumaksuvaba miinimumi muutmise korral tuleks parandused teha kahes kohas. Antud näite puhul oleks see piisavalt lihtne, kuid reaalsetes programmides juhtub tihti, et vajalik parandus unustatakse mõnes kohas tegemata. Seetõttu propageeritakse programmeerimisel nn. **DRY-printsiipi** -- see tuleb ingliskeelsest väljendist *Don't Repeat Yourself*, millega tahetakse öelda, et sarnase koodi kordamist tuleks vältida.

Tuleb välja, et funktsioonid sobivad suurepäraselt *DRY*-printsiibi rakendamiseks -- selle asemel, et samasugust koodi kirjutada erinevatesse kohtadesse, saab selle koodi esitada funktsioonina, ning edaspidi piisab selle kasutamiseks vaid funktsiooni nime mainimisest. Kui midagi on vaja muuta, siis tehakse muudatus vaid funktsiooni kehas ja see mõjub igalpool, kus funktsiooni on kasutatud.

.. index::
    single: abstraktsioon
    
Üldistamine e. *abstraktsioon*
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Kui eri kohtades on vaja sarnast, kuid teatud variatsiooniga koodi (nt. ühel juhul arvutame netopalka ema, aga teisel juhul isa brutopalga põhjal), siis tulevad appi parameetrid, mis võimaldavad meil funktsiooni kehas jätta mõned detailid lahtiseks. Teisiti öeldes -- funktsiooni parameetrid võimaldavad meil kirjutada üldisema e. **abstraktsema** lahenduse, mida saab hiljem konkreetsete argumentidega täpsustada. Nt. netopalga arvutamise funktsioonis saame brutopalga esitada parameetrina, millele antakse väärtus alles konkreetse arvutuse käivitamisel.

.. index::
    single: modulaarsus
    single: must kast
    
Modulaarsus ja *musta kasti* metafoor
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Kolmas oluline põhjus tuleb paremini esile suuremate programmide puhul. Kui me koondame teatud alamülesande lahendamiseks vajalikud laused ühte funktsiooni (e. alamprogrammi), siis programmi põhiosas saame selle alamülesande kirja panna vaid vastava funktsiooni nime mainides. Eeldades, et funktsioonide nimed on hoolikalt valitud, piisab meile programmi põhiidee mõistmiseks vaid kasutatud funktsioonide nimede lugemisest -- funktsiooni sisu võime esialgu ignoreerida. Teisiti öeldes: me võime funktsioone soovi korral käsitleda maagiliste **mustade kastidena**, mis *kuidagimoodi* teevad seda, mis nende nimest võib välja lugeda.

Taolisi "musti kaste", mida on võimalik kasutada ilma nende täpset sisu teadmata, nimetatakse tihti *mooduliteks*, ning programme, mis on jagatud alamprogrammideks nimetatakse vastavalt **modulaarseteks**. Kuna Pythonis on sõnal *moodul* spetsiifilisem tähendus, siis meie seda terminit alamprogrammi jaoks ei kasuta.
    
Keskendumine vaid "mustade kastide" *tähendusele*, ignoreerides nende *ehitust*, vabastab osa meie aju töömälust ning võimaldab luua sellevõrra keerulisemaid programme. Kõige keerulisemad programmid on saanud võimalikuks vaid seetõttu, et lihtsatest mustadest kastidest on ehitatud keerulisemad mustad kastid, neist omakorda veel keerulisemad jne.

Kui *DRY*-printsiibi juures rõhutasime seda, et funktsioonid aitavad sama koodi kasutada korduvalt, siis modulaarsuse põhiidee on selles, et me saame funktsiooni kasutada ilma selle täpse sisu peale mõtlemata, toetudes vaid ta nimele. Seetõttu on uue funktsiooni loomine põhjendatud tihti ka siis, kui seda kasutatakse vaid ühes kohas.


.. index::
    single: import
    single: moodulid

Muutujad vs funktsioonid
----------------------------
TODO

Nimede tähtsus
------------------
TODO: Tee näiteprogramm, kus muutujanimed on a,b,c,x,y,z ja lase lugejal arvata, mida see programm teeb, peab olema meeldejääb, sest seda on tarvis tagasi viidata

``import``-lause
--------------------
Pythoni `standardteegis` (so. funktsioonide ja teiste programmielementide kogum) on väga palju funktsioone (ja teisi Pythoni objekte). Nende paremaks organiseerimiseks on nad jaotatud teemade kaupa gruppidesse, mida nimetatakse `mooduliteks`. ``import`` lause teeb moodulis olevad funktsioonid programmi jaoks kättesaadavaks. Meeldetuletuseks näide, kus me soovime kasutada ainult kahte funktsiooni moodulist ``math``:

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




Moodulid ja ``import``
----------------------
Pythoniga tuleb kaasa tuhandeid erinevaid funktsioone, lisaks kirjutavad Pythoni programmeerijad üle maailma igapäevaselt tuhandeid funktsioone juurde. Sellises situatsioonis on täiesti loomulik, et mitmele erinevale funktsioonile pannakse sama nimi. Selleks, et erinevatel funktsioonidel oleks siiski võimalik vahet teha, jagatakse need **moodulitesse**.

Eelmistes peatükkides kohtusite juba moodulitega ``math`` ja ``turtle``, ning nägid, et mooduli sisu muutub kättesaadavaks ``import`` käsuga, nt:

.. sourcecode:: py3

    from math import *

Selline variant ``import`` käsust on tegelikult soovitav vaid siis, kui sul on vaja moodulist palju erinevaid funktsioone. Kui sa tead, et sul läheb moodulist tarvis vaid mõnda funktsiooni (nt. ``math`` moodulist funktsioone ``sin`` ja ``cos``), siis on soovitav kasutada ``import`` käsu varianti, kus näidatakse ära konkreetsed funktsioonide (või konstantide) nimed, mida tahetakse kasutada: 

.. sourcecode:: py3

    from math import sin, cos

Sellise variandi puhul ei teki segadust, kui tahate mõnd ``math`` moodulis defineeritud nime (nt. ``e``) kasutada mõne enda muutuja nimena.    

``import`` käsust on olemas veel üks variant, mis võimaldab moodulis olevaid funktsioone kasutada ainult koos mooduli nimega:

.. sourcecode:: py3

    >>> import math
    >>> math.sqrt(9)
    3.0
    
Ka selle variandi puhul ei pea oma muutujate nimede valimisel muretsema, kui imporditud moodulis on juba sama nime kasutatud -- antud näites võiksime vabalt luua uue muutuja nimega ``sqrt`` ja see ei läheks segamini funktsiooniga ``math.sqrt``.

.. note:: 
    ``import``-laused tuleks panna programmi algusesse. See pole Pythoni poolt range nõue, vaid lihtsalt tava --  nii on hea näha, milliste teemadega antud programm tegeleb.

.. topic:: Moodulite loomine

    Kõikide selle kursuse ülesannete puhul on aktsepteeritav, kui sinu enda programm koosneb ainult ühest failist. Samas, reaalsete programmide juures on peaaegu alati tarvilik organiseerida programmi jaoks loodud funktsioonid eraldi moodulitesse.
    
    Uue mooduli loomine on Pythonis imelihtne -- funktsioonide definitsioonid tuleb lihtsalt salvestada tavalisse *py*-laiendiga faili. Mooduli nimeks saab seejuures tema failinimi ilma *py*-laiendita. Selleks, et neid funktsioone saaks kasutada teistes failides, tuleb seal teha sobiv ``import``, justkui ``math`` või ``turtle`` mooduli puhul. 
    
    Siit tuleb ka välja, miks esimeses peatükis märgiti, et omaloodud faili nimeks ei tohiks panna `turtle.py`. Kui panna, siis hakatakse ``import turtle`` puhul funktsioone ``left()``, ``right()`` jt otsime uuest failist, kus neid aga pole.

    NB! Erinevalt standardmoodulitest, peab enda moodul olema üldjuhul samas kaustas, kus seda kasutav programm (täpsem info siit: http://docs.python.org/py3k/tutorial/modules.html#the-module-search-path)

.. index::
    single: meetodid
    

Meetodid
--------
Teises peatükis nägime, et sõnede puhul kirjutati mõne funktsiooni nimi (nt. ``count``) sõne ja argumentide vahele, nt:

.. sourcecode:: py3

    sõna = "kukununnu"
    u_tähtede_arv = sõna.count("u")

Jääb mulje, et mingil põhjusel on üks funktsiooni argumentidest (antud näites ``sõna``) lihtsalt esile tõstetud. Tuleb välja, et Python seda umbes nii ka käsitleb.

Taolisi funktsioone nimetatakse **meetoditeks**. Lisaks sellele, et meetodite puhul kirjutame esimese argumendi meetodi nime ette, on neil tavaliste funktsioonidega võrreldes veel mõningaid erinevusi, millel me praegu ei peatu. Meetod on väga tähtis mõiste *objekt-orienteeritud programmeerimises*.

.. note::
    Meetodeid ei ole vaja kunagi ``import``-ida.

Veateated ja funktsioonid
---------------------------
Esimeses peatükis soovitasime pikkade veateadete puhul keskenduda veateate viimastele ridadele. Kui täitmisaegne viga tekib mingi funktsiooni sees, siis võib ainult viimaste ridade põhjal olla raske vea põhjust tuvastada. Proovi käivitada järgnevat programmi:

.. sourcecode:: py3

    def arvuta_kuupalk(aastapalk):
        return aastapalk / 12
    
    aastapalk = input("Palun sisesta aastapalk: ")
    print("Kuupalk on", arvuta_kuupalk(aastapalk))    


Kui sisestad nõutud palganumbri, siis saad umbes taolise veateate:

.. sourcecode:: none

    Traceback (most recent call last):
      File "C:/harjutused/vigane.py", line 5, in <module>
        print("Kuupalk on", arvuta_kuupalk(aastapalk))
      File "C:/harjutused/vigane.py", line 2, in arvuta_kuupalk
        return aastapalk / 12
    TypeError: unsupported operand type(s) for /: 'str' and 'int'

Viimaste ridade järgi võiks järeldada, et probleem on real nr 2, funktsioonis ``arvuta_kuupalk``. Tegelikult oli viga aga selles, et funktsiooni kutsuti välja valet tüüpi argumendiga (peaks olema arv, aga oli sõne). Seega tuleb pöörata tähelepanu ka funktsiooni väljakutse kohale. Meie õnneks on ka väljakutse koht veateates ära näidatud -- see on real nr. 5. Kui ka väljakutse ise paiknes kuskil funktsioonis, siis on ka tolle funktsiooni väljakutse koht ära näidatud -- ülevalt alla liikudes saab veateatest välja lugeda, millises kohas kutsuti mida välja.


Funktsioonid vs. muutujad
------------------------------
TODO: Räägi siin ka importimisest


Kokkuvõte
--------------

**Funktsiooni definitsiooni** kehas olevad laused jäetakse esialgu lihtsalt meelde. Neid saab hiljem käivitada kirjutades definitsiooni päises antud nime koos sulgudega -- seda nimetatakse *funktsiooni väljakutseks* e. rakendamiseks. Funktsioonid võimaldavad keerulise programmilõigu panna kirja vaid ühekordselt, aga kasutada seda mitmes erinevas kohas.




Ülesanded 
-------------
.. note::

    Kursuse kodulehel loetletud kontrollülesannete all on mõeldud just selle ploki ülesandeid.
    
1. Ristkülik 
~~~~~~~~~~~~
Kirjuta funktsioon ``ristkylik``, mis võtab argumentideks kaks küljepikkust ja joonistab kilpkonnaga neile vastava ristküliku. Joonista loodud funktsiooni kasutades järgnev kujund:

.. image:: images/rist.png

.. hint::

    Joonis koosneb kolmest ristkülikust
    
.. hint::

    Segaduse vältimiseks on soovitav funktsiooni töö lõppedes pöörata kilpkonn tagasi algsesse suunda.

2. Kolmnurga pindala
~~~~~~~~~~~~~~~~~~~~
Kirjuta funktsioon ``kolmnurga_pindala``, mis võtab argumentideks kolmnurga külgede pikkused, ning tagastab vastava kolmnurga pindala. Eeldame, et argumentide väärtused sobivad kolmnurga küljepikkusteks.

.. hint::

    http://en.wikipedia.org/wiki/Heron%27s_formula

Lisa programmi lõppu (peale funktsiooni definitsiooni) järgmised laused:

.. sourcecode:: py3

    print("a: 1, b: 1, c: 2**0.5, pindala: " + str(kolmnurga_pindala(1, 1, 2**0.5)))
    print("a: 3, b: 2, c: 2,      pindala: " + str(kolmnurga_pindala(3, 2, 2)))
    print("a: 3, b: 4, c: 5,      pindala: " + str(kolmnurga_pindala(3, 4, 5)))
    
Veendu, et programmi käivitamisel saad järgmised tulemused:

.. sourcecode:: none

    a: 1, b: 1, c: 2**0.5, pindala: 0.49999999999999983
    a: 3, b: 2, c: 2,      pindala: 1.984313483298443
    a: 3, b: 4, c: 5,      pindala: 6.0

NB! tulemused võivad õige pisut ka erineda, sest erinevad Pythoni versioonid ümardavad erineva täpsusega.

3. Kodulaen
~~~~~~~~~~~
Kirjuta funktsioon, mis võtab argumentideks ostetava kinnisvara hinna, sissemakse suuruse ja laenuperioodi aastates ning tagastab intresside kogusumma, mis tuleb ostjal selle laenu eest pangale maksta. Lihtsuse mõttes eeldame, et igal aastal arvestatakse intress algse laenusumma põhjal.

Esimeses versioonis kasuta fikseeritud intressi -- 4% aastas.

Seejärel muutke funktsiooni selliselt, et kui sissemakse on väiksem kui 30% kinnisvara hinnast, siis on intress hoopis 6% aastas.

Lõpuks rakenda loodud funktsiooni programmis, mis küsib kasutajalt soovitud algandmed ja
väljastab antud kinnisvara soetamise kogukulu (sissemakse + laenusumma + intressid) ning eraldi ka intresside kogusumma.

Testi oma programmi ja kontrolli, kas saad järgnevad tulemused:

    * hind: 10000, sissemakse: 3000, aastaid: 10; kogusumma: 12800, intressid: 2800
    * hind: 10000, sissemakse: 2900, aastaid: 10; kogusumma: 14260, intressid: 4260
    * hind: 10000, sissemakse: 2900, aastaid: 0; kogusumma: 10000, intressid: 0

4. Pere sissetulek, ver.2
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. note::

    See ülesanne demonstreerib väga hästi *DRY*-printsiibi ning abstraktsiooni olemust.

Võtke aluseks kolmanda peatüki Ülesanne "Pere sissetulek". Muutke lahendust selliselt, et netopalga valem oleks programmis kirja pandud vaid ühes kohas.


Üks ülesanne segatud ülesannete pangast
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
TODO:


Üks ülesanne projecteulerist
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
TODO:

Lisalugemine
-----------------
Matemaatilised funktsioonid vs. Pythoni funktsioonid
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
TODO, tee graafikuid?




Projekt: Graafilised programmid
------------------------------------
Praeguseks tunned Pythonit juba piisavalt, et alustada graafiliste programmide loomisega. Kõik vajalikud funktsioonid selleks asuvad moodulis ``tkinter`` (ja selle alammoodulites).

Graafiliste programmide loomisel kasutatakse samu baaskonstruktsioone, mida oled siiani õppinud -- avaldised, laused (tingimuslause, tsükkel), funktsioonid. Oluline erinevus on see, et kasutusele võetakse uued, spetsiifilisemad andmetüübid, mis esitavad kasutajaliides komponente (nupud, sisestuskastid jne). Nendega toimetamine nõuab omajagu tähelepanu ja teadmisi detailide osas -- näiteks kuidas mingit nuppu paigutada ekraanil õigesse kohta. Seetõttu tuleb ka arvestada, et graafilised programmid kipuvad olema nende detailide tõttu pikemad kui tekstipõhised programmid.

Nagu ikka, on mõttekas alustada millestki lihtsast. Vaata üle järgnev näiteprogramm ja katseta seda:

.. sourcecode:: py3

    # impordi tk vidinad ja konstandid
    from tkinter import *
    # Pythoni moodulisüsteemi ühe nüansi tõttu tuleb ttk importida eraldi
    from tkinter import ttk 

    # loome ühe funktsiooni, mis käivitatakse nupule klõpsamisel
    # (funktsiooni sidumine nupuga tehakse allpool)
    def tervita():
        tervitus = 'Tere ' + nimi.get()
        messagebox.showinfo(message=tervitus)


    # loome akna
    raam = Tk()
    raam.title("Tervitaja")  # määrame pealkirja
    raam.geometry("300x100") # määrame akna suuruse

    # loome tekstikasti jaoks sildi
    # esimene argument (raam) näitab, et silt asub ülalpool loodud akna sees
    silt = ttk.Label(raam, text="Nimi")
    silt.place(x=5, y=5) # paigutame etteantud koordinaatidele

    # loome tekstikasti
    nimi = ttk.Entry(raam)
    nimi.place(x=70, y=5, width=150)

    # loome nupu ja seome selle ülalpool antud funktsiooniga (command=tervita)
    nupp = ttk.Button(raam, text="Tervita!", command=tervita)
    nupp.place(x=70, y=40, width=150)

    # mainloop jälgib kasutaja tegevusi (nt. hiireklõpse)
    # ja kutsub õigel hetkel välja õige funktsiooni (nt. tervita())
    raam.mainloop()
    

Loodetavasti ilmus sinu ekraanile aken, kus oli võimalik sisestada mingi tekst ja vajutada nupule. Peale nupuvajutust pidi ilmuma uus väike aken tervitusega.

Kuigi see programm on suhteliselt lihtne ja lühike, illustreerib ta küllalt hästi graafiliste programmide põhimõtteid:

    * kuskil on olemas funktsioonid ja andmetüübid, mis oskavad ekraanile manada nuppe jms. (antud juhul moodulid ``tkinter`` ja ``tkinter.ttk``)
    * erinevaid kasutajaliidese komponente (e. "vidinaid") saab paigutada üksteise sisse (antud näites ``silt``, ``nimi`` ja ``nupp`` asuvad ``raam``-i sees)
    * vidinate juures saab ära näidata, millised funktsioonid tuleb käivitada mingi kasutaja tegevuse korral (``... command=tervita ...``). Vastavates funktsioonides võid teha mida iganes oskad -- lugeda ja kirjutada faile, tõmmata midagi internetist, muuta teiste vidinate sisu või välimust jne.
    * vidinate omadusi saab määrata nende loomisel (``... text="Tervita!" ...) või ka hiljem (``nupp.place(...)``). 
    * peale kasutajaliidese paikasättimist pannakse programm kasutaja tegevusi ootama (``raam.mainloop()``).
    
Järgmine samm oleks uurida välja, milliseid erinevaid kasutajaliidese komponente ``tkinter`` toetab ja kuidas neid kasutada. Kui sul on juba olemas projektiidee, mis vajab graafilist kasutajaliidest, siis tee oma tulevase programmi väljanägemisest lihtne visand ja proovi seda realiseerida ``tkinter``-i abil.

Veel selgitusi, näiteprogramme ja linke lisainformatsioonile leiate õpiku lisast (:ref:`tkinter`).

Soovitame uurida ka järgnevaid linke, mis tutvustavad ``tkinter``-i erinevaid vidinaid (vali lehekülje paremalt servast `Show: Python`, siis näidatakse näiteid ainult keeles Python):

    * http://www.tkdocs.com/tutorial/widgets.html
    * http://www.tkdocs.com/tutorial/morewidgets.html
