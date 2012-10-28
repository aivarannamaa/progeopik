9. Andmestruktuurid
=============================================
.. warning::

    Selle peatüki materjal võib veel muutuda

Juba 2. peatükis oli juttu ühest olulisest programmeerimise mõistest -- *andmetüüp* (või lihtsalt *tüüp*). Erinevat laadi info esitamiseks/kasutamiseks on olemas erinevad andmetüübid. Seni olete tutvunud täisarvu-, ujukomaarvu-, tõeväärtus-, sõne-, listi- ja ennikutüüpidega. Selles peatükis vaatame veel kahte andmetüüpi (hulk ja sõnastik) ning lisaks uurime, miks ja kuidas võiks andmetüüpe omavahel kombineerida. Lõpuks astume sammu tagasi, ning analüüsime, mida on järjenditel, hulkadel ja sõnastikel ühist.


Hulgad
----------
TODO



Sõnastikud
----------
Sõnastik (ing.k. *dictionary*, lühendatult ``dict``) on Pythoni andmetüüp, mis meenutab jällegi mitmes mõttes järjendeid: teda kasutatakse andmete koondamisel üheks kogumiks ja temas sisalduvaid üksikuid elemente on võimalik küsida kasutades  avaldist kujul ``kogum[võti]``.

Põhiline erinevus on selles, et kui järjendi puhul on võtmeks (e. indeksiks) alati täisarv (nt. ``palgad[0]``), siis sõnastike puhul saab kasutada võtmeks ka näiteks sõnesid (nt. ``telefoninumbrid['Peeter']`` (või muid Pythoni lihtsamaid tüüpe).

Sõnastikud kirjutatakse looksulgude vahele ja iga elemendi juures näidatakse ära elemendi võti ja väärtus. Väärtuse küsimiseks tuleb nurksulgudes anda soovitud elemendi võti:

.. sourcecode:: py3
    
    # loome sõnastiku, milles on 3 elementi
    telefonid = {'politsei': '110', 'päästeamet': '112', 'president': '631 6202'}
    
    # ühe kindla elemendi küsimine (võtme järgi)
    print("Päästeameti telefoninumber on", telefonid['päästeamet'])
    
    # küsime, kas teatud võtmega element on olemas
    # NB! in-operatsioon käib võtmete, mitte väärtuste kohta
    if 'politsei' in telefonid:
        print("Politsei number on", telefonid['politsei'])

Justnagu järjendite puhul, saab kõiki sõnastiku elemente läbi vaadata kasutades ``for``-tsüklit, aga erinevalt järjenditest antakse igal sammul tsüklimuutujasse elemendi võti, mitte väärtus:

.. sourcecode:: py3
    
    # sõnastiku loomine
    telefonid = {'politsei': '110', 'päästeamet': '112', 'president': '631 6202'}
    
    # kõigi elementide läbivaatamine
    for nimi in telefonid:
        print(nimi.capitalize() + " - " + telefonid[nimi])

Kui te proovisite seda näidet käivitada, siis võis juhtuda, et telefoninumbrid väljastati teistsuguses järjekorras, kui sõnastiku loomisel. Põhjus on selles, et sõnastiku puhul ei pea Python elementide omavahelist järjekorda oluliseks ja võib neid programmi efektiivsuse huvides ümber tõsta (aga ühe elemendi võti ja väärtus jäävad siiski alati omavahel seotuks).

Sõnastiku täiendamine elementhaaval
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Justnagu järjendeid, saab ka sõnastikke programmi töö käigus täiendada, aga erinevalt järjenditest, ei kasutata mitte ``append`` meetodit, vaid võtme järgi omistamist kujul ``sõnastik[võti] = väärtus``:

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

    Siin tuleb meeles pidada, et *järjendite* puhul on taoline omistamine võimalik vaid nende indeksitega, mis juba on järjendis olemas, st. järjendit taolise lähenemisega kasvatada ei saa:
    
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


Ülesanne 1. Telefoniraamat
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Muuda ülalpool toodud telefoniraamatu näidet selliselt, et andmed loetakse sisse tekstifailist ja programm võimaldab kasutajal küsida telefoninumbrit omaniku nime järgi.

Mitmemõõtmelised andmestruktuurid
---------------------------------
Nagu teate, saab Pythonis teatud lausete sisse panna teisi lauseid (nt. tingimuslause sisse tsükleid või vastupidi) ja teatud avaldiste komponentideks võivad olla teised avaldised.

Samamoodi saab panna andmestruktuuridesse teisi andmestruktuure. Näiteks on võimalik luua järjendeid, mille elementideks on mingid järjendid või siis ennikuid, mille elementideks on ennikud ja järjendid või sõnastikke, mille elementideks on järjendid:

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

Antud näites kasutasime taolises "üksteise sisse panemises" ainult kahte taset aga vajadusel on võimalik konstrueerida mistahes tasemete arvuga andmestruktuure, näiteks järjendite järjendite järjendeid (e. 3-mõõtmelisi järjendeid):

.. sourcecode:: py3

    arvujärjendite_järjendite_järjend = [
        [[1, 2, 3], [4, 5, 6, 6, 6], [7, 8]],
        [[23, 11], [16, 63, 1], [7, 77, 777]]
    ]



Mitmemõõtmeliste järjendite läbimine
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Taoliste andmestruktuuride kasutamiseks ei ole tarvis mingisuguseid erivõtteid -- tuleb lihtsalt pidada meeles, millist tüüpi elementidega meil mingil tasemel tegemist on.

Üritame näiteks kuvada ekraanile kahemõõtmelises järjendis sisalduvat infot *(NB! enne selle programmi käivitamist käige tsüklid ise mõttes läbi ja ennustage, milline tuleb programmi väljund!)*:

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


Veidi veider võib tunduda see, et üks tsükkel on kirjutatud teise sisse. Selles pole tegelikult midagi erilist, mõlemad tsüklid toimivad tavapäraselt -- enne uuele ringile minekut tehakse tsükli keha sees olevad käsud lõpuni. See tähendab muuhulgas seda, et välimise tsükli iga korduse puhul tehakse läbi sisemise tsükli kõik kordused.

.. note::

    Viimases näites läks meil vaja kahte tsüklit, et jõuda andmestruktuuri "põhjani" välja. Alati ei ole meil aga taolist kõikide elementide läbikäimist tarviski. Järgnev näiteprogramm väljastab sama 2-mõõtmelise järjendi kõige elementide (so. arvujärjendite) summad:

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
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Eelnevates näidetes põhinesid tsüklid otse järjenditel, aga nagu teate, võib järjendeid läbida ka indeksite abil:

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


Abimuutuja ``arvujärjend`` kasutamise asemel oleksime võinud kasutada ka kahte indekseerimist järjest (pöörake tähelepanu viimasele reale):

.. sourcecode:: py3

    ...
    for i in range(len(arvujärjendite_järjend)):
        for j in range(len(arvujärjendite_järjend[i])):
            print(arvujärjendite_järjend[i][j])

Viimasel real oleva ``print``-i argumendi tähendus saab võibolla selgemaks, kui sinna kirjutada sulge juurde: 

.. sourcecode:: py3

    (arvujärjendite_järjend[i])[j]

Nüüd on ilusti näha, et sulgudes olev avaldis kujutab endast ``i``-ndat elementi ``arvujärjendite_järjend``-ist (ehk siis ühte arvujärjendit) ning sellest omakorda võetakse element indeksiga ``j``, seega on tulemuseks mingi arv.

Kokkuvõtteks: Mitmemõõtmeliste järjendite kasutamise põhimõte
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Olgu meil ühe-, kahe- või 100-mõõtmeline järjend, tegemist on ennekõike ikkagi järjendiga ja sedasi tuleb talle ka läheneda. Vaja on lihtsalt arvestada, millised on tema elemendid (vastavalt lihttüübid, ühemõõtmelised järjendid või 99-mõõtmelised järjendid).
    
Sama põhimõte kehtib ka "järjendite ennikute" ja "sõnastike ennikute järjendite sõnastike järjendite ennikute sõnastikega" -- alustage lähenemist "välimisest kihist" ja pidage meeles, millised on sisemised kihid.


Ülesanne 2. Sudoku tabeli sisselugemine
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Kirjutage programm, mis loeb etteantud failist (:download:`sudoku.txt <downloads/sudoku.txt>`) arvud kahemõõtmelisse järjendisse.

.. note:: 
    Kui jääte jänni, siis uurige järgmist punkti, aga enne kindlasti üritage ise! Kõik selle ülesande lahendamiseks vajalikud teadmised on teil juba olemas!



Näide: Mitmemõõtmelise järjendi koostamine jupphaaval
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Mitmemõõtmelise järjendi loomisel ``append`` meetodiga tuleb jällegi mõelda, millised peavad olema järjendi elemendid. Järgnev näide on üks võimalik lahendus eelnevale ülesandele (kui ülesanne jäi teile liiga raskeks, siis analüüsige seda näitelahendust eriti hoolikalt):

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
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Õppejõud koostas eksami, milles oli 7 ülesannet. Iga ülesannet eest võis saada kuni 10 punkti. Eksami tulemused on kirjas failis :download:`eksam.txt<downloads/eksam.txt>`.

Leida iga tudengi eksamipunktide kogusumma.

*NB! Enne näitelahenduse vaatamist mõelge, kuidas tuleks seda ülesannet lahendada!* 

.. sourcecode:: py3

    # Faili avamine
    file = open("Eksam.txt","r")

    # Tulemuste lugemine tabelisse
    tabel = []
    nimed = []

    for rida in file :
       # Eralda tudengi nimi
       jupid = rida.split("|")
       nimed.append(jupid[0].strip())

       # võta ülejäänud osa juppideks
       jupid = jupid[1].split(",")

       # Märgi tudengi tulemused tabelisse
       tulemused = []
       for tulemus in jupid :
           tulemused.append(int(tulemus))
       tabel.append(tulemused)

    # Faili sulgemine
    file.close()

    n = len(tabel)

    print

    # Tulemuste väljastamine
    print("Tulemused:")
    for i in range(n) :
        print("{0:>2}. {1:<25}: ".format(i+1, nimed[i]), end=' ')
        for j in range(7) :
            print("{0:>2}".format(tabel[i][j]), end=' ')
        print()


    print("-----------------")
    # Reasummad
    for i in range(n) :
        summa = 0
        for j in range(7) :
            summa += tabel[i][j]

        print("{0} sai {1} punkti".format(nimed[i], summa))



Ülesanne 3. Keskmine tulemus ülesannete kaupa
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Täiendage eelnevat näiteprogrammi nii, et see näitaks millised ülesanded olid üldiselt raskemad ja millised kergemad. Selleks väljastage keskmised tulemused ülesannete kaupa (st. eraldi kõigi tudengite 1. ülesande eest saadud punktide keskmine jne).

.. hint::

    Ühe ülesande punktide kogusumma arvutamise skeem on väga sarnane ühe tudengi punktisumma arvutamisele.


Kahekordsed tsüklid ühemõõtmelisel järjendil
--------------------------------------------
Vahel läheb mitmekordseid tsükleid tarvis ka ühemõõtmeliste järjendite töötlemiseks.

Näide: Libisev keskmine
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Antud on fail (:download:`aktsiad.txt <downloads/aktsiad.txt>`), kus on antud ühe aktsia hinnad järjestikustel päevadel. Küsida kasutajalt päevade arv *k* ning väljastada järjest iga päeva kohta sellele eelnenud *k* päeva keskmine aktsiahind.

.. sourcecode:: py3

    # Hindade lugemine failist
    hinnad = [] # hinnad on tavaline ühemõõtmeline järjend
    f = open("aktsiad.txt")
    for rida in f:
        hinnad.append(float(rida))
    f.close()


    # Keskmiste arvutamine
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


Ülesanne 4. Erinevad väärtused
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Koostage funktsioon ``kõik_erinevad``, mis tagastab ``True`` või ``False`` vastavalt sellele, kas etteantud järjendis on kõik väärtused erinevad või mitte.

.. hint::
        
    Iga elemendi vaatlemisel kontrollige sisemise tsükliga, kas sama väärtus esineb ka mõnel muul positsioonil.
    
.. note::

    Seda ülesannet saaks lahendada ka ``count`` meetodit kasutades, aga kuna ``count`` meetod kasutab sisemas samuti tsüklit, siis kokkuvõttes on Pythoni jaoks ikkagi tegemist kahekordse tsükliga.
    
Ülesanne 5. Kaugeimad punktid
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Failis :download:`punktid.txt<downloads/punktid.txt>` on antud tasandi punktide koordinaadid (kujul *<x-koordinaat> <y-koordinaat>*). Leida punktid, mis asuvad teineteisest kõige kaugemal. Väljastada ekraanile ka nende punktide koordinaadid.

.. hint::

    Kontrollida tuleb iga punkti kaugust igast teisest punktist. Seda võib teha kahekordse tsükliga. Välimises tsüklis võiks indeks ``i`` muutuda 1-st kuni n-ni, igal välimise tsükli sammul arvutatakse sisemises tsüklis i-nda punkti kaugus j-ndast punktist, kus j on sisemise for-tsükli indeks.

.. hint::

    Punktide omavahelise kauguse arvutamisel on abi *Pythagorase teoreemist*. Vajadusel visandage skeem koordinaatteljestiku ja kahe punktiga ning otsige pildilt täisnurkset kolmnurka.


Ülesanne 6. Mõistatuslik teisendus
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Proovige ennustada, mida teeb järgmine funktsioon: 

.. sourcecode:: py3
    
    def teisenda(järjend):
        # teen järjendist koopia
        uus = järjend[:]
        
        for i in range(len(uus)):
            for j in range(i+1):
                if uus[j] < uus[i]:
                    uus[i], uus[j] = uus[j], uus[i]
        
        return uus


Sisemise tsükli viimasel real on tegemist kahe elemendi väärtuse vahetamisega -- sama skeemi nägite juba ennikute teema juures.


.. hint::

    Katsetage seda funktsiooni näiteks järjendiga ``[5, 2, 1, 4, 3]``. Proovige mõttes funktsiooni töö läbi mängida mõne lühema järjendiga.


Andmestruktuurid
--------------------
Peatüki pealkirjaks on andmestruktuurid, nüüd on paras aeg lõpuks ära öelda, mida see sõna tähendab.

Laias laastus jaotatakse andmetüübid *lihttüüpideks* ja *liittüüpideks*. Lihtüübid tähistavad nö "atomaarseid" või "jagamatuid" väärtusi -- näiteks arvutüübid ja tõeväärtustüüp; liittüübid (näiteks list ja ennik) aga tähistavad väärtusi, mida saaks veel mingiteks alamkomponentideks (nt. listi elementideks) jagada. (Sõnega on Pythoni puhul pisud segased lood -- seda võib olenevalt vaatenurgast pidada nii lihttüübiks, kui liittüübiks).

Nagu öeldud, liittüüpi väärtused on kombineeritud kokku mingitest teistest väärtustest. Oluline on see, et need komponendid moodustavad mingi kindla *struktuuri*. Näiteks järjendite puhul moodustub struktuur sellest, et iga komponent (element) on teiste komponentidega võrreldes kas eespool või tagapool, teisisõnu -- järjendi struktuur määrab elementide järjestuse. Teistel Pythoni liitüüpidel on teistsugune struktuur -- näiteks hulgatüübi struktuur määrab ära vaid selle, millised elemendid hulka kuuluvad, elementide järjestus pole selles struktuuris oluline. Kuna struktuur on liittüüpide puhul väga tähtis, siis nimetatakse neid vahel ka *struktuurseteks tüüpideks* või *andmestruktuurideks*.


.. note::

    Programmeerimise teemad jaotatakse tihti tinglikult kaheks -- *algoritmid* ja *andmed* (või andmestruktuurid). Algoritmid kehastavad programmide "aktiivset" poolt -- nad kirjeldavad mingit tegevust, arvutamist, valikut, teisendamist vms. Selle poole märksõnad on näiteks ``if``, ``print``, ``while``, ``sin``.

    Andmeid (sh. andmestruktuure) võib pidada programmide "passiivseks" pooleks -- nad kehastavad mingeid abstraktseid või konkreetseid asju, seoseid või muud laadi infot ja nad "lihtsalt on". Selleks, et midagi juhtuks, peab mõni algoritm neid uurima ja saadud info põhjal midagi tegema. Selle poole märksõnadeks on nt. *väärtus*, *tüüp*, *sõne*, *list*.

Pythoni andmestruktuuride salvestamine ja sisselugemine
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
TODO pickle.load/dump




Ülesanded
---------------

0. oma split

1. Teksti analüüs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Kirjutage programm, mis aitaks võrrelda erinevate sümbolite esinemissagedust eesti- vs. ingliskeelsetes tekstides.

.. hint::

    Kirjutage funktsioon, mis võtab argumendiks failinime ja tagastab sõnastiku, mis sisaldab failis sisalduvate tähtede esinemise sagedusi.

.. hint::

    Sõnastiku võtmeteks peaks olema tähed või muud sümbolid (st. tehniliselt võttes sõned) ja väärtusteks täisarvud.

.. hint::

    Alustage tühja sõnastikuga.

.. hint::

    Meeldetuletus: sõnesid saab käsitleda justkui sümbolite järjendeid.

.. hint::
    
    Kui nuputate, millises etapis tuleks kasutada oma head tuttavat ``split`` meetodit, siis mõelge järgi, kas seda üldse läheb antud ülesandes tarvis.


2. Sudoku lahenduse kontrollimine
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Kirjutage programm, mis kontrollib, kas etteantud failis (:download:`sudoku.txt <downloads/sudoku.txt>`) on korrektne Sudoku lahendus. Mittekorrektse lahenduse korral tuleb öelda, millises veerus, reas või 3x3 ruudus probleem esineb.

Lisainfot Sudoku kohta: http://en.wikipedia.org/wiki/Sudoku

NB! testige oma programmi nii korrektse kui ka mittekorrektse lahendusega!

.. hint::

    Ülesande lahendamisel võib olla abiks üks selles peatükis defineeritud funktsioonidest.
    

3. Eksami statistika, 2. osa
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
See ülesanne põhineb ülalpool toodud näiteülesandel.

Kõigepealt muutke etteantud lahendust nii, et küsimuste arv 7 ei oleks fikseeritud, vaid tuvastataks käigu pealt, vastavalt esimesel real olevate tulemuste arvule (võib eeldada, et kõigil ridadel on võrdne arv tulemusi).

NB! Kõik järgmiste ülesannete lahendused peavad samuti töötama suvalise tulemuste arvu korral. Lahendused võib kõik teha järjest ühte samasse faili.

Ülesande lahendamisel võite muuhulgas kasutada kõiki Pythoni funktsioone (sh. ``sum`` ja ``max``).

#. **Maksimaalsed tulemused**: Leida iga ülesande kohta selle lahendamisel saadud maksimaalne skoor.

#. **Seinast seina**: Väljastage nende tudengite nimed, kes said vähemalt ühe ülesande eest 10 punkti ja mõne teise ülesande eest 0 punkti.

#. **Primused**: Leida nende tudengite nimed, kes kogusid summaarselt kõige rohkem punkte. Kui mitu inimest sai sama palju punkte, väljastada kõigi nende nimed (vihje – koguge need nimed järjendisse).

#. **Spikerdamine**: Fail on koostatud nii, et kõrvuti istunud tudengite andmed on failis järjest. Kontrollida, kas tulemused viitavad sellele, et mõni oma naabri pealt spikerdas. Spikerdamises võib tudengit kahtlustada, kui tema kõik tulemused on kas võrdsed või ülimalt 2 punkti võrra väiksemad, kui ühel tema kahest naabrist. Väljastada kõigi spikerdamises kahtlustatavate tudengite nimed.

#. **Skaleeritud hindamine**: Oletame, et hindamisskeem on selline, et kui mõne ülesande eest ei saanud keegi maksimumpunkte, siis korrutatakse kõigi tudengite punktid läbi sellise konfitsendiga, et parima tulemuse saanud tudengi uus tulemus oleks 10. Teisendage ja väljastage kõigi tudengite kõigi ülesannete punktid sellest hindamisskeemist lähtuvalt (1 komakoha täpsusega). Vihje: koostage järjend, kus on iga ülesande kohta leitud sellele vastav kordaja, ning kasutage seda tudengite hinnete tuvastamisel.



    
4. SKP
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
*See ülesanne on antud koos näitelahendusega, aga enne selle vaatamist üritage ise lahenduseni jõuda!*

Antud on fail :download:`SKP.txt<downloads/SKP.txt>`, kus on kirjas riikide nimed ja nende SKP-d semikooloniga eraldatult (miljonites USA dollarites, 2009. aasta seisuga). Küsida kasutajalt, kui suur SKP teda huvitab ning leida kolm sisestatud arvule kõige lähema SKP-ga riiki.

.. hint::

    Kõige lähema leidmine on iseenesest lihtne – leida lihtsalt selline, mille jaoks absoluutväärtus `| SKP – sisestatud arv |` oleks minimaalne. Kuidas aga leida kolme lähimat? Tuletame aga meelde, kuidas me leidsime minimaalset – me hoidsime vähimat meeles ning kui parasjagu vaadeldav element oli sellest väiksem, asendasime ta sellega. Miski ei takista meid aga hoidmast ühe vähima asemel nimekirja näiteks kolmest. Kui nüüd leidub uus, mis on kõigist kolmest väiksem, siis lisame selle sinna nimekirja ning viskame seal enne olnutest kõige suurema välja. Sama teeme tegelikult alati, kui uus väärtus on vähemalt kõige suuremast seni meeles hoitud väärtusest väiksem. Seega piisab, kui leiame igal sammul meeles peetuist suurima ja vaatame, kas uus on sellest väiksem. Kui on, asendame endise meeles peetuva suurima lihtsalt uue leituga. See aga tähendab, et igal sammul tuleb vaid leida maksimaalne meeles hoitutest – seda me aga juba oskame.

    .. sourcecode:: py3

        skp = float(input("Sisesta arv, millele lähedased SKP-d sind huvitavad:"))

        skpd = []
        vahed = []
        nimed = []

        # Faili sisse lugemine
        f = open("SKP.txt","r")
        for rida in f:
            # Teisenda rida riigiks ja skp-ks ning lisa need järjenditele
            paar = rida.split(";")
            nimed.append(paar[0])
            skpd.append(float(paar[1]))

            # Arvutada ka absoluutväärtus vahest nõutud skp-ga
            vahed.append(abs(float(paar[1])-skp))

        f.close()

        # Eralda esimesed kolm elementi esialgseks lähimate järjendiks
        lahimadskpd = skpd[0:3]
        lahimadnimed = nimed[0:3]
        lahimadvahed = vahed[0:3]

        # Leia tegelikud lähimad järjendi läbi käimise teel
        for i in range(3,len(skpd)) :
            # Leia maksimaalse erinevusega indeks meeles peetute hulgast
            maksj = 0
            for j in range(1,len(lahimadvahed)) :
                if lahimadvahed[j] > lahimadvahed[maksj] :
                    maksj=j

            # Vaadata, kas uus leitu on meie parameetrile lähemal
            if vahed[i] < lahimadvahed[maksj] :
                # Kui on, asenda seal enne olnud riigi info uuega
                lahimadvahed[maksj] = vahed[i]
                lahimadskpd[maksj] = skpd[i]
                lahimadnimed[maksj] = nimed[i]

        # Väljasta tulemus
        for i in range(0,len(lahimadvahed)) :
            print(lahimadnimed[i] + " - " + str(lahimadskpd[i]))


.. todo::

    varuülesanded ......................
    Supermarket
    
    Järjendisse on salvestatud kassajärjekorras olevate inimeste korvis olevate esemete arvud (küsida kasutajalt). Koostada programm, mis iga järjekorras oleva inimese korral leiab, mitmel inimesel tema ees on korvis rohkem kui kolm eset.
    Järjestikused naturaalarvud

    Indiaanlased
    
    Indiaanlased liiguvad hanereas, nende pikkusi kirjeldab järjend (lugeda failist või küsida kasutajalt). Mitmendal positsioonil selles reas asub indiaanlane, kelle ees (vahetult) asub kõige rohkem temast lühemaid indiaanlasi?

    Juhis: Järjendit läbides peame meeles juba vaadeldud indiaanlaste seast "parima" järjekorranumbrit ja seda, mitmest vahetult eelnevast inimesest ta pikem on. Leides iga indiaanlase korral lühemate eelkõndijate arvu, tuleb järjendis liikuda näiteks while-tsükliga ettepoole niikaua, kui järjendi liikmete väärtused on vaadeldavast väärtusest väiksemad, ja lugeda kokku selliste väärtuste arv.





Lisalugemine
------------
Keerukus
~~~~~~~~~~
Üldiselt on üht ja sama ülesannet võimalik tihti lahendada mitmel väga erineval moel. Näiteks sobib "Libisev keskmine" lahenduses keskmiste leidmiseks ka järgmine programmijupp:

.. sourcecode:: py3

    ...
    
    # Keskmiste arvutamine
    # Leia kumulatiivsed summad

    summad = [0.0]

    for i in range(0, len(hinnad)):
       summad.append(summad[i] + float(hinnad[i]))

    # Leia k eelmise päeva keskmised
    for i in range(k, len(hinnad) + 1):
       keskm = summad[i] - summad[i-k]
       keskm = keskm / k
       print("{0}-ndale päevale eelnenud {1} päeva keskmine oli {2:.2f}".format(i,k,keskm))

See programm on mingis mõttes keerulisem, kui ülesande algne lahendus, sest keskmise jaoks vajalike summade otse leidmise asemel leitakse siin alguses kõik “kumulatiivsed summad” st summad esimesest aktsiahinnast kuni i-nda aktsiahinnani (kõikide i-de jaoks) ning seejärel kasutatakse neid summasid kavalalt et k eelmise elemendi summat leida, lähtudes tõdemusest, et

.. sourcecode:: none

    a[i-k+1] + a[i-k+2] + ... + a[i] == (a[0]+a[1] + ... + a[i]) – (a[0]+a[1] + ... + a[i-k])

Kui samale ülesandele on kaks lahendust, tekib paratamatult küsimus, kumb neist parem on. Ühest vastust sellele ei ole. Õpetamise kontekstis on näiteks selge, et esimene lahendus sobib kahekordse tsükli illustreerimiseks märksa paremini, sest teine lahendus seda konstruktsiooni isegi ei kasuta. Samuti on esimene programm ehk ka lihtsamini kontrollitav, sest ta on lühem ning leiab need keskmised vahetult summade leidmise kaudu, selle asemel et mingeid trikke kasutada.

Teisel lahendusel on esimese ees siiski üks oluline eelis, mis tuleb küll välja alles suuremate andmestike puhul. Kui näiteks aktsiahindu ei vaadata mitte päevade vaid sekundite lõikes, võib neid failis olla mõnekümne asemel miljoneid, ning keskmiseid oleks vaja samuti leida ilmselt üle mitte 10 vaid pigem 100 000 eelmise väärtuse. Sellisel juhul jääks esimene lahendus märkimisväärselt aeglasemaks ja seda väga lihtsal põhjusel: esimene ülesanne teeb iga keskmise leidmiseks k liitmistehet, kuid teine lahendus saab sellega eelnevalt leitud summade abil hakkama vaid ühe lahutamistehtega. Kuigi ka summade leidmiseks kulub aega, on lihtne veenduda, on see kuluv aeg samuti vaid keskmiselt üks liitmine iga i väärtuse jaoks. Kokkuvõttes kulub teisel lahendusel seega iga k-keskmise peale üks liitmine, üks lahutamine samas kui esimene lahendus peab tegema k liitmist.

Programmi poolt tehtavate sammude arvu hindamist nimetatakse selle *ajalise keerukuse* analüüsimiseks. Selline analüüs muutub oluliseks eelkõige suurte andmemahtude korral - väikeste andmemahtude korral (paartuhat erinevat aktsiahinda) töötavad mõlemad lahendused lihtsalt nii kiiresti, et inimene nende töökiiruse erinevust ei taju, kuid mida suuremad on andmemahud, seda suurem on erinevus ja seda eelistatum on teine lahendus esimesele.

Üldiselt tehakse sellist analüüsi küllaltki umbkaudselt, loendades vaid neid samme, mida korduvalt tehakse ning tehes isegi seda tihti suhteliselt ligikaudselt. Näiteks esimest lahendust analüüsides vaadataks, et kõige rohkem tehakse sisemise tsükli liitmistehet, mis toimub kokku `(n-k)*(k-1)` ehk suurusjärgus `n*k` korda, samas kui teises lahenduses toimub kumulatiivsete summade leidmisel n liitmist ja hiljem keskmiste leidmisel `n-k` lahutamist, st. kokku `2n-k` ehk "suurusjärgus" `n` tehet. Kuna üldiselt `n` kasvades ka `k` kasvab, võib teha lisaeelduse et `k` ja `n` on umbes samas suurusjärgus, mis annaks esimese algoritmi keerukuse hinnanguks `2n` tehet ning teise jaoks lihtsalt `n` tehet. Sealt ongi näha, et mida suurema väärtus `n` omandab (st. mida suurem on andmestik), seda suuremaks muutub hinnagute erinevus ja seega ka töökiiruste erinevus.

Sellist analüüsi nimetatakse *asümptootiliseks*, sest ta kehtib `n` suurte väärtuste korral ning üldiselt seda paremini, mida suuremad `n` väärtused on. Selline ligikaudne lähenemine on tegelikult formaliseeritav nn. *O-notatsiooni* abil, mis annab ka küllalti täpsed piirangud sellele, kuidas ja mis alustel üldistada ja lihtsustada tohib. Sel viisil keerukuse hindamisest kuulete täpsemalt kursusel *Algoritmid ja andmestruktuurid*.

