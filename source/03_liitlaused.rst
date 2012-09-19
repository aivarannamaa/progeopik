3. Liitlaused
============================================

.. admonition:: Muudatused

    * 13. september -- lisatud mõned uued ülesanded.
    * 15. september -- lisatud kokkuvõte ja lisalugemine.
    * 18. september -- lisalugemise juurde lisatud π arvutamise graafiline demoprogramm.
    * 19. september -- lisatud näide "Summa arvutamine tsüklis". 4. ja 6. ülesandele lisatud kummalegi üks uus vihje.
    

.. index::
    single: tingimuslaused
    single: tingimuslaused; if-lause

Kui eelmise peatüki teemad liigitasime "lihtlausete" kategooriatesse, siis nüüd vaatame, milliseid on Pythoni olulisimad "liitlaused", mille abil saab teiste lausete toimimist muuta.


Tingimuslause e. ``if``-lause
-------------------------------
Eelmise peatüki programmidega töötas Python täiesti "tuimalt" -- alustas esimesel real oleva lausega, iga rea täitmise järel võttis ette järgmise rea, kuni jõudis programmi lõppu. Taolisest lähenemisest piisab paraku vaid väga lihtsate ülesannete puhul -- enamasti tuleb programmil mingil hetkel teha valikuid, kas jätkata üht- või teistmoodi. Python võimaldab programmeerijal taolised dilemmad panna kirja **tingimuslause** e. ``if``-lause abil.

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

Selles programmis ei täida Python enam kõiki käske -- see, kas täidetakse käsk ``vastus = -arv`` või ``vastus = arv``, sõltub konkreetsest kasutaja poolt sisestatud arvust.

Tingimuslause komponendid on *päis* (so. ``if``-i ja tingimusega rida), ``then``-haru (so. päisele järgnevad paremale nihutatud read), võtmesõna ``else``, ning ``else``-haru (jällegi paremale nihutatud).

Tingimusi saab moodustada järgmiste operaatoritega: 

* ``<``, ``>``, ``<=``, ``>=`` sobivad arvude võrdlemiseks
* Topeltvõrdusmärk (``==``) tähistab võrdsust nii arvude kui sõnede puhul
* ``!=`` tähistab mittevõrdsust nii arvude kui sõnede puhul

.. note::
    
    Ärge unustage, et üksikut võrdusmärki (``=``) kasutatakse Pythonis muutujale väärtuse omistamiseks, seetõttu on võrdsuse kontrollimiseks ette nähtud topeltvõrdusmärk (``==``).

.. admonition:: Etteruttavalt

    Mitut tingimust saab omavahel kombineerida operaatoritega ``and`` ja ``or``:
    
    .. sourcecode:: py3
        
        if x > 9 and x < 100:
            print("x on kahekohaline arv")
        else:
            print("x ei ole kahekohaline")
    
    Sellest tuleb põhjalikult juttu ühes hilisemas peatükis.

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
``if``-lause kasutamisel on vaja pöörata tähelepanu tühikutele -- tühikutega joondamine e. *treppimine* määrab, millised käsud kuuluvad tingimuslause alla ja millised mitte. Antud näites on mõlemas tingimuslause *harus* vaid üks käsk, aga neid võib seal olla ka rohkem:

.. sourcecode:: py3

    nimi = input("Mis su nimi on? ")
    if nimi == "Imelik":
        print("Tõesti?")
        print("Imelik nimi!")
    else:
        print("Tere " + nimi + "!")

Edaspidi näeme, et treppimist kasutatakse ka teistes Pythoni konstruktsioonides ning põhimõte on alati selles, et sama kaugele joondatud read moodustavad mingi terviku. 

.. admonition:: NB!

    Trepitud plokile eelnev rida lõpeb alati kooloniga (see on Pythonile lisakinnituseks, et programmeerija soovib järgmisel real alustada trepitud plokki).

.. note::
    See, miks treppimist nimetatakse treppimiseks, selgub allpool, siis kui hakkame trepitud plokke üksteise sisse paigutama.

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

Korduslaused e. tsüklid
--------------------------

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

Siinkohal tulevad appi **tsüklid** (e. korduslaused), mis on programmikonstruktsioonid käskude kordamiseks. Selles peatükis vaatame **while-tsüklit**, mis kordab etteantud lauseid niikaua, kuni teatud tingimus kehtib. 


.. index:: 
    single: while tsükkel
    single: tsükkel; while tsükkel
    

``while``-tsükkel
~~~~~~~~~~~~~~~~~~~

``while``-tsükliga saaksime ruudu joonistamise programmi panna kirja järgnevalt:

.. sourcecode:: py3
    
    from turtle import *
    
    # selle muutuja abil peame arvet, mitu külge on juba joonistatud
    joonistatud_kylgi = 0               
    
    while joonistatud_kylgi < 4:
        forward(100)
        left(90)
        joonistatud_kylgi = joonistatud_kylgi + 1   # suurendame muutuja väärtust

    exitonclick()


``while``-lause keha täidetakse vaid siis kui päises antud tingimus kehtib. Kui kehas olevad laused on täidetud, siis minnakse uuesti päises näidatud tingimust kontrollima -- kui tingimus kehtib ikka veel, siis täidetakse kehas olevad laused uuesti jne. 

Selleks, et taoline tsükkel ei jääks lõputult tööle, peab tsükli kehas olema mingi lause, mis mõjutab tingimuse kehtivust -- antud näites on selleks lause, mis muudab muutuja ``joonistatud_kylgi`` väärtust 1 võrra suuremaks.

.. note::

    Muutujaid, mille väärtust suurendatakse igal tsükli sammul, nimetatakse *loenduriteks* ja nende nimeks pannakse tavaliselt ``i``. Selliseid tsükleid, kus korduste arv on tsükli alustamise hetkel teada, nimetatakse *määratud tsükliteks*.

.. topic:: Muutuja muutmine

    Nagu 2. peatükis mainitud, on võimalik Pythonis muutuja väärtust uue väärtusega üle kirjutada. Tsüklid ongi see koht, kus seda võimalust kõige sagedamini tarvis läheb.
    
    Muutuja väärtuse suurendamiseks kirjutasime eelnevas näites ``joonistatud_kylgi = joonistatud_kylgi + 1``, st. ``joonistatud_kylgi`` uueks väärtuseks sai ``joonistatud_kylgi`` hetkeväärtus + 1. Sellist suurendamist mingi arvu võrra saab Pythonis ka lühemalt kirjutada: ``joonistatud_kylgi += 1``. Muutuja väärtuse vähendamiseks võib analoogselt kirjutada ``joonistatud_kylgi -= 1``.


.. note::

    Tegelikult on Pythonis olemas ka teine, natuke spetsiifilisem tsüklitüüp, mida nimetatakse ``for``-tsükliks ja mis sobib *n*-korduse tegemiseks isegi paremini, kui ``while``. ``for``-tsüklit vaatame järjendite peatükis.


Harjutus 3. Programm *n*-nurga joonistamiseks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Kirjutage eelmise näite põhjal programm, mis joonistab *n*-küljega hulknurga (*n* väärtus ja küljepikkus küsitakse kasutajalt). 

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

Siin peaks juba olema näha, miks programmiridade taandamist nimetatakse treppimiseks -- taandatud plokid taandatud plokkide sees moodustavad vasakult vaadates justkui trepiastmed.

.. note::

    Proovige järgi, kuidas Python käitub, kui unustate ``while`` või ``if`` lauses kasutada koolonit või jätate ära mõne taandrea. Sellega saate end taoliseks situatsiooniks juba ette valmistada.



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
Senistes näidetes kasvatasime igal kordusel loenduri väärtust 1 võrra. Nagu võib arvata, ei piira Python tegelikult, kuidas me muutuja väärtust suurendame või vähendame:

.. sourcecode:: py3

    n = int(input("Sisesta naturaalarv: "))
    
    summa = 0
    i = 0
    
    while i <= n:
        summa += i
        i += 1
    
    print(n, "esimese naturaalarvu summa on", summa)


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


Funktsioonid e. uute käskude loomine
-----------------------------------------
.. note::

    Siin on tegemist väga põgusa sissejuhatusega funktsioonide defineerimisest. Sellel teemal tuleb edaspidi palju rohkem juttu.
    
Oletame, et meil on vaja joonistada kilpkonnaga 3 ruutu, kõik küljepikkusega 30, aga nad peavad olema erinevates kohtades: esimene ruut ekraani keskel, teine üleval-paremal, kolmas üleval-vasakul ja teisest natuke allpool. Mitu rida läheks sellise programmi kirjutamiseks vaja? Kas programmi lühendamiseks oleks abi tsüklist, mis teeb 3 kordust ja joonistab igal kordusel ühe ruudu?

Kui see programm kirjutada "jõumeetodil", siis sisalduks programmis ruudu joonistamise kood kolmes kohas:

.. sourcecode:: py3

    from turtle import *

    küljepikkus = 30

    i = 0
    while i < 4:
        forward(küljepikkus)
        left(90)
        i += 1 

    up()
    forward(100)
    left(90)
    forward(100)
    down()

    i = 0
    while i < 4:
        forward(küljepikkus)
        left(90)
        i += 1 

    up()
    left(90)
    forward(200)
    down()

    i = 0
    while i < 4:
        forward(küljepikkus)
        left(90)
        i += 1 

    exitonclick()    

Lahendus oleks palju lihtsam, kui ruudu joonistamiseks oleks olemas eraldi käsk. ``turtle`` moodulis sellist käsku küll pole, aga õnneks võimaldab Python programmeerijal uusi käske e. *funktsioone* ise *defineerida*.

Funktsiooni defineerimine ja kasutamine
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Jätame hetkeks kilpkonna kõrvale ja vaatleme ühte väga lihtsat näidet funktsioonide defineerimisest. Järgnevas näiteprogrammis defineeritakse funktsioon nimega ``tere``:

.. sourcecode:: python

    def tere():
        print("Tere")
        print("Kuidas läheb?")

Esimest rida, mis algab ``def``-iga, nimetame funktsiooni **päiseks**, järgnevad read, mis on tühikutega paremale nihutatud, moodustavad funktsiooni **keha**. 

Proovige seda kolmerealist programmi käivitada. Kui kõik läks õigesti, ei ilmu ekraanile midagi. Nimelt on programmis antud juhul toodud vaid teatud tegevuse kirjeldus, kuid seal pole käsku seda (ega ühtegi teist) tegevust täita.

Sisuliselt me defineerisime uue käsu ``tere``, mille rakendamisel peab Python käivitama laused ``print("Tere")`` ja ``print("Kuidas läheb?")``. Kõik need "käsud", mida olete siiani kasutanud (nt. ``print`` ja ``sin``) on samuti kuskil funktsioonidena defineeritud. Edaspidi kasutame sõna `käsk` asemel põhiliselt sõna `funktsioon`. 

Nagu ikka, tuleb funktsiooni (käsu) kasutamiseks kirjutada selle nimi koos sulgudega e. programmeerijate kõnepruugis: funktsioon tuleb **välja kutsuda** (või *rakendada*). Proovige järgmist, täiendatud programmi:

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

    
Tavaliselt pannakse funktsioonidesse need laused, mida on vaja käivitada rohkem, kui ühel korral. Proovige programmi, kus funktsiooni ``tere`` on kaks korda välja kutsutud. Programmi käivitamisel peaks nüüd tulema kaks järjestikust tervitust.

.. note:: 

    Samamoodi nagu ``if`` ja ``while`` lausete puhul, on ka funktsiooni kehas ridade ees olevad tühikud olulised -- selle järgi saab Python aru, kus lõpeb funktsiooni definitsioon ja algavad järgmised laused. Selles veendumiseks kustutage ``print("Kuidas läheb?")`` rea eest tühikud ära ning proovige siis programmi uuesti käivitada. Miks ilmusid laused ekraanile sellises järjekorras?

Harjutus 11. Ruudu joonistamine
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Nüüd on paras aeg tulla tagasi selle teema alguses käsitletud probleemi juurde.
Kirjutage funktsioon ``ruut``, mis joonistaks kilpkonna abil ruudu (küljepikkusega 30).  Kasutage seda funktsiooni mitu korda, joonistades ruute erinevatesse kohtadesse.

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

    Kui kilpkonna rahulik tempo teid ärritab, siis andke talle käsk ``speed(10)``.


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

Lõpuks korraldage nii, et programm töötab õigesti ka siis, kui ühel (või mõlemal) vanemal on brutopalk maksuvabast miinimumist väiksem.

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

6. Kivi-paber-käärid
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

7. Raskem: Redeli asendid
~~~~~~~~~~~~~~~~~~~~~~~~~~
Ülesandeks on genereerida Pythoni kilpkonnaga joonistus, mis kujutab redelit (esitatud lihtsalt sirgjoonena) seina najal erinevate nurkade all. Joonistage redel kõigepealt horisontaalasendis ning seejärel mitmes asendis järjest suurema nurga all, kuni lõpuks jõuab redel vertikaalasendisse.

.. hint::

    Abiks võib olla ``turtle`` käsk ``back``, mis liigutab kilpkonna senise suunaga võrreldes tagurpidi. (Aga see pole ülesande lahendamiseks tingimata vajalik).

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

