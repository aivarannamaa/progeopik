*************************
8. Järjendite muteerimine
*************************

Selle peatüki põhiteema on järjendite elementhaaval koostamine ning analüüsimine. Lisaks vaatame üle mõned uued skeemid järjendite kasutamiseks.



Järjendite koostamine elementhaaval
===================================
Siiani oleme järjendi kirjapanekul loetlenud alati kõik tema elemendid. Paraku pole alati võimalik kõiki vajaminevaid elemente korraga välja tuua. Seetõttu võimaldab Python juba loodud järjendeid hiljem täiendada. Katseta järgnevat programmi:

.. sourcecode:: py3

    # loome tühja (st. 0-elemendiga) järjendi ja kuvame selle ekraanile
    a = []  
    print(a)
    
    # lisame järjendisse ükshaaval 3 elementi
    a.append(1)
    a.append(5)
    a.append(9)
    
    # uurime järjendi sisu uuesti
    print(a)


Nagu nägid, oli programmi lõpus järjendi elementideks ``1``, ``5`` ja ``9``. Selle saavutamiseks kasutasime meetodit ``append``, mis lisab järjendi lõppu uue elemendi, st. muudab olemasolevat järjendit.

Taolist järjendite elementhaaval "kasvatamist" kasutatakse siis, kui järjendi elemendid selguvad alles programmi töö käigus. Kõige tavalisema skeemi puhul luuakse kõigepealt tühi järjend ning järjendi sisu täiendatakse tsüklis:

.. sourcecode:: py3
            
    # alustame jälle tühja järjendiga
    arvud = []

    while True:
        sisend = input('Sisesta täisarv (lõpetamiseks vajuta lihtsalt ENTER): ')
        if sisend == '':
            break
        else:
            arv = int(sisend)
            arvud.append(arv)

    print('Sisestati ' + str(len(arvud)) + ' arvu')
    print('Sisestatud arvud: ' + str(arvud))
    print('Arvude summa on: ' + str(sum(arvud)))

Antud näite puhul oli tsükli aluseks kasutaja tegevused. Samahästi võiksime kasutada järjendi koostamisel kindla korduste arvuga ``for``-tsüklit:

.. sourcecode:: py3
    
    ruudud = []
    
    for arv in range(1, 10):
        ruudud.append(arv ** 2)
    
    print('Arvude 1..9 ruudud on: ' + str(ruudud))

Harjutus 1. Failist järjendisse
-------------------------------
Nagu juba teate, võib ``for``-tsükli aluseks olla ka mingi tekstifail.

Kirjuta programm, mis loeb tekstifailist ükshaaval ridu (eeldame, et igal real on üks arv) ning koostab selle käigus järjendi, mis sisaldab failist leitud paarisarve. Koostatud järjend kuvada ekraanile.


Juhuslike järjendite genereerimine
----------------------------------
Selle asemel, et harjutustes järjendeid ise sisse toksida, võime kasutada ka juhuslikult genereeritud arvujärjendeid:

.. sourcecode:: py3

    from random import randint
    
    arvud = []
    for i in range(100):
        # imiteerime täringuviskamist
        arvud.append(randint(1,6))
    
    print(arvud)

Harjutus 2. Juhuslik järjend
----------------------------
Kirjuta funktsioon ``juhuslik_järjend``, mis võtab argumendiks järjendi elementide arvu ning kaks argumenti arvuvahemiku määramiseks ning tagastab vastava juhuslikult genereeritud arvujärjendi. (Seda funktsiooni võid edaspidi kasutada alati, kui on tarvis genereerida mingi juhuslik järjend).

Genereeri loodud funktsiooni abil mitu erineva pikkusega järjendit, aga nii, et arvuvahemik on kõigil juhtudel sama.

Kirjuta ka lihtne abifunktsioon ``keskmine``, mis annab järjendi arvude aritmeetilise keskmise (siin võid kasutada Pythoni funktsioone ``sum`` ja ``len``).

Uuri, kuidas sõltub järjendite keskmine järjendi pikkusest.


Järjendite teisendamine
=======================
Järgnevates näidetes ja ülesannetes võetakse aluseks üks või mitu järjendit ning koostatakse nende põhjal uus järjend.

Järjendi elementide teisendamine
--------------------------------
Tihti on tarvis teha mingit operatsiooni järjendi iga elemendiga ning salvestada tulemused uude järjendisse. Uuri ja katseta järgnevat näiteprogrammi:

.. sourcecode:: py3

    sõned = ['1', '14', '69', '42']
    
    arvud = []
    for sõne in sõned:
        arvud.append(int(sõne))
    
    print(arvud)

Harjutus 3. Sõned arvudeks
--------------------------
Kirjuta eelneva programmi näitel funktsioon ``sõned_arvudeks``, mis võtab argumendiks sõnede järjendi ning tagastab vastava arvude järjendi. (Võid praegu eeldada, et argumendiks antud järjendis sisalduvad vaid sellised sõned, mida saab arvudeks teisendada).



Järjendi filtreerimine
----------------------
Filtreerimiseks nimetame seda operatsiooni, mis moodustab mingi järjendi põhjal uue järjendi, milles sisalduvad teatud tingimustele vastavad väärtused algsest järjendist. Uuri ja katseta järgnevat näidet:

.. sourcecode:: py3

    def paarisarvud(arvud):
        paaris = []
        for arv in arvud:
            if arv % 2 == 0:
                paaris.append(arv)
        
        return paaris
    
    print (paarisarvud([1,2,3,4,5,6,7]))

Harjutus 4. Arvude tuvastamine
------------------------------
Kirjuta funktsioon ``naturaal_sõned``, mis võtab argumendiks sõnede järjendi ning tagastab uue sõnede järjendi, milles sisalduvad vaid need esialgse järjendi väärtused, mis kujutavad naturaalarve (st. ``sõne.isnumeric() == True``). NB! Sõnede teisendamist arvudeks pole selles ülesandes tarvis.

Harjutus 5. Arvude tuvastamine koos teisendamisega
--------------------------------------------------
Kirjuta funktsioon ``filtreeri_ja_teisenda``, mis võtab argumendiks sõnede järjendi ning tagastab täisarvude järjendi, mis vastab esialgse järjendi nendele elementidele, mis kujutavad täisarve. Näide selle funktsiooni kasutamisest:

.. sourcecode:: py3

    >>> filtreeri_sõned_arvudeks(['1', 'Tere', '2', '3'])
    [1, 2, 3]

.. hint:: 

    Kui kasutad abifunktsioone ``sõned_arvudeks`` ja ``naturaal_sõned``, siis saab selle funktsiooni väga lühidalt kirja panna.
    

Järjendite ühend
----------------
Järgnevas näites võtab funktsioon ``ühend`` argumendiks kaks järjendit ning tagastab uue järjendi, mis sisaldab mõlema argumentjärjendi erinevaid väärtusi ühekordselt:

.. sourcecode:: py3

    def ühend(j1, j2):
        tulemus = []
        
        for element in j1:
            if not (element in tulemus):
                tulemus.append(element)
                
        for element in j2:
            if not (element in tulemus):
                tulemus.append(element)
        
        return tulemus
    
    print(ühend([1, 2, 3, 2], [1, 6, 6]))

Harjutus 6. Järjendite ühisosa
------------------------------
Kirjuta funktsioon ``ühisosa``, mis võtab argumendiks kaks järjendit ning tagastab **uue** järjendi, mis sisaldab (ühekordselt) neid väärtusi, mis esinevad mõlemas järjendis.


Järjendite kasutamine "andmebaasina"
====================================
Järgnevates näidetes kasutame me mitut järjendit, mille elemendid on omavahel kuidagi seotud -- nt. järjendi ``a`` element positsioonil ``16`` (st. ``a[16]``) on seotud järjendi ``b`` samal positsioonil oleva elemendiga (st. ``b[16]``). Uuri ja katseta järgnevat näidet:

.. sourcecode:: py3

    eesnimed = ['Isaac', 'Leonhard', 'David']
    perenimed = ['Newton', 'Euler', 'Hilbert']
    
    n = len(eesnimed) 
    for i in range(n):
        print(eesnimed[i] + ' ' + perenimed[i])

Kuna selles näites oli meil tarvis võtta element mõlemast järjendist samalt positsioonilt, siis ei piisanud meile "tavalisest" ``for``-tsükli variandist, mis võtab elemente lihtsalt järjest, ignoreerides nende indekseid. Seetõttu võtsime tsükli aluseks mitte järjendi vaid hoopis ``range``-i abil genereeritud indeksite loetelu.

Taolistes ülesannetes eeldame, et seotud järjendid on sama pikad, seetõttu on ükskõik, millise järjendi pikkuse järgi me loendurit kontrollime.


"Andmebaasi" sisselugemine failist
----------------------------------
Et teha järgnevaid näiteid ja ülesandeid realistlikumaks, siis loeme omavahel seotud järjendid sisse tekstifailidest. Kõige lihtsam võimalus oleks kirjutada erinevate järjendite sisu eri failidesse ning lugeda nad sealt järjenditesse, üks järjend/fail korraga. Sellise lähenemise puhul on aga failide koostamine ebamugav, kuna me peame hoolikalt jälgima, et seotud andmed (nt. sama inimese eesnimi ja perenimi) satuksid mõlemas failis ikka samadele ridadele.

Seetõttu kasutame me teistsugust võtet: kirjutame omavahel seotud andmed failis samale reale ning faili sisselugemisel kasutame ülalpool tutvustatud sõnemeetodit ``split``. Koosta tekstifail ``nimed.txt``, mille igal real on tühikuga eraldatud eesnimi ja perenimi ning katseta järgnevat programmi:

.. sourcecode:: py3

    # teeme valmis tühjad järjendid
    eesnimed = []
    perenimed = []
    
    # loeme failist järjenditesse
    f = open('nimed.txt')
    for rida in f:
        nime_osad = rida.split()
        eesnimed.append(nime_osad[0])
        perenimed.append(nime_osad[1])
        
    f.close() # faili meil enam tarvis pole
    
    # hakkame järjendeid töötlema
    n = len(eesnimed) 
    for i in range(n):
        print('Eesnimi on: ' + eesnimed[i])
        print('Perenimi on: ' + perenimed[i])


.. topic:: Millal on mõtet salvestada andmed järjendisse?

    Kui me soovime failist loetud (või kasutaja käest küsitud) järjendi põhjal arvutada midagi lihtsat (nt. arvude summat või maksimaalset arvu), siis pole järjendi koostamine tegelikult isegi vajalik -- piisaks ühest abimuutujast, mille väärtust me iga järgmise arvu sisselugemisel sobivalt uuendame. Andmete järjendisse salvestamine on oluline näiteks siis, kui andmeid on vaja mitu korda läbi vaadata, sest järjendi korduv läbivaatamine on palju kiirem, kui faili korduv lugemine.

Harjutus 7. Eksami tulemused
----------------------------
Eksami tulemused on salvestatud faili, kus igal real on tudengi täisnimi, koma ja saadud punktide arv (nt. ``Jaan Tamm,24``). Maksimaalne eksami eest saadav punktide arv on 40. Õppejõud soovib näha nende tudengite nimesid ja tulemusi, kes said eksamil vähem, kui 50% punktidest. Kirjuta programm selle probleemi lahendamiseks.

.. hint::
    Meetod ``split`` annab kõik komponendid sõnedena!

Järjendi elementide muutmine
============================
Lisaks sellele, et olemasolevale järjendile on võimalik elemente lõppu juurde lisada, saab muuta järjendis juba olemasolevaid elemente. Selleks tuleb teha omistamine kasutades järjendi indekseerimise süntaksit. Uuri ja katseta järgnevat programmi:

.. sourcecode:: py3

    a = [1, 2, 3]
    
    # muudame teist elementi (so. element järjekorranumbriga 1)
    a[1] = 22 
    
    print(a)

Nagu ikka, võib ka siin kasutada indeksina mingit täisarvulist muutujat.


Harjutus 8. Täringuvisete statistika
------------------------------------
Genereeri 100 täringuviske tulemust (kasutades eelpool defineeritud funktsiooni ``juhuslik_järjend``) ning salvesta tulemus muutujasse.

Koosta 6-elemendiline järjend ``statistika``, mis sisaldab täringuvisete statistikat -- avaldis ``statistika[0]`` peaks näitama, mitu korda tuli täringuviske tulemuseks 1, ``statistika[1]`` peaks näitama kahtede sagedust jne.

Kuva statistika ekraanile.

.. hint::

    Kusagil programmis võiks olla lause ``statistika = [0, 0, 0, 0, 0, 0]``


Muudetavate andmetüüpide omapärad
=================================
Järjendi muutmisel (nii ``append`` kui ``a[i] = x`` puhul) tuleb arvestada ühe omapäraga, mis tuleb ilmsiks siis, kui sama järjend on omistatud mitmele muutujale. Uuri järgnevat näidet ning ennusta, mida antakse selle programmi käivitamisel väljundiks:

.. sourcecode:: py3
    
    a = [1, 2, 3]
    
    b = a
    b.append(4)
    
    print(a)
 
Nagu nägid, ilmus ekraanile ``[1, 2, 3, 4]``, ehkki programmis ei paista, et kusagil oleks järjendisse ``a`` lisatud arv *4*. Selle omapära põhjus peitub real ``b = a``, mis mitte ei kopeeri muutuja ``a`` väärtust muutujasse ``b``, vaid hoopis paneb muutuja ``b`` viitama samale järjendile. Teisisõnu, ``b`` on sama järjendi alternatiivne nimi (ing.k. *alias*). Seetõttu, kui järjendit muuta kasutades nime ``b`` on muudatus näha ka nime ``a`` kaudu (ja vastupidi).

Kuna funktsiooni parameetrid on oma olemuselt samuti muutujad, siis sama efekt ilmneb ka siis, kui parameetrina antud järjendit muudetakse funktsiooni sees:

.. sourcecode:: py3

    def lisa(järjend, väärtus):
        järjend.append(väärtus)

    arvud = [1, 2, 3]
    lisa(arvud, 4)
    
    print(arvud)

Seda omapära võib vahepeal ka enda kasuks kasutada. Kui aga soovid parameetrina saadud järjendit arvutuse käigus muuta nii, et funktsioonist väljaspool muutusi näha poleks, siis tuleks teha saadud järjendist koopia, ning muudatused teha vaid koopiale. Koopia tegemiseks saab kasutada viilutamise süntaksi, jättes kirjutamata nii vasaku kui parema indeksi:

.. sourcecode:: py3
    
    a = [1, 2, 3]
    
    b = a[:] # a-st tehakse koopia
    b.append(4)
    
    print(a) # a väärtus on endine



Viitamisest täpsemalt
---------------------
Kas selline situatsioon, et erinevad muutujad viitavad samale objektile, on võimaliku ainult listide korral? Tehniliselt võttes ei -- muutujad ja omistamine toimivad alati samamoodi, hoolimata andmetüübist.

Kõik Pythoni väärtused on programmi käimise ajal esitatud mingite objektidena, mis asuvad kusagil arvuti mälus. Kui käivitatakse lause ``x = 7``, siis luuakse mälus objekt, mis tähistab arvu `7` ja muutujasse ``x`` salvestatakse tegelikult ainult viide sellele objektile. Kui me järgmisena käivitame lause ``y = x``, siis muutujasse ``y`` salvestatakse sama viit, mis on muutujas ``x``, aga uut täisarvu objekti ei looda. Seega nüüd viitavad muutujad ``x`` ja ``y`` samale objektile.

Erinevus listidest tuleb aga sellest, et täisarvu objekti ei ole võimaliku muuta, seetõttu ei ole ilma pingutamata võimalik isegi aru saada, kas need muutujad viitavad samale objektile või erinevatele objektidele, mis tähistavad sama arvu. Seetõttu ei pidanud me ei arvude ega sõnede puhul viitamise teema peale mõtlema.  

Viitamise teema täpsemal uurimisel on abiks funktsioon ``id``, mis tagastab argumendiks antud väärtuse (e. objekti) aadressi arvuti mälus -- see ongi see viide, mida muutujad sisaldavad. Järgnevas näites luuakse kaks samaväärset sõneobjekti, mille kummagi viide salvestatakse erinevasse muutujasse:

.. sourcecode:: py3

    >>> a = "tere hommikust!"
    >>> b = "tere hommikust!"

Veendume ``id`` abil, et muutujad viitavad erinevatele objektidele:

.. sourcecode:: py3

    >>> id(a)
    48829968
    >>> id(b)
    48830088

.. todo::

    Skeem


Nüüd kopeerime ühe viida uude muutujasse:

.. sourcecode:: py3

    >>> c = a
    >>> id(c)
    48829968    

Nagu näha, kopeeriti omistamisel muutujasse olemasoleva objekti viit, ja uut objekti ei loodud.

Kui proovisid seda eksperimenti lühemate sõnedega või väikeste arvudega, siis võis juhtuda, et Python vältis juba esimeste omistamiste juures kahe samaväärse objekti loomist ja omistas ``b``-le sama viite nagu ``a``-le. Arvude ja sõnede puhul on tal see vabadus, sest programmi tähendus sellest ei muutu. Listide korral aga on kindel, et järgmised omistamised tekitavad alati kaks uut objekti:

.. sourcecode:: py3

    >>> x = [1,2,3]
    >>> y = [1,2,3]
    >>> id(x)
    47840952
    >>> id(y)
    48787328    

Erinev ``id``-väärtus näitab, et tegemist on erinevate objektidega -- kui me ühte neist muteerime (näiteks ``append``-iga), siis teine sellest ei muutu. Kui me aga uue listi loomise asemel kopeerime viida, siis teeme sellega lihtsalt samale objektile uue nime:
    
.. sourcecode:: py3

    >>> z = x
    >>> id(z)
    47840952
    >>> z.append(4)
    >>> z
    [1, 2, 3, 4]
    >>> x
    [1, 2, 3, 4]
    >>> y
    [1, 2, 3]


Tuleb panna tähele, et muutuja muutmine ei ole sama, mis objekti muteerimine. Kui me omistame ``z``-le uue väärtuse, siis ``z`` lihtsalt kaotab seose eelmise objektiga -- algne objekt sellest ei muutu:

.. sourcecode:: py3

    >>> z = [6,7,8]
    >>> id(z)
    48766568
    >>> x            # x poolt viidatud objekt on sama, mis enne 
    [1, 2, 3, 4]
    >>> y
    [1, 2, 3]


Kokkuvõttes: omistamisel salvestatakse muutujasse ainult viit paremal pool näidatud väärtusele. Analoogselt toimib Python ka funktsiooni väljakutsel -- parameetrisse satub vaid viit argumendile. Päris uusi objekte saab luua literaale kasutades (aga nagu eespool mainitud, võib Python mittemuteeritavate andmetüüpide puhul siin ka objekte jagada) või kasutades mingit operatsiooni, mis teadaolevalt loob uue objekti. 

.. topic:: Kopeerimisest

    Nagu eespool põgusalt mainitud, saab listi objekte kopeerida viilutamise süntaksiga:
    
    .. sourcecode:: py3
    
        >>> x = [1,2,3]
        >>> y = x[:]
        >>> id(x)
        30988928
        >>> id(y)
        48829944
    
    
    Alternatiivina saab kasutada meetodit ``copy`` või teisendusfunktsiooni ``list``:
    
    .. sourcecode:: py3
    
        >>> a = [1,2,3]
        >>> b = a.copy()
        >>> c = list(a)
        >>> id(a)
        47840952
        >>> id(b)
        47844488
        >>> id(c)
        48830024
        

    Kui list sisaldab omakorda liste, siis kopeerimine toimub ainult välimisel tasemel:
    
    .. sourcecode:: py3
    
        >>> a = [1,2,[3,3]]
        >>> b = a.copy()
        >>> id(a[2])
        47839032
        >>> id(b[2])
        47839032
        >>> a[2].append(4)
        >>> a
        [1, 2, [3, 3, 4]]
        >>> b
        [1, 2, [3, 3, 4]]

    "Sügava" koopia tegemiseks tuleks kasutada funktsiooni ``deepcopy`` moodulist ``copy``:
    
    .. sourcecode:: py3
    
        >>> from copy import deepcopy
        >>> a = [1,2,[3,3]]
        >>> b = deepcopy(a)
        >>> a[2].append(4)
        >>> a
        [1, 2, [3, 3, 4]]
        >>> b
        [1, 2, [3, 3]]
    
            
Ülesanded
=========

1. Tagasivaade
--------------
Loe läbi selle peatüki lõpus olev :ref:`tagasivaade_1-8`


2. Lausegeneraator
------------------
* Defineeri funktsioon ``lause``, mis **võtab argumendiks** 3 sõna (sõnena), ning **tagastab** neist kombineeritud lause (muuhulgas lisab tühikud ja punkti).

* Loo 3 tekstifaili -- ``alus.txt``, ``oeldis.txt`` ning ``sihitis.txt``. Kirjuta igasse neist 10 sõna eraldi ridadele:

    * ``alus.txt`` - peaks sisaldama nimisõnu või nimesid nimetavas käändes (nt. `Margus`)
    * ``oeldis.txt`` - oleviku vormis, 3. isikus tegusõnad (nt. `õpetab`)
    * ``sihitis.txt`` - nimisõna osastavas käändes (nt. `tudengeid`)

* Kirjuta funktsioon, mis võtab argumendiks failinime ning tagastab vastava faili read järjendina (reavahetuse sümbolid tuleks eemaldada meetodiga ``strip``).

* Kirjuta programm, mis 
    
    #. loeb mainitud kolme faili sisud järjenditesse (``alused``, ``oeldised``, ``sihitised``), kasutades selleks eelmises punktis defineeritud funktsiooni
    #. genereerib 3 juhuslikku täisarvu vahemikust 0..9
    #. võtab järjendite vastavatelt positsioonidelt aluse, öeldise ja sihitise ning koostab neist lause kasutades eelnevalt defineeritud funktsiooni ``lause``.
    #. kuvab moodustatud lause ekraanile

* Muutke programmi selliselt, et see genereeriks ja väljastaks (lõpmatus tsüklis) iga ENTER vajutuse peale uue lause.


3. Palkade analüüs
------------------
Antud on tekstifail :download:`palgad.txt <downloads/palgad.txt>`, kus igal real on töötaja nimi, tema vanus ja kuupalk. Kirjutada programm mis arvutab ja väljastab antud andmete põhjal:

    * kõige suurema palgaga töötaja nime ja palga suuruse (vihje: suurima palga otsimisel jätke meelde, milliselt positsioonilt sa selle leidsid)
    * keskmise palga
    * keskmisest palgast rohkem teenijate arvu
    * keskmised vanused eraldi neile, kes teenivad keskmisest palgast vähem (või samapalju) ning neile, kes teenivad keskmisest palgast rohkem

4. Eesti-Inglise sõnaraamat
---------------------------
Lae alla Eesti-Inglise sõnastik(:download:`sonastik.txt <downloads/sonastik.txt>`, kodeeringus UTF-8). Selle igal real on kõigepealt inglisekeelne sõna või väljend, seejärel tabulaatori sümbol (kirjutatakse Pythonis ``"\t"``) ning lõpuks eestikeelne vaste.

Kirjuta programm, mis loeb failist eestikeelsed ja inglisekeelsed väljendid eraldi järjenditesse ning võimaldab kasutajal küsida inglisekeelse sõna eestikeelset vastet (või vastupidi – võid ise valida)

.. note::
    
    Antud sõnastiku fail on veidi modifitseeritud variant Eesti Keele Instituudi poolt jagatavast failist (ftp://ftp.eki.ee/pub/keeletehnoloogia/inglise-eesti/en_et.current.wbt).

5. minu_shuffle
---------------
Pythoni ``random`` moodulis on funktsioon ``shuffle``, mis ajab argumendiks antud järjendis elementide järjekorra juhuslikult segamini:

.. sourcecode:: py3

    >>> from random import shuffle
    >>> a = [1, 3, 3, 4, 5, 5, 5, 6, 6]
    >>> shuffle(a)
    >>> a
    [5, 3, 6, 5, 5, 3, 4, 1, 6]

Kirjuta ise analoogne funktsioon ``minu_shuffle``, mis teeb sama (seejuures pole lubatud kasutada olemasolevat ``shuffle`` funktsiooni).

.. hint::

    .. sourcecode:: py3
    
        >>> from random import randint
        >>> randint(1,4)
        1
        >>> randint(1,4)
        1
        >>> randint(1,4)
        3
        >>> randint(1,4)
        2
        >>> randint(1,4)
        4
        >>> randint(1,4)
        2
        >>> randint(1,4)
        2

.. hint::

    Üks võimalus on valida iga listi elemendi jaoks juhuslikult uus positsioon ...
    
.. hint::

    ... ja vahetada need kaks elementi omavahel.
    

6. Eesti filmide statistika (raskem)
------------------------------------
Veebisait http://www.imdb.com kogub ja jagab informatsiooni filmide kohta. Aadressilt ftp://ftp.funet.fi/pub/mirrors/ftp.imdb.com/pub/ saab IMDB poolt kogutud infot alla laadida pakitud tekstifailidena.

Fail :download:`filmid.zip (4.5MB) <downloads/filmid.zip>` on koostatud faili "countries.list.gz" põhjal, ning see sisaldab filmide (ja telesaadete) loetelu koos riigi nime ning valmimise aastaga. Lae see fail alla ning paki lahti.

.. note:: 

    Filmide fail on lahtipakitult ligi 18MB suurune. Kui sul ei õnnestu (Windows'is) seda faili avada Notepad'iga, siis kasuta vabavaralist programmi Notepad2 (http://www.flos-freeware.ch/notepad2.html).
    
Failis ``filmid.txt`` on ühe filmi andmed ühel real, kujul *<nimi><tühik>(<aasta>)<tabulaator><riik>*. (Notepad2-s saad tühikuid ja tabulaatoreid eristada, kui märgite menüüs *View* valiku *Show whitespace*).

Ülesandeks on kirjutada programm, mis otsib sellest failist üles Eestis valminud filmid/telesaated, ning koostab statistika selle kohta, mitu filmi/telesaadet mingil aastal valmis.

.. hint::

    Fail on kodeeringus ``UTF-8``, st. faili avamisel tuleks seda mainida: ``f = open("filmid.txt", encoding="UTF-8")``.
    
.. hint::

    Tabulaatorit kirjutatakse Pythoni sõneliteraalina nii: ``'\t'``.
.. hint::

    Võibolla tuleb kasuks uurida ülalpool antud ülesannet "Täringuvisete statistika".

.. hint::

    Kui sa loed järjenditesse kogu failis sisalduva info, siis võib Pythonil mälust puudu tulla. 
    
.. topic:: Lisaülesande lisa

    Täienda programmi selliselt, et see küsib (korduvalt) kasutajalt aastaarvu ning väljastab ekraanile kõik selle aasta Eesti filmid. Kui kasutaja sisestab tühisõne (st. vajutab lihtsalt ENTER), siis programm lõpetab töö. Selleks tuleb organiseerida sisseloetud filmid aastate kaupa eraldi.
    
    .. hint::
        
        Järjend võib sisaldada järjendeid: ``a = [[1, 2, 3], [5, 5, 6], [4, 4, 3]]``. Mõtle, mida võiks tähendada ``a[2][1]``?


.. _tagasivaade_1-8:

*Tagasivaade peatükkidele 1-8*
==============================
On teada, et mingi teema valdamiseks tuleb tegelda vaheldumisi nii teooria, kui praktikaga. Praeguseks oled harjutanud läbi kõik olulisemad Python keele võimalused ja nüüd on paras aeg astuda samm tagasi ning vaada juba läbitud materjalile uue, veidi kogenuma pilguga.

Avaldised vs. laused
--------------------
Kõik eelpool käsitletud Python keele elemendid saame jaotada kahte suurde gruppi: *avaldised* ja *laused*.

**Avaldised** on näiteks ``2``, ``2 + 3``, ``brutopalk`` ja ``sin(0.5) ** (x-1)`` -- kõigil neil on **väärtus** ja neid saab seetõttu kasutada nt. muutujate defineerimisel ja teistes keerulisemates avaldistes.

**Laused** (ing.k. *statements*) on näiteks omistamislause (``x = sin(0.5)``), tingimus- ja korduslaused (``if``, ``while`` ja ``for``) ja funktsioonide definitsioonid (``def``). Eri tüüpi lausete ühiseks omaduseks on see, et nad *teevad* midagi (nt. muudavad muutuja väärtust, defineerivad uue käsu, või teevad midagi tingimuslikult või korduvalt).

Nii avaldiste, kui lausete juures on oluline see, et neid saab panna üksteise sisse. Näiteks operaatori ``+`` kasutuse üldskeem on ``<avaldis1> + <avaldis2>``, kusjuures nii ``avaldis1`` kui ``avaldis2`` võib olla samuti mingi liitmistehe. ``if``-lause põhiskeem on:

.. sourcecode:: none

    if <avaldis>:
        <laused1>
    else:
        <laused2>

kusjuures nii ``laused1``, kui ``laused2`` võivad sisaldada suvalisi lauseid, sh. ``if``-lauseid, mille sees võib olla omakorda suvalisi lauseid.

.. note::
    Funktsiooni väljakutsed (nt. ``sin(0.5)``) on tehniliselt küll alati avaldised aga mõnesid funktsioone kasutatakse tavaliselt lausetena (nt. ``turtle.forward(100)``, või ``print("Tere")``). Seega, natuke lihtsustades võiks öelda, et nende funktsioonide väljakutsed, mis midagi arvutavad, on avaldised ja teiste funktsioonide väljakutsed, mis midagi teevad, on laused.

Muutujad
--------
Muutujad võimaldavad meil tegelda väärtustega ilma, et me peaks mainima mingit konkreetset väärtust. Näiteks, kui me salvestame kaks kasutaja poolt sisestatud arvu muutujatesse ``a`` ja ``b``, siis nende kokku liitmisel ei huvita meid enam, mis on nende muutujate konkreetne väärtus. 

Soovitav on lugeda uuesti läbi 2. peatüki osa :ref:`muutujad`, tõenäoliselt näed nüüd muutujate olemust juba uue pilguga.

Funktsioonid
------------
Kui muutujad võimaldavad meil kasutada mingit väärtust ilma, et me peaksime mõtlema mingile konkreetsele väärtusele, siis funktsioonid võimaldavad meil midagi teha või arvutada ilma, et me peaksime alati mõtlema selle peale kuidas see toiming või arvutus täpselt tehakse. Visake pilk peale järgnevale programmile:

.. sourcecode:: py3

    def kolmest_suurim(a, b, c):
        if a > b and a > c:
            return a
        elif b > a and b > c:
            return b
        else:
            return c
    
    print(kolmest_suurim(4, 15, 2))

Tõenäoliselt oskad isegi ilma funktsiooni definitsiooni süvenemata arvata, mida taoline programm ekraanile prindib. Põhjus on selles, et antud funktsiooni olemus tuleb välja juba tema nimest ja üldjuhul võime me eeldada, et funktsiooni tegelik definitsioon on tema nimele vastav. Seetõttu, kui meil on sobivad funktsioonid juba defineeritud, siis saame me programmi põhiosas (või järgmiste funktsioonide defineerimisel) töötada "kõrgemal tasemel", ilma "pisiasjade" pärast muretsemata.

Kuna funktsioonide teema on programmeerimise algkursuses tavaliselt tudengitele kõige hägusam, siis on soovitav lugeda uuesti läbi 5. peatükist vähemalt järgmised osad:

    * :ref:`Parameetrid vs. input<param-vs-input>`
    * :ref:`return vs. print <return-vs-print>`
    * :ref:`milleks-funktsioonid`
    

Tingimuslause
-------------
Tingimuslause (ehk ``if``-lause ehk hargnemislause) on oma olemuselt küllalt lihtne -- teatud tingimusel tuleb täita ühed laused ja vastasel juhul teised. Lisavõimalustena on Pythonis võimalik kirjutada ka üheharulisi tingimuslauseid (st. ilma ``else``-ta) ning mitmeharulisi (``elif``-iga).

Üks oluline punkt tingimuslause juures on lause päises antud tingimusavaldis. Nagu eelnevalt mainitud, on avaldiste moodustamiseks lõputult võimalusi -- võib kasutada konstante, muutujaid, tehteid, funktsiooni väljakutseid, või kõigi nende kombinatsioone. Tingimusavaldise juures on oluline, et avaldise tüüp oleks tõeväärtus, st. avaldise väärtustamisel saadakse kas ``True`` või ``False``. 

Mitme tingimuse kombineerimiseks saab kasutada operaatoreid ``and`` ja ``or``, tingimuse "ümberpööramiseks" on operaator ``not``. Ära unusta, et tingimuses saad kasutada ka isetehtud funktsioone, aga need peavad sel juhul tagastama tõeväärtuse.


Korduslaused e. tsüklid
-----------------------
Pythonis on kaks erinevat korduslauset -- ``while``-tsükkel, mis on väga paindlik ning ``for``-tsükkel, mis on lihtsam, aga mis ei sobi kõigil juhtumitel.

``for``-tsükli juures on oluline mõista, et tema tööpõhimõte on ``while``'ist kaunis erinev. Kui ``while``-tsükli kordused põhinevad mingil tingimusel, siis ``for``-tsükli kordused põhinevad mingil järjendil (või järjendisarnasel asjal, nt. failil või vahemikul).

Järjendid
---------
Järjendite abil saame koondada mingi hulga andmeid ühe nime alla.

Järjendid on vajalikud neil juhtudel, kus programmi kirjutades pole võimalik öelda, mitme "andmejupiga" peab programm töötama (vastasel juhul võiksime iga andmejupi jaoks võtta programmis kasutusele ühe muutuja).

Järjendeid saab programmi "sisse kirjutada", koostada teiste järjendite põhjal või lugeda failist. Kui järjendeid on vaja ükshaaval järjest läbi vaadata, siis on selleks kõige mugavam kasutada ``for``-tsüklit, kui on vaja lugeda järjendist mingit konkreetset elementi, siis tuleks kasutada indekseerimist.

Kust saab rohkem infot?
-----------------------
Kes soovib läbitud teemade kohta rohkem detaile või lihtsalt teist vaatenurka, siis soovitame lugeda läbi Pythoni ametliku `tutoriali`: http://docs.python.org/3/tutorial/.

Mis ootab ees?
--------------
Järgmistes peatükkides tulevad küll mõned uued teemad aga põhiliselt keskendume suuremate (ja huvitavamate) ülesannete lahendamisele, kasutades juba õpitud vahendeid.


Lisalugemine
============
Pööratud Poola notatsioon
-------------------------
Tänapäeval oleme harjunud kirjutama matemaatilisi avaldisi nõndanimetatud infiksnotatsioonis, kus tehtemärk on nende kahe arvu vahel, millega ta töötab. See tekitab tegelikult aga igasuguseid probleeme, seoses sellega, et vahel on raske öelda, mis järjestuses tehteid tegema peab. Koolis õpetatakse meile, et kõigepealt tuleb teha astendamised, siis korrutamised ja jagamised ning alles siis liitmised ja lahutamised. Kui tehteid tuleb mingis muus järjestuses teha, saab kasutada sulge.

Tegelikult on aga juba ammusest olnud tuntud viise avaldiste kirjutamiseks nii, et sulge pole vaja, kuid kõik tehete tegemise järjestused oleks ometi kirjeldatavad. Ehk tuntuim neist on nõndanimetatud postfiksnotatsioon ehk pööratud Poola notatsioon (Poola notatsioon on nii nimetatud, sest selle põhiline propageerija oli poola matemaatik Jan Łukasiewicz ja ta pakkus selle välja 1920. aastal; pööratud Poola notatsiooni pakkusid välja F. L. Bauer ja E. W. Dijkstra kuuekümnendates).

Selles kirjutatakse tehe mitte rakendatavate arvude vahele vaid vahetult nende järgi. Nii teisendatakse
2 + 3 avaldiseks 2 3 +. Kui üheks neist arvudest juhtub aga olema juba mõne eelneva tehte tulemus, siis täidabki selle arvu rolli just see tehtemärk. Nii saab näiteks 2 + 3 – 1 teisendada kujule 2 3 + 1 -. See tähendab siis seda, et kõigepealt tehakse liitmine 2 ja 3 vahel ning seejärel lahutamine selle liitmise tulemuse ja 1 vahel. Selline kirjutamisviis kaotab igasuguse vajaduse sulgude jaoks: (2 + 7) * 3 saab kirjutada ju lihtsalt kui 2 7 + 3 * kusjuures on üheselt selge, et kõigepealt tehakse 2 ja 7 liitmine ning alles siis korrutatakse selle tulemus ja kolm omavahel. Muuseas võib juhtuda, et järjest on ka kaks või kolm või isegi enam tehtemärki. Näiteks teiseneb 3 + 2 * (4 - 1) kujule 3 2 4 1 - * +.

Selle kirjapildi teine tõsine eelis on see, et see muudab aritmeetiliste avaldiste töötlemise arvuti jaoks kõvasti lihtsaks. Tuleb vaid meeles pidada, mis arvud parasjagu loetud on ning tehtemärki kohates kaks viimati lisatud arvu välja võtta, neile see tehe rakendada ning siis see tulemus uuesti meeles peetud arvude nimekirja lõppu lisada. Seega on väga lihtne koostada programm, mis antud avaldise tulemuse välja arvutab. Toomegi siinkohal programmi, mis seda teeb:

 
.. sourcecode:: py3

    rida = input("Sisesta avaldis: ")
    kasud = rida.split()
    
    # Töötle avaldis
    loend = []
    
    for kask in kasud :
        # Liitmine
        if kask == "+" :
            # asenda viimane element tulemusega
            loend[-1] = loend[-2] + loend[-1]
            # eemalda eelviimane element
            loend.pop(-2)
    
        # Lahutamine
        elif kask == "-" :
            loend[-1] = loend[-2] - loend[-1]
            loend.pop(-2)
    
        # Korrutamine
        elif kask == "*" :
            loend[-1] = loend[-2] * loend[-1]
            loend.pop(-2)
    
        # Jagamine
        elif kask == "/" :
            loend[-1] = loend[-2] / loend[-1]
            loend.pop(-2)
        else :
            # polegi käsk, seega loodetavasti hoopis number
            loend.append(float(kask))
    
    print("Tulemus on: " + str(loend[-1]))

Tegu on ka asjaga, mis on praktikas täiesti kasutust leidnud. Oma töötlemise lihtsuse tõttu ehitati selline arvutamise süsteem sisse mõningatesse võimsamatesse kalkulaatoritesse, mida kunagi müüdi. Viimase 15 aasta jooksul on see aga arvutusvõimsuse kasvu tõttu vaikselt kalkulaatorites asendunud meile loomulikuma koolis õpitud infiksnotatsiooniga.

