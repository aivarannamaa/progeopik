.. _listide-muteerimine: 

**********************
9. Listide muteerimine
**********************

.. todo::

    CSV failist teatud veergude kirjutamine teise faili
    

Pythoni listid on *muteeritavad*, st sama list võib programmi käivitamise erinevatel hetkedel sisaldada erinevaid väärtusi. Esmapilgul võib olla raske eristada listi muteerimist ja uue, muudetud listi samasse muutujasse salvestamist, aga erinevused on olemas ning nende mitteteadmine võib valusasti hammustada.


Meetod ``append``
=================
Eelmises peatükis vaatasime ühte skeemi listide kasvatamiseks. See seisnes vana listi ja uue info põhjal uue, pikema listi moodustamises:

.. sourcecode:: py3

    >>> a = [1,2,3]
    >>> a = a + [4,5]
    >>> a
    [1, 2, 3, 4, 5]
    >>> a += [6]
    >>> a
    [1, 2, 3, 4, 5, 6]

Tuleb välja, et peaaegu sama efekti saamiseks on olemas alternatiivne viis -- meetod ``append``:

.. sourcecode:: py3

    >>> a = [1,2,3]
    >>> a.append(4)
    >>> a.append(5)
    >>> a.append(6)
    >>> a
    [1, 2, 3, 4, 5, 6] 

Selles näites me peale esialgset omistamist muutuja sisu otseselt ei muutnud, küll aga muutsime listi enda sisu. 


Harjutus. Arvude küsimine
-------------------------
Kirjuta eelmises peatükis toodud :ref:`arvude küsimise näide<arvude-liitmine-listi>` ümber ``append``-i kasutades.

Järjendi elementide muutmine
============================
Lisaks sellele, et olemasolevale järjendile on võimalik elemente lõppu juurde lisada, saab välja vahetada järjendi mingil positsioonil olevat elementi. Selleks tuleb teha omistamine kasutades järjendi indekseerimise süntaksit. Uuri ja katseta järgnevat programmi:
 
.. sourcecode:: py3

    a = [1, 2, 3]
    
    # muudame teist elementi (s.o element järjekorranumbriga 1)
    a[1] = 22 
    
    print(a)

Nagu ikka, võib ka siin kasutada indeksina mingit täisarvulist muutujat.


Harjutus. Täringuvisete statistika
----------------------------------
Genereeri 100 täringuviske tulemust (kasutades näiteks :ref:`eelmises peatükis<juhuslik-jarjend>` defineeritud funktsiooni ``juhuslik_järjend``) ning salvesta tulemus muutujasse.

Koosta 6-elemendiline järjend ``statistika``, mis sisaldab täringuvisete statistikat -- avaldis ``statistika[0]`` peaks näitama, mitu korda tuli täringuviske tulemuseks 1, ``statistika[1]`` peaks näitama kahtede sagedust jne.

Kuva statistika ekraanile.

.. hint::

    Kusagil programmis võiks olla lause ``statistika = [0, 0, 0, 0, 0, 0]``
    
.. hint::

    Näidislahendus:
    
    .. sourcecode:: py3
    
        from random import randint

        def juhuslik_järjend(n, alates, kuni):
            arvud = []
        
            for i in range(n):
                arvud.append(randint(alates, kuni))
        
            return arvud
        
        statistika = [0, 0, 0, 0, 0, 0]
        visked = juhuslik_järjend(100, 1, 6)
        
        for vise in visked:
            # visked on arvud 1..6
            # listi statistika indeksid on 0..5
            indeks = vise-1
            statistika[indeks] += 1
        
        print(statistika)

Veel järjendimeetodeid
======================
Lisaks ``append``-ile on listidel veel meetodeid mis ei tagasta midagi, vaid muudavad listi sisu. Järgnev tabel näitab, kuidas mõjuvad erinevad meetodid listile ``[3,1,2,3,1,4]``, mis on salvestatud muutujasse ``a``.  

+---------------------+-----------------+-----------------------+--------------------------------------------------------+
| Meetodi rakendamine | Tagastusväärtus | Listi uus sisu        | Kommentaarid                                           |
+=====================+=================+=======================+========================================================+
| ``a.append(7)``     | ``None``        | ``[3,1,2,3,1,4,7]``   | lisab elemendi listi lõppu                             |
+---------------------+-----------------+-----------------------+--------------------------------------------------------+
| ``a.extend([7,8])`` | ``None``        | ``[3,1,2,3,1,4,7,8]`` | lisab listitäie elemente listi lõppu                   |
+---------------------+-----------------+-----------------------+--------------------------------------------------------+
| ``a.insert(0,34)``  | ``None``        | ``[34,3,1,2,3,1,4]``  | lisab näidatud positsioonile näidatud elemendi,        |
+---------------------+-----------------+-----------------------+ järgnevate elementide positsioonid nihkuvad            |
| ``a.insert(1,34)``  | ``None``        | ``[3,34,1,2,3,1,4]``  |                                                        |
+---------------------+-----------------+-----------------------+--------------------------------------------------------+
| ``a.remove(1)``     | ``None``        | ``[3,2,3,1,4]``       | eemaldab esimese näidatud väärtusega elemendi          |
+---------------------+-----------------+-----------------------+--------------------------------------------------------+
| ``a.pop()``         | ``4``           | ``[3,1,2,3,1]``       | eemaldab viimase elemendi ja tagastab selle            |
+---------------------+-----------------+-----------------------+--------------------------------------------------------+
| ``a.pop(0)``        | ``3``           | ``[1,2,3,1,4]``       | eemaldab näidatud indeksiga elemendi ja tagastab selle |
+---------------------+-----------------+-----------------------+--------------------------------------------------------+
| ``a.clear()``       | ``None``        | ``[]``                | eemaldab listist kõik elemendid                        |
+---------------------+-----------------+-----------------------+--------------------------------------------------------+
| ``a.sort()``        | ``None``        | ``[1,1,2,3,3,4]``     | sorteerib                                              |
+---------------------+-----------------+-----------------------+--------------------------------------------------------+
| ``a.reverse()``     | ``None``        | ``[4,1,3,2,1,3]``     | pöörab elementide järjekorra ümber                     |
+---------------------+-----------------+-----------------------+--------------------------------------------------------+

Nagu näha, tagastab enamik neist meetoditest selle veidra väärtuse ``None``, mis tähendab sisuliselt väärtuse puudumist. Teisti öeldes, neid meetodeid käivitatakse vaid `kõrvalefekti` pärast. Antud juhul on kõrvalefektiks listi muteerimine.



Muudetavate andmetüüpide omapärad
=================================
Järjendi muutmisel või täiendamisel (nii ``append``-i kui ``a[i] = x`` puhul) tuleb arvestada ühe omapäraga, mis tuleb ilmsiks siis, kui sama järjend on omistatud mitmele muutujale. Uuri järgnevat näidet ning ennusta, mis antakse selle programmi käivitamisel väljundiks:

.. sourcecode:: py3
    
    a = [1, 2, 3]
    
    b = a
    b.append(4)
    
    print(a)
 
Nagu nägid, ilmus ekraanile ``[1, 2, 3, 4]``, ehkki programmist ei paista, et kusagil oleks järjendisse ``a`` lisatud arv *4*. Selle omapära põhjus peitub real ``b = a``, mis mitte ei kopeeri muutuja ``a`` väärtust muutujasse ``b``, vaid hoopis paneb muutuja ``b`` viitama samale järjendile. Teisisõnu, ``b`` on sama järjendi alternatiivne nimi (ingl *alias*). Seetõttu, kui järjendit muuta kasutades nime ``b``, on muudatus näha ka nime ``a`` kaudu (ja vastupidi).

Kuna funktsiooni parameetrid on oma olemuselt samuti muutujad, siis sama efekt ilmneb ka siis, kui parameetrina antud järjendit muudetakse funktsiooni sees:

.. sourcecode:: py3

    def lisa(järjend, väärtus):
        järjend.append(väärtus)

    arvud = [1, 2, 3]
    lisa(arvud, 4)
    
    print(arvud)

Seda omapära võib vahepeal ka enda kasuks kasutada. Kui aga soovid parameetrina saadud järjendit arvutuse käigus muuta nii, et funktsioonist väljaspool muutusi näha poleks, siis tuleks teha saadud järjendist koopia ning muudatused teha vaid koopiale. Koopia tegemiseks saab kasutada viilutamise süntaksit, jättes kirjutamata nii vasaku kui parema indeksi:

.. sourcecode:: py3
    
    a = [1, 2, 3]
    
    b = a[:] # a-st tehakse koopia
    b.append(4)
    
    print(a) # a väärtus on endine


.. note::

    Eelmises peatükis sai põgusalt mainitud, et listide puhul pole ``x = x + [y]`` päris sama, mis ``x += [y]``. Asi on selles, et kasutades ``+=`` operatsiooni, Python tegelikult ei tee uut listi, vaid täiendab olemasolevat:
    
    .. sourcecode:: py3 

        >>> a = [1, 2, 3]
        >>> b = a
        >>> b += [4]
        >>> a
        [1, 2, 3, 4]
        >>> b
        [1, 2, 3, 4]
    
    Samas ``x = x + [y]`` puhul tehakse alati uus list:
    
    .. sourcecode:: py3
        :emphasize-lines: 3, 5
        
        >>> a = [1, 2, 3]
        >>> b = a
        >>> b = b + [4]
        >>> a
        [1, 2, 3]
        >>> b
        [1, 2, 3, 4]

Viitamisest täpsemalt
---------------------
Kas selline situatsioon, et erinevad muutujad viitavad samale objektile, on võimalik ainult listide korral? Tehniliselt võttes ei -- muutujad ja harilik (``=``-ga) omistamine toimivad alati samamoodi hoolimata andmetüübist.

Kõik Pythoni väärtused on programmi käimise ajal esitatud mingite objektidena, mis asuvad kusagil arvuti mälus. Kui käivitatakse lause ``x = 7``, siis luuakse mälus objekt, mis tähistab arvu `7` ja muutujasse ``x`` salvestatakse tegelikult ainult viide sellele objektile. Kui me järgmisena käivitame lause ``y = x``, siis muutujasse ``y`` salvestatakse sama viit, mis on muutujas ``x``, aga uut täisarvu objekti ei looda. Seega nüüd viitavad muutujad ``x`` ja ``y`` samale objektile.

Erinevus listidest tuleneb aga sellest, et täisarvu objekti ei ole võimalik muuta, seetõttu ei ole ilma pingutamata võimalik isegi aru saada, kas need muutujad viitavad samale objektile, või erinevatele objektidele, mis tähistavad sama arvu. Seetõttu ei pidanud me ei arvude ega sõnede puhul viitamise teema peale mõtlema.  

Viitamise teema täpsemal uurimisel on abiks funktsioon ``id``, mis tagastab argumendiks antud väärtuse (e objekti) aadressi arvuti mälus -- see ongi see viide, mida muutujad sisaldavad. Järgnevas näites luuakse kaks samaväärset sõneobjekti, mille kummagi viide salvestatakse erinevasse muutujasse:

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

Nagu näha, kopeeriti omistamisel muutujasse olemasoleva objekti viit ja uut objekti ei loodud.

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
        

    Kui list sisaldab omakorda liste, siis toimub kopeerimine ainult välimisel tasemel:
    
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
Loe läbi selle peatüki lõpus olev :ref:`tagasivaade_1-9`.



2. Palkade analüüs
------------------
Antud on tekstifail :download:`palgad.txt <downloads/palgad.txt>`, kus igal real on töötaja nimi, tema vanus ja kuupalk. Kirjuta programm, mis väljastab antud andmete põhjal:

* kõige suurema palgaga töötaja nime ja palga suuruse (vihje: suurima palga otsimisel jäta meelde, milliselt positsioonilt sa selle leidsid);
* keskmise palga;
* keskmisest palgast rohkem teenijate arvu;
* keskmised vanused eraldi neile, kes teenivad keskmisest palgast vähem (või samapalju), ning neile, kes teenivad keskmisest palgast rohkem.

3. minu_shuffle
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
    

4. Eesti filmide statistika (raskem)
------------------------------------
Veebisait http://www.imdb.com kogub ja jagab informatsiooni filmide kohta. Aadressilt ftp://ftp.funet.fi/pub/mirrors/ftp.imdb.com/pub/ saab IMDB poolt kogutud infot alla laadida pakitud tekstifailidena.

Fail :download:`filmid.zip (4.5MB) <downloads/filmid.zip>` on koostatud faili "countries.list.gz" põhjal ning see sisaldab filmide (ja telesaadete) loetelu koos riigi nime ning valmimise aastaga. Lae see fail alla ning paki lahti.

.. note:: 

    Filmide fail on lahtipakitult ligi 18MB suurune. Kui sul ei õnnestu (Windowsis) seda faili avada Notepadiga, siis kasuta vabavaralist programmi Notepad2 (http://www.flos-freeware.ch/notepad2.html).
    
Failis ``filmid.txt`` on ühe filmi andmed ühel real kujul *<nimi><tühik>(<aasta>)<tabulaator><riik>*. (Notepad2-s saad tühikuid ja tabulaatoreid eristada, kui märgid menüüs *View* valiku *Show whitespace*.)

Ülesanne on kirjutada programm, mis otsib sellest failist üles Eestis valminud filmid/telesaated ning koostab statistika selle kohta, mitu filmi/telesaadet mingil aastal valmis.

.. hint::

    Fail on kodeeringus ``UTF-8``, st faili avamisel tuleks seda mainida: ``f = open("filmid.txt", encoding="UTF-8")``.
    
.. hint::

    Tabulaatorit kirjutatakse Pythoni sõneliteraalina nii: ``'\t'``.
.. hint::

    Võibolla tuleb kasuks uurida ülalpool antud ülesannet "Täringuvisete statistika".

.. hint::

    Kui sa loed järjenditesse kogu failis sisalduva info, siis võib Pythonil mälust puudu tulla. 
    
.. topic:: Lisaülesande lisa

    Täienda programmi selliselt, et see küsib (korduvalt) kasutajalt aastaarvu ning väljastab ekraanile kõik selle aasta Eesti filmid. Kui kasutaja sisestab tühisõne (st vajutab lihtsalt ENTER-it), siis programm lõpetab töö. Selleks tuleb organiseerida sisseloetud filmid aastate kaupa eraldi.
    
    .. hint::
        
        Järjend võib sisaldada järjendeid: ``a = [[1, 2, 3], [5, 5, 6], [4, 4, 3]]``. Mõtle, mida võiks tähendada ``a[2][1]``?


.. _tagasivaade_1-9:

*Tagasivaade peatükkidele 1-9*
==============================
On teada, et mingi teema valdamiseks tuleb tegelda vaheldumisi nii teooria kui ka praktikaga. Praeguseks oled harjutanud läbi kõik olulisemad Python keele võimalused ja nüüd on paras aeg astuda samm tagasi ning vaadata juba läbitud materjalile uue, veidi kogenuma pilguga.

Avaldised vs laused
-------------------
Kõik eelpool käsitletud Python keele elemendid saame jaotada kahte suurde gruppi: *avaldised* ja *laused*.

**Avaldised** on näiteks ``2``, ``2 + 3``, ``brutopalk`` ja ``sin(0.5) ** (x-1)`` -- kõigil neil on **väärtus** ja neid saab seetõttu kasutada nt muutujate defineerimisel ja teistes keerulisemates avaldistes.

**Laused** (ingl *statements*) on näiteks omistamislause (``x = sin(0.5)``), tingimus- ja korduslaused (``if``, ``while`` ja ``for``) ja funktsioonide definitsioonid (``def``). Eri tüüpi lausete ühine omadus on see, et nad *teevad* midagi (nt muudavad muutuja väärtust, defineerivad uue käsu või teevad midagi tingimuslikult või korduvalt).

Nii avaldiste kui ka lausete juures on oluline see, et neid saab panna üksteise sisse. Näiteks operaatori ``+`` kasutuse üldskeem on ``<avaldis1> + <avaldis2>``, kusjuures nii ``avaldis1`` kui ka ``avaldis2`` võivad olla samuti mingi tehted. ``if``-lause põhiskeem on:

.. sourcecode:: none

    if <avaldis>:
        <laused1>
    else:
        <laused2>

kusjuures nii ``laused1`` kui ka ``laused2`` võivad sisaldada suvalisi lauseid, sh ``if``-lauseid, mille sees võib olla omakorda suvalisi lauseid.

.. note::
    Funktsiooni väljakutsed (nt ``sin(0.5)``) on tehniliselt küll alati avaldised, aga mõnesid funktsioone kasutatakse tavaliselt lausetena (nt ``turtle.forward(100)`` või ``print("Tere")``). Seega, natuke lihtsustades võiks öelda, et nende funktsioonide väljakutsed, mis midagi arvutavad, on avaldised, ja teiste funktsioonide väljakutsed, mis midagi teevad, on laused.

Muutujad
--------
Muutujad võimaldavad meil tegelda väärtustega ilma et me peaks mainima mingit konkreetset väärtust. Näiteks kui me salvestame kaks kasutaja poolt sisestatud arvu muutujatesse ``a`` ja ``b``, siis nende kokku liitmisel ei huvita meid enam, mis on nende muutujate konkreetne väärtus. 

Soovitatav on lugeda uuesti läbi 2. peatüki osa :ref:`muutujad`, tõenäoliselt näed nüüd muutujate olemust juba uue pilguga.

Funktsioonid
------------
Kui muutujad võimaldavad meil kasutada mingit väärtust ilma et me peaksime mõtlema mingile konkreetsele väärtusele, siis funktsioonid võimaldavad meil midagi teha või arvutada ilma et me peaksime alati mõtlema selle peale, kuidas see toiming või arvutus täpselt tehakse. Viska pilk peale järgnevale programmile:

.. sourcecode:: py3

    def kolmest_suurim(a, b, c):
        if a > b and a > c:
            return a
        elif b > a and b > c:
            return b
        else:
            return c
    
    print(kolmest_suurim(4, 15, 2))

Tõenäoliselt oskad isegi ilma funktsiooni definitsiooni süvenemata arvata, mida taoline programm ekraanile prindib. Põhjus on selles, et antud funktsiooni olemus tuleb välja juba tema nimest ja üldjuhul võime me eeldada, et funktsiooni tegelik definitsioon on tema nimele vastav. Seetõttu, kui meil on sobivad funktsioonid juba defineeritud, siis saame me programmi põhiosas (või järgmiste funktsioonide defineerimisel) töötada kõrgemal tasemel, ilma pisiasjade pärast muretsemata.

Kuna funktsioonide teema on programmeerimise algkursusel tavaliselt tudengitele kõige hägusam, siis on soovitatav lugeda uuesti läbi 5. peatükist vähemalt järgmised osad.

* :ref:`Parameetrid vs input<param-vs-input>`
* :ref:`return vs. print <return-vs-print>`
* :ref:`milleks-funktsioonid`
    

Tingimuslause
-------------
Tingimuslause (ehk ``if``-lause ehk hargnemislause) on oma olemuselt küllalt lihtne -- teatud tingimusel tuleb täita ühed laused ja vastasel juhul teised. Lisavõimalusena on Pythonis võimalik kirjutada ka üheharulisi (st ilma ``else``-ta) ning mitmeharulisi (``elif``-iga) tingimuslauseid.

Üks oluline punkt tingimuslause juures on lause päises antud tingimusavaldis. Nagu eelnevalt mainitud, on avaldiste moodustamiseks lõputult võimalusi -- võib kasutada konstante, muutujaid, tehteid, funktsiooni väljakutseid või kõigi nende kombinatsioone. Tingimusavaldise juures on oluline, et avaldise tüüp oleks tõeväärtus, st avaldise väärtustamisel saadakse kas ``True`` või ``False``. 

Mitme tingimuse kombineerimiseks saab kasutada operaatoreid ``and`` ja ``or``, tingimuse ümberpööramiseks on operaator ``not``. Ära unusta, et tingimuses saad kasutada ka isetehtud funktsioone, aga need peavad sel juhul tagastama tõeväärtuse.


Korduslaused e tsüklid
----------------------
Pythonis on kaks erinevat korduslauset -- ``while``-tsükkel, mis on väga paindlik, ning ``for``-tsükkel, mis on lihtsam, aga mis ei sobi kõigil juhtumitel.

``for``-tsükli juures on oluline mõista, et tema tööpõhimõte on ``while``'ist kaunis erinev. Kui ``while``-tsükli kordused põhinevad mingil tingimusel, siis ``for``-tsükli kordused põhinevad mingil järjendil (või järjendisarnasel asjal, nt failil või vahemikul).

Järjendid
---------
Järjendite abil saame koondada mingi hulga andmeid ühe nime alla.

Järjendid on vajalikud neil juhtudel, kus programmi kirjutades pole võimalik öelda, mitme andmejupiga peab programm töötama (vastasel juhul võiksime iga andmejupi jaoks võtta programmis kasutusele ühe muutuja).

Järjendeid saab programmi sisse kirjutada, koostada teiste järjendite põhjal või lugeda failist. Kui järjendeid on vaja ükshaaval järjest läbi vaadata, siis on selleks kõige mugavam kasutada ``for``-tsüklit, kui on vaja lugeda järjendist mingit konkreetset elementi, siis tuleks kasutada indekseerimist.

Kust saab rohkem infot?
-----------------------
Kes soovib läbitud teemade kohta rohkem detaile või lihtsalt teist vaatenurka, siis soovitame lugeda läbi Pythoni ametliku juhendi: http://docs.python.org/3/tutorial/.


Lisalugemine
============
Pööratud Poola notatsioon
-------------------------
Tänapäeval oleme harjunud kirjutama matemaatilisi avaldisi nõndanimetatud infiksnotatsioonis, kus tehtemärk on nende kahe arvu vahel, millega ta töötab. See tekitab tegelikult aga igasuguseid probleeme seoses sellega, et vahel on raske öelda, mis järjestuses tehteid tegema peab. Koolis õpetatakse meile, et kõigepealt tuleb teha astendamised, siis korrutamised ja jagamised ning alles siis liitmised ja lahutamised. Kui tehteid tuleb mingis muus järjestuses teha, saab kasutada sulge.

Tegelikult on aga juba ammusest olnud tuntud viise avaldiste kirjutamiseks nii, et sulge pole vaja, kuid kõik tehete tegemise järjestused on ometi kirjeldatavad. Ehk tuntuim neist on nõndanimetatud postfiksnotatsioon ehk pööratud Poola notatsioon (Poola notatsioon on nii nimetatud, sest selle põhiline propageerija oli poola matemaatik Jan Łukasiewicz ja ta pakkus selle välja 1920. aastal; pööratud Poola notatsiooni pakkusid välja F. L. Bauer ja E. W. Dijkstra kuuekümnendatel).

Selles ei kirjutata tehe mitte argumentide vahele, vaid järele. Nii teisendatakse
näiteks 2 + 3 avaldiseks 2 3 +. Kui üks neist argumentidest juhtub aga olema juba mõne eelneva tehte tulemus, siis tähistabki vastavat tulemust see tehtemärk. Nii saab näiteks 2 + 3 – 1 teisendada kujule 2 3 + 1 -. See tähendab seda, et kõigepealt tehakse liitmine 2 ja 3 vahel ning seejärel lahutamine selle liitmise tulemuse ja 1 vahel. Selline kirjutamisviis kaotab igasuguse vajaduse sulgude jaoks: (2 + 7) * 3 saab kirjutada ju lihtsalt kui 2 7 + 3 * kusjuures on üheselt selge, et kõigepealt tehakse 2 ja 7 liitmine ning alles siis korrutatakse selle tulemus ja kolm omavahel. Muuseas võib juhtuda, et järjest on ka kaks või kolm või isegi enam tehtemärki. Näiteks teiseneb 3 + 2 * (4 - 1) kujule 3 2 4 1 - * +.

Selle kirjapildi teine tõsine eelis on see, et see muudab aritmeetiliste avaldiste töötlemise arvuti jaoks kõvasti lihtsaks. Tuleb vaid meeles pidada, mis arvud parasjagu loetud on, tehtemärki kohates kaks viimati lisatud arvu välja võtta, neile see tehe rakendada ning siis see tulemus uuesti meeles peetud arvude nimekirja lõppu lisada. Seega on väga lihtne koostada programm, mis antud avaldise tulemuse välja arvutab. Toomegi siinkohal programmi, mis seda teeb:

 
.. sourcecode:: py3

    rida = input("Sisesta avaldis: ")
    kasud = rida.split()
    
    # töötle avaldis
    loend = []
    
    for kask in kasud :
        # liitmine
        if kask == "+" :
            # asenda viimane element tulemusega
            loend[-1] = loend[-2] + loend[-1]
            # eemalda eelviimane element
            loend.pop(-2)
    
        # lahutamine
        elif kask == "-" :
            loend[-1] = loend[-2] - loend[-1]
            loend.pop(-2)
    
        # korrutamine
        elif kask == "*" :
            loend[-1] = loend[-2] * loend[-1]
            loend.pop(-2)
    
        # jagamine
        elif kask == "/" :
            loend[-1] = loend[-2] / loend[-1]
            loend.pop(-2)
        else :
            # polegi käsk, seega loodetavasti hoopis number
            loend.append(float(kask))
    
    print("Tulemus on: " + str(loend[-1]))

Tegu on ka asjaga, mis on praktikas täiesti kasutust leidnud. Oma töötlemise lihtsuse tõttu ehitati selline arvutamise süsteem sisse mõningatesse võimsamatesse kalkulaatoritesse, mida kunagi müüdi. Viimase 15 aasta jooksul on see aga arvutusvõimsuse kasvu tõttu vaikselt kalkulaatorites asendunud meile loomulikuma koolis õpitud infiksnotatsiooniga.


Kommentaarid
============
.. disqus::
    :disqus_identifier: muteerimine