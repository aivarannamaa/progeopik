.. _listid2:

*********************************
8. Järjendid ja ``for``-tsükkel 2
*********************************

Selle peatüki põhiteema on järjendite elementhaaval koostamine ning analüüsimine. Lisaks vaatame üle mõned uued skeemid järjendite kasutamiseks.



Järjendite koostamine elementhaaval
===================================
Siiani oleme järjendi kirjapanekul loetlenud alati kõik tema elemendid. Paraku pole alati võimalik kõiki elemente korraga välja tuua. Appi tuleb järjendite liitmine:

.. sourcecode:: py

    >>> [1 ,2, 3] + [6, 4, 9]
    [1, 2, 3, 6, 4, 9]
    
    >>> [1] + [2] + [3]
    [1, 2, 3]
    
    >>> [1, 2, 3] + [4]
    [1, 2, 3, 4]
    >>> [1] + [2] + [3] + [1, 2, 3]
    [1, 2, 3, 1, 2, 3]
    
    >>> [1] + []
    [1]
    >>> [] + [1]
    [1]
    >>> [] + []
    []


Salvestades täiendatud järjendi samasse muutujasse, saavutame järjendi kasvamise efekti:

.. sourcecode:: py

    >>> a = []
    >>> a = a + [1]
    >>> a = a + [2]
    >>> a = a + [6]
    >>> a = a + [2]
    >>> a
    [1, 2, 6, 2]
    >>> a += [5]   # nagu arvude puhul, saab ka siin kasutada liitmisega omistamist
    >>> a
    [1, 2, 6, 2, 5]
 

Taolist järjendite elementhaaval kasvatamist kasutatakse siis, kui järjendi elemendid selguvad alles programmi töö käigus.  Kõige tavalisema skeemi puhul luuakse kõigepealt tühi järjend ning järjendi sisu täiendatakse tsüklis -- igal kordusel täiendatakse järjendit ühe uue elemendiga. Selleks kombineeritakse olemasolev järjend üheelemendilise järjendiga:   

.. sourcecode:: py3
            
    arvud = []

    while True:
        sisend = input('Sisesta täisarv (lõpetamiseks vajuta lihtsalt ENTER): ')
        if sisend == '':
            break
        else:
            arvud += [int(sisend)]

    print('Sisestati', len(arvud), 'arvu')
    print('Sisestatud arvud:', arvud)
    print('Arvude summa on:', sum(arvud))

Antud näite puhul olid tsükli aluseks kasutaja tegevused. Samahästi võiksime kasutada järjendi koostamisel kindla korduste arvuga ``for``-tsüklit:

.. sourcecode:: py3
    
    ruudud = []
    
    for arv in range(1, 10):
        ruudud += [arv ** 2]
    
    print('Arvude 1..9 ruudud on:', ruudud)

Harjutus. Failist järjendisse
-----------------------------
Nagu juba tead, võib ``for``-tsükli aluseks olla ka mingi tekstifail.

Kirjuta programm, mis loeb tekstifailist ükshaaval ridu (eeldame, et igal real on üks arv) ning koostab selle käigus järjendi, mis sisaldab failist leitud paarisarve. Koostatud järjend kuvada ekraanile.


Juhuslike järjendite genereerimine
----------------------------------
Selle asemel, et harjutustes järjendeid ise sisse toksida, võime kasutada ka juhuslikult genereeritud arvujärjendeid:

.. sourcecode:: py3

    from random import randint
    
    arvud = []
    for i in range(100):
        # imiteerime täringuviskamist
        arvud += [randint(1,6)]
    
    print(arvud)

Harjutus. Juhuslik järjend
--------------------------
Kirjuta funktsioon ``juhuslik_järjend``, mis võtab argumendiks järjendi elementide arvu ning kaks argumenti arvuvahemiku määramiseks, ning tagastab vastava juhuslikult genereeritud arvujärjendi. (Seda funktsiooni võid edaspidi kasutada alati, kui on tarvis genereerida mingi juhuslik järjend.)

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
        arvud += [int(sõne)]
    
    print(arvud)

Harjutus. Sõned arvudeks
------------------------
Kirjuta eelneva programmi näitel funktsioon ``sõned_arvudeks``, mis võtab argumendiks sõnede järjendi ning tagastab vastava arvude järjendi. (Võid praegu eeldada, et argumendiks antud järjendis sisalduvad vaid sellised sõned, mida saab arvudeks teisendada.)



Järjendi filtreerimine
----------------------
Filtreerimiseks nimetame seda operatsiooni, mis moodustab mingi järjendi põhjal uue järjendi, milles sisalduvad teatud tingimustele vastavad väärtused algsest järjendist. Uuri ja katseta järgnevat näidet:

.. sourcecode:: py3

    def paarisarvud(arvud):
        paaris = []
        for arv in arvud:
            if arv % 2 == 0:
                paaris +=  [arv]
        
        return paaris
    
    print(paarisarvud([1,2,3,4,5,6,7]))

Harjutus. Arvude tuvastamine
----------------------------
Kirjuta funktsioon ``naturaal_sõned``, mis võtab argumendiks sõnede järjendi ning tagastab uue sõnede järjendi, milles sisalduvad vaid need esialgse järjendi väärtused, mis kujutavad naturaalarve (st ``sõne.isnumeric() == True``). NB! Sõnede teisendamist arvudeks pole selles ülesandes tarvis.

Harjutus. Arvude tuvastamine koos teisendamisega
------------------------------------------------
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
                tulemus += [element]
                
        for element in j2:
            if not (element in tulemus):
                tulemus += [element]
        
        return tulemus
    
    print(ühend([1, 2, 3, 2], [1, 6, 6]))

Harjutus. Järjendite ühisosa
----------------------------
Kirjuta funktsioon ``ühisosa``, mis võtab argumendiks kaks järjendit ning tagastab **uue** järjendi, mis sisaldab (ühekordselt) neid väärtusi, mis esinevad mõlemas järjendis.


Järjendite kasutamine "andmebaasina"
====================================
Järgnevates näidetes kasutame me mitut järjendit, mille elemendid on omavahel kuidagi seotud -- nt järjendi ``a`` element positsioonil ``16`` (st. ``a[16]``) on seotud järjendi ``b`` samal positsioonil oleva elemendiga (st ``b[16]``). Uuri ja katseta järgnevat näidet:

.. sourcecode:: py3

    eesnimed = ['Isaac', 'Leonhard', 'David']
    perenimed = ['Newton', 'Euler', 'Hilbert']
    
    n = len(eesnimed) 
    for i in range(n):
        print(eesnimed[i] + ' ' + perenimed[i])

Kuna selles näites oli meil tarvis võtta element mõlemast järjendist samalt positsioonilt, siis ei piisanud meile tavalisest ``for``-tsükli variandist, mis võtab elemente lihtsalt järjest, ignoreerides nende indekseid. Seetõttu ei võtnud me tsükli aluseks mitte järjendi, vaid hoopis ``range``-i abil genereeritud indeksite loetelu.

Taolistes ülesannetes eeldame, et seotud järjendid on sama pikad, seetõttu on ükskõik, millise järjendi pikkuse järgi me loendurit kontrollime.


"Andmebaasi" sisselugemine failist
----------------------------------
Et teha järgnevaid näiteid ja ülesandeid realistlikumaks, siis loeme omavahel seotud järjendid sisse tekstifailidest. Kõige lihtsam võimalus oleks kirjutada erinevate järjendite sisu eri failidesse ning lugeda nad sealt järjenditesse, üks järjend/fail korraga. Sellise lähenemise puhul on aga failide koostamine ebamugav, kuna me peame hoolikalt jälgima, et seotud andmed (nt sama inimese eesnimi ja perenimi) satuksid mõlemas failis ikka samale reale.

Seetõttu kasutame me teistsugust võtet: kirjutame omavahel seotud andmed failis samale reale ning faili sisselugemisel kasutame ülalpool tutvustatud sõnemeetodit ``split``. Koosta tekstifail ``nimed.txt``, mille igal real on tühikuga eraldatud eesnimi ja perenimi, ning katseta järgnevat programmi:

.. sourcecode:: py3

    # teeme valmis tühjad järjendid
    eesnimed = []
    perenimed = []
    
    # loeme failist järjenditesse
    f = open('nimed.txt')
    for rida in f:
        nime_osad = rida.split()
        eesnimi = nime_osad[0]
        perenimi = nime_osad[1]
        eesnimed += [eesnimi]
        perenimed += [perenimi]
        
    f.close() # faili meil enam tarvis pole
    
    # hakkame järjendeid töötlema
    n = len(eesnimed) 
    for i in range(n):
        print('Eesnimi on: ' + eesnimed[i])
        print('Perenimi on: ' + perenimed[i])


.. topic:: Millal on mõtet salvestada andmed järjendisse?

    Kui me soovime failist loetud (või kasutaja käest küsitud) järjendi põhjal arvutada midagi lihtsat (nt arvude summat või maksimaalset arvu), siis pole järjendi koostamine tegelikult isegi vajalik -- piisaks ühest abimuutujast, mille väärtust me iga järgmise arvu sisselugemisel sobivalt uuendame. Andmete järjendisse salvestamine on oluline näiteks siis, kui andmeid on vaja mitu korda läbi vaadata, sest järjendi korduv läbivaatamine on palju kiirem kui faili korduv lugemine.

Harjutus. Eksami tulemused
--------------------------
Eksami tulemused on salvestatud faili, kus igal real on tudengi täisnimi, koma ja saadud punktide arv (nt ``Jaan Tamm,24``). Maksimaalne eksami eest saadav punktide arv on 40. Õppejõud soovib näha nende tudengite nimesid ja tulemusi, kes said eksamil vähem kui 50% punktidest. Kirjuta programm selle probleemi lahendamiseks.

.. hint::
    Meetod ``split`` annab kõik komponendid sõnedena!

Topelttsükkel
=============

