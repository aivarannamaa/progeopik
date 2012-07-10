V. Hargnemine ja tsüklid
=======================================

.. todo::
    Siin on praegu koos vastavate teemade Pythoni ja tahvlipraksi (teoreetilisem) osa.
    Pythoni konstruktsioonide tutvustus ja lihtsamad ülesanded tuleks (osaliselt) liigutada peatükki "liitlaused". Ülejäänud materjalis võiks äkki plokkskeemide ja teooria osa põimida Pythoni harjutustega?


Selles praktikumis käsitleme kahte teemat. Kõigepealt uurime põhjalikumalt tingimuslause (e. ``if``-lause) erinevaid vorme ja tingimuse moodustamise võimalusi. Seejärel õpime ära konstruktsiooni, mis käseb Pythonil lauseid korduvalt käivatada.

.. topic:: NB!

    Osadele selle praktikumi ülesannetele tuleb loogiline jätk koduülesannetes -- seega on soovitav praktikumis lahendatud ülesanded koju kaasa võtta.

.. index::
    single: bool; tõeväärtustüüp
    single: boolean; tõeväärtustüüp

Tõeväärtustüüp ``bool``
-----------------------
Lisaks sõnedele ja arvudele on Pythonis üks oluline andmetüüp nimega ``bool`` (lühend sõnast ``boolean``), milles on vaid kaks võimalikku väärtust -- ``True`` ja ``False``. Eesti keeles nimetatakse seda andmetüüpi **tõeväärtustüübiks**.

Tõeväärtustüübiga olete tegelikult juba kokku puutunud -- ``if``-lause tingimuseks olev avaldis on justnimelt tõeväärtustüüpi. Samas, tõeväärtustüübi kasutusvõimalused pole piiratud vaid ``if``-lausega -- nagu kõiki väärtusi, saab ka tõeväärtusi muutujasse salvestada või funktsiooni argumendina kasutada. Selles veendumiseks mängime läbi järgneva lihtsa näite:

.. sourcecode:: py3

    vastus = 3 > 2
    print(vastus)

* kõigepealt väärtustakse avaldis ``3 > 2``
* tulemuseks saadud väärtus ``True`` salvestatakse muutujasse ``vastus``
* muutuja ``vastus`` väärtus kuvatakse ekraanile

Kuna ``if``-lause tingimuses võib tõeväärtus olla antud mistahes kujul, siis võiksime kontrolli tulemuse salvestada eelnevalt muutujasse ning hiljem kasutada seda muutujat tingimusena:

.. sourcecode:: py3

    arv = int(input("Sisesta arv: "))
    jagub_kahega = arv % 2 == 0 # salvestame tõeväärtuse abimuutujasse
    
    if jagub_kahega:
        print("Sisestati paarisarv")
    else:
        print("Sisestati paaritu arv")

Enamasti pole siiski taolist abimuutujat tarvis ja me võime kirjutada lihtsalt:

.. sourcecode:: py3

    arv = int(input("Sisesta arv: "))
    
    if arv % 2 == 0:
        print("Sisestati paarisarv")
    else:
        print("Sisestati paaritu arv")


Tõeväärtusega avaldised
~~~~~~~~~~~~~~~~~~~~~~~
Pythonis on olemas hulk operaatoreid ning funktsioone, mis tagastavad tõeväärtuse ja mida saab seetõttu kasutada ``if``-lause tingimuses. Proovige käsureal järgmisi avaldisi:

    * ``4 < 3``
    * ``4 >= 4``
    * ``4 == 3``
    * ``4 != 3``
    * ``4 != 4``
    * ``'r' in 'tore'``
    * ``'r' in 'tobe'``
    * ``'Tallinn'.endswith('linn')``
    * ``'Tartu'.startswith('reha')``
    * ``'10203'.isnumeric()`` (sobib märgita täisarvude tuvastamiseks)
    * ``'suramura'.isnumeric()``

Loomulikult saab kõiki mainitud operatsioone kasutada ka muutujatega.

.. topic:: Terminoloogia

    Avaldisi, mis tagastavad tõeväärtuse, nimetatakse *loogilisteks avaldisteks*.


Ülesanne 1. Arvu ruut koos kontrolliga
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Kirjutage programm, mis küsib kasutajalt positiivse täisarvu ning kontrollib, kas sisestatud tekst on numbriline. Kui jah, siis kuvatakse antud arvu ruut, vastasel juhul kuvatakse veateade. 

.. index::
    single: loogilised avaldised

Tõeväärtuste kombineerimine
~~~~~~~~~~~~~~~~~~~~~~~~~~~
Kuna tõeväärtustüübis on vaid kaks väärtust, ei ole nende väärtuste kombineerimiseks nii palju võimalusi, kui näiteks sõnede või arvude puhul. Kõige tähtsamad operaatorid, mis võtavad argumendiks tõeväärtused (e. *loogilised tehted*), on ``and``, ``or`` ja ``not``. Nende operaatorite tähendus on arvatavasti intuitiivselt arusaadav, kuid vajadusel saab kõik kombinatsioonid Pythoni käsureal järgi proovida:

    * ``True and False``
    * ``True and True``
    * ...
    * ``True or False``
    * ``True or True``
    * ...
    * ``not True``
    * ``not False``

Tehete järjekord
~~~~~~~~~~~~~~~~
Keerulisemate avaldiste puhul tuleb arvestada, et ``not`` on kõrgema prioriteediga kui ``and`` ning ``and`` on kõrgema prioriteediga kui ``or``, seega ``not x or not y and z`` tähendab ``(not x) or ((not y) and z)``.

Kuna ühes avaldises võivad olla koos aritmeetilised tehted, võrdlustehted ja loogilised tehted, siis selleks, et vähendada sulgude vajadust, on aritmeetilised tehted kõige kõrgema prioriteediga (st. tehakse esimesena) ning loogilised tehted on kõige madalama prioriteediga (tehakse viimasena).

Järgnev loetelu võtab kokku tähtsamate tehete prioriteedid (kõrgema prioriteediga tehted on ülalpool, samal real olevad operaatorid on sama prioriteediga):

    * ``**``
    * ``-x`` (*unaarne* miinus)
    * ``*``, ``/``, ``//``, ``%``
    * ``+``, ``-``
    * ``==``, ``!=``, ``<``, ``<=``, ``>``, ``>=``, ``in``
    * ``not``
    * ``and``
    * ``or``

Kahtluse korral kasutage soovitud tehete järjekorra määramiseks sulge.
    
Loogiliste avaldiste samaväärsus
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Tihti on teatud tähendusega tõeväärtusavaldist võimalik kirjutada mitmel erineval kujul, näiteks:

    * ``not (x or y)`` on sama, mis ``(not x) and (not y)``
    * ``not (x and y)`` on sama, mis ``(not x) or (not y)``

Samaväärsetest variantidest tuleks valida selline, mis toob avaldise mõtte paremini esile.

Tõeväärtusega funktsioonid
~~~~~~~~~~~~~~~~~~~~~~~~~~
Kui programmis on mitmes kohas vaja kontrollida sarnast tingimust, siis võib selle tingimuse panna kirja funktsioonina, mis tagastab tõeväärtuse. Järgnev programm  demonstreeribki tõeväärtusega funktsiooni loomist ja kasutamist:

.. sourcecode:: py3

    def on_positiivne_paarisarv(x):
        return (x > 0) and (x % 2 == 0)

    arv = int(input("Sisesta arv: "))
    if on_positiivne_paarisarv(arv):
        print("Arv on positiivne ja paaris")
    else:
        print("Arv pole positiivne või pole paaris")

Ülesanne 2. Liigaasta tuvastamine
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Kirjutage funktsioon ``on_liigaasta``, mis võtab argumendiks aastaarvu ning **tagastab tõeväärtuse** vastavalt sellele, kas antud aasta on liigaasta või mitte.

Kirjutage programm, mis küsib kasutajalt aastaarvu ning väljastab ekraanile info selle kohta, kas tegemist on liigaastaga või mitte. Liigaasta tuvastamiseks kasutage eelnevalt defineeritud funktsiooni.

.. hint::

    Liigaasta on selline, kus aastaarv jagub 4-ga, välja arvatud juhud, kus aastaarv jagub 100-ga, aga ei jagu 400-ga. Näiteks aastad 2004 ja 2000 on liigaastad aga 1900 mitte.

.. note::
    Kui programmis läheb mõni lause liiga pikaks, siis võite ta kirjutada mitmele reale, aga sel juhul tuleb rea "murdmise" koht märkida ära langkriipsuga (``\``):
    
    .. sourcecode:: py3
    
        tulemus = (see >= teine * math.pi) \
            and (niimoodi or naamoodi) \
            and (x > y or u != 1)
        

    Sellist rea murdmist võib kasutada suvaliste lausete korral. Murda ei saa vaid sõneliteraali ja kommentaaari sees.

Tingimuslaused
--------------
Siiani oleme kasutanud tingimuslauset (e. ``if``-lauset e. hargnemislauset) kõige lihtsamal kujul, kus on välja toodud täpselt 2 alternatiivi. Järgnevalt vaatame kuidas kirjutada "üheharulist" tingumuslauset ning kuidas mitut tingimuslauset kombineerida. 

``if`` ilma ``else``-ta
~~~~~~~~~~~~~~~~~~~~~~~
Tingimuslauses võib ``else`` osa ära jätta -- seda kasutatakse siis, kui tingimuse mittekehtimise puhul ei ole vaja midagi spetsiifilist teha:

.. sourcecode:: py3

    x = int(input("Sisesta esimene arv: "))
    y = int(input("Sisesta teine arv: "))
    
    print("Arvude erinevus on " + str(abs(x-y)))
    if x == y:
        print("... seega on nad võrdsed")

Tingimuslaused üksteise sees
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Tingimuslauseid võib panna üksteise sisse, sel juhul tuleb hoolikalt jälgida korrektset treppimist:

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

Ülesanne 3. Päevade arv kuus
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Kirjutage funktsioon ``päevade_arv``, mis võtab argumendiks kuu numbri ja aastaarvu ning tagastab mitu päeva on selles kuus. Kasutage abifunktsioonina eelnevalt defineeritud funktsiooni ``on_liigaasta``. (Kirjutage need funktsioonid samasse faili).

Ülesanne 4. Kuupäeva kontrollimine
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Kirjutage funktsioon ``on_legaalne_kuupäev``, mis võtab argumendiks päeva, kuu ja aasta (arvudena) ning tagastab tõeväärtuse vastavalt sellele, kas argumentidele vastav kuupäev on legaalne või mitte. Kasutage abifunktsioonidena eelmistes ülesannetes defineeritud funktsioone.

Testige loodud funktsiooni järgnevate avaldistega:

    - ``on_legaalne_kuupäev(31, 1, 2001)``
    - ``on_legaalne_kuupäev(29, 2, 2001)``
    - ``on_legaalne_kuupäev(29, 2, 2000)``

    

``elif`` konstruktsioon
~~~~~~~~~~~~~~~~~~~~~~~
Ülalpool toodud arvude võrdlemise näite saab kirjutada ümber kasutades ``elif`` konstruktsiooni (tuleb sõnadest *else if*):

.. sourcecode:: py3
    
    arv1 = int(input("Sisesta esimene arv: "))
    arv2 = int(input("Sisesta teine arv: "))
    
    if arv1 > arv2:
        print("Esimene arv on suurem")
    elif arv2 > arv1:
        print("Teine arv on suurem")
    else:
        print("Arvud on võrdsed")

Pange tähele, et ``elif`` algab samast veerust, kus ``if`` ja ``else`` -- viimased 6 rida antud näites moodustavad üheainsa tingimuslause. ``if``-i ja ``else`` vahele võib kirjutada ka mitu ``elif`` osa.

``elif`` on kasulik siis, kui meil on vaja kontrollida mitut alternatiivset tingimust. ``elif``-i asemel saaks alati kasutada ka üksteise sisse pandud tingimuslauseid, aga siis võib treppimine minna liiga keeruliseks.

NB! Ühes tingimuslauses täidetakse ühel käivitamisel vaid üks haru (ning kui ``else`` osa puudub, siis võib juhtuda, et ei täideta ühtegi haru). Tingimusi hakatakse kontrollima ülevalt alla -- kui leitakse esimene kehtiv tingimus, siis täidetakse selle juurde kuuluvad laused ja järgnevaid harusid ning nende tingimusi enam ei vaadata.

Näide: Hinde arvutamise programm
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. sourcecode:: py3

    def hinne(punkte):
        if punkte >= 91:
            return 'A'
        elif punkte >= 81:
            return 'B'
        elif punkte >= 71:
            return 'C'
        elif punkte >= 61:
            return 'D'
        elif punkte >= 51:
            return 'E'
        else:
            return 'F'

    punkte = int(input("Sisesta punktide arv"))
    print("Nende punktidega saab hindeks " + hinne(punkte))

Ülesanne 5. Kuu esitamine sõnena
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Kirjutage funktsioon ``kuu_nimi``, mis võtab argumendiks kuu numbri ning tagastab vastava kuu nime. Kui argumendi väärtus on väiksem kui 1 või suurem kui 12, siis tagastatakse sõne ``'Vigane kuu number'``.

Testige oma funktsiooni!

.. index:: 
    single: while tsükkel
    single: tsükkel; while tsükkel
    
``while``-tsükkel
-----------------
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

Loenduriga tsükkel
~~~~~~~~~~~~~~~~~~
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


.. note::

    Tegelikult on Pythonis olemas ka teine, natuke spetsiifilisem tsüklitüüp, mida nimetatakse ``for``-tsükliks ja mis sobib *n*-korduse tegemiseks isegi paremini, kui ``while``. ``for``-tsüklit vaatame järgmises praktikumis.

Ülesanne 6. Funktsioon *n*-nurga joonistamiseks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Kirjutage eelmise näite põhjal funktsioon, mis joonistab *n*-küljega hulknurga. Funktsioonil peavad olema parameetrid nurkade arvu ning küljepikkuse määramiseks.

.. hint::
    Iga nurga juures peab kilpkonn pöörama 360/n kraadi.
    
Testige loodud funktsiooni joonistades üksteise kõrvale kolmnurga, ruudu ja viisnurga.


Määramata tsükkel
~~~~~~~~~~~~~~~~~
Alati pole võimalik ette öelda, kui mitu korda midagi kordama peab enne, kui jõutakse soovitud tulemuseni. Järgmine näiteprogramm laseb kasutajal arvata juhuslikult valitud arvu niikaua, kuni ta jõuab õige vastuseni:

.. sourcecode:: py3

    from random import randint 
    
    arv = randint(1,999) # randint annab juhusliku täisarvu näidatud vahemikust
    arvamus = int(input("Arva, millist tuhandest väiksemat arvu ma mõtlen: "))

    # Kuni pakutud arv erineb arvuti valitust
    while arvamus != arv :
        if arv > arvamus:
            print("Minu arv on suurem!")
        else:   
            print("Minu arv on väiksem!")
            
        arvamus = int(input("Arva veelkord: "))
        
    print("Ära arvasid! Tubli!")

Ülesanne 7. Algandmete kontrollimine tsükliga
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Tsükleid saab kasutada algandmete sisestamise juures -- me võime vigase sisendi puhul lasta kasutajal sisestamist korrata niikaua, kuni oleme sistatud infoga rahul.

Modifitseerige 1. ülesande lahendust -- kui kasutaja poolt sisestatud tekst polnud numbriline, siis peaks programm kordama küsimist ja andmete sisselugemist niikaua, kuni kasutaja sisestab numbrilise teksti.

Alles siis, kui korrektne sisend on käes, tuleks väljastada sisestatud arvu ruut.

Ülesanne 8. Täiendatud arvamismäng
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~    
Täiendage arvamismängu selliselt, et tsükli töö lõpeb ka sel juhul, kui kasutaja pole 10 arvamisega suutnud õiget arvu ära arvata. (Vihje: tarvis on võtta kasutusele loendur ning täiendada kordamise tingimust).


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
    

``break`` kasutamise asemel saab tsükli alati ümber kirjutada nii, et kõiki lõpetamise tingimusi kontrollitakse tsükli päises.

Mõnikord on kasulik tsükli lõpetamise tingimust kontrollida ainult tsükli kehas, sel juhul pannakse tsükli päisesse alati kehtiv tingimus ``True``. Järgnev programm küsib kasutajalt arve ja näitab nende ruute niikaua, kuni kasutaja sisestab *tühisõne* (st. vajutab ENTER ilma midagi tegelikult sisestamata):

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

Ülesanne 9. Juhuslikud arvud
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Kirjutage programm, mis väljastab iga ENTER vajutuse järel (st. tühisõne sisestamisel) ekraanile juhusliku täisarvu vahemikus 1..999. Tsükli töö tuleks lõpetada (kasutades ``break``-i) siis, kui kasutaja sisestab tühisõne asemel sõne ``'aitab'``.


Algoritm ja plokkskeem
--------------------------
Peale antud teema läbimist üliõpilane oskab

    * selgitada algoritmi mõistet;
    * lihtsamate ülesannete korral esitada probleemi täpse püstituse, st välja selgitada algandmed ja nõutava tulemuse;
    * leida antud ülesande lahendamiseks kohased põhitegevused ja esitada nende täitmise järjekorra;
    * esitada lihtsamate ülesannete lahendust plokkskeemina (nt. lihtsamate kilpkonnaülesannete korral).



**Ülesanne 1.** Dokumentideta võõras linnas
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Kujutle end võõras linnas välisüliõpilanena. Saabudes ühiselamu juurde avastad, et ühiselamu võti, ID-kaart ja mobiiltelefon on kadunud. Kuidas lahendada olukord?

Meie igapäevaelus tuleb meil ette suuri ja väikesi ülesandeid. Mõned on lihtsad lahendada, teiste lahendamine pöörab kogu elu pahupidi (arst avastab sinu lähedasel üliharva esineva ravimatu haiguse). Mõnedele ülesannetele on olemas standardvastused, teiste korral tuleb neid alles hakata otsima. Mõned probleemid tunduvad huvitavana, mõned mitte.  
Ülesanded varieeruvad oma olemuselt matemaatilistest kuni filosoofilisteni (Mis on elu mõte?). Arvutiteaduses me tegeleme probleemidega, mille lahendust saab esitada algoritmina. 

*Algoritmiks* nimetatakse probleemi lahendamiseks vajalikku instruktsioonide hulka, mida on võimalik tõlkida arvuti jaoks arusaadavale kujule (programm) ja  mida täidab arvuti. 

Pöördume tagasi ülesande 1 juurde. Siin on ülesande püstitus puudulik. Tekib palju küsimusi, millele pole vastuseid: Kuhu need asjad kadusid? Kas need kadusid korraga? Kas need kadusid teel koju? Kas nad jäid ülikooli mõnda auditooriumi? 

Selliseid küsimusi saab esitada veel ja lahendust pole võimalik üheselt määrata.    

**Ülesanne 2.** Ruut ja ring
~~~~~~~~~~~~~~~~~~~~~~~~~~~~


Ringi sisse on joonistatud ruut, mille külje pikkus on a. Leida ringi pindala. 

.. image:: _static/l04_fig1.gif

Siin on tegemist täpselt defineeritud geomeetriaülesandega. Peale ülesandest arusaamist on vaja lahendusplaani. On vaja välja selgitada sisend (ristküliku külg) ja väljund (ringi pindala) ja kasutada sobivat tähistust.  Edasi on vaja välja selgitada seos sisendi ja väljundi vahel, mis viib lahenduseni. See võib sisaldada vahepealsete tulemuste arvutamist, nt ristküliku diagonaali arvutamist. On vaja kasutada tasandilise geomeetria põhiteadmisi (antud juhul Pythagorase teoreemi). Täiendame joonist 

.. image:: _static/l04_fig2.gif

ja esitame lahenduse kahe sammuna:

.. centered::
    :math:`d=\sqrt{a^2+a^2}=\sqrt{2}a`
    :math:`S=\frac {\pi d^2}{4}= \frac {\pi a^2}{2}`

**Ülesanne 3.** Hundi, kitse ja kapsa üle jõe viimine 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Mees peab ületama jõe paadiga, millesse mahub peale tema ainult üks kaaslane. Ta peab üle jõe viima hundi, kitse ja kapsapea. Mees peab tegutsema nii, et samal ajal, kui ta ise on paadiga jõel, ei sööks hunt ära kitse ega kits kapsapead. 

Seda tüüpi ülesanne sisaldab loogikat. Tulemuseks ei ole arvutatav väärtus nagu ülesandes 2, vaid rida käike, mis esitavad üleminekut algseisundist (kõik tegelased on ühel pool jõge) lõppseisundisse (kõik tegelased on teisel pool jõge). 

.. note::
   Leida ülesandele vähemalt üks lahendus.

**Ülesanne 4.** 
~~~~~~~~~~~~~~~
Joonisel on esitatud Pascal'i arvude kolmnurk

.. image:: _static/l04_fig4.gif

Äärmistel kohtadel on arv 1. Ülejäänute korral on väärtuseks kahe lähima arvu summa arvule vahetult ülemisel real. Kuidas arvutada kombinatsioonide arvu *n* elemendist *k* kaupa

.. centered::
    :math:`C_{k}^n=\frac {n!(n - k)!}{k!}`
    

kus 

.. centered::
    :math:`n!=1\cdot 2 \cdot 3 \cdot \ldots \cdot n`

kasutades Pascali kolmnurka?
Kuidas on Pascali kolmnurga arvud seotud kordajatega valemis  

.. centered::
    :math:`(x + y)^n`

peale valemi lahtikirjutamist? 
Toodud näited illustreerivad olukordi, mis tekivad ülesannete lahendamisel. 


Ülesande lahendamise protsess (problem solving)  
-----------------------------------------------
Ülesande lahendamise arvutil võib jagada järgmisteks etappideks:

1. Algoritmi koostamine ja esitamine.
2. Programmi koostamine mingis konkreetses programmeerimiskeeles.
3. Programmi sisestamine arvutisse.
4. Programmi testimine ja silumine.
5. Programmi käivitamine arvutis, andmete sisestamine ja tulemuse saamine arvutist.


.. index::
    single: algoritm
    
.. _algoritm:    

Algoritm
--------

Mõiste *‘algoritm’* on tuletatud 9. sajandi Pärsia matemaatiku Mohammed al-Khowarizmi nimest. Al-Khowarizmi on Algorismus (ladina keeles) - algorithm.

Esitame nüüd algoritmile täpsema definitsiooni.

**Algoritm**  on  täpselt defineeritud (arvutuslik) protseduur, mis koosneb instruktsioonide hulgast, mis saab sisendina ette mingi väärtuse või väärtuste hulga ja leiab väljundiks mingi väärtuse või väärtuste hulga. Teiste sõnadega, algoritm on protseduur, mis võtab andmed ja manipuleerib nendega, järgides ettekirjutatud samme ja leiab otsitavad väärtused.

.. image:: _static/l04_fig8.gif 

Kokkuvõtvalt, algoritm on arvutispetsialistide kõnepruugis lihtsalt protseduur. Erinevate elukutsete inimestel on erinev vorm oma töövoost ja nad nimetavad seda erinevalt. Näiteks kokk järgib protseduuri, mida nimetatakse  retseptiks. Retsept kirjeldab algoritmi, mis teisendab rea sammude abil toiduained (sisend) mingiks toiduks (väljund). Algoritm hõlmab lahenduse kogu loogikat. Seega ülesande lahendamine jaotub kaheks etapiks:

* algoritmi koostamine, mis lahendaks ülesande,
* algoritmi teisendamine programmiks.

Viimast protsessi nimetatakse programmeerimiseks ja see protsess on suhteliselt lihtsam, sest kogu loogika on juba olemas ja tuleb lihtsalt järgida kasutatava programmeerimiskeele süntaksit. Esimene etapp võib olla komistuskiviks paljudele ja seda kahel põhjusel:

* esitatakse väljakutse vaimsetele võimetele (mõtlemisele), et leida õige lahendus.
* see nõuab võimet selgesti väljendada lahenduskäik täpselt samm-sammuliste isntruktsioonidena.

Teist oskust omandatakse ja täiustatakse pidevalt läbi praktika. 
   
.. index::
    single: algoritmi omadused


Algoritmi omadused
------------------
Algoritmil on neli olulist omadust:

1. Algoritmi iga samm peab olema *täpne*, st olema ühetähenduslik.
2. Algoritm peab olema *lõplik*. Vastasel juhul me ei saa probleemile lahendust.
3. Algoritm peab olema *efektiivne*, st ta peab andma probleemile korrektse vastuse.
4. Algoritm peab olema *üldine*, st ta peab lahendama ülesande iga eksemplari. Näiteks programm, mis leiab ringi pindala, peab töötama kõigi võimalike algandmete korral antud programmeerimiskeele ja arvuti korral. 

.. index::
    single: algoritmi esitus plokkskeemina
    
.. _algoritmi esitus plokkskeemina:    

Algoritmi esitus plokkskeemina
------------------------------

Algoritmi tavaliseks esitusviisiks on nn pseudokood, mis on segu loomuliku keele sõnadest, matemaatilistest märkidest ja programmeerimiskeele võtmesõnadest. 
Algoritmi saab esitada ka graafiliselt, nt plokkskeemina. Vaatleme järgnevalt plokkskeemis kasutatavaid kujundeid:

.. index::
    single: plokkskeem
    
.. _plokkskeem:    


.. image:: _static/l04_fig9.gif 

Ringi pindala
~~~~~~~~~~~~~
1. Esitame ülesande 2 lahenduse plokkskeemina:

 .. image:: _static/l04_fig20.gif 

Siin ülesande sisendiks on ruudu külje pikkus *a*. Märgime siinjuures, et jätsime vahele diagonaali arvutamise, sest ringi pindala *S* saame arvutada otse otse ruudu külje pikkuse kaudu. 
Lahendame nüüd selle ülesande arvutil, tehes läbi ka ülesande lahendamise teised etapid. 


2. Koostame programmi, kasutades programmeerimiskeelt Python:

.. sourcecode:: py3

    from math import *

    a = int(input("Sisesta külje pikkus a: "))
    S = pi*a*a/2
    print("Kui ruudu külje pikkus on " + str(a) + ", siis ringi pindala on " +  str(S))

3. Enamasti me teostame sammud 2 ja 3 korraga, st programmi koostamise käigus sisestame selle ka arvutisse.

4. Selgub, et meie programm jääb hätta siis kui kasutaja ei sisesta midagi või sisestab külje pikkuse asemel midagi muud, nt "kuus". Seega saab öelda, et antud programm töötab vaid korrektse arvulise sisendi korral, vigase sisendi korral programmi töö lõpeb veaga.   

5. Käivitame programmi konkreetse küljepikkuse jaoks ja leiame ringi pindala.  

Robotkilpkonn
~~~~~~~~~~~~~

.. image:: _static/l04_fig10.gif 

Tuleme tagasi eelmistest paragrahvidest tuttava robotkilpkonna juurde. Oletame, et robotkilpkonn 
liigub ristkülikukujulisel mänguväljakul, mille mõõtmed pole teada:

 .. image:: _static/l04_fig11.gif 
 
Kilpkonn oskab sooritada järgmiseid tegevusi:

 .. image:: _static/l04_fig12.gif  
 
**Ülesanne 5.** Kolm sammu edasi ja ümberpöörd
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 Robotkilpkonn asub näoga seina poole selliselt, et seinani on vähemalt 3 sammu. Kilpkonnal on vaja liikuda kolm sammu edasi ja pöörata näoga tuldud tee suunas (pöörata ümber).   

.. image:: _static/l04_fig13.gif  

Lahenduse võib esitada järgmise plokkskeemina:

.. image:: _static/l04_fig14.gif  

**Ülesanne 6.** Kui võimalik, kolm sammu  edasi ja ümberpöörd 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Robotkilpkonn asub näoga seina poole ja ei ole teada, mitu sammu on seinani. Kilpkonnal on vaja liikuda kolm sammu edasi ja pöörata näoga tuldud tee suunas (pöörata ümber). Kui seinani on vähem kui kolm sammu, siis liikuda seinani ja pöörata ümber. 

.. image:: _static/l04_fig15.gif  

Nüüd on lahendus juba veidi keerulisem:  

.. image:: _static/l04_fig16.gif  

**Ülesanne 7.** Ring ümber mänguväljaku 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Kilpkonn asub ruudustiku vasakus ülemises nurgas näoga paremale. Ruutude arv ei ole teada. Kilpkonnal on vaja läbi käia suurim ring ja jõuda esialgsesse positsiooni tagasi. Koostada plokkskeem.  

.. image:: _static/l04_fig17.gif  

**Ülesanne 8.** Liikumine takistusest mööda
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Kilpkonn asub ruudustiku suvalisel ruudul. Ruutude arv ei ole teada. Ruudustikul võib olla sirge vahesein, mille otsad ei ulatu ruudustiku servani. Kilpkonnal on vaja liikuda ruudustiku selle välisseinani, mille poole ta näoga on. Koostada plokkskeem.  

.. hint:: 
    Antud ülesande korral võib olla olukord, kus takistus asub roboti ees

    .. image:: _static/l04_fig18.gif  

    või siis ei asu

    .. image:: _static/l04_fig19.gif  

.. note:: 

    Laadides alla väikese programmi, on võimalik kilpkonna liikumist modelleerivate plokkskeemide koostamist testida ka arvuti abil: http://www.physicsbox.com/indexrobotprogen.html


Lisalugemist
------------

Kuna algoritmi koostamine on ülesande lahendamise kõige olulisem osa, siis on ülesannete lahendusprotsessi uuritud ka süstemaatiliselt. Üheks selle ala klassikuks võib lugeda Ungari matemaatikut George Pólyat, kes uuris ülesande lahendamise protsessi lähemalt ja avaldas oma kuulsa raamatu "Kuidas seda lahendada?". Oma raamatus toob ta välja neli etappi, millega ülesande lahendajal tuleb kokku puutuda. Esitame siinkohal tema kuulsa tsitaadi:

.. index::
    single: Pólya
    
.. _Pólya:    

George Pólya:

*Suur avastus lahendab suure probleemi, kuid väike avastus on olemas iga probleemi lahenduses. Sinu probleem võib olla tagasihoidlik, kuid kui see esitab väljakutse sinu uudishimule ja toob mängu sinu leiutaja omadused. Kui sa seda lahendad omaenda vahenditega, võid kogeda pingutust ja nautida avastuse triumfi. Sellised kogemused võivad vastuvõtlikus eas tekitada vajaduse vaimse töö järele ja jätta jälje terveks eluks.*

George Pólya selgitab oma raamatus ülesande lahendamise nelja etappi, mida soovitame ka antud kursuse ülesannete korral hoolikalt järgida. 

1. Ülesandest arusaamine
~~~~~~~~~~~~~~~~~~~~~~~~
* Mis on otsitavaks? Mis on antud? Milles seisnevad ülesande tingimused?
* Kas tingimusi on võimalik üldse rahuldada? Kas tingimused on otsitava tulemi määramiseks piisavad? Kas nende hulgas on ülearuseid? Kas tingimused on vastuolulised?
* Valmista joonis. Võta kasutusele sobiv tähistus.

2. Lahendamise idee ja sellele vastava plaani koostamine
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* Kas tead mõnd teist antud ülesandega seonduvat ülesannet?
* Vaatle otsitavat! Püüa meenutada mõnda tuntud ülesannet, milles on sama või sarnane otsitav.
* Kas on võimalik seda ülesannet ära kasutada? Kas peab sisse tooma mingi abielemendi, mis võimaldaks varem lahendatud ülesannet ära kasutada?
* Kas saab ülesannet teisiti sõnastada? Veel teisiti? Pöördu tagasi definitsiooni juurde.
* Kui sa ei suuda antud ülesannet lahendada, siis proovi lahendada kõigepealt mõni temaga seonduv ja võib-olla lihtsam ülesanne. Või üldisem ülesanne? Või erijuht? Või sarnane ülesanne? Jättes osa tingimustest kõrvale, kuivõrd on otsitav siis määratud?
* Kas kasutasid kõiki andmeid? Kas kasutasid kõiki tingimusi? Kas arvestasid kõiki ülesandes sisalduvaid mõisteid?

3. Lahendusplaani täitmine
~~~~~~~~~~~~~~~~~~~~~~~~~~
* Veendu iga sammu õigsuses.

4. Tagasivaade
~~~~~~~~~~~~~~
* Kas saad kontrollida tulemust? Kas saad kontrollida lahenduskäiku?
* Kas saad tulemust teisiti leida?
* Kas tulemus või lahenduskäik on kasutatav mõne teise ülesande korral?







Koduülesanded
-------------

1. Kuupäeva esitamine sõnena
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Kirjutage funktsioon ``kuupäev_sõnena``, mis võtab argumentideks päeva, kuu ja aasta (arvudena) ning tagastab sõne, mis esitab kuupäeva kujul *<päev>. <kuu nimi> <aasta>* (nt. *24. veebruar 1918*).

Seejärel kirjutage programm, mis küsib kasutajalt arvudena päeva, kuu ja aasta. Kui neile vastav kuupäev on legaalne, siis kuvada ekraanile vastav kuupäev sõnena, vastasel juhul kuvada ``'Viga: mittelegaalne kuupäev'``.

Kasutage abifunktsioonidena praktikumi ajal loodud funktsioone (vt. ülesandeid 2-5).

2. Õpikuülesanne
~~~~~~~~~~~~~~~~
Lahendage `õpiku 5. peatükist <http://courses.cs.ut.ee/2011/programmeerimine/uploads/Raamat/ch05.html>`_ ülesanded 13 ja 14.

3. Klaveri mahutamine
~~~~~~~~~~~~~~~~~~~~~
Ülikool on ostnud endale uue klaveri peahoone aula tarbeks. Paraku unustati  kontrollida, kas see klaver üldse välisuksest sisse mahub. Kirjutada programm, mis küsib kasutajalt klaverit sisaldava kasti kolm mõõdet (pikkus, laius, kõrgus) ning ukse laiuse ja kõrguse ning vastab, kas klaver on võimalik aulasse sisse toimetada.

4. Paprikasupp
~~~~~~~~~~~~~~
Kausitäis paprikasuppi jahtub minuti jooksul 19% võrra supi ja ruumi temperatuuride vahest. Koostage programm, mis väljastab supi temperatuuri iga minuti kohta, kui supi algtemperatuur on 90 kraadi. Ruumi temperatuur on 20 kraadi.

Hoiatus: olge ettevaatlik tsükli jätkamistingimusega! Kui lasete supil jahtuda 20 kraadini, peate väga kaua ootama. Mõelge ja/või proovige järele, miks.

5. Kujundid
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


Soovituslik lisaülesanne: Ruudustik
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Kirjutage funktsioon ``ruudustik``, mis võtab argumentideks ruutude arvu vertikaalsuunal, ruutude arvu horisontaalsuunal ja ruudu küljepikkuse, ning joonistab kilpkonna abil vastava ruudustiku. Näiteks funktsiooni väljakutse ``ruudustik(4, 6, 20)`` peaks tegema sellise ruudustiku:

.. image:: _static/ruudustik.png

.. topic:: Lisaülesande lisa
    
    Uurige kilpkonna dokumentatsioonist, kuidas värvida soovitud ala (http://docs.python.org/py3k/library/turtle.html). Seejärel proovige joonistada malelaud.