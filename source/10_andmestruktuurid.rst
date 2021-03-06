.. _andmestruktuurid:

********************
10. Andmestruktuurid
********************

.. todo::
    
    Sõnastikud kui objektid a la 
    isik = {'nimi':'Peeter', 'vanus': 19, 'sugu': 'mees'} 

    Kas nad saavad teada, et kui sul on vaja nt. hulkade listis ühte hulka midagi lisada, siis ei pea seda hulka sealt välja võtma, vaid võid teha kohe lst[i].add("blah") ?
    
    "Listid kui andmebaas" tüüpi ülesanded domineerivad tudengite mõtetes. Võibolla oleks vaja teha rohkem väikeseid, lihtsaid aga mitmekesiseid ülesandeid, enne kui minna suurte, mahukate ülesannete juurde. 

Erinevat laadi info esitamiseks/kasutamiseks on olemas erinevad andmetüübid. Seni oled tutvunud täisarvu-, ujukomaarvu-, tõeväärtus-, sõne-, listi- ja ennikutüüpidega. Selles peatükis vaatame veel kahte andmetüüpi (hulk ja sõnastik) ning lisaks uurime, miks ja kuidas võiks andmetüüpe omavahel kombineerida. Lõpuks astume sammu tagasi ning analüüsime, mida on järjenditel, hulkadel ja sõnastikel ühist.


Hulgad
======
Pythoni *hulga* (ingl *set*) andmetüüp on küllalt sarnane listiga -- iga hulgatüüpi väärtus võib sisaldada 0 või rohkem elementi. Esimene oluline erinevus on see, et just nagu matemaatikast tuttava hulga puhul, ei ole ka Pythoni hulga elementide omavaheline järjestus määratud, seetõttu ei saa hulga elemente ka indekseerida. Teine erinevus on see, et hulk ei sisalda kunagi korduvaid elemente (nagu ka matemaatiline hulk).

Konkreetse hulga kirjapanekuks kasutatakse loogelisi sulge. Järgnev käsurea näide demonstreerib eelmainitud hulkade omadusi:

.. sourcecode:: py3
    :linenos:
    
    >>> {1,2,4}
    {1, 2, 4}
    >>> {1,2,2}
    {1, 2}
    >>> {1,2,4} == {2,4,1}
    True

Real 3 üritasime luua korduvate elementidega hulka, aga vastusest on näha, et Python arvestas arvu *2* vaid ühekordselt. 

.. note::

    Ära üllatu, kui mõnikord näitab Python sinu poolt esitatud hulga elemente teistsuguses järjekorras, kui sa need kirja panid. Kuna hulga puhul ei ole elementide järjekord tähtis, siis Python võib need ümber paigutada, kui see lubab tal hulka efektiivsemalt hoida või kasutada.
    
Olulisimad hulgaoperatsioonid on mingi väärtuse hulgas sisalduvuse kontroll (``in``), hulga elementide arvu leidmine (``len``) ning hulka elemendi lisamine (``add``):

.. sourcecode:: py3

    >>> nimed = {'Tõnu', 'Toomas', 'Malle'}
    >>> len(nimed)
    3
    >>> 'Malle' in nimed
    True
    >>> 'Kalle' in nimed
    False
    >>> nimed.add('Kalle')
    >>> 'Kalle' in nimed
    True
    >>> nimed
    {'Kalle', 'Toomas', 'Malle', 'Tõnu'}
    >>> len(nimed)
    4
    
Nagu näha, ei pea hulgas olema vaid arvud -- just nagu listis, saab ka hulgas hoida erinevaid Pythoni väärtusi. (Selle väite osas teeme allpool väikese korrektuuri, aga praegu on oluline, et hulgas saab hoida vähemalt täisarve, ujukomaarve, tõeväärtusi ja sõnesid.)

Pane tähele, et elemendi hulka lisamiseks on meetod ``add``, mitte ``append`` nagu listide puhul. Põhjus on selles, et sõna *append* viitab justnimelt lõppu lisamisele, aga kuna hulga elementide järjekord pole tähtis, siis kasutatakse üldisemat sõna *add*.

Kui proovisid tühja hulka kirja panna kirjutades ``{}``, siis said sellise hulga kasutamisel ilmselt veateate. Põhjus on selles, et sellist tähistust kasutatakse Pythonis ühe teise andmestruktuuri, nimelt tühja sõnastiku tähistamiseks. Tühi hulk tuleb kirjutada kasutades funktsiooni ``set``:

.. sourcecode:: py3

    >>> a = set()
    >>> a
    set()
    >>> a.add(1)
    >>> a
    {1}
    >>> a.add(2)
    >>> a
    {1, 2}
    
Funktsiooni ``set`` saab kasutada ka mõnede teiste andmetüüpide teisendamiseks hulkadeks:

.. sourcecode:: py3

    >>> set("abc")
    {'a', 'c', 'b'}
    >>> set([1,2,3])
    {1, 2, 3}

Nii nagu järjendite puhul, saab ka hulga kõiki elemente läbi käia kasutades ``for``-tsüklit:


.. sourcecode:: py3

    nimed = {'Tõnu', 'Toomas', 'Malle'}
    
    # läbimise järjekorra võib Python valida oma suva järgi
    for nimi in nimed:
        print(nimi) 

Täpsemat infot Pythoni hulkade kohta saab aadressilt http://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset.

Harjutus. Hulkade vahe
----------------------
Kirjuta funktsioon, mis võtab argumendiks kaks hulka ja tagastab esimese ja teise hulga vahe, st hulga, mis sisaldab kõiki neid esimese hulga elemente, mis ei sisaldu teises hulgas.

.. admonition:: NB!

    Pythonis saab tegelikult hulkade vahet arvutada ka tavalise miinusmärgiga:
    
    .. sourcecode:: py3
    
        >>> {1,2,3} - {1,3}
        {2}
    
    Harjutamise mõttes aga proovi see operatsioon ise defineerida. Miinusmärki kasuta pärast oma funktsiooni kontrollimiseks.


Sõnastikud
==========

.. todo::

    * Sõnastiku kasutamine kirjetena
    * Rohkem sõnastikuga ülesandeid http://www.greenteapress.com/thinkpython/html/thinkpython012.html
    * sõnastiku läbimine võtmete järjestuses

Sõnastik (ingl *dictionary*, lühendatult ``dict``) on Pythoni andmetüüp, mis meenutab jällegi mitmes mõttes järjendeid: teda kasutatakse andmete koondamisel üheks kogumiks ja temas sisalduvaid üksikuid elemente on võimalik küsida kasutades  avaldist kujul ``kogum[võti]``.

Põhiline erinevus on selles, et kui järjendi puhul on võtmeks (e indeksiks) alati täisarv (nt ``palgad[0]``), siis sõnastike puhul saab kasutada võtmena ka näiteks sõnesid (nt ``telefoninumbrid['Peeter']``) või muid Pythoni lihtsamaid tüüpe.

Sõnastikud kirjutatakse looksulgude vahele nagu hulgadki, aga iga elemendi juures näidatakse ära elemendi võti ja väärtus. Väärtuse küsimiseks tuleb nurksulgudes anda soovitud elemendi võti:

.. sourcecode:: py3
    
    # loome sõnastiku, milles on 3 elementi
    telefonid = {'politsei': '110', 'päästeamet': '112', 'president': '631 6202'}
    
    # ühe kindla elemendi küsimine (võtme järgi)
    print("Päästeameti telefoninumber on", telefonid['päästeamet'])
    
    # küsime, kas teatud võtmega element on olemas
    # NB! in-operatsioon käib võtmete, mitte väärtuste kohta
    if 'politsei' in telefonid:
        print("Politsei number on", telefonid['politsei'])

.. note::

    Sõnastike ja hulkade sarnast kirjapaneku viisi saab selgitada sellega, et sõnastikku võib vaadata kui paaride hulka, kus paari esimene komponent on võti ja teine on väärtus.

Nii nagu järjendite puhul, saab kõiki sõnastiku elemente läbi vaadata kasutades ``for``-tsüklit, aga erinevalt järjenditest antakse igal sammul tsüklimuutujasse elemendi võti, mitte väärtus:

.. sourcecode:: py3
    
    # sõnastiku loomine
    telefonid = {'politsei': '110', 'päästeamet': '112', 'president': '631 6202'}
    
    # kõigi elementide läbivaatamine
    for nimi in telefonid:
        print(nimi.capitalize() + " - " + telefonid[nimi])

Kui sa proovisid seda näidet käivitada, siis võis juhtuda, et telefoninumbrid väljastati teistsuguses järjekorras kui sõnastiku loomisel. Põhjus on selles, et nii nagu hulkade puhul, ei pea ka sõnastiku puhul Python elementide omavahelist järjekorda oluliseks ja võib neid programmi efektiivsuse huvides ümber tõsta (aga ühe elemendi võti ja väärtus jäävad siiski alati omavahel seotuks).

Sõnastiku täiendamine elementhaaval
-----------------------------------
Ka sõnastikke saab programmi töö käigus täiendada, aga seejuures ei kasutata mitte meetodeid ``append`` või ``add``, vaid võtme järgi omistamist kujul ``sõnastik[võti] = väärtus``:

.. sourcecode:: py3

    # alustame tühja sõnastikuga
    telefoniraamat = {}

    while True:
        nimi = input("Sisesta inimese nimi (lõpetamiseks jäta tühjaks): ")
        if nimi == "":
            break
        telefon = input("Sisesta telefoninumber: ")
        telefoniraamat[nimi] = telefon
    
    print("Telefoniraamatu sisu: ")
    print(telefoniraamat)

.. note::

    Siin tuleb meeles pidada, et järjendite puhul on taoline omistamine võimalik vaid nende indeksitega, mis juba on järjendis olemas, st järjendit taolise lähenemisega kasvatada ei saa:
    
    .. sourcecode:: py3
    
        >>> sõnastik = {}
        >>> sõnastik[0] = "Tere"
        >>> sõnastik
        {0: 'Tere'}
        
    .. sourcecode:: py3
    
        >>> järjend = []
        >>> järjend[0] = 1
        Traceback (most recent call last):
          File "<pyshell#10>", line 1, in <module>
            järjend[0] = 1
        IndexError: list assignment index out of range

Sõnastiku elemendi väärtuse muutmine käib samasuguse süntaksiga nagu elemendi lisamine:

.. sourcecode:: py3

    telefonid = {'politsei': '110', 'päästeamet': '112', 'president': '631 6202'}
    
    uus_number = input("Sisesta uus presidendi number: ")
    telefonid['president'] = uus_number
    
    print("Uuendatud telefoniraamat:", telefonid)


Harjutus. Telefoniraamat
------------------------
Muuda ülalpool toodud telefoniraamatu näidet selliselt, et andmed loetakse sisse tekstifailist ja programm võimaldab kasutajal küsida telefoninumbrit omaniku nime järgi.

Mitmemõõtmelised andmestruktuurid
=================================
Nagu tead, saab Pythonis teatud lausete sisse panna teisi lauseid (nt tingimuslause sisse tsükleid või vastupidi) ja teatud avaldiste komponentideks võivad olla teised avaldised.

Samamoodi saab panna andmestruktuuridesse teisi andmestruktuure. Näiteks on võimalik luua järjendeid, mille elementideks on mingid järjendid, või siis ennikuid, mille elementideks on ennikud ja järjendid, või sõnastikke, mille elementideks on järjendid:

.. sourcecode:: py3
    
    # järjendite järjend
    tulemused = [[77, 2, 13], [64, 5, 6], [75, 8, 9]]
    
    # ennikute järjend
    arvunimed = [(1, "üks", "uno"), (2, "kaks", "dos"), (3, "kolm", "tres")]
    
    # ennik, mis sisaldab järjendit
    õpilase_andmed = ("Peeter", "Paat", 1997, [5, 4, 5, 3, 4, 3, 5, 5])
    
    # sõnastik, mille väärtusteks on järjendid
    hinded = { # Python lubab sulgude sees reavahetust vabalt kasutada
        'Peeter Paat': [5, 4, 5, 3, 4, 3, 5, 5],
        'Kadri Karu' : [5, 5, 5, 5, 4, 5, 5, 5],
        'Mart Maru'  : [3, 3, 3, 3, 5, 3, 3, 4]
    }

Antud näites kasutasime taolises üksteise sisse panemises ainult kahte taset, aga vajadusel on võimalik konstrueerida mistahes tasemete arvuga andmestruktuure, näiteks järjendite järjendite järjendeid (e kolmemõõtmelisi järjendeid):

.. sourcecode:: py3

    arvujärjendite_järjendite_järjend = [
        [[1, 2, 3], [4, 5, 6, 6, 6], [7, 8]],
        [[23, 11], [16, 63, 1], [7, 77, 777]]
    ]


.. topic:: Mitmemõõtmelised hulgad?
    
    Hulkade puhul peame pisut hoogu tagasi tõmbama -- kui soovime luua hulka, mille elementideks on hulgad, siis saame Pythonilt veateate:
    
    .. sourcecode:: py3

        >>> {{1,2}, {3,4,5}}
        Traceback (most recent call last):
          File "<pyshell#45>", line 1, in <module>
            {{1,2}, {3,4,5}}
        TypeError: unhashable type: 'set'        

    Lahtiseletatult ütleb veateade, et tüübil ``set`` puudub teatud omadus *hashable*, mille olemasolu on vajalik, et Python saaks väga kiiresti ja kindlalt kontrollida kahe väärtuse võrdsust. Kuna elementide võrdsuse kontroll on hulkade juures oluline (et vältida kahe võrdse elemendi sattumist samasse hulka), siis Python keeldub loomast hulkade hulka. Sama lugu on ka listide hulgaga:

    .. sourcecode:: py3

        >>> {[1,2], [3,4,5]}
        Traceback (most recent call last):
          File "<pyshell#46>", line 1, in <module>
            {[1,2], [3,4,5]}
        TypeError: unhashable type: 'list'

    Seevastu ennikute hulgaga jääb Python rahule:

    .. sourcecode:: py3

        >>> {(1,2), (3,4,5)}
        {(1, 2), (3, 4, 5)}

    Põhjus on selles, et ennikud pole muteeritavad ning seetõttu saab Python kasutada erinevaid lisanippe, et nendega opereerimist (sh nende võrdsuse kontrollimist) piisavalt efektiivselt korraldada.

    *Listid* ei sea mingeid piiranguid oma elementide tüübile, sest listi ei huvita elementide võrdsus või mittevõrdsus. Seetõttu pole mingit probleemi koostada Pythonis näiteks hulkade listi.
    
    *Sõnastike* puhul on piirangud vaid sõnastiku võtme tüübile -- ka siin nõutakse omadust *hashable* (kuna sõnastikku ei tohi lubada korduvaid võtmeid). Kirje väärtuse tüübi osas kitsendusi ei seata -- seega saab vabalt luua näiteks sõnastiku, mille võtmetüübiks on sõne ning väärtuse tüübiks arvude list -- nii nagu on demonstreeritud ülalpool toodud näites, kus sõnastikku ``hinded`` on kasutatud hinnete loetelu sidumiseks inimese nimega.




Mitmemõõtmeliste järjendite läbimine
------------------------------------
Taoliste andmestruktuuride kasutamiseks ei ole tarvis mingisuguseid erivõtteid -- tuleb lihtsalt meeles pidada, millist tüüpi elementidega meil mingil tasemel tegemist on.

Üritame näiteks kuvada ekraanile kahemõõtmelises järjendis sisalduvat infot *(NB! Enne selle programmi käivitamist käi tsüklid ise mõttes läbi ja ennusta, milline tuleb programmi väljund!)*:

.. sourcecode:: py3

    arvujärjendite_järjend = [
        [1, 2, 3, 4, 5, 6], 
        [6, 6, 7, 8],
        [23, 11, 16, 63],
        [17, 77, 777]
    ]
    
    print("Arvujärjendite järjend:", arvujärjendite_järjend)
    
    # tegemist on igal juhul mingi järjendiga,
    # seega kasutame tema läbimiseks for-tsüklit
    for arvujärjend in arvujärjendite_järjend:
        # arvujärjend tähistab ühte arvujärjendite_järjend-i elementi
        # selle läbimiseks kasutame jällegi for-tsüklit
        print("Välimine tsükkel, arvujärjend:", arvujärjend)
        for arv in arvujärjend:
            print("Sisemine tsükkel, arv:", arv)


Kuigi tsüklit tsükli sees oled ka juba eespool kohanud, võib see siiski tunduda pisut veider. Selles pole tegelikult midagi erilist, mõlemad tsüklid toimivad tavaliselt -- enne uuele ringile minekut tehakse tsükli keha sees olevad käsud lõpuni. See tähendab muuhulgas seda, et välimise tsükli iga korduse puhul tehakse läbi sisemise tsükli kõik kordused.

.. note::

    Viimases näites läks meil vaja kahte tsüklit, et jõuda välja andmestruktuuri põhjani välja. Alati ei ole meil aga taolist kõikide elementide läbikäimist tarviski. Järgnev näiteprogramm väljastab sama kahemõõtmelise järjendi kõigi elementide (s.o arvujärjendite) summad:

    .. sourcecode:: py3

        arvujärjendite_järjend = [
            [1, 2, 3, 4, 5, 6], 
            [6, 6, 7, 8],
            [23, 11, 16, 63],
            [17, 77, 777]
        ]
        
        for arvujärjend in arvujärjendite_järjend:
            print(sum(arvujärjend))



Mitmemõõtmeliste järjendite indekseerimine
------------------------------------------
Eelnevates näidetes põhinesid tsüklid otse järjenditel, aga nagu tead, võib järjendeid läbida ka indeksite abil:

.. sourcecode:: py3

    arvujärjendite_järjend = [
        [1, 2, 3, 4, 5, 6], 
        [6, 6, 7, 8],
        [23, 11, 16, 63],
        [17, 77, 777]
    ]
        
    # väljastan kõik järjendis sisalduvad arvud
    for i in range(len(arvujärjendite_järjend)):
        arvujärjend = arvujärjendite_järjend[i]
        for j in range(len(arvujärjend)):
            arv = arvujärjend[j]
            print(arv)


Abimuutuja ``arvujärjend`` kasutamise asemel oleksime võinud kasutada ka kahte indekseerimist järjest (pööra tähelepanu viimasele reale):

.. sourcecode:: py3

    ...
    for i in range(len(arvujärjendite_järjend)):
        for j in range(len(arvujärjendite_järjend[i])):
            print(arvujärjendite_järjend[i][j])

Viimasel real oleva ``print``-i argumendi tähendus saab võibolla selgemaks, kui sinna sulge juurde kirjutada: 

.. sourcecode:: py3

    (arvujärjendite_järjend[i])[j]

Nüüd on ilusti näha, et sulgudes olev avaldis kujutab endast ``i``-ndat elementi ``arvujärjendite_järjend``-ist (ehk siis ühte arvujärjendit) ning sellest omakorda võetakse element indeksiga ``j``, seega on tulemuseks mingi arv.

Kokkuvõtteks: Mitmemõõtmeliste andmestruktuuride kasutamise põhimõte
--------------------------------------------------------------------
Pythonis ei ole tehniliselt võttes eraldi konstruktsiooni "kahemõõtmeline järjend". On järjendid ja järjendite elemendid võivad olla suvalist tüüpi (sh järjenditüüpi). Mõistet *kahemõõtmeline järjend* kasutatakse vaid selleks, et anda lugejale/kuulajale veidi lisainfot vaadeldava järjendi sisu/kuju kohta.

Olgu meil ühe-, kahe- või sajamõõtmeline järjend, tegemist on alati ikkagi järjendiga ja nii tuleb talle ka läheneda. Vaja on lihtsalt arvestada, millised on tema elemendid (vastavalt lihttüüpi väärtused, ühemõõtmelised järjendid või 99-mõõtmelised järjendid).
    
Sama põhimõte kehtib ka "järjendite ennikute" ja "hulkade sõnastike ennikute järjendite sõnastike järjendite ennikute sõnastikega" -- alusta lähenemist välimisest kihist ja pea meeles, millised on sisemised kihid.

.. note::

    Proovi panna kirja üks hulkade sõnastike ennikute järjendite sõnastike järjendite ennikute sõnastik.


Harjutus. Sudoku tabeli sisselugemine
-------------------------------------
Kirjuta programm, mis loeb etteantud failist (:download:`sudoku.txt <downloads/sudoku.txt>`) arvud kahemõõtmelisse järjendisse.

.. note:: 
    Kui jääd jänni, siis uuri järgmist punkti, aga enne kindlasti ürita ise! Kõik selle ülesande lahendamiseks vajalikud teadmised on sul juba olemas!



Näide: Mitmemõõtmelise järjendi koostamine jupphaaval
-----------------------------------------------------
Mitmemõõtmelise järjendi loomisel ``append`` meetodiga tuleb jällegi mõelda, millised peavad olema järjendi elemendid. Järgnev näide on üks võimalik lahendus eelnevale ülesandele (kui ülesanne jäi sulle liiga raskeks, siis analüüsi seda näitelahendust eriti hoolikalt):

.. sourcecode:: py3

    f = open("sudoku.txt")

    sudoku_tabel = []
    for rida in f:
        jupid = rida.split()
        
        # kõigepealt teen abimuutujasse valmis ühe tabeli rea ...
        sudoku_rida = []
        
        for jupp in jupid:
            sudoku_rida.append(int(jupp))

        # ... ja siis lisan selle tabelisse
        sudoku_tabel.append(sudoku_rida)    

    f.close()
    print(sudoku_tabel)


Näide: Eksami statistika
------------------------
Õppejõud koostas eksami, milles oli 7 ülesannet. Iga ülesande eest võis saada kuni 10 punkti. Eksami tulemused on kirjas failis :download:`eksam.txt<downloads/eksam.txt>`.

Leiame iga tudengi eksamipunktide kogusumma.

*NB! Enne näitelahenduse vaatamist mõtle, kuidas tuleks seda ülesannet lahendada!* 

.. sourcecode:: py3

    # faili avamine
    file = open("Eksam.txt")

    # tulemuste lugemine tabelisse
    tabel = []
    nimed = []

    for rida in file :
       # eralda tudengi nimi
       jupid = rida.split("|")
       nimed.append(jupid[0].strip())

       # võta ülejäänud osa juppideks
       tulemuste_jupid = jupid[1].split(",")

       # märgi tudengi tulemused tabelisse
       tulemused = []
       for tulemus in tulemuste_jupid:
           tulemused.append(int(tulemus))
       tabel.append(tulemused)

    # faili sulgemine
    file.close()

    n = len(tabel)

    print()

    # Tulemuste väljastamine
    print("Tulemused:")
    for i in range(n) :
        print("{0:>2}. {1:<25}: ".format(i+1, nimed[i]), end=' ')
        for j in range(7) :
            print("{0:>2}".format(tabel[i][j]), end=' ')
        print()


    print("-----------------")
    # reasummad
    for i in range(n) :
        summa = 0
        for j in range(7) :
            summa += tabel[i][j]

        print("{0} sai {1} punkti".format(nimed[i], summa))



Harjutus. Keskmine tulemus ülesannete kaupa
-------------------------------------------
Täienda eelnevat näiteprogrammi nii, et see näitaks, millised ülesanded olid üldiselt raskemad ja millised kergemad. Selleks väljasta keskmised tulemused ülesannete kaupa (st eraldi kõigi tudengite 1. ülesande eest saadud punktide keskmine jne).

.. hint::

    Ühe ülesande punktide kogusumma arvutamise skeem on väga sarnane ühe tudengi punktisumma arvutamisega.

Tabelite esitamine
==================
Üritame nüüd oma teadmisi listidest ja sõnastikest kasutada tabelite esitamiseks.

Andmetabelites tähistab tavaliselt iga rida mingit objekt ja iga veerg mingi objekti tunnust:

+----------+-------------+------------+-------------+
| Eesnimi  | Perenimi    | Sünniaasta | Kinganumber |
+==========+=============+============+=============+
| Mari     | Maasikas    | 1994       | 37          |
+----------+-------------+------------+-------------+
| Peeter   | Pontsakas   | 2001       |             |
+----------+-------------+------------+-------------+
| Albert   | Abivalmis   | 1969       | 44          |
+----------+-------------+------------+-------------+

Pythonis on selliste andmete esitamiseks mitu võimalust. 

Tabel kui maatriks
------------------
Kõige otsesemalt saab tabeleid esitada muidugi listide listina e maatriksina, kus välise listi elementideks on tabeli read ja iga rida on esitatud omakorda listi või ennikuna, mille elementideks on rea lahtrid / objekti tunnused. Ülalpool näidatud tabeli võiks esitada sellise Pythoni maatriksiga:

.. sourcecode:: py3

    [["Mari", "Maasikas", 1994, 37],
     ["Peeter", "Pontsakas", 2001, None],
     ["Albert", "Abivalmis", 1969, 44]]
     
Kuna Peeter Pontsaka kinganumber polnud teada, siis kasutasime selle asemel väärtust ``None``, mida tavapäraselt kasutatakse puuduva väärtuse tähistamiseks. Kui oleksime Peetri listi jätnud lihtsalt lühemaks, siis see oleks teinud maatriksi töötlemise keerulisemaks.

Ilmselt märkasid, et see maatriks ei sisalda meie algse tabeli kogu infot -- veerupealkirjad on puudu. Veerupealkirjade rea ärajätmine võib teha maatriksi analüüsimise veidi lihtsamaks, kuna siis ei pea esimest rida ülejäänutest erinevalt käsitlema. Miinuseks on see, et sellise lähenemise korral peab eraldi meeles pidama, mitmendas veerus on millised andmed. 

Tabeli esitamine veergude kaupa
-------------------------------
Tabelile võib läheneda ka teisiti, võttes esmaseks jaotuseks veerud. Sel juhul võiksime andmed jaotada näiteks mitmesse listi, kus ühe inimese andmed on alati samal positsioonil:

.. sourcecode:: py3

    eesnimed = ["Mari", "Peeter", "Albert"]
    perenimed = ["Maasikas", "Pontsakas", "Abivalmis"]
    sünniaastad = [1994, 2001, 1969]
    kinganumbrid = [37, None, 44]

Sellise jaotuse puhul on meil kerge koostada näiteks histogrammi, mis näitab kui sagedasti mingit kinganumbrit esineb.

Rea esitamine sõnastikuna
-------------------------
Tabeli võime esitada ka sõnastike listina, kus iga sõnastik tähistab ühte rida:

.. sourcecode:: py3

    [{"Eesnimi" : "Mari", "Perenimi": "Maasikas", "Sünniaasta" : 1994, "Kinganumber" : 37},
     {"Eesnimi" : "Peeter", "Perenimi": "Pontsakas", "Sünniaasta" : 2001},
     {"Eesnimi" : "Albert", "Perenimi": "Abivalmis", "Sünniaasta" : 1969, "Kinganumber" : 44}]

See lähenemine on eriti mugav siis, kui objekti võimalike tunnuste loetelu on lahtine või kui võimalikke tunnuseid on palju, aga enamiku objektide korral on teada vaid mõned tunnused. Selles näites ongi erinevatel objektidel kirjas erinev arv tunnuseid.



Kahekordsed tsüklid ühemõõtmelisel järjendil
============================================
Vahel läheb mitmekordseid tsükleid tarvis ka ühemõõtmeliste järjendite töötlemiseks.

Näide: Libisev keskmine
-----------------------
Antud on fail (:download:`aktsiad.txt <downloads/aktsiad.txt>`), kus on antud ühe aktsia hinnad järjestikustel päevadel. Küsida kasutajalt päevade arv *k* ning väljastada järjest iga päeva kohta sellele eelnenud *k* päeva keskmine aktsiahind.

.. sourcecode:: py3

    # hindade lugemine failist
    hinnad = [] # hinnad on tavaline ühemõõtmeline järjend
    f = open("aktsiad.txt")
    for rida in f:
        hinnad.append(float(rida))
    f.close()


    # keskmiste arvutamine
    k = int(input("Mitut eelnevat päeva soovid keskmise arvutamisel kasutada: "))

    # kuna meil on vaja k eelnevat päeva, siis alustame indeksist k
    for i in range(len(hinnad)):
        print("{0:>2}. päev, hind oli {1:>6.2f}.".format(i, hinnad[i]), end=' ')

        # eelneva k päeva keskmist saame näidata alates päevast k
        if i >= k:
            k_eelmise_summa = 0
            for j in range(i-k, i):
                k_eelmise_summa = k_eelmise_summa + hinnad[j]
            keskmine = k_eelmise_summa / k
            print("Eelnenud {0} päeva keskmine hind oli {1:>6.2f}".format(k, keskmine))
        else:
            # esimeste päevade juurde paneme ainult reavahetuse
            print()
    
Sisemise tsükli jaoks on valitud väiksem indeksivahemik (``range(i-k, i)``), mis vastab *k* eelnevale päevale ja see tsükkel läbib sama järjendit nende indeksite piires.

.. note::

    Tegelikult on seda ülesannet võimalik lahendada ka ilma sisemist tsüklit kasutamata. Sellest, kuidas seda teha, on võimalik lugeda selle peatüki lisas "Keerukus". 


Harjutus. Erinevad väärtused
----------------------------
Koosta funktsioon ``kõik_erinevad``, mis tagastab ``True`` või ``False`` vastavalt sellele, kas etteantud järjendis on kõik väärtused erinevad või mitte.

.. hint::
        
    Iga elemendi vaatlemisel kontrolli sisemise tsükliga, kas sama väärtus esineb ka mõnel muul positsioonil.
    
.. note::

    Seda ülesannet saaks lahendada ka ``count`` meetodit kasutades, aga kuna ``count`` meetod kasutab sisemas samuti tsüklit, siis kokkuvõttes on Pythoni jaoks ikkagi tegemist kahekordse tsükliga.
    
    On veel üks viis selle ülesande lahendamiseks, mille jaoks läheb vaja ühe selle peatüki teema tundmist.
    
    .. hint::

        >>> set([1,2,3,2])
        {1, 2, 3}
    
    
    
Harjutus. Mõistatuslik teisendus
--------------------------------
Proovi ennustada, mida teeb järgmine funktsioon: 

.. sourcecode:: py3
    
    def teisenda(järjend):
        # teen järjendist koopia
        uus = järjend[:]
        
        for i in range(len(uus)):
            for j in range(i+1):
                if uus[j] < uus[i]:
                    uus[i], uus[j] = uus[j], uus[i]
        
        return uus


Sisemise tsükli viimasel real on tegemist kahe elemendi väärtuse vahetamisega -- sama skeemi nägid juba ennikute teema juures.


.. hint::

    Katseta seda funktsiooni näiteks järjendiga ``[5, 2, 1, 4, 3]``. Proovi mõttes funktsiooni töö läbi mängida mõne lühema järjendiga.


Andmestruktuurid
================
Peatüki pealkiri on "Andmestruktuurid", nüüd on paras aeg lõpuks ära öelda, mida see sõna tähendab.

Programmeerimisel jaotatakse andmetüübid laias laastus *lihttüüpideks* ja *liittüüpideks*. Lihttüübid tähistavad atomaarseid (e jagamatuid) väärtusi -- näiteks arvutüübid ja tõeväärtustüüp; liittüübid (näiteks list ja ennik) aga tähistavad väärtusi, mida saaks veel mingiteks alamkomponentideks (nt listi elementideks) jagada. (Sõnega on Pythoni puhul pisut segased lood -- seda võib olenevalt vaatenurgast pidada nii lihttüübiks kui ka liittüübiks.)

Nagu öeldud, liittüüpi väärtused on kombineeritud mingitest teistest väärtustest. Oluline on see, et need komponendid moodustavad mingi kindla struktuuri. Näiteks järjendite puhul moodustub struktuur sellest, et iga komponent (element) on teiste komponentidega võrreldes kas eespool või tagapool, teisisõnu -- järjendi struktuur määrab elementide järjestuse. Teistel Pythoni liitüüpidel on teistsugune struktuur -- näiteks hulgatüübi struktuur määrab ära vaid selle, millised elemendid hulka kuuluvad, elementide järjestus pole selles struktuuris oluline. Kuna struktuur on liittüüpide puhul väga tähtis, siis nimetatakse neid vahel ka *struktuurseteks tüüpideks* või *andmestruktuurideks*.

Antud õpiku käsitluses on erinevatel andmestruktuuridel erinevad kasutusviisid, mida nad toetavad -- listi puhul saab elementi ``append``-ida, sõnastikus saab küsida elementi tema (suvalist tüüpi) võtme järgi jne, st meid huvitab eelkõige mida mingi andmestruktuur teha oskab. Reaalsetes programmides aga on tihti vaja teada ka seda, kuidas seda tehakse. Seetõttu on loodud näiteks erinevaid listitüüpe, millega saab teha samu asju, aga mis sisemas töötavad erinevalt ning seetõttu sobivad eri situatsioonidesse paremini või halvemini (näiteks ühe tuntud listitüübi variatsiooni puhul toimib indekseerimine väga kiiresti, aga teise puhul saab väga kiiresti listi algusesse uue elementi lisada).

Algoritmid ja andmestruktuurid
------------------------------
Programmeerimise teemad jaotatakse tihti tinglikult kaheks pooleks -- *algoritmid* ja *andmestruktuurid* (või lihtsalt *andmed*).
    
Algoritmid kehastavad programmide aktiivset poolt -- nad kirjeldavad mingit tegevust, arvutamist, valikut, teisendamist vms. Selle poole märksõnad on näiteks ``if``, ``print``, ``while``, ``sin``.

Andmeid (sh andmestruktuure) võib pidada programmide passiivseks pooleks -- nad kehastavad mingeid abstraktseid või konkreetseid asju, seoseid või muud laadi infot ja nad "lihtsalt on". Selleks, et midagi juhtuks, peab mõni algoritm neid manipuleerima või uurima ja saadud info põhjal midagi tegema. Selle poole märksõnadeks on nt *väärtus*, *tüüp*, *sõne*, *list*.




Ülesanded
=========

1. Teksti analüüs
-----------------
Kirjuta funktsioon ``sümbolite_sagedus``, mis võtab argumendiks sõne ja tagastab sõnastiku, mis sisaldab sõnes sisalduvate tähtede esinemise sagedusi. Sõnastiku võtmeteks peaksid olema tähed või muud sümbolid (st tehniliselt võttes sõned) ja väärtusteks täisarvud.

Kirjuta ka funktsioon ``erinevad_sümbolid``, mis võtab samuti argumendiks sõne, aga tagastab hulga kõikide antud sõnes leiduvate erinevate sümbolitega.


Näited:

.. sourcecode:: py3

    >>> sümbolite_sagedus("Tere maailm!")
    {'!' : 1, 'i' : 1, 'T' : 1, 'r' : 1, 'm' : 2, 'a' : 2, 'e' : 2, ' ' : 1, 'l' : 1}
    >>> erinevad_sümbolid("hulk ei sisalda kunagi korduvaid elemente")
    {'v', 't', 'i', 'r', 'h', 'u', 'm', 'g', 'a', 'o', ' ', 'e', 's', 'd', 'k', 'n', 'l'}

.. hint::

    Sümbolite sageduse leidmisel alusta tühja sõnastikuga.

.. hint::

    Meeldetuletus: sõnesid saab käsitleda sümbolite järjendina.

.. hint::
    
    Kui nuputad, millises etapis tuleks kasutada oma head tuttavat ``split`` meetodit, siis mõtle järele, kas seda üldse läheb antud ülesandes tarvis.



2. Eksami statistika, 2. osa
----------------------------
See ülesanne põhineb ülalpool toodud näiteülesandel.

Kõigepealt muuda etteantud lahendust nii, et küsimuste arv ei oleks fikseeritud, vaid tuvastataks käigu pealt vastavalt esimesel real olevate tulemuste arvule (võib eeldada, et kõigil ridadel on võrdne arv tulemusi).

Kõik järgmiste ülesannete lahendused peavad samuti töötama suvalise tulemuste arvu korral. Lahendused võib kõik teha järjest ühte samasse faili. Ülesande lahendamisel võid kasutada kõiki Pythoni funktsioone (sh ``sum`` ja ``max``).

#. **Maksimaalsed tulemused**: leia iga ülesande kohta selle lahendamisel saadud maksimaalne skoor.

#. **Seinast seina**: väljasta nende tudengite nimed, kes said vähemalt ühe ülesande eest 10 punkti ja mõne teise ülesande eest 0 punkti.

#. **Priimused**: leia nende tudengite nimed, kes kogusid summaarselt kõige rohkem punkte. Kui mitu inimest sai sama palju punkte, väljasta kõigi nende nimed (vihje – kogu need nimed järjendisse).

#. **Spikerdamine**: fail on koostatud nii, et kõrvuti istunud tudengite andmed on failis järjest. Kontrolli, kas tulemused viitavad sellele, et mõni spikerdas oma naabri pealt. Loeme, et spikerdamises võib tudengit kahtlustada, kui tema kõik tulemused on kas võrdsed või ülimalt 2 punkti võrra väiksemad kui ühel tema kahest naabrist. Väljasta kõigi spikerdamises kahtlustatavate tudengite nimed.

#. **Skaleeritud hindamine**: oletame, et hindamisskeem on selline, et kui mõne ülesande eest ei saanud keegi maksimumpunkte, siis korrutatakse kõigi tudengite punktid läbi sellise koefitsiendiga, et parima tulemuse saanud tudengi uus tulemus oleks 10. Teisenda ja väljasta kõigi tudengite kõigi ülesannete punktid sellest hindamisskeemist lähtuvalt (ühe komakoha täpsusega). Vihje: koosta järjend, kus on iga ülesande kohta leitud sellele vastav kordaja, ning kasuta seda tudengite hinnete tuvastamisel.

#. **Hobide mõju**: failis :download:`hobid.txt<downloads/hobid.txt>` on eksami teinute hobid. Täienda programmi nii, et see väljastaks iga hobi kohta vastavate tudengite keskmise eksamitulemuse.

3. Lapsed ja vanemad
--------------------
Failis :download:`lapsed.txt <downloads/lapsed.txt>` on igal real vanema isikukood, tühik ja lapse isikukood. Failis :download:`nimed.txt <downloads/nimed.txt>` on igal real ühe inimese isikukood, tühik ja tema nimi. Võib eeldada, et korduvaid nimesid failis ei esine. Võib eeldada, et iga failis *lapsed.txt* oleva isikukoodi jaoks on failis *nimed.txt* välja toodud vastav nimi. 

Kirjuta programm, mis väljastab ekraanile iga lapsevanema kohta ühe rea: tema nimi, koolon, tühik ning seejärel komade ja tühikutega eraldatuna tema laste nimed. Näiteks antud failide korral peaks ekraanile ilmuma järgnevad read (lapsevanemate ega nende laste järjekord pole seejuures tähtis):

.. sourcecode:: none

    Madli Peedumets: Robert Peedumets, Maria Peedumets
    Peeter Peedumets: Robert Peedumets, Maria Peedumets
    Kadri Kalkun: Liisa-Maria Jaaniste
    Karl Peedumets: Peeter Peedumets

Põhitöö tuleks delegeerida funktsioonile ``seosta_lapsed_ja_vanemad``, mis võtab argumentideks laste faili nime ja nimede faili nime, ning tagastab sõnastiku, kus kirje võtmeks on lapsevanema nimi ja väärtuseks tema laste nimede hulk. 

Näiteks antud failide korral peaks ``seosta_lapsed_ja_vanemad("lapsed.txt", "nimed.txt")`` tagastama

.. sourcecode:: py3

    {'Madli Peedumets': {'Robert Peedumets', 'Maria Peedumets'},
     'Peeter Peedumets': {'Robert Peedumets', 'Maria Peedumets'},
     'Kadri Kalkun': {'Liisa-Maria Jaaniste'},
     'Karl Peedumets': {'Peeter Peedumets'}}
    

4. Trips-traps-trull
--------------------
Kirjuta funktsioon ``võitja``, mis võtab argumendiks maatriksina (st listide listina) esitatud trips-traps-trulli mängu seisu, ning tagastab ``'O'`` (so suurtäht *O*, mitte null) kui O-ga mängija on võitnud, ``'X'``, kui X-ga mängija on võitnud ja ``'?'``, kui mäng on pooleli või viigis.

Näited:

.. sourcecode:: py3

    >>> võitja([['O',' ','X'],
                ['O','X',' '],
                ['X',' ',' ']])
    'X'

    >>> võitja([['O',' ','X'],
                ['O',' ',' '],
                ['X',' ',' ']])
    '?'

      



5. Sudoku lahenduse kontrollimine
---------------------------------

Kirjuta programm, mis kontrollib, kas etteantud failis (:download:`sudoku.txt <downloads/sudoku.txt>`) on korrektne Sudoku lahendus. Mittekorrektse lahenduse korral tuleb öelda, millises veerus, reas või 3x3 ruudus probleem esineb.

Lisainfot Sudoku kohta: http://en.wikipedia.org/wiki/Sudoku.

NB! Testi oma programmi nii korrektse kui ka mittekorrektse lahendusega!

.. note::

    Tegemist on küllalt mahuka ülesandega, seega on kasulik jagada ülesanne mõttes alamülesanneteks ja panna iga alamülesande lahendus kirja eraldi funktsioonina. 
    


.. hint::
    
    Üks võimalik viis lahenduse struktureerimiseks:
    
    .. sourcecode:: py3
    
        def loe_tabel(failinimi):
            tabel = []
            ...
            return tabel
        
        def veerg_on_korras(tabel, veeru_indeks):
            # tagastab True või False
            ...
        
        def rida_on_korras(tabel, rea_indeks):
            ...
            
        def ruut_3x3_on_korras(tabel, nurga_rea_indeks, nurga_veeru_indeks):
            ...
        
        
        # kõigepealt loeme andmed failist kahemõõtmelisse järjendisse
        tabel = loe_tabel("sudoku.txt")
        
        # alustame kontrollimist optimistlikult
        lahendus_on_korras = True
        
        # kontrollime üle kõik veerud
        for i in range(9):
            if not veerg_on_korras(tabel, i):
                # tuleb välja, et optimism polnud põhjendatud
                # korrigeerime on seisukohta
                lahendus_on_korras = False
        ...
        ...
        
        if lahendus_on_korras:
            print("Korras")
        else:
            print("Viga!)
            # aga kuidas öelda vea asukoht?
        


.. hint::

    Iga rea, veeru ja 3x3 ruudukese kontrollimisel koosta vaadeldavatest elementidest arvuhulk ...
    
.. hint::

    ... ja kontrolli, kas see arvuhulk võrdub ühe konkreetse (ning Sudoku puhul olulise) arvuhulgaga.


    
6. SKP
------
*See ülesanne on antud koos näitelahendusega, aga enne selle vaatamist ürita ise lahenduseni jõuda!*

Antud on fail :download:`SKP.txt<downloads/SKP.txt>`, kus on kirjas riikide nimed ja nende SKP-d semikooloniga eraldatult (miljonites USA dollarites 2009. aasta seisuga). Küsida kasutajalt, kui suur SKP teda huvitab, ning leida kolm sisestatud arvule kõige lähema SKP-ga riiki.

.. hint::

    Kõige lähema leidmine on iseenesest lihtne – leida lihtsalt selline, mille jaoks absoluutväärtus `| SKP – sisestatud arv |` oleks minimaalne. Kuidas aga leida kolme lähimat? Tuletame aga meelde, kuidas me leidsime minimaalset – me hoidsime vähimat meeles ning kui parasjagu vaadeldav element oli sellest väiksem, asendasime ta sellega. Miski ei takista meid aga hoidmast ühe vähima asemel nimekirja näiteks kolmest. Kui nüüd leidub uus, mis on kõigist kolmest väiksem, siis lisame selle sinna nimekirja ning viskame seal enne olnutest kõige suurema välja. Sama teeme tegelikult alati, kui uus väärtus on vähemalt kõige suuremast seni meeles hoitud väärtusest väiksem. Seega piisab, kui leiame igal sammul meeles peetuist suurima ja vaatame, kas uus on sellest väiksem. Kui on, asendame endise meeles peetava suurima lihtsalt uue leituga. See aga tähendab, et igal sammul tuleb vaid leida maksimaalne meeles hoitutest – seda me aga juba oskame.

    .. sourcecode:: py3

        skp = float(input("Sisesta arv, millele lähedased SKP-d sind huvitavad:"))

        skpd = []
        vahed = []
        nimed = []

        # faili sisse lugemine
        f = open("SKP.txt","r", encoding="UTF-8")
        for rida in f:
            # teisenda rida riigiks ja SKP-ks ning lisa need järjenditele
            paar = rida.split(";")
            nimed.append(paar[0])
            skpd.append(float(paar[1]))

            # arvutada ka absoluutväärtus vahest nõutud SKP-ga
            vahed.append(abs(float(paar[1])-skp))

        f.close()

        # eralda esimesed kolm elementi esialgseks lähimate järjendiks
        lahimadskpd = skpd[0:3]
        lahimadnimed = nimed[0:3]
        lahimadvahed = vahed[0:3]

        # leia tegelikud lähimad järjendi läbi käimise teel
        for i in range(3,len(skpd)) :
            # leia maksimaalse erinevusega indeks meeles peetute hulgast
            maksj = 0
            for j in range(1,len(lahimadvahed)) :
                if lahimadvahed[j] > lahimadvahed[maksj] :
                    maksj=j

            # vaata, kas uus leitu on meie parameetrile lähemal
            if vahed[i] < lahimadvahed[maksj] :
                # kui on, asenda seal enne olnud riigi info uuega
                lahimadvahed[maksj] = vahed[i]
                lahimadskpd[maksj] = skpd[i]
                lahimadnimed[maksj] = nimed[i]

        # väljasta tulemus
        for i in range(0,len(lahimadvahed)) :
            print(lahimadnimed[i] + " - " + str(lahimadskpd[i]))



Projekt
=======
Pythoni andmestruktuuride salvestamine ja sisselugemine
-------------------------------------------------------
Selleks, et järjendikujulist infot failis hoida, oleme seni kasutanud mingit lihtsat tekstilist formaati, mida on mugav näiteks tsükli ja ``split``-i abil töödelda. Selle lähenemise eelis on see, et taolist tekstiformaati saab vabalt ka suvalises tekstiredaktoris lugeda või koostada.

Keerulisemate andmestruktuuride ja nende kombinatsioonide (nt sõnastike või mitmemõõtmeliste järjendite) puhul võib sobiva formaadi väljatöötamine ja kasutamine olla küllalt suur töö. Seetõttu on Pythonis olemas vahendid, mis seda tööd lihtsustavad.

Esimese võimalusena uurime käske ``repr`` ja ``eval``:

.. sourcecode:: py3

    >>> repr(3)
    '3'
    >>> repr("tere")
    "'tere'"
    >>> repr({'a', 'b', 'c'})
    "{'a', 'c', 'b'}"
    >>> eval("3")
    3
    >>> eval("'tere'")
    'tere'
    >>> eval("{'a', 'c', 'b'}")
    {'a', 'c', 'b'}
    >>> eval(repr(3))
    3

Nende kasutamise põhimõte on lihtne: ``repr`` teisendab argumendiks antud väärtuse sõneks ja ``eval`` teeb sõnena esitatud väärtuse tagasi algseks väärtuseks. Faili salvestamisel tuleks lihtsalt väärtus teisendada sõneks ja salvestada saadud sõne juba tuttavate vahenditega. Failist lugemisel tuleb sisseloetud sõne teisendada ``eval``-iga tagasi algseks väärtuseks.

.. note:: 

    Kui sulle tundub, et ``repr`` ja ``str`` on väga sarnased funktsioonid, siis on sul täiesti õigus -- paljude andmetüüpide puhul toimivad nad täpselt samamoodi. Mõnede tüüpide puhul on aga ``str``-i ülesandeks moodustada väärtuse "kasutajasõbralik" esitus ja ``repr`` ülesandeks moodustatada "``eval``-i sõbralik" esitus, seetõttu on tavaks kasutada koos ``eval``-iga justnimelt funktsiooni ``repr``.

Tegelikult sobib ``eval`` suvalise sõnena esitatud Pythoni avaldise väärtustamiseks. Seetõttu on selle kasutamisel oht, et kui keegi sinu andmeid pahatahtlikult modifitseerib, siis andmete ``eval``-iga sisselugemisel käivitab programm hoopis mingi pahatahtliku käsu (näiteks kustutab kogu kõvaketta sisu). Seega maksab uurida ka alternatiivset viisi Pythoni andmete faili salvestamiseks -- käsud ``pickle.dump`` ja ``pickle.load``: http://docs.python.org/3/library/pickle.html. 


Lisalugemine
============
Keerukus
--------
Üldiselt on üht ja sama ülesannet võimalik tihti lahendada mitmel väga erineval moel. Näiteks sobib ülesande "Libisev keskmine" lahenduses keskmiste leidmiseks ka järgmine programmijupp:

.. sourcecode:: py3

    ...
    
    # keskmiste arvutamine
    # leia kumulatiivsed summad

    summad = [0.0]

    for i in range(0, len(hinnad)):
       summad.append(summad[i] + float(hinnad[i]))

    # Leia k eelmise päeva keskmised
    for i in range(k, len(hinnad) + 1):
       keskm = summad[i] - summad[i-k]
       keskm = keskm / k
       print("{0}-ndale päevale eelnenud {1} päeva keskmine oli {2:.2f}".format(i,k,keskm))

See programm on mingis mõttes keerulisem kui ülesande algne lahendus, sest keskmise jaoks vajalike summade otse leidmise asemel leitakse siin alguses kõik kumulatiivsed summad, st summad esimesest aktsiahinnast kuni i-nda aktsiahinnani (kõikide i-de jaoks). Seejärel kasutatakse neid summasid kavalalt, et *k* eelmise elemendi summat leida, lähtudes tõdemusest, et

.. sourcecode:: none

    a[i-k+1] + a[i-k+2] + ... + a[i] == (a[0]+a[1] + ... + a[i]) – (a[0]+a[1] + ... + a[i-k])

Kui samale ülesandele on kaks lahendust, tekib paratamatult küsimus, kumb neist parem on. Ühest vastust sellele ei ole. Õpetamise kontekstis on näiteks selge, et esimene lahendus sobib kahekordse tsükli illustreerimiseks märksa paremini, sest teine lahendus seda konstruktsiooni isegi ei kasuta. Samuti on esimene programm ehk ka lihtsamini kontrollitav, sest ta on lühem, ning selle asemel, et mingeid trikke kasutada, leiab need keskmised vahetult summade leidmise kaudu.

Teisel lahendusel on esimese ees siiski üks oluline eelis, mis tuleb küll välja alles suuremate andmestike puhul. Kui näiteks aktsiahindu ei vaadata mitte päevade, vaid sekundite lõikes, võib neid failis olla mõnekümne asemel miljoneid, ning keskmiseid oleks vaja samuti leida ilmselt mitte üle 10 vaid pigem üle 100 000 eelmise väärtuse. Sellisel juhul jääks esimene lahendus märkimisväärselt aeglasemaks ja seda väga lihtsal põhjusel: esimene lahendus teeb iga keskmise leidmiseks *k* liitmistehet, kuid teine lahendus saab sellega eelnevalt leitud summade abil hakkama vaid ühe lahutamistehtega. Kuigi ka summade leidmiseks kulub aega, on lihtne veenduda, et see kuluv aeg on samuti vaid keskmiselt üks liitmine iga *i* väärtuse jaoks. Kokkuvõttes kulub teisel lahendusel seega iga *k*-keskmise peale üks liitmine ja üks lahutamine, samas kui esimene lahendus peab tegema k liitmist.

Programmi poolt tehtavate sammude arvu hindamist nimetatakse selle *ajalise keerukuse* analüüsimiseks. Selline analüüs muutub oluliseks eelkõige suurte andmemahtude korral - väikeste andmemahtude korral (paartuhat erinevat aktsiahinda) töötavad mõlemad lahendused lihtsalt nii kiiresti, et inimene nende töökiiruse erinevust ei taju, kuid mida suuremad on andmemahud, seda suurem on erinevus ja seda eelistatum on teine lahendus esimesele.

Üldiselt tehakse sellist analüüsi küllaltki umbkaudselt, loendades vaid neid samme, mida korduvalt tehakse ning tehes isegi seda tihti ligikaudselt. Näiteks esimest lahendust analüüsides vaadataks, et kõige rohkem tehakse sisemise tsükli liitmistehet, mis toimub kokku `(n-k)*(k-1)` ehk suurusjärgus `n*k` korda, samas kui teises lahenduses toimub kumulatiivsete summade leidmisel n liitmist ja hiljem keskmiste leidmisel `n-k` lahutamist, st kokku `2n-k` ehk suurusjärgus `n` tehet. Kuna üldiselt `n` kasvades ka `k` kasvab, võib teha lisaeelduse, et `k` ja `n` on umbes samas suurusjärgus, mis annaks esimese algoritmi keerukuse hinnanguks `n`\ :sup:`2` tehet ning teise jaoks lihtsalt `n` tehet. Sealt ongi näha, et mida suurema väärtuse `n` omandab (st mida suurem on andmestik), seda suuremaks muutub hinnagute erinevus ja seega ka töökiiruste erinevus.

Sellist analüüsi nimetatakse *asümptootiliseks*, sest ta kehtib `n` suurte väärtuste korral ning üldiselt seda paremini, mida suuremad `n` väärtused on. Selline ligikaudne lähenemine on tegelikult formaliseeritav nn *O-notatsiooni* abil, mis annab ka küllalti täpsed piirangud sellele, kuidas ja mis alustel üldistada ja lihtsustada tohib.


Kommentaarid
============
.. disqus::
    :disqus_identifier: andmestruktuurid