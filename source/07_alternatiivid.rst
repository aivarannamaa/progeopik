7. Alternatiivsed lahendused
=======================================

sisuliselt refactoring, samaväärsus

.. todo::

    * koodi lühendamine: 0-kordusega tsüklid
    * maini uuesti alternatiivsete lahenduste teemat (nested if vs keerulisem bool avaldis; bool avaldise kapseldamine funktsiooni; sügava treppimise asendamine funktsiooni väljakutsetega; pika koodi jaotamine mitmeks funktsiooniks)
    * conditional vs alternative execution ???
    * chained & nested conditionals (st. keele poolt pakutavad mugavus-alternatiivid)
    * if-harudes toimingu kordamine eri argumendiga vs. muutujasse salvestamine ja pärast toimingu tegemine muutujaga
    * Harjutus loogiliste avaldiste samaväärsuse kontrollimiseks (õpeta ka testima)
    * Harjutus "wrap this code in a function"
    * tabelite genereerimine
    * kilpkonnaga rooma numbrite joonistamine
    * funktsiooni sissetoomine
    * kalendri printimine
    * etteantud 2-3 muutujaga tõeväärtustabeli põhjal avaldise kirjutamine
    



TODO: selgita, et programmi käik sõltub sisendandmetest

Selles peatükis uurime põhjalikumalt tingimuslause (e. ``if``-lause) erinevaid vorme ja tingimuse moodustamise võimalusi, ...

Tingimused
----------
TODO


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
Kirjuta funktsioon ``on_liigaasta``, mis võtab argumendiks aastaarvu ning **tagastab tõeväärtuse** vastavalt sellele, kas antud aasta on liigaasta või mitte.

Kirjuta programm, mis küsib kasutajalt aastaarvu ning väljastab ekraanile info selle kohta, kas tegemist on liigaastaga või mitte. Liigaasta tuvastamiseks kasuta eelnevalt defineeritud funktsiooni.

.. hint::

    Liigaasta on selline, kus aastaarv jagub 4-ga, välja arvatud juhud, kus aastaarv jagub 100-ga, aga ei jagu 400-ga. Näiteks aastad 2004 ja 2000 on liigaastad aga 1900 mitte.

.. note::
    Kui programmis läheb mõni lause liiga pikaks, siis võid ta kirjutada mitmele reale, aga sel juhul tuleb rea "murdmise" koht märkida ära langkriipsuga (``\``):
    
    .. sourcecode:: py3
    
        tulemus = (see >= teine * math.pi) \
            and (niimoodi or naamoodi) \
            and (x > y or u != 1)
        

    Sellist rea murdmist võib kasutada suvaliste lausete korral. Murda ei saa vaid sõneliteraali ja kommentaaari sees.

Tingimuslaused
--------------
Pythoni tingimuslausega oled juba kokku puutunud, aga vaatame siinkohal mõned punktid veel üle. Lisaks tutvustame "mitmeharulist" tingimuslauset.

Harjutus 4. Päevade arv kuus
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Kirjuta funktsioon ``päevade_arv``, mis võtab argumendiks kuu numbri ja aastaarvu ning tagastab mitu päeva on selles kuus. Kasuta abifunktsioonina eelnevalt defineeritud funktsiooni ``on_liigaasta``. (Kirjuta need funktsioonid samasse faili).

Harjutus 5. Kuupäeva kontrollimine
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Kirjuta funktsioon ``on_legaalne_kuupäev``, mis võtab argumendiks päeva, kuu ja aasta (arvudena) ning tagastab tõeväärtuse vastavalt sellele, kas argumentidele vastav kuupäev on legaalne või mitte. Kasuta abifunktsioonidena eelmistes ülesannetes defineeritud funktsioone.

Testi loodud funktsiooni järgnevate avaldistega:

    - ``on_legaalne_kuupäev(31, 1, 2001)``
    - ``on_legaalne_kuupäev(29, 2, 2001)``
    - ``on_legaalne_kuupäev(29, 2, 2000)``

    

``elif`` konstruktsioon e. mitmeharuline tingimuslause
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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
Kirjuta funktsioon ``kuu_nimi``, mis võtab argumendiks kuu numbri ning tagastab vastava kuu nime. Kui argumendi väärtus on väiksem kui 1 või suurem kui 12, siis tagastatakse sõne ``'Vigane kuu number'``.

Testi oma funktsiooni!


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

    Ära aja segamini ka tingimusavaldist ja loogilist avaldist. Loogiline avaldis on avaldis, mille tüüp on ``bool``. Tingimusavaldis on avaldis, milles on kasutatud äsja tutvustatud valikuskeemi, tingimusavaldise tüüp tavaliselt *ei ole* ``bool``.

.. note::

    Kui sulle siiski tundub, et tingimusavaldis teeb sinu jaoks asjad liiga segaseks, siis võid seda rahumeeli ignoreerida. Alati saab hakkama ka ainult tingimuslausega. Mitmes populaarses programmeerimiskeeles isegi pole tingimusavaldist.

Erijuhtude käsitlemine
----------------------------
TODO



Alamülesannete tuvastamine ja alamprogrammide loomine
---------------------------------------------------------
Eelmise peatüki lõpus läksid mõned programmid võrdlemisi keeruliseks -- näiteks põranda värvimise ülesandes tuli sul tõenäoliselt läbi mõelda ja kirja panna kuidas teha vahet, milline veerg värvida ja milline mitte, kuidas korraldada liikumise ja värvimise vaheldumine, millal ja kuhupoole tuleks pöörata, millal on ülesanne täidetud jne. Kõikide nende probleemide lahendused kokku kirjutatuna võivad esialgu silme eest kirjuks võtta. Kui keegi küsiks sult praegu, millise eesmärgiga on sinu programmis mingi konkreetne rida või plokk, siis ilmselt peaksid enne vastamist omajagu süvenema.

Kuna enamus praktikas kasutatavaid programme on palju keerulisemad kui põranda värvimise programm, peab eksisteerima mingi nipp taolise keerukusega toimetulekuks. Käesolev peatükk ongi mõeldud selle nipi selgitamiseks ja harjutamiseks.



Tuleb välja, et programmeerimises kasutatakse keeruliste ülesannete lahendamisel sama nippi nagu "päris elus" -- esmalt jaotatakse ülesanne parajateks osadeks e. alamülesanneteks, seejärel lahendatakse alamülesanded (keskendudes korraga vaid ühele) ning lõpuks kombineeritakse alamülesannete lahendused. Seejuures juhtub küllalt tihti (nii programmeerimises, kui päris elus), et mõni alamülesanne on juba mingi teise probleemi kontekstis varem lahendatud, sel juhul saab vastavat lahendust taaskasutada.

Programmeerimises nimetatakse alamülesande lahendust **alamprogrammiks** (see on üldisem nimetus) või ka **funktsiooniks** (Pythoni programmeerijad eelistavad seda nimetust). Pythoni funktsioonide defineerimist sai tegelikult juba liitlausete peatükis veidi tutvustatud (vt. Uute käskude loomine), aga selles peatükis käsitleme funktsioonide kasutusvõimalusi palju sügavamalt ja laiemalt.

.. note::

    Erinevalt teistest siiani tutvustatud Pythoni põhikonstruktsioonidest (hargnemine ja tsükkel), ei ole alamprogrammid tehniliselt võttes programmeerimisel hädavajalikud -- kõik programmid on teoreetiliselt võimalik kirjutada kasutades vaid väikest hulka sisseehitatud käske. Taoliselt kirjutatud praktilised programmid aga läheksid peagi nii suureks ja keeruliseks, et ka parimad programmeerijad ei suudaks neid enam hallata.

Võtame esimeseks näiteks juba mainitud ülesande, kus robot peab värvima põranda triibuliseks (vt. 3. ptk :ref:`triibuliseks`. Kui sul on jäänud see ülesanne lahendamata, siis enne jätkamist on soovitav see ülesanne praeguste teadmiste abil ära teha). 

Toome siinkohal ära ühe võimaliku lahenduse, kus pole alamprogramme kasutatud:

.. sourcecode:: py3

    from pykkar import *

    create_world("""
    ########
    #      #
    #      #
    #  ^   #
    #      #
    #      #
    ########
    """)

    # eeldame, et robot alustab alati näoga põhjasuunas

    # liigu põhjaseinani
    while not is_wall():
        step()

    # pööra läänesuunda
    right()
    right()
    right()

    # liigu lääneseinani
    while not is_wall():
        step()

    # pööra lõunasuunda
    right()
    right()
    right()

    # välimine tsükkel käib üle veergude (kaks veergu korraga, üks allaminnes, 
    # koos värvimisega ja teine üles tulles, ilma värvimiseta)
    while True:

        # allaminek ja värvimine
        paint()
        while not is_wall():
            step()
            paint()

        # liigu järgmisele veerule (kui võimalik)
        right()
        right()
        right()
        
        if is_wall():
            # rohkem veerge pole
            break

        # kui jõudsime siia, siis on järelikult veel veerge
        step()
        # pööra nina põhjasuunda
        right()
        right()
        right()

        # liigu üles
        while not is_wall():
            step()

        # proovime liikuda järgmisele (värvitavale) veerule
        right()
        if is_wall():
            # pole rohkem veerge
            break

        step()
        # pöörame õigesse suunda
        right()

        
        

    


Nagu juba varem mainitud, oskab meie robot pöörata vaid paremale. Seetõttu on näitekoodis koht, kus 90° võrra vasakule pööramise saavutamiseks on antud 3 korda järjest käsklus ``paremale()``. See on üks koht, mis võib programmi lugejale esmapilgul segadust tekitada. Kasutame võimalust ja defineerime uue alamprogrammi (e. funktsiooni või "käsu") vasakule pööramiseks. Selleks lisame esialgse programmi algusse uue *funktsiooni definitsiooni*:

.. sourcecode:: py3

    from pykkar import *

    def left():
        right()
        right()
        right()
    
    ...



Sisuliselt defineerisime ühe uue roboti juhtimise käsu ja me võime algses programmis kolmekordse paremale pööramise asendada käsuga ``left()``. Nii ei jäta me koodi lugejale enam kahtlust, mida me soovime kolmekordse pööramisega saavutada.

Teine korduv motiiv esialgses programmis on seinani liikumine. Ka selle saame vormistada funktsioonina:

.. sourcecode:: py3

    ...
    
    def move_to_wall():
        while not is_wall():
            step()
    
    ...

Kui nüüd mõlemaid uusi käske programmis kasutada, saame juba omajagu lihtsama tulemuse:

.. sourcecode:: py3

    from pykkar import *

    def left():
        right()
        right()
        right()

    def move_to_wall():
        while not is_wall():
            step()

    create_world("""
    ########
    #      #
    #      #
    #  ^   #
    #      #
    #      #
    ########
    """)

    # eeldame, et robot alustab alati näoga põhjasuunas

    # liigu põhjaseinani
    move_to_wall()

    # pööra läänesuunda
    left()

    # liigu lääneseinani
    move_to_wall()

    # pööra lõunasuunda
    left()

    # välimine tsükkel käib üle veergude (kaks veergu korraga, üks allaminnes, 
    # koos värvimisega ja teine üles tulles, ilma värvimiseta)
    while True:

        # allaminek ja värvimine
        paint()
        while not is_wall():
            step()
            paint()

        # liigu järgmisele veerule (kui võimalik)
        left()
        
        if is_wall():
            # rohkem veerge pole
            break

        # kui jõudsime siia, siis on järelikult veel veerge
        step()
        # pööra nina põhjasuunda
        left()

        # liigu üles
        move_to_wall()
        
        # proovime liikuda järgmisele (värvitavale) veerule
        right()
        if is_wall():
            # pole rohkem veerge
            break

        step()
        # pöörame õigesse suunda
        right()


Nende funktsioonide loomine ja kasutuselevõtt tuli kasuks kahel moel. Esiteks, funktsiooni defineerimisega **andsime (potentsiaalselt) keerulisele programmilõigule selgitava nime** ning võisime programmi põhiosas mainida ainult nime -- nii muutsime programmi põhiosa veidi lihtsamaks. Nüüd on meil võimalus analüüsida seda värjaeraldatud koodi põhiprogrammist eraldi ja samuti on võimalik analüüsida põhiprogrammi ilma, et peaks muretsema detailide pärast. Näiteks, põhiprogrammi uurides piisab meile teadmisest, et robot pöörab mingis kohas vasakule, me ei pea muretsema selle pärast, kuidas ta seda teeb. Samas, kui meid detailid siiski huvitavad, siis saame alati otsida üles vastava funktsiooni definitsiooni.

Teiseks, me **defineerisime funktsiooni ühekordselt, aga saime seda kasutada mitmes kohas**, seega hoidsime kokku tippimise vaeva.

.. note::

    Alamprogrammide defineerimine on tihti mõistlik ka siis, kui väljaeraldatud koodi on kasutatud vaid ühes kohas, aga ta on piisavalt keeruline, et programmi mõistmist raskendada. Meie näite puhul võiksime eraldi funktsiooni luua veel kuni seinani värvimise kohta:
    
    .. sourcecode:: py3
    
        def paint_until_wall():
            paint()
            while not is_wall():
                step()
                paint()
    
    Selle funktsiooni kasutamisega saaksime lahti ka kahekordsest tsüklist (tsükkel tsükli sees), mis võib mõnele programmi lugejale tunduda keeruline.
    

Harjutus 1. Liigu nurka
~~~~~~~~~~~~~~~~~~~~~~~~~~
Lisa vaadeldud näiteprogrammi veel ühe funktsiooni definitsioon -- ``liigu_nurka`` peaks liigutama kilpkonna temast vasakule-ettepoole jäävasse nurka (võime eeldada ristküliku kujulist põrandat).

Kasuta seda funktsiooni programmis sobival kohal.


Erindid
----------
TODO


Erineva efektiivsusega samaväärsed programmid
----------------------------------------------
TODO:


Ülesanded
-------------

1. Kuupäeva esitamine sõnena
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Kirjuta funktsioon ``kuupäev_sõnena``, mis võtab argumentideks päeva, kuu ja aasta (arvudena) ning tagastab sõne, mis esitab kuupäeva kujul *<päev>. <kuu nimi> <aasta>* (nt. *24. veebruar 1918*).

Seejärel kirjuta programm, mis küsib kasutajalt arvudena päeva, kuu ja aasta. Kui neile vastav kuupäev on legaalne, siis kuvada ekraanile vastav kuupäev sõnena, vastasel juhul kuvada ``'Viga: mittelegaalne kuupäev'``.

Kasuta abifunktsioonidena ülalpood loodud funktsioone (vt. harjutusi 3-6).

2. Täisnurkne kolmnurk
~~~~~~~~~~~~~~~~~~~~~~~~~~
Kirjuta funktsioon, mis võtab argumentideks kolmnurga külgede pikkused ja tagastab ``True`` või ``False`` vastavalt sellele, kas tegemist oli täisnurkse kolmnurgaga või mitte.

.. note:: 

    Lihtsustamise mõttes võid esialgu eeldada, et pikim külg antakse alati kolmanda argumendina. Kui saad esialgse variandi tööle, siis muutke programmi selliselt, et küljepikkuseid võib anda suvalises järjekorras.

.. note::
    
    Ära unusta, et mitte igast küljepikkuste komplektist ei saa moodustada kolmnurka! Soovitame kirjutada abifunktsiooni, mis ütleb, kas antud küljepikkused üldse sobivad kolmnurgale.
    
.. note::

    Ära unusta, et ujukomaarvud on pisut ebatäpsed, seega võib olla vajalik võrdsuse kontrollimise asemel kontrollida sarnasust:
    
    .. sourcecode :: py3
    
        if abs(x - y) < 0.000001:      # x on peaaegu võrdne y-ga
            ...

.. hint::

    Tuleta jälle meelde see vana hea koolimatemaatika teoreem.


Kasuta loodud funktsiooni, küsides kasutajalt kolmnurga 3 külje pikkused ja väljastades info selle kohta, kas antud kolmnurk on täisnurkne või mitte. Kui küljepikkused ei sobi kolmnurgale, siis tuleks ka seda öelda.

3. Klaveri mahutamine
~~~~~~~~~~~~~~~~~~~~~
Ülikool on ostnud endale uue klaveri peahoone aula tarbeks. Paraku unustati  kontrollida, kas see klaver üldse välisuksest sisse mahub. Kirjutada programm, mis küsib kasutajalt klaverit sisaldava kasti kolm mõõdet (pikkus, laius, kõrgus) ning ukse laiuse ja kõrguse ning vastab, kas klaver on võimalik aulasse sisse toimetada.

4. Pitsapood
~~~~~~~~~~~~
Kirjuta programm, mis küsib kasutajalt infot tellitava pitsa suuruse, komponentide ja kättetoimetamise detailide kohta. Igal sammul tuleks esitada kasutajale võimalikud valikud koos vastavate koodidega, nt:

.. sourcecode:: none

    ...
    ...
    Millise suurusega pitsat soovid? Valikud on:
      1 - väike (18cm)
      2 - keskmine (25cm)
      3 - suur (35cm)
    Palun sisesta oma valik: 2
    ...
    ...
    Mida lisada pitsa peale? 
      0 - rohkem mitte midagi
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
Eelmises peatükis tutvustasime mõningaid tkinter'i võimalusi graafiliste kasutajaliideste loomisel. Seal demonstreerisime põhiliste "standardvidinate", nagu nuppude ja tekstisisestuskastide kasutamist. Seekord uurime ühte väga paindlikku vidinat, mille nimi on *Canvas* (tõlkes *lõuend*). *Canvase* peale saab joonistada kujundeid, laadida pilte, neid pilte ja kujundeid saab liigutada, nendele klõpsamist on võimalik registreerida jne.

Salvesta endale järgnev näiteprogramm. Enne käivitamist salvesta samasse kausta ka fail :download:`juku.gif <downloads/juku.gif>`.

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

Käivita programm, vajuta nooleklahve, klõpsa hiirega kriipsujukul.

See näiteprogramm oli siinkohal mõeldud vaid "isuäratajana" -- selleks, et sellest aru saada, loe esmalt lihtsamate Canvase programmide selgitusi õpiku lisast *tkinter*, jaotusest :ref:`canvas`.