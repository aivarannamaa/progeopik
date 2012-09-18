6. ``bool`` ja tingimuslaused
=======================================

..
    COMMENTS:
    http://courses.cs.ut.ee/2011/programmeerimine/uploads/Raamat/ch05.html
    Give the logical opposites of these conditions

    a > b
    a >= b
    a >= 18  and  day == 3
    a >= 18  and  day != 3



.. warning::

    Selle peatüki materjal võib veel muutuda

Selles peatükis uurime põhjalikumalt tingimuslause (e. ``if``-lause) erinevaid vorme ja tingimuse moodustamise võimalusi


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

Tingimuste kasutamine tsükli päises
---------------------------------------
TODO

Koduülesanded
-------------

1. Kuupäeva esitamine sõnena
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Kirjutage funktsioon ``kuupäev_sõnena``, mis võtab argumentideks päeva, kuu ja aasta (arvudena) ning tagastab sõne, mis esitab kuupäeva kujul *<päev>. <kuu nimi> <aasta>* (nt. *24. veebruar 1918*).

Seejärel kirjutage programm, mis küsib kasutajalt arvudena päeva, kuu ja aasta. Kui neile vastav kuupäev on legaalne, siis kuvada ekraanile vastav kuupäev sõnena, vastasel juhul kuvada ``'Viga: mittelegaalne kuupäev'``.

Kasutage abifunktsioonidena ülalpood loodud funktsioone (vt. ülesandeid 2-5).

2. Õpikuülesanne
~~~~~~~~~~~~~~~~
Lahendage `õpiku 5. peatükist <http://courses.cs.ut.ee/2011/programmeerimine/uploads/Raamat/ch05.html>`_ ülesanded 13 ja 14.

3. Klaveri mahutamine
~~~~~~~~~~~~~~~~~~~~~
Ülikool on ostnud endale uue klaveri peahoone aula tarbeks. Paraku unustati  kontrollida, kas see klaver üldse välisuksest sisse mahub. Kirjutada programm, mis küsib kasutajalt klaverit sisaldava kasti kolm mõõdet (pikkus, laius, kõrgus) ning ukse laiuse ja kõrguse ning vastab, kas klaver on võimalik aulasse sisse toimetada.

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

.. image:: images/ruudustik.png

.. topic:: Lisaülesande lisa
    
    Uurige kilpkonna dokumentatsioonist, kuidas värvida soovitud ala (http://docs.python.org/py3k/library/turtle.html). Seejärel proovige joonistada malelaud.