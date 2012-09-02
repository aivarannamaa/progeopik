VII. Järjendid ja ``for``-tsükkel
=================================
Meie senistes programmides on iga andmejupp kuskil eraldi ära mainitud (nt. muutujana). Kui mõelda reaalsete programmide peale (nt. firma raamatupidamissüsteem), siis üldjuhul ei ole võimalik kõiki asjassepuutuvaid objekte (nt. töötajad või arved) programmis üksikult ära mainida, kuna selliste objektide hulk pole piiratud.

Selles praktikumis õpite, kuidas käsitleda mitut objekti ühe kogumina ning mida taolise kogumiga Pythonis teha saab.

Järjendid
---------
Järjend (ing.k. *list*) on andmetüüp loetelude esitamiseks. Järjendi loomiseks on kõige lihtsam viis kirjutada järjendisse kuuluvad väärtused (e. järjendi *elemendid*) komadega eraldatult nurksulgude vahele: 

.. sourcecode:: py3

    pikad_kuud = [1, 3, 5, 7, 8, 10, 12]
    linnad = ['Tartu', 'Tallinn', 'Põltsamaa']
    
Me salvestasime muutujasse ``pikad_kuud`` ühe arvujärjendi (31-päevaliste kuude numbrid) ning muutujasse ``linnad`` ühe sõnejärjendi 3 sõnega.

TODO: skeem, kus järjendi elemendid on nummerdatud kastikesed

Operatsioonid järjenditega
~~~~~~~~~~~~~~~~~~~~~~~~~~
Kui me oleme järjendi kirja pannud, siis tekib loomulikult küsimus, mida sellega teha saab? Mõningaid põhioperatsioone demonstreerib järgnev programm:

.. sourcecode:: py3
    
    # järjendi loomine
    pikad_kuud = [1, 3, 5, 7, 8, 10, 12]
    
    # järjendit võib lihtsalt ekraanile kuvada
    print(pikad_kuud)
    
    # elementide arvu (e. järjendi pikkuse) leidmine
    arv = len(pikad_kuud)
    print('Aastas on ' + str(arv) + ' pikka kuud')
    
    # järjendisse kuulumise kontroll
    if 2 in pikad_kuud:
        print("Veebruar kuulub pikkade kuude hulka")
    else:
        print("Veebruar ei kuulu pikkade kuude hulka")

    # ühe elemendi väärtuse küsimine järjekorranumbri järgi
    # NB! järjekorranumbrid algavad 0-st!
    esimene_pikk_kuu = pikad_kuud[0]
    teine_pikk_kuu = pikad_kuud[1]
    print("Esimene pikk kuu on " + str(esimene_pikk_kuu) \
        + ", teine pikk kuu on " + str(teine_pikk_kuu))

Ilmselt märkasite kahte operatsiooni (``len`` ja ``in``), mida olete juba kasutanud sõnede puhul. Kuna sõnet saab vaadelda kui sümbolite järjendit, siis ongi Pythonis korraldatud nii, et paljud järjendioperatsioonid toimivad ka sõnedega.

Järgnev tabel demonstreerib olulisimaid järjendioperatsioone:

+----------------------------+------------------+---------------------------------+
| Avaldis                    | Väärtus          | Kommentaar                      |
+============================+==================+=================================+
| ``len([2, 1, 3, 16])``     | ``4``            | Elementide arv                  |
+----------------------------+------------------+---------------------------------+
| ``min([2, 1, 3])``         | ``1``            | Minimaalne element              |
+----------------------------+------------------+---------------------------------+
| ``max([2, 1, 3])``         | ``3``            | Maksimaalne element             |
+----------------------------+------------------+---------------------------------+
| ``sum([2, 1, 3])``         | ``6``            | Elementide summa                |
+----------------------------+------------------+---------------------------------+
| ``sorted([2, 1, 3])``      | ``[1, 2, 3]``    | Tagastab järjestatud järjendi   |
+----------------------------+------------------+---------------------------------+
| ``3 in [2, 1, 3]``         | ``True``         | Elemendi sisaldumine järjendis  |
+----------------------------+------------------+---------------------------------+
| ``[2, 1] + [3, 1]``        | ``[2, 1, 3, 1]`` | Järjendite liitmine             |
+----------------------------+------------------+---------------------------------+
| ``[2, 1, 3, 1].count(1)``  | ``2``            | Elemendi esinemiste arv         |
+----------------------------+------------------+---------------------------------+
| ``[1, 2] == [2, 1]``       | ``False``        | Elementide järjekord loeb       |
+----------------------------+------------------+---------------------------------+


NB! Nagu viimastest ridadest selgub, võib järjendis olla korduvaid väärtusi, ning elementide järjekord on oluline.
    
Ülesanne 1. Järjendiavaldiste kasutamine
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Olgu meil defineeritud järgnevad järjendimuutujad:

    * ``a = [2, 3, 1, 5]``
    * ``b = [6, 4]``

Koostage muutujaid ``a`` ja ``b`` ning järjendioperatsioone kasutades avaldis, mille väärtuseks oleks järjend ``[1, 2, 3, 4, 5, 6]``.


Järjendi elementide küsimine e. indekseerimine
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Nagu esimeses näites juba mainitud, võimaldab Python küsida järjendimuutujast mingil konkreetsel positsioonil olevat elementi, kirjutades järjendi nime taga olevatesse nurksulgudesse soovitud elemendi positsiooni e. **indeksi** :

.. sourcecode:: py3
    
    pikad_kuud = [1, 3, 5, 7, 8, 10, 12]

    # küsi elemente indeksi järgi
    esimene_pikk_kuu = pikad_kuud[0] 
    teine_pikk_kuu = pikad_kuud[1]
    
    print("Esimene pikk kuu on " + str(esimene_pikk_kuu) \
        + ", teine pikk kuu on " + str(teine_pikk_kuu))

Ilmselt on pisut ootamatu aga see, et esimest positsiooni ei tähista mitte number ``1`` vaid ``0``, st. elementide nummerdamine algab 0-st. Selle omapäraga tuleb **indekseerimisel** (st. indeksi järgi elementide küsimisel) alati arvestada.

.. topic:: Miks alustatakse järjendi elementide nummerdamist 0-st? 

    Vanemates programmeerimiskeeltes oli taoline valik tingitud järjendite esitusviisist arvuti mälus. Teine põhjus on selles, et nii saab mõningaid keerulisemaid indekseerimisavaldisi veidi lühemalt kirja panna. Kolmas ja kõige olulisem põhus on see, et enamikus programmeerimiskeeltes on sedasi koguaeg tehtud ning väga paljud programmeerijad on harjunud taolise nummerdamisega. 
    
NB! indeksiks võime kasutada ka mingit täisarvulist muutujat. Seetõttu, kui kombineerime indekseerimise ``while``-tsükliga, siis saame iga järjendi elemendi ükshaaval ette võtta ja sellega midagi teha (nt. ekraanile kuvada):

.. sourcecode:: py3

    linnad = ['Tartu', 'Tallinn', 'Põltsamaa']
    
    i = 0
    while i < len(linnad):
        print("Linn indeksiga " + str(i) + " on " + linnad[i])
        i += 1

Sellel teemal me praegu pikemalt ei peatu, sest tuleb välja, et elementide ükshaaval läbivaatamiseks on olemas parem võimalus kui ``while`` tsükkel ja indekseerimine.


``for``-tsükkel
---------------
Lisaks ``while``-tsüklile on Pythonis veel üks tsüklitüüp -- ``for``-tsükkel, mis on oma olemuselt väga tihedalt seotud järjenditega.

Käivitage järgnev näiteprogramm, mis koosneb ühest lihtsast ``for``-tsüklist:

.. sourcecode:: py3

    for linn in ["Tartu", "Tallinn", "Põltsamaa"]:
        print(linn)

Nagu näete, sarnaneb ``for``-tsükkel kuju poolest ``while``-tsüklile -- esimesel real on *päis*, mis määrab korduste korralduse ning edasi tuleb taandreaga esitatud *keha*, mis sisaldab lauseid, mida igal kordusel käivitatakse.

``for``-tsükli kordused põhinevad mingil etteantud järjendil -- antud näites on selleks kolme linna nimest koosnev järjend. Igal kordusel küsitakse järjendist üks element, salvestatakse tema väärtus *tsüklimuutujasse* (antud näites ``linn``) ning seejärel käivitatakse tsükli kehas olevad laused. Elemente loetakse järjendist järjekorras, st. esimesel kordusel esimene element jne. Kui kõik elemendid on sedasi läbi käidud, siis on tsükli töö tehtud -- seega käivitatakse tsükli keha niipalju kordi kui on järjendis elemente.

Järjendite töötlemine
---------------------
Paljude ülesannete puhul on vaja antud järjend elementhaaval läbi vaadata ning koguda sealjuures mingit infot. Järgnevas näites on defineeritud funktsioon, mis leiab etteantud arvujärjendi elementide hulgast suurima:

.. sourcecode:: py3

    def suurim_element(arvud):
        # alustuseks oletame, et esimene element on suurim
        seni_suurim = arvud[0]
        
        # hakkame järjendit läbi vaatama
        # kui leiame seni leitust veel suurema, siis uuendame muutuja väärtust
        for arv in arvud:
            if arv > seni_suurim:
                seni_suurim = arv
        
        # kui kõik arvud on läbi vaadatud, siis ongi abimuutujasse jäänud õige vastus
        return seni_suurim
    
    # Katsetame seda funktsiooni.
    # Nagu näha, järjendit, nagu iga teist väärtust, saab anda argumendiks
    s = suurim_element([8, 45, 12, 331, 123])
    
    print("Suurim element on " + str(s))

Sellise töötlemise juures kasutatakse enamasti abimuutujat, mida nimetatakse *akumulaatoriks* ja millesse kogutakse samm-sammult infot läbivaadatud järjendi osa kohta. Antud näite käivitamisel on igal tsükli sammul muutuja ``seni_suurim`` väärtuseks läbivaadatud elementide hulgast suurim.

Tegelikult on Pythonisse juba sisse ehitatud mitmeid funktsioone, mis koguvad etteantud järjendi kohta mingit infot. Näiteks funktsioon ``max`` teeb sama, mis meie eelmise näite funktsioon. Selle praktikumi raames aga üritame taolisi funktsioone ise "leiutada", et õppida järjendeid ning ``for``-tsüklit paremini tundma.

Ülesanne 2. Elementide summa
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Kirjutage funktsioon ``elementide_summa``, mis võtab argumendiks arvujärjendi ning tagastab kõigi elementide summa. (Selle jaoks on küll Pythonis juba olemas funktsioon ``sum``, aga ärge praegu seda kasutage).

NB! Erinevalt suurima elemendi leidmise funktsioonist, peaks summa funktsioon töötama ka tühja järjendiga, st. ``elementide_summa([])`` peaks andma vastuseks ``0``.

.. hint::
    
    Jälgige eelmise näite skeemi -- hoidke akumulaatoris seni läbivaadatud summat ning igal tsükli sammul uuendage akumulaatorit. Samuti mõelge, mis on antud ülesande juures sobiv akumulaatori algväärtus.

Lõpuks kontrollige, kas teie funktsioon annab samade järjendite puhul sama tulemuse, mis Pythoni funktsioon ``sum``.    
    

Failist lugemine
-----------------
Tuleb välja, et ``for``-tsükkel on väga mugav ka failist lugemiseks:

.. sourcecode:: py3

    f = open('andmed.txt')
    
    for rida in f:
        print('Lugesin järgneva rea: ' + rida)
    
    f.close()

Selle näidet kommenteerides võiks lihtsustatult öelda, et:

    #. funktsioon ``open`` tagastab failis sisalduvad read sõnejärjendina ...
    #. ... mis salvestatakse muutujasse ``f`` 
    #. ``for``-tsükkel käib selle järjendi elemendid ükshaaval läbi.

Tegelikult ei ole muutujas ``f`` siiski mitte järjend, vaid natuke keerulisem väärtus. Õnneks oskab ``for``-tsükkel käsitleda seda väärtust justkui järjendit, seetõttu ei pea me muretsema, kuidas need faili read on tegelikult esitatud.

Ülesanne 4. Temperatuuride lugemine failist
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Kirjutage programm, mis loeb tekstifailist ükshaaval Celsiuse skaalas esitatud temperatuure (iga arv on antud eraldi real) ning väljastab need ekraanile koos vastavate väärtustega Fahrenheiti skaalas.

.. hint:: 
    Meeldetuletus: Justnagu ``input`` käsu puhul, saame ka tekstifailist lugedes sisendi alati tekstina, seetõttu tuleb antud ülesandes teisendada algandmed enne kasutamist arvudeks.


Funktsioon ``range``
--------------------
Vaatame nüüd pisut teistsuguse ilmega ``for``-tsükli näidet:

.. sourcecode:: py3

    for i in range(10):
        print(i)

Selle programmi käivitamisel ilmuvad ekraanile numbrid *0..9*. Selleks, et antud näitest paremini aru saada, proovige käsureal läbi järgnev näiteavaldis:

.. sourcecode:: py3

    >>> list(range(5))
    [0, 1, 2, 3, 4]

Avaldis ``range(5)`` genereerib ühe järjendit meenutava väärtuse -- nimelt *vahemiku*. Funktsioon ``list`` teisendas selle väärtuse päris järjendiks, mis sisaldab täisarve *0..4*.

Nüüd peaks olema selge, miks meie ``for``-tsükli näide sedasi käitus -- ``range(10)`` genereerib vahemikku *0..9* kujutava väärtuse ja kuigi tegemist pole päris järjendiga, oskab ``for``-tsükkel seda käsitleda justkui järjendit. Edasi toimub kõik samamoodi nagu varem kirjeldatud -- "pseudo-järjendist" loetakse ükshaaval elemente, mis salvestatakse kordamööda tsüklimuutujasse ``i`` ning igal kordusel käivitatakse tsükli kehas olevad laused.

.. note::

    Mõnikord läheb meile korda ainult see, mitu korda tsükli keha on vaja korrata, st. tsüklimuutuja konkreetsete väärtuste vastu me huvi ei tunnegi. Järgnev ruudu joonistamise näide peaks olema tuttav eelmisest praktikumist, ainult, et seekord kasutame me ``while``-tsükli asemel ``for``-tsüklit:

    .. sourcecode:: py3
        
        from turtle import *
        
        for i in range(4):
            forward(100)
            left(90)

        exitonclick()

    Kuigi me muutuja ``i`` väärtust ei kasutanud, siis Pythoni süntaks nõuab ikkagi selle muutuja kirjapanekut.


Ülesanne 3. Kilpkonn tsüklis
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Proovige ennustada, mida joonistab järgmine programm:

.. sourcecode:: python

    from turtle import *
    
    for i in range(30) :
        forward(i * 2)
        left(90)
    
    exitonclick()

.. topic:: Selgitus

    Nagu näete, joonistub ekraanile kandiline spiraal. Kuidas see programm aga kilpkonna abil sellise tulemuseni jõuab?

    Tegelikult on antud programmi puhul üldine seletus lihtne:

    * ``for i in range(30)`` ütleb, et talle järgnevat koodiblokki (taandatud ridasid) tuleb korrata 30 korda, kusjuures esimest korda on selle bloki jaoks ``i`` väärtus 0, siis 1, siis 2 jne. kuni 29-ni välja.
    * Esimesel kordusel, kui i=0, ei liigu kilpkonn üldse edasi, kuid pöörab 90 kraadi vasakule (nina üles suunda).
    * Teisel kordusel, kui i=1, liigub kilpkonn kaks (``i*2``) sammu edasi (üles), ning siis 90 kraadi vasakule (nina nüüd vasakus suunas).
    * Kolmandal kordusel, kui i=2, liigub kilpkonn 4 sammu edasi (vasakule) ja siis pöörab jälle 90 kraadi vasakule (nii et nina on nüüd alla suunatud).
    * jne kuni i=29 -ni.

    Et iga kord on joonistatav lõik eelmisest pikem, tekibki selle tsükli tulemusena kandiline spiraal.

Katsetage erinevaid pööramise nurki ning erinevaid teepikkusi. Proovige joonistada kuuekandiline spiraal!

``range``'i variandid
~~~~~~~~~~~~~~~~~~~~~
Funktsiooni ``range`` saab kasutada ka 2 või 3 argumendiga. Järgnevas käsurea näites kasutame jälle ``list`` funktsiooni, et näha, mida mingi ``range`` variant tähendab:

.. sourcecode:: py3

    >>> list(range(5))
    [0, 1, 2, 3, 4]
    >>> list(range(0, 5))
    [0, 1, 2, 3, 4]
    >>> list(range(2, 5))
    [2, 3, 4]
    >>> list(range(0, 15, 2))
    [0, 2, 4, 6, 8, 10, 12, 14]
    >>> list(range(5, 0, -1))
    [5, 4, 3, 2, 1]
    >>> list(range(0, 5, 1))
    [0, 1, 2, 3, 4]

Kommentaarid:

    * ühe argumendiga variandi puhul algab loetelu 0-st ning lõpeb *enne* näidatud argumendi väärtuseni jõudmist
    * kahe argumendi puhul algab loetelu esimese argumendi väärtusest ja lõpeb *enne* teise argumendini jõudmist
    * kolme argumendi puhul näitab kolmas argument väärtuste kasvamise sammu

Ülesanne 4. Kolmega jaguvad arvud
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Kirjutage ``for``-tsükkel koos sobiva ``range`` variandiga, mis kuvab ekraanile kõik 3-ga jaguvad arvud vahemikus 10 kuni 100.

Ülesanne 5. ``range`` avaldis
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Kirjutage avaldis kujul ``list(range(...))``, mis tagastaks järgmise järjendi:

 ``[100, 93, 86, 79, 72, 65, 58, 51, 44, 37, 30, 23, 16]``




``for`` vs. ``while``
---------------------
Tegelikult saaks ``for``-tsükli asemel alati kasutada ka ``while``-tsüklikt, aga tulemus poleks alati nii selge. Võrdleme omavahel samaväärseid ``while`` ja ``for``-tsükleid:

+----------------------------------+-----------------------------------+
| .. sourcecode:: py3              | .. sourcecode:: py3               |
|                                  |                                   |
|     i = 0                        |     for i in range(10)            |
|     while i < 10:                |         print(i)                  |
|         print(i)                 |                                   |
|         i += 1                   |                                   |
+----------------------------------+-----------------------------------+

Kui meenutate eelmist praktikumi, siis selleks, et ``while`` tsükliga teha mingit toimingut *n* korda, tuleb:

    * võtta kasutusele abimuutuja (loendur) algväärtusega 0
    * tsükli kehas suurendada muutuja väärtust igal kordusel
    * tsükli päises kontrollida, et loenduri väärtus on väiksem kui *n*

Nagu näha, annab ``for``-tsükkel koos ``range``-ga sama tulemuse palju lihtsamalt -- tsüklimuutuja algväärtustamine, selle suurendamine ja tsükli lõpetamise kontrollimine toimuvad kõik automaatselt. Seetõttu ongi soovitav loenduril põhinevad tsüklid kirjutada ``for``-tsüklina.

Samas, mõnede probleemide lahendamisel ei piisa ``for``-tsüklist. Näiteks eelmises praktikumis kirjeldatud arvamismängu ei saa ``for``-tsükliga kirja panna. Seetõttu ongi Pythonis kaks erinevat korduslauset -- paindlik, aga pisut tülikas ``while``-lause ning mugav, aga teatud juhtudel ebasobiv ``for``-lause.


Veel järjendioperatsioone
-------------------------
    

Sõne kui järjend
~~~~~~~~~~~~~~~~
Nagu eelmises praktikumis juba mainitud, saab sõnet käsitleda justkui sümbolite järjendit:

.. sourcecode:: py3

    sõne = 'Tere'
    print(sõne[0])
    
    for täht in sõne:
        print(täht)

Selleks, et sõnet muuta päris järjendiks, saab kasutada funktsiooni ``list``:
    
.. sourcecode:: py3

    >>> list('Tere')
    ['T', 'e', 'r', 'e']

Meetodid ``split`` ja ``join``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Tihti on tarvis teha mingi sõne pisut suuremateks juppideks kui üksikud tähed -- näiteks võib olla vaja jagada sõnena esitatud lause eraldi sõnadeks. Selle jaoks saab kasutada sõnemeetodit ``split``:

.. sourcecode:: py3

    >>> 'Tere hommikust'.split()
    ['Tere', 'hommikust']
    >>> 'CY2X44;3;66;T'.split(';')
    ['CY2X44', '3', '66', 'T']

Kui ``split``-i kasutada ilma argumentideta, siis tehakse "lõikamine" tühikute, tabulaatorite ja reavahetuste kohalt. Kui anda ette mingi muu sümbol, siis lõigatakse sõne juppideks just selle sümboli kohalt. 

Sama operatsiooni saab "ümber pöörata" meetodiga ``join``:

.. sourcecode:: py3

    >>> ' '.join(['Tere', 'hommikust'])
    'Tere hommikust'
    >>> ';'.join(['CY2X44', '3', '66', 'T'])
    'CY2X44;3;66;T'

Ülesanne 1. Kuupäeva "lahtiharutamine"
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Kirjutage funktsioon ``kuu``, mis võtab argumendiks sõne kujul *<päev>. <kuu> <aasta>* (nt. ``'24. veebruar 1918'`` ning tagastab vastava kuu nime.

Negatiivsed indeksid
~~~~~~~~~~~~~~~~~~~~
Järjendeid (ja sõnesid) saab indekseerida ka negatiivsete indeksitega, sel juhul hakatakse lugema järjendi lõpust:

.. sourcecode:: py3

    >>> sõne = 'Tere'
    >>> sõne[-1]
    'e'
    >>> sõne[-2]
    'r'
    >>> sõne[-3]
    'e'
    >>> sõne[-4]
    'T'

Avaldis ``järjend[-0]`` tähistab siiski esimest elementi, sest *-0 = 0*.

Järjendite "viilutamine"
~~~~~~~~~~~~~~~~~~~~~~~~
Kirjutades nurksulgudesse indeksi asemel *indeksivahemiku* on järjendist (ja sõnedest) võimalik võtta alamjärjendeid (alamsõnesid):

.. sourcecode:: py3

    >>> a = ['a', 'b', 'c', 'd', 'e', 'f']
    
    >>> a[0:2]
    ['a', 'b']
    >>> a[:2]
    ['a', 'b']
    
    >>> a[2:6]
    ['c', 'd', 'e', 'f']
    >>> a[2:]
    ['c', 'd', 'e', 'f']

    >>> a[-2:]
    ['e', 'f']
    >>> a[:]
    ['a', 'b', 'c', 'd', 'e', 'f']
    
    >>> s = "Tere"
    >>> s[0:3]
    'Ter'

Koolonist vasakule tuleb kirjutada see indeks, millest alates tuleb elemente tulemusse kopeerida, ning koolonist paremale see indeks, mille juures tuleb kopeerimine lõpetada (st. selle indeksiga element jääb tulemusest välja). Kui vasak indeks jätta kirjutamata, siis alustatakse esimesest elemendist ja kui parem indeks jätta kirjutamata, siis kopeeritakse kuni järjendi lõpuni (viimane element kaasaarvatud).

Valed indeksid
~~~~~~~~~~~~~~~~~~
Proovige läbi järgnev näide, et te tunneksite saadud veateate edaspidi ära:

.. sourcecode:: py3

    a = ['a', 'b', 'c']
    print(a[66])


Ülesanne 2. Sõne viilutamine
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Kirjutage funktsioon ``kaja``, mis võtab argumendiks sõne, ning tagastab selle sõne 3 viimast tähte. Kui sõnes on vähem kui 3 tähte, siis tagastada terve sõne.



Koduülesanded
-------------

1. Õpikuülesanne
~~~~~~~~~~~~~~~~
Lahendage `õpiku 6. peatükist <http://courses.cs.ut.ee/2011/programmeerimine/uploads/Raamat/ch06.html>`_ ülesanne nr. 1.


2. Ruudud
~~~~~~~~~~~~~~~~~~
Kirjutage programm, mis küsib sisendiks täisarvu ning väljastab kõikide arvude ruudud alates 1-st kuni sisestatud arvuni (kaasaarvatud) ja lõpuks ka kõigi nende ruutude summa.

3. Laulusõnad
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Kirjutage programm, mis kuvab ekraanile laulu "99 Bottles of Beer on the Wall" sõnad.  Tulemus peaks olema selline, nagu näidatud siin: :download:`99-bottles.txt <downloads/99-bottles.txt>`. (NB! See fail on vaid näiteks -- sõnad tuleb genereerida, mitte failist sisse lugeda).

.. note::
    Ärge unustage tulemust testida! Viisi saab kuulata siit: http://www.youtube.com/watch?v=3KnpZYkTWno

4. Teksti esitamine
~~~~~~~~~~~~~~~~~~~~
Kirjutage programm, mis küsib kasutajalt failinime ning kuvab faili sisu ekraanile.

Seejärel täiendage programmi sedasi, et teksti näidatakse 20 rea kaupa -- st. iga kord peale 20 rea näitamist jääb programm ootama kasutajapoolset ENTER-i vajutust (vihje: ``input()``).

Testimiseks võib alla laadida nt. "Alice in Wonderland" teksti aadressilt http://www.gutenberg.org/files/11/11.txt.



5. Keskmise hinde leidmine
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Olgu meil fail nimega ``hinded.txt``, kus on igal real üks hinne (vahemikus 1 kuni 5). Kirjutage programm, mis arvutab nende hinnete keskmise. (Ärge unustage, et failist ridade sisselugemisel antakse read sõnedena, mitte arvudena).

Kui olete programmi tööle saanud, siis muutke programmi põhiosa funktsiooniks, mis **võtab argumendiks** failinime ning **tagastab** failis olevate hinnete keskmise.


.. todo::
    NB! selle sissepanemiseks on tarvis et selles praksis on split-i tutvustatud
    lisaülesanne: Kilpkonna interpretaator
    
    Kilpkonnaga Pythoni käsureal joonistamine on üpris lõbus, kuid muutub pikkade käskude tõttu kähku tüütuks. Arvutid on aga just mõeldud tüütute ülesannete automatiseerimiseks ja lihtsustamiseks. See motiveerib ka järgnevat ülesannet.

    Antud on fail, kus igal real on kilpkonna käsk – täht ja selle järel number, näiteks:


    .. sourcecode:: none

        F 100
        L 90
        B 100
        R 120

    Kirjutada programm, mis loeb sisse vastava faili ja edastab need käsud kilpkonnale, lastes sellel joonistada siis neile vastava kujundi.

    Programm ise on tegelikult üsna lihtne:

    .. sourcecode:: py3

        import turtle

        # Faili avamine
        file = open("Kilpkonn.txt","r")

        # Faili töötlemine ja kilpkonnaga joonistamine
        while True:
            rida = file.readline()
            # Katkesta viimase rea puhul
            if rida == "" :
                break

           

            # Teisenda käsk kaheks komponendiks
            kask = rida.split()
            tyyp = kask[0]
            param = int(kask[1])

            if tyyp == "L" :
                turtle.left(param)
            elif tyyp == "R" :
                turtle.right(param)
            elif tyyp == "F" :
                turtle.forward(param)
            elif tyyp == "B" :
                turtle.backward(param)
            else :
                print "Failis oli tundmatu käsk!"

    Sisuliselt kirjutasime me just interpretaatori niiöelda "Kilpkonna keele" jaoks, mis tõlkis lihtsalt loetud käsud meie kilpkonnale arusaadavasse keelde. Põhimõtteliselt sama moodi toimivad ka teiste keelte interpretaatorid. Interpretaator ei ole seega midagi keerulist ja abstraktset – tegu on lihtsalt asjaga, mis loeb käske ja täidab neid.

     



Lisalugemine
------------

.. todo::

    need teemad võiks äkki panna (osaliselt) eelmise praksi lisalugemiseks

Kõigis järgnevates näiteprobleemides kasutatakse tulemuseni jõudmiseks tsükleid.

Paroolide murdmine
~~~~~~~~~~~~~~~~~~
Järgnev näide demonstreerib jõumeetodil paroolide murdmise põhiideed.

Turvalisuse huvides salvestatakse infosüsteemides kasutajate paroolide asemel ühesuunalise krüpteerimismeetodiga saadud *räsikoode*. Kuigi räsikoodist pole otseselt võimalik parooli tuletada, tuleks seda siiski võõraste eest kaitsta, sest pahalane võib proovida krüptida sama meetodiga palju erinevaid paroole ning kui tulemuseks on sama räsikood, siis on ka parool teada.

Vali mingi inglisekeelne, väikeste tähtedega sõna parooliks, ning koosta sellest MD5 räsikood, kasutades vormi aadressil: http://www.miraclesalad.com/webtools/md5.php

Lae alla inglisekeelsete paroolide nimekiri aadressilt http://www.apasscracker.com/dictionaries/ ning paki zip failis olev tekstifail lahti.

Järgnev programm küsib kasutajalt MD5 räsikoodi, ning otsib paroolisõnastikust sobivat vastet. Edu korral näidatakse parool ekraanile.

.. sourcecode:: py3

    import hashlib

    räsi = input("Sisesta parooli MD5 räsi: ")
    f = open("english.dic", encoding="latin_1")

    # esialgu veel pole midagi leidnud
    tulemus = "Ei leidnud parooli"

    for rida in f:
        # strip eemaldab rea lõpust reavahetuse
        parool = rida.strip()
        
        if hashlib.md5(parool.encode('ascii', 'ignore')).hexdigest() == räsi:
            tulemus = "Vastav parool on: " + parool
            break # edasi pole vaja vaadata

    # faili me enam ei vaja
    f.close()

    print(tulemus)
    
Tegelikkuses ei lähe paroolide murdmine siiski nii libedalt -- esiteks piirasime end praegu vaid väikeste tähtedega paroolidega ja teiseks, reaalselt kasutatavad krüptimismeetodid on palju aeglasemad, kui meie kasutatud *MD5*.

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

    for i in range(0,n):
        # Genereeri juhuslik punkt
        x = random.uniform(-1,1)
        y = random.uniform(-1,1)

        # Kontrolli, kas ta on ringi sees
        if (x**2 + y**2 < 1):
            c=c+1

    print("Hinnanguks on "+ str((4.0*c) / n))

Funktsioon ``random.uniform`` valib ühtlase jaotuse põhjal juhuslikult ühe reaalarvu etteantud vahemikust. Kõik muu programmi juures peaks olema juba tuttav.

Katsetamine erinevate katsete arvudega (10,100,1000,...,1000000) peaks veenma, et kuigi tulemused on reeglina π-le lähedased, on see siiski suhteliselt halb meetod π kohtade leidmiseks sest vähegi mõistliku täpsuse saamiseks tuleb teha väga palju katseid.

Selliseid arvutusmeetodeid nimetatakse Monte Carlo meetoditeks (kuulsa kasiinolinna järgi Monakos). Antud näide on taas pigem illustratiivne – praktikas kasutatakse seda reeglina ülesannete puhul, mida muud moodi lahendada ei osata. π arvutamiseks teatakse aga palju teisi ja oluliselt paremaid meetodeid.
