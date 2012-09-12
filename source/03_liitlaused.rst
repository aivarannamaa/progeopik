3. Liitlaused
============================================

.. warning::

    Selle peatüki materjali veel täiendatakse


.. index::
    single: tingimuslaused
    single: tingimuslaused; if-lause

Kui eelmise peatüki teemad liigitasime "lihtlausete" kategooriatesse, siis nüüd vaatame, milliseid on Pythoni olulisimad "liitlaused", mille abil saab lihtlauseid erinevatesse seostesse paigutada.


Tingimuslause e. ``if``-lause
-------------------------------
Eelmise peatüki programmidega töötas Python täiesti "tuimalt" -- alustas esimesel real oleva lausega, iga rea täitmise järel võttis ette järgmise rea, kuni jõudis programmi lõppu. Taolisest lähenemisest piisab paraku vaid väga lihtsate ülesannete puhul -- enamasti tuleb programmil mingil hetkel teha valikuid, kas jätkata üht- või teistmoodi. Python võimaldab programmeerijal taolised dilemmad koos soovitud valikukriteeriumidega panna kirja **tingimuslause** e. ``if``-lause abil.

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

    Kuigi Pythoni on treppimise osas võrdlemisi paindlik, tuleks segaduste vältimiseks alati kasutada joondamiseks 4 tühikut. IDLE-s kirjutades võib treppimiseks vajutada ka TAB klahvi -- IDLE genereerib sellepeale TAB sümboli asemel 4 tühikut.
    Tegelikult pole enamasti vaja IDLE-s isegi TAB klahvi kasutada -- kui vajutada kooloniga lõppeval real uue rea saamiseks ENTER-it, taipab redaktor ise, et järgmine rida tuleb treppida ja lisab uue rea algusesse vajaliku arvu tühikuid. Ka järgmistele ridadele paneb IDLE usinalt tühikud ette. Andmaks märku, et uus rida enam tingimuse alla ei kuulu, tuleb need tühikud ära kustutada ja alustada käsu kirjutamist jälle ekraani vasakust servast.


Harjutus 5. Eristav kasutaja tervitamine 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Muutke ülesandes 2 kirjeldatud kasutaja tervitamise programmi selliselt, et kasutajat nimega `Margus` tervitatakse familiaarselt aga kõiki ülejäänuid tervitatakse formaalselt.


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

``while``-tsükliga saaksime ruudu joonistamise funktsiooni panna kirja järgnevalt:

.. sourcecode:: py3
    
    from turtle import *
    
    i = 0               # i näitab, mitu külge on juba joonistatud
    while i < 4:
        forward(100)
        left(90)
        i = i + 1       # suurendame i väärtust

    exitonclick()


``while``-lause keha täidetakse vaid siis kui päises antud tingimus kehtib. Kui kehas olevad laused on täidetud, siis minnakse uuesti päises näidatud tingimust kontrollima -- kui tingimus kehtib ikka veel, siis täidetakse kehas olevad laused uuesti jne. 

Selleks, et taoline tsükkel ei jääks lõputult tööle, peab tsükli kehas olema mingi lause, mis mõjutab tingimuse kehtivust -- antud näites on selleks lause, mis muudab muutuja ``i`` väärtust 1 võrra suuremaks. Muutujaid, mille väärtust suurendatakse igal tsükli sammul, nimetatakse *loenduriteks* ja nende nimeks pannakse tavaliselt ``i``. Selliseid tsükleid, kus korduste arv on tsükli alustamise hetkel teada, nimetatakse *määratud tsükliteks*.

.. topic:: Muutuja muutmine

    Nagu 2. peatükis mainitud, on võimalik Pythonis muutuja väärtust uue väärtusega üle kirjutada. Tsüklid ongi see koht, kus seda võimalust kõige sagedamini tarvis läheb.
    
    Muutuja väärtuse suurendamiseks kirjutasime eelnevas näites ``i = i + 1``, st. ``i`` uueks väärtuseks sai ``i`` hetkeväärtus + 1. Sellist suurendamist mingi arvu võrra saab Pythonis ka lühemalt kirjutada: ``i += 1``. Muutuja väärtuse vähendamiseks võib analoogselt kirjutada ``i -= 1``.


.. note::

    Tegelikult on Pythonis olemas ka teine, natuke spetsiifilisem tsüklitüüp, mida nimetatakse ``for``-tsükliks ja mis sobib *n*-korduse tegemiseks isegi paremini, kui ``while``. ``for``-tsüklit vaatame järjendite peatükis.


Harjutus 6. Funktsioon *n*-nurga joonistamiseks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Kirjutage eelmise näite põhjal funktsioon, mis joonistab *n*-küljega hulknurga. Funktsioonil peavad olema parameetrid nurkade arvu ning küljepikkuse määramiseks.

.. hint::
    Iga nurga juures peab kilpkonn pöörama 360/n kraadi.
    
Testige loodud funktsiooni joonistades üksteise kõrvale kolmnurga, ruudu ja viisnurga.


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


Harjutus x. Kolmeaastase lapse simulaator
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Kirjutage programm, mis küsib kasutajalt mingi küsimuse ja seejärel küsib iga sisestuse peale "Aga miks?" niikaua, kuni kasutaja sisestab mingi kindla "võlusõna".

Proovige kirjutada ka terapeudi variant, kus vahelduvad kaks erinevat küsimust.
    
.. hint::

    "Millest sa veel sooviksid rääkida?"
    
    "Milliseid tundeid see sinus tekitab?"


Harjutus 7. Algandmete kontrollimine tsükliga
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. todo:: Kontrolli viidatud ülesannet

Tsükleid saab kasutada algandmete sisestamise juures -- me võime vigase sisendi puhul lasta kasutajal sisestamist korrata niikaua, kuni oleme sistatud infoga rahul.

Modifitseerige 1. ülesande lahendust -- kui kasutaja poolt sisestatud tekst polnud numbriline, siis peaks programm kordama küsimist ja andmete sisselugemist niikaua, kuni kasutaja sisestab numbrilise teksti.

Alles siis, kui korrektne sisend on käes, tuleks väljastada sisestatud arvu ruut.

Harjutus 8. Täiendatud arvamismäng
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~    
Täiendage arvamismängu selliselt, et programm ütleb õige vastuse ära, kui kasutaja pole 10 arvamisega suutnud õiget pakkumist teha.

.. hint:: 
    
    Siin tuleks kombineerida loenduri kasutamine ning kasutaja pakkumise kontrollimine.


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
    

Tegelikult pole ``break`` lause hädavajalik - tsükli saab alati ümber kirjutada nii, et kõiki jätkamise/lõpetamise tingimusi kontrollitakse tsükli päises, aga vahel on ``break``-iga lahendus lihtsam.

Mõnikord on vaja tsükli lõpetamise tingimust kontrollida *ainult* tsükli kehas, sel juhul pannakse tsükli päisesse alati kehtiv tingimus ``True``. Järgnev programm küsib kasutajalt arve ja näitab nende ruute niikaua, kuni kasutaja sisestab *tühisõne* (st. vajutab ENTER ilma midagi tegelikult sisestamata):

.. sourcecode:: py3

    while True:
        tekst = input("Sisesta arv ja vajuta ENTER (lõpetamiseks vajuta ainult ENTER): ")
        
        if tekst.isnumeric():
            arv = int(tekst)
            print("Arvu ruut on: " + str(arv * arv))
        elif tekst == "":  
            print("OK, lõpetan")
            break
        else: # ei olnud ei arv ega tühisõne
            print("Vigane sisend, proovi uuesti!")

Harjutus 9. Juhuslikud arvud
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Kirjutage programm, mis väljastab iga ENTER vajutuse järel (st. tühisõne sisestamisel) ekraanile juhusliku täisarvu vahemikus 1..999. Tsükli töö tuleks lõpetada (kasutades ``break``-i) siis, kui kasutaja sisestab tühisõne asemel sõne ``'aitab'``.

Harjutus. Algandmete kontrollimine ja ``break``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Kirjutage algandmete kontrollimise ülesande lahendus ümber nii, et ``input`` käsku on programmis kasutatud vaid ühes kohas.

Lausete kombineerimine
----------------------------------------
.. todo:: for!

Tingimuslauseid võib kasutada näiteks ka ``for``-tsükli sees. Uurige ja seejärel katsetage järgmist programmi:

.. sourcecode:: py3

    f = open('nimed.txt')
    
    for nimi in f:
        if nimi.strip() == 'Margus':  # strip eemaldab reavahetuse sümboli
            print('Hommik!')
            print('Kuis kulgeb?')
        else:
            print('Tervist, lugupeetud ' + nimi.strip() + '!')
    
    f.close()

.. note::

    Proovige järgi, kuidas Python käitub, kui unustate ``for`` või ``if`` lauses kasutada koolonit või jätate ära mõne taandrea. Sellega saate end taoliseks situatsiooniks juba ette valmistada.

.. index::
    single: veaotsing
    
.. topic:: Veaotsingust

    Selle näite tingimuses kasutasime ``strip`` meetodit seepärast, et failist ridade lugemisel jäetakse rea lõppu ka reavahetuse sümbol. Selline nüanss aga ei pruugi alati meelde tulla ja sel juhul programm lihtsalt ei tööta õieti.
    
    Kui tekib selline situatsioon, kus programm, ei tööta nii nagu te soovite, siis võiks kõigepealt uurida, kas sisendandmed loeti sisse selliselt nagu te arvasite. Antud programmis võiks ``for``-tsüklis esimese asjana (enne tingimuslauset) kuvada ekraanile loetud nime. Selleks, et oleks näha ka tühikute ning reavahetuste paiknemine, võib kuvamist teha nt. selliselt: ``print('>' + nimi + '<')``.

.. topic:: Etteruttavalt:

    Tingimuslause sisse võib panna veel teisi tingimuslauseid või tsükleid (mille sees võib omakorda olla tingimuslauseid ja tsükleid jne.) Lisaks on võimalik tingimusi omavahel kombineerida kasutades operaatoreid ``and`` ja ``or``. Nende teemadega tegeleme põhjalikult peatükis `Tingimuslaused`.
 
Funktsioonid e. uute käskude loomine
-----------------------------------------
Oletame, et meil on vaja joonistada kilpkonnaga 3 ruutu, kõik küljepikkusega 30, aga nad peavad olema erinevates kohtades: esimese ruudu vasak-ülemine nurk koordinaatidel (0,0), teisel (50,20), kolmandal (130,85). Mitu rida läheks sellise programmi kirjutamiseks vaja? Kas programmi lühendamiseks oleks abi tsüklist, mis teeb 3 kordust ja joonistab igal kordusel ühe ruudu?

Kui see programm kirjutada "jõumeetodil", siis sisalduks programmis kolm identset plokki:

.. todo:: näide

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
    
    tere() # funktsiooni väljakutse e. rakendamine

.. note::

    Antud näites on nii funktsiooni definitsioonis, kui ka väljakutses kirjutatud tühjad sulud, kuna see funktsioon *ei võta argumente*. Argumentidega funktsioonidest tuleb juttu alamprogrammide peatükis.

.. note::

    Selles peatükis kirjutame funktsiooni definitsiooni koos väljakutse(te)ga samasse faili. Edaspidi vaatame ka varianti, kus funktsioonide definitsioonide jaoks luuakse eraldi fail.
    
Tavaliselt pannakse funktsioonidesse need laused, mida on vaja käivitada rohkem, kui ühel korral. Proovige programmi, kus funktsiooni ``tere`` on kaks korda välja kutsutud. Programmi käivitamisel peaks nüüd tulema kaks järjestikust tervitust.

.. note:: 

    Samamoodi nagu ``if`` ja ``while`` lausete puhul, on ka funktsiooni kehas ridade ees olevad tühikud olulised -- selle järgi saab Python aru, kus lõpeb funktsiooni definitsioon ja algavad järgmised laused. Selles veendumiseks kustutage ``print("Kuidas läheb?")`` rea eest tühikud ära ning proovige siis programmi uuesti käivitada. Miks ilmusid laused ekraanile sellises järjekorras?

Harjutus ?. Ruudu joonistamine
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Nüüd on paras aeg tulla tagasi selle teema alguses käsitletud probleemi juurde. Kirjutage funktsioon ``ruut()``, mis joonistaks kilpkonna abil ruudu (küljepikkusega 30).  Kasutage seda funktsiooni mitu korda, joonistades ruute erinevatesse kohtadesse.

.. hint:: 

    Tuletage meelde, mida tegid kilpkonna käsud ``up()`` ja ``down()``
    
.. hint::

    Kui kilpkonna rahulik tempo teid ärritab, siis andke talle käsk ``speed(10)``.


Harjutus ?. Tingimuslause kasutamine funktsioonis
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Funktsiooni kehas saab kasutada suvalist tüüpi lauseid, st. ka tingimuslauset ja korduslauset (või ka nende kombinatsiooni, ükskõik kui keerulist). 

.. todo:: ülesanne

Harjutus ?. Korduslause kasutamine funktsioonis
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Kirjutage mingi funktsioon, mille kehas oleks kasutatud korduslauset. 



Ülesanded
-------------------
1. Paaris või paaritu
~~~~~~~~~~~~~~~~~~~~~
Koostage tekstifail, mis sisaldab täisarve erinevatel ridadel. Kirjutage programm, mis loeb antud failist ükshaaval arve ning kuvab iga arvu kohta ekraanile info, kas tegemist oli paaris või paaritu arvuga.

2. Pere sissetulek
~~~~~~~~~~~~~~~~~~
Kirjutage programm, mis küsib isa brutopalga, ema brutopalga ning alaealiste laste arvu ja arvutab selle põhjal pere kuusissetuleku. (Oletame, et iga alaealise lapse kohta makstakse toetust 20€ kuus.) 

Esialgu võite eeldada, et mõlema vanema kuupalk on vähemalt sama suur kui maksuvaba miinimum.

Lõpuks korraldage nii, et programm töötab õigesti ka siis, kui ühel (või mõlemal) vanemal on brutopalk maksuvabast miinimumist väiksem.

3. Busside logistika
~~~~~~~~~~~~~~~~~~~~~
Olgu meil vaja transportida teatud arv inimesi bussidega, milles on teatud arv kohti. Mitu bussi on vaja selleks, et kõik inimesed kohale saaksid ja mitu inimest on viimases bussis (eeldusel, et eelmised on kõik täiesti täis)? Kirjutage programm, mis küsib inimeste arvu ja busside suuruse ning lahendab seejärel selle ülesande. 

.. note::
    Võib tunduda, et selle ülesande jaoks läheb tarvis tingimuslauset, aga tegelikult on võimalik see lahendada ka lihtsamalt. Vihje: abiks võivad olla ``//``, ``%``, ``floor`` või ``ceil``, valige neist selle ülesande jaoks sobivad.
    
**Testige** oma programmi muuhulgas järgmiste algandmetega:

* inimeste arv: 60, kohtade arv: 40
* inimeste arv: 80, kohtade arv: 40
* inimeste arv: 20, kohtade arv: 40
* inimeste arv: 40, kohtade arv: 40

Üritage mõista, miks valiti taolised testiandmed.



Lisalugemine
-----------------
Veaotsingust
~~~~~~~~~~~~~~
.. todo:: 
    selgita
    http://openbookproject.net/thinkcs/python/english3e/app_a.html