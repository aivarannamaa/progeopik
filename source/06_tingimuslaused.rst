6. ``bool`` ja tingimuslaused
=======================================


Meeldetuletus 3. peatükist -- Pythoni programmi kood koosneb lausetest ja lause komponentideks on avaldised. Tuleb välja, et ka ``if`` või ``while`` lause päises olev tingimus on tegelikult avaldis. Kuna igal avaldisel on väärtus ja igal väärtusel on tüüp, siis mis on tingimuse tüüp?

Selles peatükis uurime põhjalikumalt tingimuslause (e. ``if``-lause) erinevaid vorme ja tingimuse moodustamise võimalusi, aga kõigepealt tutvume ühe uue andmetüübiga, mida olete tegelikult juba korduvalt kasutanud.


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


Harjutus 1. Arvu ruut koos kontrolliga
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

Harjutus 2
~~~~~~~~~~~~~~~~
Pange kirja järgnevate avaldiste loogilised *vastandid*:

.. sourcecode:: none

    a > b
    a >= b
    a >= 18  and  day == 3
    a >= 18  and  day != 3
    
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

Harjutus 3. Liigaasta tuvastamine
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

Harjutus 4. Päevade arv kuus
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Kirjutage funktsioon ``päevade_arv``, mis võtab argumendiks kuu numbri ja aastaarvu ning tagastab mitu päeva on selles kuus. Kasutage abifunktsioonina eelnevalt defineeritud funktsiooni ``on_liigaasta``. (Kirjutage need funktsioonid samasse faili).

Harjutus 5. Kuupäeva kontrollimine
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

Harjutus 6. Kuu esitamine sõnena
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Kirjutage funktsioon ``kuu_nimi``, mis võtab argumendiks kuu numbri ning tagastab vastava kuu nime. Kui argumendi väärtus on väiksem kui 1 või suurem kui 12, siis tagastatakse sõne ``'Vigane kuu number'``.

Testige oma funktsiooni!

Tingimuste kasutamine tsükli päises
---------------------------------------
Justkui tingimuslause päises, lubatakse ka ``while``-lause päises suvalisel kujul tingimust, peamine, et tegemist oleks ``bool`` tüüpi avaldisega:

.. sourcecode:: py3
    
    a = ...
    b = ...
    c = ...
    s = ...

    
    while (a == b or b > c) and s == "Tere":
        ...

        
    tingimus = ... or ... or ... or ...
    while tingimus or a > b or s.endswith("kala"):
        ...
        a = ...
        ...

    
    while True:
        ...


Tingimusavaldis
-----------------
Lisaks ``if``-*lausele* on Pythonis olemas ka ``if``-*avaldis* e. *tingimusavaldis*. Selle olemust on kõige lihtsam selgitada näitega:

.. sourcecode:: py3

    >>> a = 1
    >>> b = 2
    >>> 'suurem' if a > b else 'väiksem'
    'väiksem'

Ka ``if``-avaldise juures kasutatakse võtmesõnu ``if`` ja ``else``, aga nende paigutus on erinev -- tõesele tingumusele vastav haru kirjutatakse ``if``-i ette ja väärale tingimusele vastav haru kirjutatakse ``else`` järele, koolonit ega treppimist ei kasutata. Oluline on veel see, et erinevalt tingimuslausest, ei käi tingimusavaldise harudesse mitte laused vaid avaldised. Tingimusavaldise väärtus võetakse ühest või teisest harust, vastavalt tingimusele. See asjaolu tingib ka selle, et mõlemad harud peavad olema antud.

Toome siinkohal veel ühe näite tingimusavaldise kasutamise kohta:

.. sourcecode:: py3

    def neto(bruto):
        return bruto if bruto <= 144 else (bruto - 144) * 0.79 + 144

Tingimusavaldise asemel saab alati kasutada tingimuslauset ...
    
.. sourcecode:: py3

    def neto(bruto):
        if bruto <= 144:
            vastus = bruto
        else:
            vastus = (bruto - 144) * 0.79 + 144
            
        return vastus

... aga mõnikord saab tingimusavaldisega oma idee lihtsalt kompaktsemalt kirja panna.


.. note:: 

    Ärge ajage segamini ka tingimusavaldist ja loogilist avaldist. Loogiline avaldis on avaldis, mille tüüp on ``bool``. Tingimusavaldis on avaldis, milles on kasutatud äsja tutvustatud valikuskeemi, tingimusavaldise tüüp tavaliselt *ei ole* ``bool``.

.. note::

    Kui teile siiski tundub, et tingimusavaldis teeb teie jaoks asjad liiga segaseks, siis võite seda rahumeeli ignoreerida. Alati saab hakkama ka ainult tingimuslausega. Mitmes populaarses programmeerimiskeeles isegi pole tingimusavaldist.


Ülesanded
-------------

1. Kuupäeva esitamine sõnena
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Kirjutage funktsioon ``kuupäev_sõnena``, mis võtab argumentideks päeva, kuu ja aasta (arvudena) ning tagastab sõne, mis esitab kuupäeva kujul *<päev>. <kuu nimi> <aasta>* (nt. *24. veebruar 1918*).

Seejärel kirjutage programm, mis küsib kasutajalt arvudena päeva, kuu ja aasta. Kui neile vastav kuupäev on legaalne, siis kuvada ekraanile vastav kuupäev sõnena, vastasel juhul kuvada ``'Viga: mittelegaalne kuupäev'``.

Kasutage abifunktsioonidena ülalpood loodud funktsioone (vt. harjutusi 3-6).

2. Täisnurkne kolmnurk
~~~~~~~~~~~~~~~~~~~~~~~~~~
Kirjutage funktsioon, mis võtab argumentideks kolmnurga külgede pikkused ja tagastab ``True`` või ``False`` vastavalt sellele, kas tegemist oli täisnurkse kolmnurgaga või mitte.

.. note:: 

    Lihtsustamise mõttes võite esialgu eeldada, et pikim külg antakse alati kolmanda argumendina. Kui saate esialgse variandi tööle, siis muutke programmi selliselt, et küljepikkuseid võib anda suvalises järjekorras.
    
.. note::

    Ärge unustage, et ujukomaarvud on pisut ebatäpsed, seega võib olla vajalik võrdsuse kontrollimise asemel kontrollida sarnasust:
    
    .. sourcecode :: py3
    
        if abs(x - y) < 0.000001:      # x is peaaegu võrdne y-ga
            ...


3. Klaveri mahutamine
~~~~~~~~~~~~~~~~~~~~~
Ülikool on ostnud endale uue klaveri peahoone aula tarbeks. Paraku unustati  kontrollida, kas see klaver üldse välisuksest sisse mahub. Kirjutada programm, mis küsib kasutajalt klaverit sisaldava kasti kolm mõõdet (pikkus, laius, kõrgus) ning ukse laiuse ja kõrguse ning vastab, kas klaver on võimalik aulasse sisse toimetada.

4. Pitsapood
~~~~~~~~~~~~
Kirjutage programm, mis küsib kasutajalt infot tellitava pitsa suuruse, komponentide ja kättetoimetamise detailide kohta. Igal sammul tuleks esitada kasutajale võimalikud valikud koos vastavate koodidega, nt:

.. sourcecode:: none

    ...
    ...
    Millise suurusega pitsat soovite? Valikud on:
      1 - väike (18cm)
      2 - keskmine (25cm)
      3 - suur (35cm)
    Palun sisesta oma valik: 2
    ...
    ...
    Mida kasutada pitsa katmisel? 
      0 - pitsa kate valmis
      1 - juust
      2 - vorst
      3 - ...   
      4 - ...   
    ...
    ...
    Kuidas pitsa kohale toimetada? 
      1 - tulen ise järele
      2 - sisestan aadressi ja telefoninumbri
    ...
    
Pitsakatte komponente peaks saama valida ükskõik kui palju. Aadressi küsida ainult siis, kui kasutaja ei soovi ise järele tulla. Kogutud andmed salvestada tekstifaili.

Projekt
------------
Tkinter'i Canvas
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Eelmises peatükis tutvustasime mõningaid tkinter'i võimalusi graafiliste kasutajaliideste loomisel. Siis demonstreerimsime põhiliste "standardvidinate", nagu nuppude ja tekstisisestuskastide kasutamist. Seekord uurime ühte väga paindlikku vidinat, mille nimi on *Canvas* (tõlkes *lõuend*). *Canvase* peale saab joonistada kujundeid, laadida pilte, neid pilte ja kujundeid saab liigutada, nendele klõpsamist on võimalik registreerida jne.

Salvestage endale järgnev näiteprogramm. Enne käivitamist salvestage samasse kausta ka fail :download:`juku.gif <downloads/juku.gif>`.

.. sourcecode:: py3

    from tkinter import *
    from random import randint

    # mõningad abikonstandid
    juku_sammu_pikkus = 50
    tahvli_laius = 600
    tahvli_kõrgus = 600

    # funktsioonid, mis käivitatakse vastavalt kasutaja tegevusele
    def hiireklõps_juku_peal(event):
        # liigutan Juku juhuslikku positsiooni
        uus_x = randint(0, tahvli_laius-50)
        uus_y = randint(0, tahvli_kõrgus-50)
        tahvel.coords(juku_id, uus_x, uus_y)

    def nool_üles(event):
        tahvel.move(juku_id, 0, -juku_sammu_pikkus)

    def nool_alla(event):
        tahvel.move(juku_id, 0, juku_sammu_pikkus)

    def nool_vasakule(event):
        tahvel.move(juku_id, -juku_sammu_pikkus, 0)

    def nool_paremale(event):
        tahvel.move(juku_id, juku_sammu_pikkus, 0)


    # tavaline raami ja tahvli loomine
    raam = Tk()
    raam.title("Tahvel")
    tahvel = Canvas(raam, width=tahvli_laius, height=tahvli_kõrgus, background="white")
    tahvel.grid()

    # tavaline pildi sisselugemine
    juku = PhotoImage(file="juku.gif")

    # pildi loomisel jätan meelde pildi id 
    juku_id = tahvel.create_image(100, 100, image=juku)

    # pildi id kaudu seon sellel pildil toimunud klõpsud vastava funktsiooniga
    # <1> tähistab vasakut hiireklahvi
    tahvel.tag_bind(juku_id, '<1>', hiireklõps_juku_peal)

    # seon nooleklahvid vastavate funktsioonidega
    raam.bind_all("<Up>",    nool_üles)
    raam.bind_all("<Down>",  nool_alla)
    raam.bind_all("<Left>",  nool_vasakule)
    raam.bind_all("<Right>", nool_paremale)

    raam.mainloop()

Käivitage programm, vajutage nooleklahve, klõpsake hiirega kriipsujukul.

See näiteprogramm oli siinkohal mõeldud vaid "isuäratajana" -- selleks, et sellest aru saada, lugege esmalt lihtsamate Canvase programmide selgitusi õpiku lisast *tkinter*, jaotusest :ref:`canvas`.