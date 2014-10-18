.. _listid2:

*********************************
8. Järjendid ja ``for``-tsükkel 2
*********************************

Selles peatükis me uusi Pythoni konstruktsioone sisse ei too, vaid uurime erinevaid võimalusi juba tuttavate teemade kombineerimiseks ja kasutamiseks.

TODO: map, filter, reduce, zip, keskmine, mediaan, standardhälve


Järjendite koostamine elementhaaval
===================================
Siiani oleme järjendi kirjapanekul loetlenud alati kõik tema elemendid. Paraku pole alati võimalik kõiki elemente korraga välja tuua. Appi tuleb järjendite liitmine. Tuletame kõigepealt meelde, mida see tähendas:

.. sourcecode:: py

    >>> [1, 2, 3] + [6, 4, 9]
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


TODO: eelnevate kasutamine listdir-iga

TODO: readlines, splitlines, list(f) [need vist pigem sobiks eelmisse]


Otsimine
========

TODO: leidub / ei leidu, indeksi tagastamine



Järjendite kasutamine "andmebaasina"
====================================

TODO: kas seda on üldse vaja ??????????????????????????????????
Sõnastiku ülesanne ajab asja ära

Võibolla peaks siin lihtsalt tutvustama zip operatsioone .........

Näide, kus eri failides on tudengite nimed ja hinded (nt. anonüümsuse saavutamiseks)
2. näide juhuslikust paaritamisest

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
TODO: pixboard





Sõnede algoritmid
=================

Palindroom

Anagrammid

http://www.greenteapress.com/thinkpython/html/thinkpython010.html

*Vahepala: sõnede ja väljundi formaatimine*
===========================================
Seni oleme sõnede ja teiste andmetüüpide kombineerimisel kasutanud komponentide ühendamiseks operatsiooni ``+`` ning teisendamiseks funktsiooni ``str``. Nüüd vaatame alternatiivset viisi selle toimingu tegemiseks.

Sõnedel on olemas meetod ``format``, millega saab teisendada andmeid erinevatele sõnekujudele. Selle meetodi põhiolemust demonstreerib järgnev käsurea näide:

.. sourcecode:: py3

    >>> eesnimi = "Kalle"
    >>> perenimi = "Kala"
    >>> vanus = 25
    >>> 'Klient: {0} {1}, vanus: {2}'.format(eesnimi, perenimi, vanus)
    'Klient: Kalle Kala, vanus: 25'

Meetod ``format`` konstrueerib tulemuse (uue sõne) mitmest komponendist: esimene komponent on lähtesõne, mis sisaldab muuhulgas loogeliste sulgudega tähistatud "pesasid" (ingl `placeholders`); ülejäänud komponendid (st meetodi argumendid) on suvalised väärtused, mis kopeeritakse vastavatesse pesadesse.

Pesa kirjeldus on kõige lihtsamal juhul täisarv, mis näitab, kui mitmes argumentväärtus tuleb antud pesasse panna. Seejuures tuleb arvestada, et loendamist alustatakse 0-st. 

Pesa kirjeldusse saab märkida ka lisatingimusi andmete formaadi kohta:

.. sourcecode:: py3
    
    pikkused = [173.235235, 33.0, 167.333]

    for i in range(len(pikkused)):
        pikkus_sõnena = "{0}. pikkus on {1:>6.2f}cm".format(i, pikkused[i])
        print(pikkus_sõnena)

Hakkame jupphaaval analüüsima pesa ``{1:>6.2f}`` tähendust.

* Koolonist vasakul on pesa järjekorranumber.
* ``>6`` näitab, et sisu esitamiseks on ette nähtud 6 positsiooni ja kui tegelik sisu võtab vähem ruumi, siis tuleb sisu ette panna niipalju tühikuid, et kokku saaks 6 sümbolit.
* ``.2f`` ütleb, et vastavat väärtust tuleb tõlgendada ujukomaarvuna (`f` nagu `float`), mis tuleb esitada 2 komakohaga.
    
.. note::

    | ``format`` meetodi teiste võimalustega saab tutvuda aadressil:    
    | http://docs.python.org/3/library/string.html#format-examples








Ülesanded
=========


Statistika failist

nt. loenda ilma e-deta sõnu, 
!!! sõnad, mille tähed on alfabeetilises järjekorras 

1. Veergude eraldamine
----------------------
CSV failist teatud veergude kirjutamine teise faili


2. Lausegeneraator
------------------
* Defineeri funktsioon ``lause``, mis **võtab argumendiks** 3 sõna (sõnena) ning **tagastab** neist kombineeritud lause (muuhulgas lisab tühikud ja punkti).

* Loo 3 tekstifaili -- ``alus.txt``, ``oeldis.txt`` ning ``sihitis.txt``. Kirjuta igasse neist 10 sõna eraldi ridadele.

    * ``alus.txt`` - peaks sisaldama nimisõnu või nimesid nimetavas käändes (nt `Margus`).
    * ``oeldis.txt`` - oleviku vormis, 3. isikus tegusõnad (nt `õpetab`).
    * ``sihitis.txt`` - nimisõna osastavas käändes (nt `tudengeid`).

* Kirjuta funktsioon, mis võtab argumendiks failinime ning tagastab vastava faili read järjendina (reavahetuse sümbolid tuleks eemaldada meetodiga ``strip``).

* Kirjuta programm, mis:
    
    #. loeb mainitud kolme faili sisud järjenditesse (``alused``, ``oeldised``, ``sihitised``), kasutades selleks eelmises punktis defineeritud funktsiooni;
    #. genereerib 3 juhuslikku täisarvu vahemikust 0..9;
    #. võtab järjendite vastavatelt positsioonidelt aluse, öeldise ja sihitise ning koostab neist lause kasutades eelnevalt defineeritud funktsiooni ``lause``;
    #. kuvab moodustatud lause ekraanile.

* Muuda programmi selliselt, et see genereeriks ja väljastaks (lõpmatus tsüklis) iga ENTER-i vajutuse peale uue lause.

4. Eesti-inglise sõnaraamat
---------------------------
Lae alla eesti-inglise sõnastik(:download:`sonastik.txt <downloads/sonastik.txt>`, kodeeringus UTF-8). Selle igal real on kõigepealt inglisekeelne sõna või väljend, seejärel tabulaatori sümbol (kirjutatakse Pythonis ``"\t"``) ning lõpuks eestikeelne vaste.

Kirjuta programm, mis loeb failist eestikeelsed ja ingliskeelsed väljendid eraldi järjenditesse ning võimaldab kasutajal küsida ingliskeelse sõna eestikeelset vastet (või vastupidi -- võid ise valida).

.. note::
    
    Antud sõnastiku fail on veidi modifitseeritud variant Eesti Keele Instituudi poolt jagatavast failist (ftp://ftp.eki.ee/pub/keeletehnoloogia/inglise-eesti/en_et.current.wbt).

5. funktsioon is-sorted, has duplicates, remove duplicates
----------------------------------------------------------
TODO

6. kiire otsing sõnastikust
---------------------------



EULER
-----
https://projecteuler.net/problem=4

Lisalugemine
============
Map, filter, reduce

List comprehension