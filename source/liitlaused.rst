III. Liitlaused
============================================

.. todo::

    Siia tuleks peatükkidest "kontrollvoog" ja "alamprogrammid" ümber tõsta Pythoni vastavate konstruktsioonide tutvustus ja lihtsamad ülesanded.
    

.. index::
    single: tingimuslaused
    single: tingimuslaused; if-lause

Kui eelmise peatüki teemad liigitasime "lihtlausete" kategooriatesse, siis nüüd vaatame, milliseid on Pythoni olulisimad "liitlaused", mille abil saab lihtlauseid erinevatesse seostesse paigutada.


Tingimuslause
--------------
Eelmise peatüki programmidega töötas Python täiesti "tuimalt" -- alustas esimesel real oleva käsuga, iga rea täitmise järel võttis ette järgmise rea, kuni jõudis programmi lõppu. Taolisest lähenemisest piisab paraku vaid väga lihtsate ülesannete puhul -- enamasti tuleb programmil mingil hetkel teha situatsioonist sõltuvalt valikuid, kas jätkata üht- või teistmoodi. Python võimaldab programmeerijal taolised dilemmad koos soovitud valikukriteeriumidega panna kirja **tingimuslause** e. ``if``-lause abil.

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

``if``-lause kasutamisel on vaja pöörata tähelepanu tühikutele -- tühikutega joondamine e. *treppimine* määrab, millised käsud kuuluvad tingimuslause alla ja millised mitte. Antud näites on mõlemas tingimuslause *harus* vaid üks käsk, aga neid võib seal olla ka rohkem. Samuti tuleb jälgida, et nii tingimuse rida, kui ka ``else`` rida lõpeks kooloniga.

.. note::

    Kuigi Pythoni on treppimise osas võrdlemisi paindlik, tuleks segaduste vältimiseks alati kasutada joondamiseks 4 tühikut. IDLE-s kirjutades võib treppimiseks vajutada ka TAB klahvi -- IDLE genereerib sellepeale TAB sümboli asemel 4 tühikut.
    Tegelikult pole enamasti vaja IDLE-s isegi TAB klahvi kasutada -- kui vajutada kooloniga lõppeval real uue rea saamiseks ENTER-it, taipab redaktor ise, et järgmine rida tuleb treppida ja lisab uue rea algusesse vajaliku arvu tühikuid. Ka järgmistele ridadele paneb IDLE usinalt tühikud ette. Andmaks märku, et uus rida enam tingimuse alla ei kuulu, tuleb need tühikud ära kustutada ja alustada käsu kirjutamist jälle ekraani vasakust servast.

Tingimuslause *päises* (st. ``if``-iga algaval real) saab tingimusi moodustada järgmiste operaatoritega: 

* ``<``, ``>``, ``<=``, ``>=`` sobivad arvude võrdlemiseks
* Topeltvõrdusmärk (``==``) tähistab võrdsust nii arvude kui sõnede puhul
* ``!=`` tähistab mittevõrdsust nii arvude kui sõnede puhul

.. note::
    
    Ärge unustage, et üksikut võrdusmärki (``=``) kasutatakse Pythonis muutujale väärtuse omistamiseks, seetõttu on võrdsuse kontrollimiseks ette nähtud topeltvõrdusmärk (``==``).


Ülesanne 5. Eristav kasutaja tervitamine 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Muutke ülesandes 2 kirjeldatud kasutaja tervitamise programmi selliselt, et kasutajat nimega `Margus` tervitatakse familiaarselt aga kõiki ülejäänuid tervitatakse formaalselt.


.. index:: 
    single: tsükkel

Tsüklid
-----------

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

Siinkohal tulevad appi **tsüklid** (e. korduslaused), mis on programmikonstruktsioonid käskude kordamiseks. Selles praktikumis vaatame **while-tsüklit**, mis kordab etteantud lauseid niikaua, kuni etteantud tingimus kehtib. 


.. index:: 
    single: while tsükkel
    single: tsükkel; while tsükkel
    

``while``-tsükkel
-----------------

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

    Nagu 2. praktikumis mainitud, on võimalik Pythonis muutuja väärtust uue väärtusega üle kirjutada. Tsüklid ongi see koht, kus seda võimalust kõige sagedamini tarvis läheb.
    
    Muutuja väärtuse suurendamiseks kirjutasime eelnevas näites ``i = i + 1``, st. ``i`` uueks väärtuseks sai ``i`` hetkeväärtus + 1. Sellist suurendamist mingi arvu võrra saab Pythonis ka lühemalt kirjutada: ``i += 1``. Muutuja väärtuse vähendamiseks võib analoogselt kirjutada ``i -= 1``.


.. todo::

    Programm, mis kordab "Ütle 'Palun!'", kuni kasutaja selle lõpuks sisestab

.. note::

    Tegelikult on Pythonis olemas ka teine, natuke spetsiifilisem tsüklitüüp, mida nimetatakse ``for``-tsükliks ja mis sobib *n*-korduse tegemiseks isegi paremini, kui ``while``. ``for``-tsüklit vaatame järgmises praktikumis.



Tsükli ja tingimuslause kombineerimine
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Tingimuslauseid võib kasutada näiteks ka ``for``-tsükli sees. Uurige ja seejärel katsetage järgmist programmi:

.. sourcecode:: py3

    f = open('nimed.txt')
    
    for nimi in f:
        if nimi.strip() == 'Margus':  # strip eemaldab reavahetuse
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

    Tingimuslause sisse võib panna veel teisi tingimuslauseid või tsükleid (mille sees võib omakorda olla tingimuslauseid ja tsükleid jne.) Lisaks on võimalik tingimusi omavahel kombineerida kasutades operaatoreid ``and`` ja ``or``. Nende teemadega tegeleme põhjalikult 4. praktikumis.
 
Funktsioonid e. uute käskude loomine
-----------------------------------------
Oletame, et meil on vaja joonistada kilpkonnaga 3 ruutu, kõik küljepikkusega 30, aga nad peavad olema erinevates kohtades: esimese ruudu vasak-ülemine nurk koordinaatidel (0,0), teisel (50,20), kolmandal (130,85). Mitu rida läheks sellise programmi kirjutamiseks vaja? Kas programmi lühendamiseks oleks abi tsüklist, mis teeb 3 kordust ja joonistab igal kordusel ühe ruudu?

Kui see programm kirjutada "jõumeetodil", siis sisalduks programmis kolm identset plokki:

.. todo:: näide

.. todo:: tee ruudu ülesanne näiteks ja tere näide ülesandeks

Funktsiooni defineerimine ja kasutamine
---------------------------------------
Järgnevas näiteprogrammis **defineeritakse** funktsioon nimega ``tere``:

.. sourcecode:: python

    def tere():
        print("Tere")
        print("Kuidas läheb?")

Esimest rida, mis algab ``def``-iga, nimetame funktsiooni **päiseks**, järgnevad read, mis on tühikutega paremale nihutatud, moodustavad funktsiooni **keha**. 

.. note::
    
    Tühikute kasutamisel tuleb olla täpne. Soovitav on kasutada funktsiooni keha joondamiseks alati 4 tühikut, aga põhitingimuseks on praegu see, et iga rida funktsiooni kehas on joondatud sama kaugele.
    
Proovige seda käivitada. Kui kõik läks õigesti, ei ilmu ekraanile midagi. Nimelt on programmis antud juhul toodud vaid ühe tegevuse kirjeldus, kuid seal pole käsku seda (ega ühtegi teist) tegevust täita.

Sisuliselt me defineerisime uue käsu ``tere``, mille saamisel peab Python käivitama laused ``print("Tere")`` ja ``print("Kuidas läheb?")``. Kõik need "käsud", mida olete siiani kasutanud (nt. ``print`` ja ``sin``) on samuti kuskil defineeritud alamprogrammide e. funktsioonidena. Edaspidi kasutame sõna `käsk` asemel põhiliselt sõna `funktsioon`. 

Nagu ikka, tuleb funktsiooni (käsu) kasutamiseks kirjutada selle nimi koos sulgudega (antud juhul on sulud tühjad, kuna see funktsioon ei võta argumente). Programmeerijate kõnepruugis: funktsioon tuleb **välja kutsuda** (või *rakendada*). Proovige järgmist, täiendatud programmi:

.. sourcecode:: python

    def tere():
        print("Tere")
        print("Kuidas läheb?")
    
    tere() # funktsiooni väljakutse e. rakendamine e. aplikatsioon

.. note::

    Selle praktikumi põhiosas kirjutame funktsiooni definitsiooni koos väljakutse(te)ga samasse faili.
    
Tavaliselt pannakse alamprogrammidesse need laused, mida on vaja käivitada rohkem, kui ühel korral. Proovige programmi, kus funktsiooni ``tere`` on kaks korda välja kutsutud. Programmi käivitamisel peaks nüüd tulema kaks järjestikust tervitust.

.. note:: 

    Nagu eespool mainitud, funktsiooni kehas on ridade ees olevad tühikud olulised, selle järgi saab Python aru, kus lõpeb funktsiooni definitsioon ja algavad järgmised laused. Selles veendumiseks kustutage ``print("Kuidas läheb?")`` rea eest tühikud ära ning proovige siis programmi uuesti käivitada.

Ülesanne 1. Ruudu joonistamine
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Ka selles praktikumis kasutame meile juba varem tuttavat kilpkonna. Kirjutage funktsioon ``ruut()``, mis joonistaks kilpkonna abil ruudu (küljepikkusega 100).  Kasutage seda funktsiooni mitu korda, joonistades mitu ruutu erinevatesse kohtadesse.

.. hint:: 

    Tuletage meelde, mida tegid kilpkonna käsud ``up()`` ja ``down()``
    
.. hint::

    Kui kilpkonna rahulik tempo teid ärritab, siis andke talle käsk ``speed(10)``.

.. index::
    single: parameetrid; funktsiooni parameetrid
    single: funktsioon; parameetrid





Parameetritega funktsioonid
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. todo::

   selgita, miks olid eelmise näites tühjad sulud

Täpselt sama tegevuse kordamist on tegelikult vaja siiski üpris harva. Pigem on tarvis teha midagi sarnast, kuid mitte päris identset. Näiteks võib olla vaja anda isikustatud tervitus, mis sisaldab ka tervitatava nime, mis on aga iga kord erinev. Seda saab teha, kasutades alamprogrammi **parameetreid**:

.. sourcecode:: python

    def tere(nimi):
        print("Tere " + nimi)
        print("Kuidas läheb?")
        
    tere("Kalle")
    tere("Malle")
    
Selles näites on funktsioonil ``tere`` parameeter nimega "nimi". Parameetri näol on sisuliselt tegu *muutujaga*, mille väärtus antakse ette funktsiooni väljakutsel. Konkreetsed väärtused kirjutatakse väljakutsel funktsiooni nime järel olevatesse sulgudesse. Antud juhul on parameetri väärtuseks esimesel väljakutsel "Kalle" ning teisel väljakutsel "Malle". Funktsioon töötab aga mõlemal juhul samamoodi – ta võtab parameetri väärtuse ning lisab selle tervitusele. Kuna aga väärtused on kahel juhul erinevad, on ka tulemus erinev.


.. index::
    single: funktsioon; argumendid
    single: argumendid; funktsiooni argumendid

.. topic:: Terminoloogia: Parameetrid vs. argumendid

    Koos parameetritega räägitakse enamasti ka **argumentidest**. Argumendiks nimetakse funktsiooni väljakutses sulgudes antud avaldise väärtust, millest saab vastava parameetri väärtus. Parameetrid on seotud funktsiooni definitsiooniga, argumendid on seotud funktsiooni väljakutsega. Meie viimases näites on ``nimi`` funktsiooni ``tere`` `parameeter`, aga sõneliteraal ``"Kalle"`` on vastav `argument` funktsiooni väljakutses.

    `Parameetri` vs. `argumendi` asemel võite mõnikord kohata ka väljendeid `formaalne parameeter` vs. `tegelik parameeter`.  



Ülesanne 2. Parameetriseeritud ``ruut``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Täiustage eespool mainitud ruudu joonistamise funktsiooni nii, et ruudu küljepikkuse saab määrata funktsiooni väljakutsel. Kasutage loodud funktsiooni, joonistades mitu erineva suurusega ruutu.
    
    
Mitu parameetrit
~~~~~~~~~~~~~~~~
Parameetreid (ja vastavaid argumente) võib olla ka rohkem kui üks. Proovige näiteks järgmist programmi:

.. sourcecode:: python

    def tere(nimi, aeg):
        print("Tere, " + nimi)
        print("Pole sind juba " + str(aeg) + " päeva näinud")
	
    tere("Kalle", 3)

Nagu näete, tuleb funktsiooni väljakutsel argumendid anda samas järjekorras nagu on vastavad  parameetrid funktsiooni definitsioonis. Teisisõnu, argumendi *positsioon* määrab, millisele parameetrile tema väärtus omistatakse.

.. note::

    Mõnede funktsioonide puhul on ühe parameetri väärtus tavaliselt sama ja seda on vaja vaid harvadel juhtudel muuta. Sellisel juhul on võimalik see "tavaline" väärtus funktsiooni definitsioonis ära mainida. Kui funktsiooni väljakutsel sellele parameetrile väärtust ei anta, kasutatakse lihtsalt seda vaikeväärtust. Seda võimalust demonstreerime eelmise näite modifikatsiooniga:

    .. sourcecode:: python

        def tere(nimi, aeg = "mitu"):
            print("Tere, " + nimi)
            print("Pole sind juba " + str(aeg) + " päeva näinud")
        
        tere("Kalle", 3)
        tere("Malle")
    
    Eelmises praktikumis juba nägime, et funktsioonil ``print`` on lisaks põhiparameetrile veel parameeter nimega `end`, millele on antud vaikeväärtus ``"\n"`` (so. reavahetus). See on põhjus, miks ``print`` vaikimisi kuvab teksti koos reavahetusega. Kuna selle funktsiooni definitsioonis kasutatakse Pythoni keerulisemaid võimalusi, siis ``print``-i väljakutsel ei olegi võimalik `end` väärtust määrata ilma parameetri nime mainimata, st. seda ei saa anda positsiooniliselt.

Ülesanne 3. Värviline ruut
~~~~~~~~~~~~~~~~~~~~~~~~~~
Kilpkonna "pliiatsi" värvi saab muuta funktsiooniga ``color``, andes sellele argumendiks sõne ingliskeelse värvinimega, nt. ``color('red')``. Peale seda teeb kilpkonn järgmised jooned nõutud värviga. 

.. note::

    Soovi korral vaadake täpsemat infot siit:
    http://docs.python.org/py3k/library/turtle.html#turtle.color

Lisage funktsioonile ``ruut`` uus parameeter joone värvi määramiseks. Katsetage.


Väärtusega funktsioonid
--------------------------
Pere sissetuleku ülesandes kordasite tõenäoliselt netopalga arvutamise valemit kahes kohas -- ema ja isa netopalga arvutamisel. (Kui teil jäi see ülesanne tegemata, siis on väga soovitav see praegu, enne edasi lugemist ära teha). Edasise arutelu illustreerimiseks toome siin ära mainitud ülesande ühe võimaliku lahenduse:

.. sourcecode:: py3

    # TODO

Siin polnud õnneks tegemist eriti keerulise valemiga ning copy-paste'ga oli võimalik topelt tippimise vaeva vältida. Aga kui netopalga arvutamise valem peaks muutuma, siis peab olema meeles programmi muuta kõigis kohtades, kus seda valemit on kasutatud. 

Ilmselt juba aimate, et taolise kordamise vältimiseks on jälle abiks funktsioonid -- netopalga arvutamiseks tuleb defineerida uus funktsioon (nt. nimega ``neto``), valem tuleb kirja panna selle funktsiooni kehas, ning edaspidi tuleb netopalga arvutamiseks kasutada uut funktsiooni. Kuidas aga saada funktsiooni käest vastust kätte? Võib proovida muutujatega, aga kuna antud programmi puhul tuleb ühel juhul salvestatakse tulemus muutujasse ``isa_sissetulek`` ja teisel juhul muutujasse ``ema_sissetulek``, siis pole selge, millist muutujat kasutada. Mis teha siis, kui mõnikord on tarvis tulemus kohe ekraanile näidata ja muutujat polegi tarvis?

Taolisel juhul tuleb appi ``return`` käsk, mis on mõeldud justnimelt funktsioonist vastuse välja andmiseks, ilma, et programmeerija peaks funktsiooni defineerimisel täpsustama, kuhu see vastus peab jõudma:

.. sourcecode:: py3

    # TODO

Kogu real nr. X tehtavat toimingut nimetame *tagastamiseks* ja ``return`` järel oleva avaldise väärtust nimetame *tagastusväärtuseks*. Tagastusväärtusega funktsiooni võib nimetada ka lihtsalt *väärtusega funktsiooniks*. Kui funktsiooni tagastusväärtus on arvutüüpi, siis saab seda funktsiooni kasutada igal pool, kus läheb vaja arvu (nt. matemaatilises avaldises), kui tagastusväärtus on sõnetüüpi, siis võib seda funktsiooni kasutada igal pool, kus läheb vaja sõne jne. Seda demonstreerib veidi muudetud versioon vaadeldavast programmist:

.. sourcecode:: py3

    # TODO



.. topic:: Protseduurid vs funktsioonid 

    Võibolla juba märkasite, et ülalpool defineeritud funktsioon ``ruut`` on oma olemuselt ja otstarbelt üpriski erinev nendest funktsioonidest, millest räägitakse matemaatikas. ``ruut`` ja ``tere`` kirjeldavad mingit *tegevust* (vastavalt ekraanile ruudu joonistamine või kasutajaga suhtlemine), seevastu näiteks matemaatiline siinusfunktsioon (või ``sin``, nagu teda Pythonis nimetatakse) meenutab pigem mingit aritmeetilist tehet, mis genereerib *vastuse* vastavalt etteantud argumendile.
