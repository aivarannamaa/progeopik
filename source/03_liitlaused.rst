3. Tingimus- ja korduslaused
============================================

.. todo::

    * counting digits (algul anna vigane variant)
    * ASCII ja kilpkonna tulpdiagrammid
    
    .. sourcecode:: none
    
             _________
            /        /\
           /        /  \
          /________/    \
          \        \    /
           \        \  /
            \________\/    

.. index::
    single: tingimuslaused
    single: tingimuslaused; if-lause

Eelmise peatüki programmidega töötas Python täiesti "tuimalt" -- alustas esimesel real oleva lausega, iga rea täitmise järel võttis ette järgmise rea, kuni jõudis programmi lõppu -- programmi käik oli täielikult ette ennustatav. Taolisest lähenemisest piisab paraku vaid väga lihtsate ülesannete puhul. 

Antud peatükis vaatame, kuidas panna Python valikuid tegema. Selleks täiendame oma arsenali kahe uue lausetüübiga, mille abil on võimalik määrata teiste lausete käivitamise tingimused.



.. admonition:: Õpinipp

    Olge aktiivne! Proovige olla materjalist sammu võrra ees, märgates seoseid ja võimalusi enne, kui õpik neid mainib. Iga näite juures lugege esimese asjana programmi tekst hoolikalt läbi ja ennustage, mida iga rida teeb.
    
    Teisiti öeldes: eelistage värsket "mõttetoitu" õpiku "läbimälutud" tarkuseterade asemel! 



Tingimuslause e. ``if``-lause
-------------------------------
Praktiliselt kõikides mittetriviaalsetes programmides tuleb mingil hetkel teha valikuid, kas jätkata üht- või teistmoodi. Python võimaldab programmeerijal taolised dilemmad panna kirja **tingimuslause** e. **valikulause** e. **if-lause** abil.

Järgnevas näiteskriptis kasutatakse tingimuslauset arvu absoluutväärtuse arvutamiseks:

.. sourcecode:: py3

    arv_tekstina = input('Palun sisesta mingi arv: ')
    arv = float(arv_tekstina)
    
    if arv < 0:
        # kui oli tegemist negatiivse arvuga, 
        # siis salvestan vastuse jaoks mõeldud muutujasse antud arvu vastandväärtuse
        vastus = -arv
    else:
        # vastasel juhul on vastuseks esialgne väärtus ise
        vastus = arv
    
    print('Selle arvu absoluutväärtus on ' + str(vastus))

Selles programmis ei täida Python enam kõiki käske -- see, kas täidetakse käsk ``vastus = -arv`` või ``vastus = arv``, sõltub konkreetsest kasutaja poolt sisestatud arvust. Antud näites on mõlemas tingimuslause *harus* vaid üks käsk, aga neid võib seal olla ka rohkem.

Tingimuslause komponendid on *päis* (so. ``if``-i ja tingimusega rida), ``then``-haru (so. päisele järgnevad paremale nihutatud read), võtmesõna ``else``, ning ``else``-haru (jällegi paremale nihutatud).

Tingimusi saab (muuhulgas) moodustada järgmiste operaatoritega: 

* ``<``, ``>``, ``<=``, ``>=`` sobivad arvude võrdlemiseks
* Topeltvõrdusmärk (``==``) tähistab võrdsust nii arvude kui sõnede puhul
* ``!=`` tähistab mittevõrdsust nii arvude kui sõnede puhul

.. note::
    
    Ärge unustage, et üksikut võrdusmärki (``=``) kasutatakse Pythonis muutujale väärtuse omistamiseks, seetõttu on võrdsuse kontrollimiseks ette nähtud topeltvõrdusmärk (``==``).

Harjutus 1. Jaguvus
~~~~~~~~~~~~~~~~~~~~
Kirjutage programm, mis küsib kasutajalt kaks arvu ning vastab, kas esimene arv jagub teisega või mitte.

.. hint::

    Tuletage meelde, mida teeb operaator ``%``.

.. hint::

    >>> 6 % 4
    2
    >>> 6 % 3
    0
    >>> 4 % 3
    1
    >>> 4 % 2
    0    
    >>> 4 % 4
    0
    >>> 4 % 1
    0

Treppimine
~~~~~~~~~~~~~~~~
``if``-lause kasutamisel on vaja pöörata tähelepanu tühikutele -- tühikutega joondamine e. *treppimine* määrab, millised käsud kuuluvad tingimuslause alla ja millised mitte: 

.. sourcecode:: py3

    nimi = input("Mis su nimi on? ")
    if nimi == "Imelik":
        print("Tõesti?")
        print("Imelik nimi!")
    else:
        print("Tere " + nimi + "!")
    print("Meeldiv tutvuda!")

Antud näites kuuluvad tingimuslause *then*-harusse laused ``print("Tõesti?")`` ja ``print("Imelik nimi!")`` ning *else*-harusse üksainus lause ``print("Tere " + nimi + "!")``. Võib ka öelda, et need joondatud laused kuuluvad ``if``-lause *alla* -- nende käivitamine sõltub ``if``-lausest.

Programmi viimane lause ei ole trepitud ja seetõttu ei ole ta millegi "alluvuses" vaid on täiesti "iseseisev". (Kontrollküsimus: Kuidas muutuks programmi käitumine, kui ka viimase rea ette panna 4 tühikut?)

Edaspidi näeme, et treppimist kasutatakse ka teistes Pythoni konstruktsioonides ning põhimõte on alati selles, et sama kaugele joondatud järjestikused read moodustavad mingi terviku. 

.. admonition:: NB!

    Trepitud plokile eelnev rida lõpeb alati kooloniga (see on Pythonile lisakinnituseks, et programmeerija soovib järgmisel real alustada trepitud plokki).

.. admonition:: Katsetus
    
    Proovige järgi, kuidas Python käitub, kui unustate kasutada koolonit või jätate ära mõne taandrea. Sellega saate end taoliseks situatsiooniks juba ette valmistada.



.. note::

    Kuigi Python on treppimise osas võrdlemisi paindlik, tuleks segaduste vältimiseks alati kasutada joondamiseks 4 tühikut. IDLE-s kirjutades võib treppimiseks vajutada ka TAB klahvi -- IDLE genereerib sellepeale TAB sümboli asemel 4 tühikut.
    Tegelikult pole enamasti vaja IDLE-s isegi TAB klahvi kasutada -- kui vajutada kooloniga lõppeval real uue rea saamiseks ENTER-it, taipab redaktor ise, et järgmine rida tuleb treppida ja lisab uue rea algusesse vajaliku arvu tühikuid. Ka järgmistele ridadele paneb IDLE usinalt tühikud ette. Andmaks märku, et uus rida enam tingimuse alla ei kuulu, tuleb need tühikud ära kustutada ja alustada käsu kirjutamist jälle ekraani vasakust servast.


Harjutus 2. Eurokalkulaator
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Kirjutage programm, mis küsib kasutajalt rahasumma ja selle, kas ta soovib teisendada Eesti kroone eurodeks või vastupidi. Seepeale kuvab programm teisenduse tulemuse ekraanile. 

.. hint::

    .. sourcecode:: py3
        
        ...
        algyhik = input("Kas sinu summa on eurodes (EUR) või kroonides (EEK) ?")
        ...

Proovige kirjutada sellest programmist kaks varianti erinevate kitsendustega: 

    * esimeses programmis kasutatakse muutujale omistamist ainult ühes kohas
    * teises programmis kasutatakse ``print`` käsku ainult ühes kohas

.. hint::

    .. sourcecode:: py3
        
        ...
        if ... :
            print(...)
        else:
            print(...)
        ...
    
    vs.

    .. sourcecode:: py3
        
        ...
        if ... :
            tulemus = ...
        else:
            tulemus = ...
        
        print(...)

.. index:: 
    single: tsükkel

Üheharuline ``if``-lause
~~~~~~~~~~~~~~~~~~~~~~~~~
Tingimuslauses võib ``else`` osa ära jätta -- seda kasutatakse siis, kui tingimuse mittekehtimise puhul ei ole vaja midagi spetsiifilist teha:

.. sourcecode:: py3

    x = int(input("Sisesta esimene arv: "))
    y = int(input("Sisesta teine arv: "))
    
    print("Arvude erinevus on " + str(abs(x-y)))
    if x == y:
        print("... järelikult on nad võrdsed")

Harjutus
~~~~~~~~~~~~~~
TODO


Tingimuslaused üksteise sees
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Tingimuslauseid võib panna üksteise sisse:

.. sourcecode:: py3
    
    arv1 = int(input("Sisesta esimene arv: "))
    arv2 = int(input("Sisesta teine arv: "))
    
    if arv1 > arv2:
        print("Esimene arv on suurem")
    else:
        if arv2 > arv1:
            print("Teine arv on suurem")
        else:
            print("Arvud on võrdsed")

Põhimõte on sama nagu lihtlausete "allutamisel" -- alluvuse tähistamiseks lisatakse vastavate ridade algusesse 4 tühikut. Kui alluvatel endal on alluvaid, siis võibki mõne rea ette sattuda 8, 12, üldisemalt `n * 4` tühikut. 

.. note::

    Nüüd peaks olema ka näha, miks treppimist nimetatakse treppimiseks -- kui joondamine toimub mitmel tasemel, siis paistab nagu programmi tekst paikneks trepiastmetel.

Harjutus
~~~~~~~~~~~~~~~~ 
TODO


Tingimusega korduslause e. ``while``-lause
-----------------------------------------------
Kui meil on vaja teha sama toimingut mitu korda järjest, siis võiks arvata, et programmi tuleb lihtsalt kirjutada laused lihtsalt mitmekordselt, nagu järgmises programmis, mis joonistab kilpkonnaga ruudu:

.. sourcecode:: py3
    
    from turtle import *
    
    küljepikkus = 100
    forward(küljepikkus)
    left(90)
    forward(küljepikkus)
    left(90)
    forward(küljepikkus)
    left(90)
    forward(küljepikkus)
    left(90)
    
    exitonclick()
    

Selline lahendus muutub väga kohmakaks, kui korduste arv läheb suureks. Pealegi, kui sooviksime kirjutada üldisema programmi, mis joonistab *n* küljega hulknurga vastavalt kasutaja poolt sisestatud *n* väärtusele, siis jääksime hätta, kuna me ei tea, mitu korda tuleks ühe külje joonistamise ja pööramise käske kirjutada.

Siinkohal tulevad appi **tsüklid** (e. korduslaused), mis on programmikonstruktsioonid käskude kordamiseks. Selles peatükis vaatame **while-lauset**, mis kordab tema alluvusse paigutatud lauseid niikaua, kuni teatud tingimus kehtib. 


.. index:: 
    single: while tsükkel
    single: tsükkel; while tsükkel
    

``while``-lausega saaksime ruudu joonistamise programmi panna kirja järgnevalt:

.. sourcecode:: py3
    
    from turtle import *
    
    # selle muutuja abil peame arvet, mitu külge on juba joonistatud
    joonistatud_kylgi = 0               
    
    while joonistatud_kylgi < 4:
        forward(100)
        left(90)
        joonistatud_kylgi = joonistatud_kylgi + 1   # suurendame muutuja väärtust

    exitonclick()


``while``-lause keha täidetakse vaid siis kui päises antud tingimus kehtib. Selles suhtes on ``while`` väga sarnane üheharulisele ``if``-lausele. Erinevus on selles, et kui kehas olevad laused on täidetud, siis minnakse uuesti päises näidatud tingimust kontrollima -- kui tingimus kehtib ikka veel, siis täidetakse kehas olevad laused uuesti jne. 

Selleks, et taoline tsükkel ei jääks lõputult tööle, peab tsükli kehas olema midagi, mis mõjutab tingimuse kehtivust -- antud näites on selleks lause ``joonistatud_kylgi = joonistatud_kylgi + 1``. Kuju poolest on siin tegemist täiesti tavalise omistuslausega, ainuke veider asi on see, et paremal pool mainitakse sedasama muutujat, mida parasjagu defineeritakse. Kas siin ei lähe miskit "sõlme"?

Muutuja muutmine
~~~~~~~~~~~~~~~~~~~
Pythoni muutujate süsteem on ehitatud selliselt, et muutuja väärtust on võimalik *üle defineerida* või lihtsamalt öeldes *muuta*. Iga muutuja viitab tegelikult ühele pesale või lahtrile kuskil Pythoni sisemuses olevas tabelis, ja selles lahtri sisu on võimalik omistuslausega muuta.
    
Antud näites genereerisime muutujale ``joonistatud_kylgi`` uue väärtuse tema eelmise väärtuse põhjal. Selles pole Pythoni jaoks midagi erilist -- nagu eelmises peatükis mainitud, väärtustab Python omistuslause käivitamisel kõigepealt parema poole ja salvestab saadud tulemuse vasakul pool näidatud muutujasse. Seega, kui ``joonistatud_kylgi`` väärtuseks oli ``0``, siis kõigepealt arvutati välja parema poole väärtus ``1`` ning alles seejärel uuendati muutuja sisu.

.. topic:: Tähelepanu!!!

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



Lühem kirjapilt muutuja kasvatamiseks / kahandamiseks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Muutuja väärtuse suurendamist mingi arvu võrra saab Pythonis ka lühemalt kirjutada: ``x = x + 1`` asemel võime kirjutada ``x += 1``. Muutuja väärtuse vähendamiseks võib analoogselt kirjutada ``x -= 1``. 

.. admonition:: Terminoloogia

    Muutujaid, mille väärtust suurendatakse igal tsükli sammul ühe võrra, nimetatakse *loenduriteks*. Selliseid tsükleid, kus korduste arv on tsükli alustamise hetkel teada, nimetatakse *määratud tsükliteks*.

.. admonition:: Katsetus

    Nagu mäletate, on ``+`` defineeritud ka sõnede jaoks. Mida võiks ``+=`` tähendada sõnede puhul?



Harjutus 3. Programm *n*-nurga joonistamiseks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Kirjutage ruudu näite põhjal programm, mis joonistab *n*-küljega hulknurga (*n* väärtus ja küljepikkus küsitakse kasutajalt). 

.. hint::
    Iga nurga juures peab kilpkonn pöörama 360/n kraadi.
    
Tsükli ja tingimuslause kombineerimine
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Nii ``if``-lause, kui ``while``-lause keha võib koosneda suvalistest Pythoni lausetest. Järelikult võib panna ka ``if``-lause ``while``-lause sisse (ja vastupidi):

.. sourcecode:: py3

    i = 1

    while i <= 10:
        print("Vaadeldav arv on", i)
        if i % 2 == 0:
            print("Tegemist on paarisarvuga")
        else:
            print("Tegemist on paaritu arvuga")

        ruut = i * i
        if ruut % 2 == 0:
            print("Tema ruut", ruut, "on paarisarv")
        else:
            print("Tema ruut", ruut, "on paaritu arv")

        print("--------------------------------")
        i += 1
    
    print("Sellega on meie arvuteoreetiline uurimus lõppenud")

.. note::

    Eelmises peatükis soovitati valida muutujatele nimed, mis kirjeldavad nende tähendust. Selles näites on aga muutuja nimega ``i``, mis ei paista midagi tähedavat. Milles asi?
    
    Asi on selles, et nime ``i`` kasutamine tsüklimuutuja jaoks lihtsalt väga levinud. Nähes muutujat nimega ``i`` kusagil tsükli läheduses, eeldab iga vähegi kogenud programmeerija, et seda muutujat kasvatatakse igal tsükli sammul ühe võrra. Seega ei rikkunud me antud näites tähendusrikka muutujanime reeglit -- sellele  nimele lihtsalt ongi kujunenud oma tähendus.



Harjutus 4. Loendamine
~~~~~~~~~~~~~~~~~~~~~~
Täiendage eelnevat programmi veel ühe loenduriga, mille abil loetakse kokku 3-ga jaguvate ruutude arv. Kui kõik arvud on läbi vaadatud, siis väljastage saadud tulemus.

Määramata tsükkel
~~~~~~~~~~~~~~~~~
Alati pole võimalik ette öelda, kui mitu korda midagi kordama peab enne, kui jõutakse soovitud tulemuseni. ``while`` lause sobib ka neil juhtudel, sest tsükli päises võime kasutada suvalist tingimust. Järgmine näiteprogramm laseb kasutajal arvata juhuslikult valitud arvu niikaua, kuni ta jõuab õige vastuseni:

.. sourcecode:: py3

    from random import randint 
    
    arv = randint(1, 999) # randint annab juhusliku täisarvu näidatud vahemikust
    arvamus = int(input("Arva, millist tuhandest väiksemat arvu ma mõtlen: "))

    # Kuni pakutud arv erineb arvuti valitust
    while arvamus != arv :
        if arv > arvamus:
            print("Minu arv on suurem!")
        else:   
            print("Minu arv on väiksem!")
            
        arvamus = int(input("Arva veelkord: "))
        
    print("Ära arvasid! Tubli!")


Harjutus 5. Kolmeaastase lapse simulaator
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Kirjutage programm, mis küsib kasutajalt mingi küsimuse ja seejärel küsib iga sisestuse peale "Aga miks?" niikaua, kuni kasutaja sisestab mingi kindla "võlusõna".

Proovige kirjutada ka terapeudi variant, kus vahelduvad kaks erinevat küsimust.
    
.. hint::

    "Millest sa veel sooviksid rääkida?"
    
    "Milliseid tundeid see sinus tekitab?"


Harjutus 6. Algandmete kontrollimine tsükliga
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Tsükleid saab kasutada algandmete sisestamise juures -- me võime vigase sisendi puhul lasta kasutajal sisestamist korrata niikaua, kuni oleme sistatud infoga rahul.

Kirjutage ruutjuure arvutamise programm, mis enne ruutjuure võtmist kontrollib, kas sisestati positiivne arv. Niikaua kuni sisestati mittepositiivne arv, tuleb sisendi küsimist jätkata (koos selgitusega, miks eelmine sisend ei sobinud).


Käsk ``break``
~~~~~~~~~~~~~~
Tsükli lõpetamise määrab tavaliselt tsükli päises olev tingimus. Sellele lisaks on Pythonis veel üks võimalus tsükli töö lõpetamiseks -- selleks tuleb tsükli kehas anda sobival hetkel käsk ``break``.

Järgnevas näites on arvamismängu täiendatud selliselt, et ühte tsükli lõpetamise tingimust (arvu ära arvamine) kontrollitakse tsükli päises ning teist tingimust (10 ebaõnnestunud arvamist) kontrollitakse tsükli kehas:

.. sourcecode:: py3

    from random import randint 
    
    arv = randint(1,999) # randint annab juhusliku täisarvu näidatud vahemikust
    arvamus = int(input("Arva, millist tuhandest väiksemat arvu ma mõtlen: "))
    arvamise_kordi = 1
    
    while arvamus != arv :
        if arv > arvamus:
            print("Minu arv on suurem!")
        else:
            print("Minu arv on väiksem!")
            
        if arvamise_kordi == 10:
            break # lõpetab tsükli töö
        
        arvamus = int(input("Arva veelkord: "))
        arvamise_kordi += 1 # lühem kirjapilt muutuja väärtuse suurendamiseks
    
    # kuna tsükkel võis lõppeda ka ebaedukalt, siis peame enne kiitmist kontrollima...
    if arv == arvamus:
        print("Ära arvasid! Tubli!")
    else:
        print("Kümnest arvamisest ei piisanud, äkki peaksid taktikat muutma?")

.. note::

    Selles programmis kasutasime ka ``if``-lause "üheharulist" varianti -- st ``if`` ilma ``else``-ta. Selle variandi puhul ei tee ``if``-lause tingimuse mittekehtimise puhul mitte midagi. Erinevatest tingimuslause kujudest tuleb täpsemalt juttu ühes hilisemas peatükis.

Tegelikult pole ``break`` lause Pythoni programmides hädavajalik - tsükli saab alati ümber kirjutada nii, et kõiki jätkamise/lõpetamise tingimusi kontrollitakse tsükli päises, aga vahel on ``break``-iga lahendus lihtsam.

Mõnikord on mugav tsükli lõpetamise tingimust kontrollida *ainult* tsükli kehas, sel juhul pannakse tsükli päisesse alati kehtiv tingimus ``True``. Järgnev programm küsib kasutajalt arve ja näitab nende ruute niikaua, kuni kasutaja sisestab *tühisõne* (st. vajutab ENTER ilma midagi tegelikult sisestamata):

.. sourcecode:: py3

    while True:
        tekst = input("Sisesta arv ja vajuta ENTER (lõpetamiseks vajuta ainult ENTER): ")
        
        if tekst == "":  
            print("OK, lõpetan")
            break
        else: # ei olnud ei arv ega tühisõne
            arv = float(tekst)
            print("Selle arvu ruut on", arv * arv)

Harjutus 7. Juhuslikud arvud
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Kirjutage programm, mis väljastab iga ENTER vajutuse järel (st. tühisõne sisestamisel) ekraanile juhusliku täisarvu vahemikus 1..999. Tsükli töö tuleks lõpetada (kasutades ``break``-i) siis, kui kasutaja sisestab tühisõne asemel sõne ``'aitab'``.

Harjutus 8. Algandmete kontrollimine ja ``break``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Kirjutage algandmete kontrollimise ülesande lahendus ümber nii, et ``input`` käsku on programmis kasutatud vaid ühes kohas.

Summa arvutamine tsüklis
~~~~~~~~~~~~~~~~~~~~~~~~~~
Senistes näidetes kasvatasime igal kordusel loenduri väärtust 1 võrra. Tegelikult ei ole Pythonil mingit põhjust piirata, kuidas me muutuja väärtust suurendame (või vähendame). Uurige ja proovige mõista järgmist näidet: 

.. sourcecode:: py3

    n = int(input("Sisesta naturaalarv: "))
    
    summa = 0
    i = 0
    
    while i <= n:
        summa += i
        i += 1
    
    print(n, "esimese naturaalarvu summa on", summa)

Antud juhul suurendasime igal tsükli kordusel ühe muutuja väärtust teise muutuja väärtuse võrra.


Harjutus 9. Faktoriaali arvutamine
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Kirjutage programm, mis arvutab etteantud arvu faktoriaali.

.. note:: 

    Kuidas käitub teie programm negatiivse arvu korral?

Failist lugemine tsükliga
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Meie senised failist lugemise näiteprogrammid teadsid (õigemini eeldasid), mitu rida antud failis on. Praktikas tuleb aga palju sagedamini ette situatsioone, kus faili ridade arv pole teada. Järgnev näide demonstreerib faili kõikide ridade lugemist:

.. sourcecode:: py3

    f = open('nimed.txt')
    
    while True:
        nimi = f.readline()
        # kui jõuti faili lõppu, siis readline tagastab "tühja sõne"
        if nimi == "":
            break
            
        if nimi.strip() == 'Margus':  # strip eemaldab reavahetuse sümboli
            print('Hommik!')
            print('Kuis kulgeb?')
        else:
            print('Tervist, lugupeetud ' + nimi.strip() + '!')
    
    f.close()

.. admonition:: Veaotsingust

    Selles näites kasutasime ``strip`` meetodit seepärast, et failist ridade lugemisel jäetakse rea lõppu ka reavahetuse sümbol. Selline nüanss aga ei pruugi alati meelde tulla ja sel juhul programm lihtsalt ei tööta õigesti.
    
    Kui tekib selline situatsioon, kus programm ei tööta nii nagu te soovite, siis võiks kõigepealt uurida, kas sisendandmed loeti sisse selliselt nagu te arvasite. Antud programmis võiks tsüklis esimese asjana (enne tingimuslauset) kuvada ekraanile loetud nime. Selleks, et oleks näha ka tühikute ning reavahetuste paiknemine, võib kuvamist teha nt. selliselt: ``print('>' + nimi + '<')``.

Harjutus 10. Failis olevate temperatuuride teisendamine
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Kirjutage programm, mis loeb tekstifailist temperatuure Fahrenheiti skaalas ja väljastab ekraanile vastavad temperatuurid Celsiuse skaalas.

.. hint::

    Ärge unustage, et ``readline`` tagastab sõne. Arvutamiseks on vaja see teisendada arvuks.





.. index::
    single: bool; tõeväärtustüüp
    single: boolean; tõeväärtustüüp

Tõeväärtustüüp ``bool``
-----------------------
Nagu varem mainitud, koosneb iga Pythoni programmi lausetest ja lause komponentideks on avaldised. Tuleb välja, et Python peab ka ``if`` või ``while`` lause päises olevat tingimust avaldiseks. Aga kui igal avaldisel on väärtus, siis millised näevad välja tingimuse väärtused? Proovime järgi:

.. sourcecode:: py3

    >>> 3 > 2
    True
    >>> 3 > 3
    False
    >>> 3 >= 3
    True
    >>> x = 4
    >>> y = 5
    >>> x == y
    False
    >>> y > x
    True
    >>> toit = "Kapsas"   # NB! ühe võrdusmärgiga on omistamine
    >>> toit == "kapsas"  # kahe võrdusmärgiga on võrduse kontrollimine
    False
    >>> toit.lower() == "kapsas"
    True

Selgitus: Tingimuste jaoks on Pythonis eraldi andmetüüp nimega ``bool``, milles on vaid kaks võimalikku väärtust -- ``True`` ja ``False``. Eesti keeles nimetatakse seda andmetüüpi **tõeväärtustüübiks** (``bool`` on lühend sõnast ``boolean``, mis tuleb omakorda matemaatiku George Boole'i nimest).

Pole kokkusattumus, et me käsitleme seda andmetüüpi just tingimuslausete peatükis -- kõik avaldised, mis annavad väärtustamisel tulemuseks ``True`` või ``False`` sobivad ``if`` või ``while``-lause päisesse ning nende lausete päised on põhiline koht, kus tõeväärtusi kohtab. 

.. note::

    Just nagu iga avaldise puhul, saab ka tõeväärtusavaldise põhjal defineerida muutujaid. Kuna ``if``-lause päises võib tõeväärtus olla antud mistahes kujul, siis võiksime mingi kontrolli tulemuse salvestada eelnevalt muutujasse ning hiljem kasutada seda muutujat tingimusena:

    .. sourcecode:: py3

        arv = int(input("Sisesta arv: "))
        jagub_kahega = arv % 2 == 0 # salvestame tõeväärtuse abimuutujasse
        
        if jagub_kahega:
            print("Sisestati paarisarv")
        else:
            print("Sisestati paaritu arv")

    Antud näites ei andnud abimuutuja kasutamine küll midagi juurde -- samaväärse programmi võiksime panna kirja ka lihtsamalt:

    .. sourcecode:: py3

        arv = int(input("Sisesta arv: "))
        
        if arv % 2 == 0:
            print("Sisestati paarisarv")
        else:
            print("Sisestati paaritu arv")

    Keerulisemate tingimuste korral võib aga abimuutuja kasutamine teha koodi paremini loetavaks.


Tõeväärtustehted
~~~~~~~~~~~~~~~~~~~~~~~
Kuigi tõeväärtustüübis on vaid kaks väärtust ``True`` ja ``False``, on olemas palju erinevaid viise nende genereerimiseks. Järgnev tabel demonstreerib mõnesid neist:

+----------------------------------+---------+---------------------------------------------------------------------+
| Avaldis                          | Väärtus | Kommentaar                                                          |
+==================================+=========+=====================================================================+
| ``2 == 2.0``                     |``True`` | ``==`` sobib nii sõnede, kui arvude võrduse kontrollimiseks         |
+----------------------------------+---------+                                                                     +
| ``'tere' == 'tere'``             |``True`` |                                                                     |
+----------------------------------+---------+---------------------------------------------------------------------+
| ``2 == '2'``                     |``False``| Ükski sõne pole ühegi arvuga võrdne                                 |
+----------------------------------+---------+---------------------------------------------------------------------+
| ``2 != '2'``                     |``True`` | ``!=`` annab ``True`` neil juhtudel kus ``==`` annaks ``False``     |
+----------------------------------+---------+ ja vastupidi                                                        +
| ``2 != 2``                       |``False``|                                                                     |
+----------------------------------+---------+---------------------------------------------------------------------+
| ``3 > 3``                        |``False``| Arvude võrdlemine toimub ootuspäraselt                              |
+----------------------------------+---------+                                                                     +
| ``3 >= 3``                       | ``True``|                                                                     |
+----------------------------------+---------+                                                                     +
| ``2 < 3``                        | ``True``|                                                                     |
+----------------------------------+---------+                                                                     +
| ``2 <= 3``                       | ``True``|                                                                     |
+----------------------------------+---------+---------------------------------------------------------------------+
| ``'koer' < 'kirp'``              | ``True``| Sõnede võrdlemine toimub tähestiku järgi                            |
+----------------------------------+---------+---------------------------------------------------------------------+
| ``'r' in 'tore'``                | ``True``| ``in`` kontrollib tähe või *alamsõne* leidumist sõnes               |
+----------------------------------+---------+                                                                     +
| ``'r' in 'tobe'``                |``False``|                                                                     |
+----------------------------------+---------+                                                                     +
| ``'art' in 'Tartu'``             | ``True``|                                                                     |
+----------------------------------+---------+---------------------------------------------------------------------+
| ``'Tallinn'.endswith('linn')``   | ``True``| Sõnemeetodid ``startswith`` ja ``endswith`` teevad seda, mida võiks |
+----------------------------------+---------+ nende nimedest arvata                                               +
| ``'Tallinn'.startswith('reha')`` |``False``|                                                                     |
+----------------------------------+---------+---------------------------------------------------------------------+
| ``'10203'.isnumeric()``          | ``True``| ``isnumeric`` annab ``True`` kui sõne sisaldab ainult numbreid      |
+----------------------------------+---------+---------------------------------------------------------------------+

Loomulikult saab kõiki mainitud operatsioone kasutada ka muutujatega.



Harjutus x. Mitte-tõstutundlik sõnede võrdlemine
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
TODO



Harjutus 1. Arvu ruut koos kontrolliga
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Kirjutage programm, mis küsib kasutajalt positiivse täisarvu ning kontrollib, kas sisestatud tekst on numbriline. Kui jah, siis kuvatakse antud arvu ruut, vastasel juhul kuvatakse veateade. 

.. index::
    single: loogilised avaldised

Tõeväärtuste kombineerimine
~~~~~~~~~~~~~~~~~~~~~~~~~~~
Nägime, et tõeväärtused on paljude arvu- ja sõnetehete tulemuseks. Kas on olemas mingeid mõistlikke tehteid, mida saab teha tõeväärtuste endiga?

Kõige tähtsamad tehted, mille argumentideks on tõeväärtused, so. **loogilised tehted**, on ``and``, ``or`` ja ``not``. Nende operaatorite tähendus on arvatavasti intuitiivselt arusaadav, kuid vajadusel saab kõik kombinatsioonid Pythoni käsureal järgi proovida:

    * ``True and False``
    * ``True and True``
    * ...
    * ``True or False``
    * ``True or True``
    * ...
    * ``not True``
    * ``not False``

Loomulikult ei hakka keegi kirjutama programmi, mis arvutaks välja avaldise ``True and False`` väärtuse -- loogilisi tehteid kasutatakse üldjuhul teiste tõeväärtusavaldiste kombineerimiseks, just nagu järgmises näites:

.. sourcecode:: py3

    parool = input("Sisesta oma uus parool: ")
    
    if len(parool) >= 8 and parool != "password":
        print("Hea valik!")
    else:
        print("See parool jääb lahjaks!")
    
    
Keerulisemate loogiliste avaldiste puhul tuleb arvestada, et ``not`` on kõrgema prioriteediga kui ``and`` ning ``and`` on kõrgema prioriteediga kui ``or``, seega ``not x or not y and z`` tähendab ``(not x) or ((not y) and z)``.

Kuna ühes avaldises võivad olla koos aritmeetilised tehted, võrdlustehted ja loogilised tehted, siis selleks, et vähendada sulgude vajadust, on aritmeetilised tehted kõrgema prioriteediga (st. tehakse esimesena) ning loogilised tehted on madalama prioriteediga (tehakse viimasena), seega ``a > b and b > c`` tähendab ``(a > b) and (b > c)``.

Harjutus 2. Vastandid
~~~~~~~~~~~~~~~~~~~~~~
Pange kirja järgnevate avaldiste loogilised *vastandid*:

.. sourcecode:: none

    a > b
    a >= b
    a >= 18  and  b == 3
    a >= 18  and  b != 3

Tingimuste kasutamine tsükli päises
---------------------------------------
Justkui tingimuslause päises, lubatakse ka ``while``-lause päises suvalisel kujul tingimust, peamine, et tegemist oleks ``bool`` tüüpi avaldisega:

.. sourcecode:: py3
    
    a = ...
    b = ...
    c = ...
    s = ...

    
    while (a == b or b > c) and s == "Tere":
        ...

        
    tingimus = ... or ... or ... or ...
    while tingimus or a > b or s.endswith("kala"):
        ...
        a = ...
        ...

    
    while True:
        ...

Pykkar
-----------------------
Kui tegite eelnevate harjutuste plokkskeemid paberile, siis saite sedasi esitatud algoritme "käivitada" vaid enda peas. Nagu teada, on inimene aga ekslik ja seetõttu võisid mõned vead algoritmides jääda märkamatuks. 

Nüüd on teil võimalus teisendada oma skeemid Pythoni koodiks ja näha roboti liikumist oma ekraanil. Kõigepealt laadige alla moodul :download:`pykkar.py <downloads/pykkar.py>` ja salvestage see oma töökausta.

Nüüd salvestage samasse kausta järgnev näiteskript ja käivitage see:

.. sourcecode:: py3

    from pykkar import *
    
    # create_world võtab argumendiks mitmerealise sõne, mis esitab
    # roboti "maailma"
    # Trellid tähistavad seinu, nooleke tähistab robotit
    # (noole suund tähistab roboti suunda)
    create_world("""
    ########
    #  >   #
    #      #
    #      #
    #      #
    #      #
    ########
    """)

    samme_jäänud = 3
    while samme_jäänud > 0:
        if is_wall(): # ei lase robotil vastu seina põrgata
            break
        else:
            step() # robot liigub ühe ruudu võrra edasi
            samme_jäänud -= 1
    
    # pöörame ringi
    right()
    right()

Loodetavasti nägite programmi käivitamisel umbes sellist pilti:

.. image:: images/pykkar.png

Justnagu plokkskeemi robot, mõistab ka Pykkar liikuda ühe sammu edasi (``step()``), pöörata 90° paremale (``right()``), värvida enda all olevat ruutu (``paint()``) ning kontrollida, kas ta ees on sein (``is_wall()``). 

Antud näiteprogramm vastab umbkaudselt eespool toodud harjutusele "2. Kui võimalik, kolm sammu  edasi ja ümberpöörd" (lahendus on küll natuke üldisem). Muutke programmis roboti algset asukohta ja katsetage, kas programm toimib õieti ka siis, kui seinani on vähem, kui 3 sammu.

Harjutus 6. Plokkskeemi kohandamine Pythoni programmiks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Kirjutage nüüd eespool antud robotiülesanded ümber Pythoni programmideks, kasutades moodulit ``pykkar``.






Kokkuvõte
----------
Selles peatükis nägime, et Pythoni programm ei pruugi olla vaid lihtsate käskude jada, mida täidetakse üksteise järel kuni jõutakse programmi lõppu. Vaatlesime kolme programmikonstruktsiooni, millel kõigil on **päis** ja tühikutega veidi paremale nihutatud **keha**, kusjuures kehas olevate lausete täitmise viis on kõigil kolmel juhul erinev:

    * **Tingimuslause** e. ``if``-lause peaharus olevad laused täidetakse ainult siis, kui päises esitatud tingimus kehtib. Kui tingimuslauses on olemas ka ``else`` haru, siis seal olevad laused täidetakse siis, kui tingimus *ei* kehti. Sellise konstruktsiooniga saab muuta programme paindlikumaks, pannes selle käituma üht- või teistmoodi vastavalt olukorrale.
    * **Korduslause** e. tsükli puhul täidetakse kehas olevad laused 0 või rohkem korda, vastavalt päisele. Selles peatükis vaadeldud ``while``-lause korral kontrollitakse enne kehas olevate lausete täitmist, kas päises antud tingimus kehtib, justnagu tingimuslausegi puhul. Erinevalt tingimuslausest, minnakse peale keha täitmist uuesti tingimust kontrollima ja kui see kehtib endiselt, siis täidetakse kehas olevad laused uuesti jne. Seda protsessi korratakse niikaua, kuni tingimus enam ei kehti. Korduslausega saame kirjeldada protsesse, kus sama toimingut tuleb teha mitu korda järjest (ja seejuures ei pruugi me korduste arvu programmi kirjutamisel ette teada).
    * **Funktsiooni definitsiooni** kehas olevad laused jäetakse esialgu lihtsalt meelde. Neid saab hiljem käivitada kirjutades definitsiooni päises antud nime koos sulgudega -- seda nimetatakse *funktsiooni väljakutseks* e. rakendamiseks. Funktsioonid võimaldavad keerulise programmilõigu panna kirja vaid ühekordselt, aga kasutada seda mitmes erinevas kohas.

Kõiki vaadeldavaid programmikonstruktsioone nimetatakse Pythonis **liitlauseteks**. Nagu ülalpool mainitud, koosnevad nende kehad suvalist liiki lausetest -- see võimaldab näiteks funktsiooni definitsioonis lisaks lihtlausetele (vt. eelmisest peatükist) kasutada ka korduslauset, mille kehas on omakorda kasutatud tingmuslauset, mille kehas on veel üks tingimuslause jne.

Taolist lausete üksteise sisse panemist esitatakse Pythonis **treppimisega** -- samasse kehasse (e. plokki) kuuluvate lausete vasakud servad joondatakse tühikute abil sama kaugele. Liitlausete puhul joondatakse eelnevate ja järgnevate lausetega vaadeldava lause päis, keha nihutatakse päisega võrreldes veel rohkem paremale.

Kõikide nimetatud programmikonstruktsioonide kohta andsime selles peatükis vaid kõige olulisema info, neist kõigist tuleb edaspidi veel palju juttu.

Ülesanded
-------------------

1. Paaris või paaritu
~~~~~~~~~~~~~~~~~~~~~
Koostage tekstifail, mis sisaldab täisarve erinevatel ridadel. Kirjutage programm, mis loeb antud failist ükshaaval arve ning kuvab iga arvu kohta ekraanile info, kas tegemist oli paaris või paaritu arvuga.

2. Pere sissetulek
~~~~~~~~~~~~~~~~~~
Kirjutage programm, mis küsib isa brutopalga, ema brutopalga ning alaealiste laste arvu ja arvutab selle põhjal pere kuusissetuleku. (Oletame, et iga alaealise lapse kohta makstakse toetust 20€ kuus.) 

Esialgu võite eeldada, et mõlema vanema kuupalk on vähemalt sama suur kui maksuvaba miinimum. (Siiamaani saaksite selle ülesande lahendada ka ilma selle peatüki vahenditeta).

Lõpuks korraldage nii, et programm töötab õigesti ka siis, kui ema või isa brutopalk on maksuvabast miinimumist väiksem.

.. note::

    Kui teile tundub, et selle ülesande juures oleks kasu funktsioonidest, siis olete täiesti õigel teel. Paraku tuleks sissetuleku funktsiooni defineerimisel kasutada teatud lisavigureid, mida selles peatükis polnud mahti tutvustada. Seega, praegu soovitame selle ülesande lahendada ilma uusi funktsioone defineerimata (aga soovi korral võite muidugi vajalikud vigurid juba välja uurida).

3. Busside logistika
~~~~~~~~~~~~~~~~~~~~~
Olgu meil vaja transportida teatud arv inimesi bussidega, milles on teatud arv kohti. Mitu bussi on vaja selleks, et kõik inimesed kohale saaksid ja mitu inimest on viimases bussis (eeldusel, et eelmised on kõik täiesti täis)? Kirjutage programm, mis küsib inimeste arvu ja busside suuruse ning lahendab seejärel selle ülesande. 

    
**Testige** oma programmi muuhulgas järgmiste algandmetega:

* inimeste arv: 60, kohtade arv: 40
* inimeste arv: 80, kohtade arv: 40
* inimeste arv: 20, kohtade arv: 40
* inimeste arv: 40, kohtade arv: 40

Üritage mõista, miks valiti taolised testiandmed.

4. projecteuler.net, problem 1
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Kirjutage programm, mis lahendab esimese ülesande aadressilt http://projecteuler.net/problems.

.. hint::

    .. sourcecode:: py3
    
        if esimene_tingimus or teine_tingimus:
            ...

.. note::

    Soovitame otsida sellelt saidilt endale huvipakkuvaid ülesandeid ka edaspidi! Kui teete endale seal konto, siis saate oma progressi salvestada ja tulemusi kontrollida.

5. Ringi joonistamise funktsioon
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Kirjutage *funktsioon* ``ring()``, mis joonistab kilpkonnaga pisikestest sirglõikudest koosneva ringitaolise kujundi. Ringi suurus pole praegu oluline. Lisage programmi ka selle funktsiooni väljakutse.

.. hint::

    Sarnane ülesanne on ülalpool juba antud, aga natuke teises sõnastuses. Nüüd on aga vaja lahendus vormistada funktsioonina.

6. Kujundid
~~~~~~~~~~~~

Kirjutage programm, mis küsib kasutajalt ridade arvu ning väljastab ekraanile vastava kõrgusega kujundid järgneva skeemi järgi:

.. sourcecode:: none

    # # # # # # #
    #           #
    #           #
    #           #
    #           #
    #           #
    # # # # # # #


.. sourcecode:: none

    * 
    * * 
    * * * 
    * * * * 
    * * * * * 
    * * * * * * 
    * * * * * * * 

.. hint::
    
    Tuletage meelde, mida tähendab ``'Tere' * 4``



7. Kivi-paber-käärid
~~~~~~~~~~~~~~~~~~~~~~~~
Kirjutage programm, mis väljastab iga ENTER-klahvi vajutuse peale ühe juhuslikult valitud sõna loetelust "kivi", "paber", "käärid". Programmi töö lõpetamiseks tuleb kasutajal enne ENTERi vajutamist sisestada "aitab".

.. hint::

    ENTER-i vajutamine on Pythoni jaoks sama, mis tühja sõne sisestamine

.. hint::

    >>> from random import randint
    >>> randint(1,3)
    3
    >>> randint(1,3)
    1

.. hint::

    .. sourcecode:: py3
    
        if ...:
            ...
        else:
            if ...:
                ...
            else:
                ...

8. Raskem: Redeli asendid
~~~~~~~~~~~~~~~~~~~~~~~~~~
Ülesandeks on genereerida Pythoni kilpkonnaga joonistus, mis kujutab redelit (esitatud lihtsalt sirgjoonena) seina najal erinevate nurkade all. Joonistage redel kõigepealt horisontaalasendis ning seejärel mitmes asendis järjest suurema nurga all, kuni lõpuks jõuab redel vertikaalasendisse.

.. hint::

    Abiks võib olla ``turtle`` käsk ``back``, mis liigutab kilpkonna senise suunaga võrreldes tagurpidi. (Aga see pole ülesande lahendamiseks tingimata vajalik).

9. Raskem: Ruudustik
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Kirjutage programm mis küsib ruutude arvu vertikaalsuunal, ruutude arvu horisontaalsuunal, ning joonistab kilpkonna abil vastava ruudustiku, nt:

.. image:: images/ruudustik.png

.. topic:: Lisaülesande lisa
    
    Uurige kilpkonna dokumentatsioonist, kuidas värvida soovitud ala (http://docs.python.org/py3k/library/turtle.html). Seejärel proovige joonistada malelaud.
    

Ülesanne. mp3
~~~~~~~~~~~~~~~~~~~~
Loe mp3 metadatat
mingi olemasoleva parseriga / ise parsides vt. struct module

Praktilisi näpunäiteid
------------------------
Veaotsingust
~~~~~~~~~~~~~~
Esimeses peatükis sai juba veidi tutvustatud Pythoni veateadete hingeelu. (Kuna nüüd olete veateateid juba rohkem näinud, on soovitav see osa uuesti, uue pilguga üle lugeda.)

Nagu ilmselt juba olete kogenud, on kõige problemaatilisemad vead aga need, mille kohta Python veateadet ei taipa anda. Selleks, et taolisi vigu väiksema närvikuluga avastada, soovitame lugeda läbi lihtsad ja kasulikud retseptid järgnevalt aadressilt: http://openbookproject.net/thinkcs/python/english3e/app_a.html


Lisalugemine
-----------------

.. admonition:: Matemaatika ja programmeerimine

    Loodetavasti veendute järgnevat lugedes, et matemaatikat ja programmeerimist (ning matemaatika ja programmeerimise õppimist) saab omavahel väga edukalt siduda. Tegelikult ongi väga kasulik mingi uue matemaatilise mõiste õppimisel proovida väljendada seda mõnes programmeerimiskeeles. Erinevalt tavakeelest peab programmeerimiskeeles väljendama ennast alati absoluutselt täpselt, seetõttu toob taoline harjutus välja need aspektid, mille osas teie arusaamine antud mõistest on jäänud veidi hägusaks.

    Loomulikult ei pruugi alati tulla head ideed, kuidas mingit matemaatilist teemat programmeerimisega siduda. Selles osas on tavaliselt abi Wikipediast (nt http://en.wikipedia.org/wiki/Square_root#Computation)

Ruutjuure leidmine
~~~~~~~~~~~~~~~~~~
Kuidas arvutada ruutjuurt? Kui importida moodul ``math``, on asi muidugi lihtne. Tegelikult ei vasta see aga küsimusele, vaid lükkab selle lihtsalt meist kaugemale – me teame, et seda funktsiooni välja kutsudes saame me õige tulemuse, kuid me ei tea, kuidas arvuti selleni jõuab. Järgnevalt vaatame ühte viisi ruutjuure leidmiseks kus kasutatakse vaid lihtsaid aritmeetilisi tehteid.

Olgu meil antud arv `y`. Otsime sellist `x` et `x * x = y`. Siis aga `x = y / x`. Seega, kui võtta mingi lähend x\ :sub:`0` selle ruutjuure jaoks, võiks x\ :sub:`0` ja y/x\ :sub:`0` aritmeetiline keskmine olla tegelikule ruutjuure väärtusele juba lähemal, kui x\ :sub:`0` ise seda on. Tuleb välja, et nii enamasti ka on. See lubab ruutjuure leidmiseks kirjutada järgmise programmi:

.. sourcecode:: py3

    y = float(input("Sisestage arv, mille ruutjuurt tahate leida: "))

    x0 = 1
    while True :
        eelmine_x0 = x0
        
        x0 = (x0 + y / x0 ) / 2.0

        print("Lähend on " + str(x0))

        # Lõpeta arvutamine, kui lähend enam eriti ei muutu
        if abs(x0-eelmine_x0) < 0.0000001:
            break

    print("Ruutjuur on ligikaudu: " + str(x0))

``while True`` tähendab lõpmatut kordust. Tsükli kehas on aga siiski ``if``-lause, mille täidetuse korral kordus break-käsuga lõpetatakse. ``if``-lause kontrollib sisuliselt seda, kas eelmise lähendi ja uue lähendi erinevus on väiksem, kui 0,0000001. Peale natukest katsetamist peaks olema selge, et enamasti jõutakse sellise täpsuseni väga väheste korduste arvuga. Võiksite kontrollimise huvides võrrelda selle programmi ja näiteks ``math.sqrt`` tulemusi. Sellist lähendi leidmise meetodit nimetatakse Newtoni iteratsioonimeetodiks, inglise matemaatiku ja füüsiku Isaac Newtoni auks.

π leidmine
~~~~~~~~~~~~~~~~~~~~~~~~~
Järgmisena kirjeldaksime aga hästi kavalat viisi kuidas leida π (ringi ümbermõõdu ja diameetri vahelise suhte) väärtust. Kui joonistada ruut ja selle sisse ring, siis kui ringi raadius on `r`, on ruudu pindala `(2*r)*(2*r) = 4*r**2` ja ringi pindala `pi*r**2`. Seega ringi pindala moodustab `pi/4` kogu ruudu pindalast. Seega, valides juhusliku punkti ruudu seest, asub ta ringi sees tõenäosusega `pi/4`. Seega, kui valida juhuslikult palju punkte ruudu seest, peaks ligikaudu `pi/4` osa neist olema ringi sees. Neid kokku lugedes saame seega hinnata `pi/4` väärtust suhtega `ringi sees olevate arv` / `katsete koguarv`.

Teame, et ringi moodustavad kõik punktid, mis on tema keskpunktile lähemal kui raadius. Seega, kui keskpunkt on (0,0), siis on ringi sees täpselt need punktid (x,y) mille korral 
`sqrt(x**2 + y**2) ≤  r`, st. `x**2 + y**2 ≤  r**2`. Valides `r=1`, saame koostada järgmise programmi:

.. sourcecode:: py3

    import random

    n = int(input("Sisesta katsete arv: "))
    c = 0

    i = 0
    while i < n:
        # Genereeri juhuslik punkt
        x = random.uniform(-1,1)
        y = random.uniform(-1,1)

        # Kontrolli, kas ta on ringi sees
        if (x**2 + y**2 < 1):
            c=c+1
        
        i += 1

    print("Hinnanguks on "+ str((4.0*c) / n))

Funktsioon ``random.uniform`` valib ühtlase jaotuse põhjal juhuslikult ühe reaalarvu etteantud vahemikust. Kõik muu programmi juures peaks olema juba tuttav.

Katsetamine erinevate katsete arvudega (10,100,1000,...,1000000) peaks veenma, et kuigi tulemused on reeglina π-le lähedased, on see siiski suhteliselt halb meetod π kohtade leidmiseks sest vähegi mõistliku täpsuse saamiseks tuleb teha väga palju katseid.

.. admonition:: Graafiline versioon

    Kui selle lahenduskäigu põhimõte jäi hägusaks, siis laadige alla järgnev programm, mis demonstreerib sama asja graafiliselt: :download:`pi_demo.py <downloads/pi_demo.py>`. Juhuslike täppide genereerimiseks tehke programmi aknas hiireklõpse (hiirekursori asukoht pole tähtis). Iga uue täpi lisandumisel korrigeeritakse arvutatud pi väärtust vastavalt sellele, kas täpp sattus ringi sisse või mitte. Jooksvat tulemust näidatakse käsurea aknas.

Selliseid arvutusmeetodeid nimetatakse Monte Carlo meetoditeks (kuulsa kasiinolinna järgi Monakos). Antud näide on taas pigem illustratiivne – praktikas kasutatakse seda reeglina ülesannete puhul, mida muud moodi lahendada ei osata. π arvutamiseks teatakse aga palju teisi ja oluliselt paremaid meetodeid.

Collatzi jada
~~~~~~~~~~~~~~~~~~
TODO