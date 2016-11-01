**********
Matplotlib
**********

TODO: joonestusala vs teljestik

TODO: selle juhendi läbilugemine aitab ka dokumentatsioonis orienteeruda

Paketi paigaldamine
===================
...

Paigalduse kontrollimiseks käivita järgmine kood:

.. sourcecode:: py3

    ...




Andmed
======
listid vs NumPy

Näites on aastad ja vastavad elanike arvud antud harilike Pythoni listidena, aga nende asemel võivad vabalt olla ka NumPy massiivid.

Põhimõtted
==========
Oletame, et meil on andmed mingi firma sissetulekute kohta erinevatel kuudel. Proovime seda infot kõigepealt visualiseerida ``matplotlib``-i joongraafiku abil: 

.. sourcecode:: py3

    import matplotlib.pyplot as plt
    
    kuud         = [  1,    4,    5,    6,    7,    8,    9,   10,  11,  12]
    sissetulekud = [710, 1200, 1445, 1690, 1350, 1223, 1470, 1200, 808, 698]
    
    fig = plt.figure()           # Kõigepealt loome joonist tähistava objekti
    ax = fig.add_subplot(1,1,1)  # ja lisame joonisele joonestusala.
    
    ax.plot(kuud, sissetulekud)  # Lisame joonestusalale joondiagrammi.
    
    fig.show()                   # Kuvame joonise ekraanile.

Käivita see programm ja katseta avanenud aknas olevaid nuppe. 

Selle lihtsa näite põhjal saame välja tuua kõige olulisemad ``matplotlib``-i põhimõtted ja tavad.

* Kõige sagedamini kasutatav matplotlib-i moodul on :py:mod:`matplotlib.pyplot`, mis imporditakse tavaliselt lühema nime ``plt`` alla.
* Imporditud moodulis on funktsioon :py:func:`figure<matplotlib.pyplot.figure>`, mille abil luuakse joonist tähistav objekt.
* Ühel joonisel võib olla mitu graafikut/joonestusala (ing k *subplot*). Uue joonestusala loomiseks kasutatakse joonise meetodit :py:meth:`add_subplot<matplotlib.figure.Figure.add_subplot>`, mille argumendid näitavad mitmeks reaks ja veeruks joonis jagada ning mitmes joonestusala luua. Ühe joonestusalaga jooniste puhul on argumendid alati ``1,1,1``.
* ``add_subplot`` tagastab objekti klassist :py:class:`Axes<matplotlib.axes.Axes>` (*teljestik*), mille abil saab konkreetsele joonestusalale elemente lisada.
    * Antud näites kasutasime joonestamiseks meetodit :py:meth:`plot<matplotlib.axes.Axes.plot>`, mis on mõeldud joondiagrammide koostamiseks, aga ``Axes`` oskab joonistada ka sektor-,  tulp- ja hajuvusdiagramme, histogramme, lihtsaid kujundeid ja palju muud.
    * Sama objekti kaudu käib näiteks ka telje, skaala ja legendi seadistamine.
* Tulemust saab näha kasutades joonise meetodit :py:meth:`show<matplotlib.figure.Figure.show>`. Alternatiivina (või lisaks) võib joonise meetodiga :py:meth:`savefig<matplotlib.figure.Figure.savefig>` ka faili salvestada. 

.. admonition:: Alternatiiv: pyplot-stiil

    Internetis ringi vaadates leiate palju matplotlib-i kasutamise näiteid, kus pole meetodeid ``figure`` ja ``add_subplot`` üldse kasutatud. Meie näide võiks olla neis kohtades kirja pandud umbes selliselt:
    
    .. sourcecode:: py3
    
        import matplotlib.pyplot as plt
        
        kuud         = [  1,    4,    5,    6,    7,    8,    9,   10,  11,  12]
        sissetulekud = [710, 1200, 1445, 1690, 1350, 1223, 1470, 1200, 808, 698]
        
        plt.plot(kuud, sissetulekud)  # Lisame joonestusalale joondiagrammi.
        
        plt.show()       
    
    Nagu näha on siin ``plot``, ``legend`` ja ``show`` võetud otse moodulist :py:mod:`matplotlib.pyplot`.
    
    Tegelikult luuakse ka sellise koodi korral joonisele ja joonestusalale vastavad objektid, aga see toimub automaatselt. Teisisõnu :py:func:`matplotlib.pyplot.plot`, :py:func:`matplotlib.pyplot.legend` ja :py:func:`matplotlib.pyplot.show` on veidi kavalamad, kui vastavad :py:class:`Axes<matplotlib.axes.Axes>` ja :py:class:`Figure<matplotlib.figure.Figure>` meetodid.
    
    Kuna praktiliselt kõigile ``Axes`` meetoditele olemas vastavad kavalad :py:mod:`matplotlib.pyplot` funktsioonid, siis saaks selle stiiliga panna kokku sama keerulisi jooniseid nagu eraldi väljatoodud ``Axes`` objektide abil.
    
    Kui sellised kavalad funktsioonid on olemas, miks siis üldse näha vaeva :py:class:`Figure<matplotlib.figure.Figure>` ja :py:class:`Axes<matplotlib.axes.Axes>` objektide loomisega? Tegelikult ei olegi tarvis -- eriti just lihtsate, ühekordseks kasutamiseks mõeldud graafikute koostamiseks on pyplot-stiil väga mugav ja asjakohane. Keerulisemate graafikute puhul aga võimaldavad eraldi väljatoodud ``Figure`` ja ``Axes`` objektid (st. objekt-orienteeritud stiil) lahendust selgemalt struktureerida ning teatud puhkudel on nende sissetoomine lausa möödapääsematu. Seepärast ongi selles õpikus matplotlib-i tutvustamiseks valitud objektorienteeritud stiil.
    
    Selle teema kohta saab lähemalt lugeda siit: http://matplotlib.org/faq/usage_faq.html#coding-styles
        

Joondiagramm
============
Eelmisest näitest nägime, et joondiagramme saab koostada :py:class:`Axes<matplotlib.axes.Axes>` meetodi :py:meth:`plot<matplotlib.axes.Axes.plot>` abil. Uurime nüüd asja lähemalt. 

Teljestiku seadistamine
-----------------------
Ülaltoodud koodi käivitamisel pidi ilmuma umbes selline aken:

.. image:: images/mpl_joon1.png

Nagu näha, on matplotlib seadistanud graafiku teljestiku nii, et etteantud andmepunktid mahuvad parajasti ära, aga see ei pruugi olla alati parim valik -- selle pildi järgi tundub jaanuari ja juuni erinevus palju suurem, kui see tegelikult oli. Telgede ulatuse seadistamiseks saame kasutada meetodeid :py:meth:`set_xlim<matplotlib.axes.Axes.set_xlim>` ja :py:meth:`set_ylim<matplotlib.axes.Axes.set_ylim>`, mis määravad vastava telje nähtavuspiirkonna.

Teine probleem on see, et y-teljel ei ole kõikide kuude numbreid. Õnneks saab meetoditega :py:meth:`set_xticks<matplotlib.axes.Axes.set_xticks>` ja :py:meth:`set_yticks<matplotlib.axes.Axes.set_yticks>` määrata, millistesse kohtadesse tuleb telgedel märgid (*ticks*) kuvada. 

Täiendame nüüd oma graafikut neid võimalusi kasutades:

.. sourcecode:: py3
    :emphasize-lines: 12,13

    import matplotlib.pyplot as plt
    
    kuud         = [  1,    4,    5,    6,    7,    8,    9,   10,  11,  12]
    sissetulekud = [710, 1200, 1445, 1690, 1350, 1223, 1470, 1200, 808, 698]
    
    fig = plt.figure()           # Kõigepealt loome joonist tähistava objekti
    ax = fig.add_subplot(1,1,1)  # ja lisame joonisele joonestusala.
    
    ax.plot(kuud, sissetulekud)  # Lisame joonestusalale joondiagrammi.
    
    ax.set_ylim(0, 2000)         # Määrame y-telje nähtavuspiirkonna
    ax.set_xticks([1,2,3,4,5,6,7,8,9,10,11,12])  # ja x-telje märgid
    
    fig.show()                   # Kuvame joonise ekraanile.

.. image:: images/mpl_joon2.png

Joone ja andmepunktide seadistamine
-----------------------------------

Kui uurid meie firma sissetuleku andmeid lähemalt, siis märkad, et veebruari ja märtsi andmed on puudu ja joondiagrammi vastav lõik on joonistatud lihtsalt jaanuari ja aprilli vahele. Oleks hea, kui graafikust tuleks välja, milliste kuude kohta on tegelikud andmepunktid olemas. 

Joone ja andmepunktide välimust saame määrata ``plot`` meetodi kolmanda argumendiga:


.. sourcecode:: py3
    :emphasize-lines: 9

    import matplotlib.pyplot as plt
    
    kuud         = [  1,    4,    5,    6,    7,    8,    9,   10,  11,  12]
    sissetulekud = [710, 1200, 1445, 1690, 1350, 1223, 1470, 1200, 808, 698]
    
    fig = plt.figure()           # Kõigepealt loome joonist tähistava objekti
    ax = fig.add_subplot(1,1,1)  # ja lisame joonisele joonestusala.
    
    ax.plot(kuud, sissetulekud, "o-")  # Lisame joonestusalale joondiagrammi.
    
    ax.set_ylim(0, 2000)         # Määrame y-telje nähtavuspiirkonna
    ax.set_xticks([1,2,3,4,5,6,7,8,9,10,11,12])  # ja x-telje märgid
    
    fig.show()                   # Kuvame joonise ekraanile.


Antud näites ``o`` tähendab seda, et iga andmepunkti kohale tuleb joonistada täpike ja ``-`` tähendab seda, et andmepunktide vahele tuleb tõmmata kriips. 

Lisaks punkti ja kriipsu kuju määramisele, saaks sama argumendiga näidata ära ka nende värvi. Näiteks ``"^--g"`` (g nagu green) tekitab rohelised kolmnurksed andmepunktid ja katkendliku joone ning ``"*r"`` tekitab punased tärnikujulised andepunktid ilma jooneta.

Rohkem infot leiab meetodi :py:meth:`plot<matplotlib.axes.Axes.plot>` dokumentatsioonist.

Mitme näitaja võrdlemine
------------------------
Tuli välja, et firmal on kogutud andmed ka antud kuude väljaminekute kohta. Teeme graafiku, mis näitab sissetulekuid ja väljaminekuid korraga. Selleks, et oleks, selge, kumb joon tähistab kumba näitajat, lisame graafikule ka legendi -- selleks lisame ``plot`` väljakutsetele ``label`` argumendid ja kutsume välja joonestusala meetodi :py:meth:`legend()<matplotlib.axes.Axes.legend>`: 

.. sourcecode:: py3
    :emphasize-lines: 5,11-12,16

    import matplotlib.pyplot as plt
    
    kuud         = [  1,    4,    5,    6,    7,    8,    9,   10,  11,  12]
    sissetulekud = [710, 1200, 1445, 1690, 1350, 1223, 1470, 1200, 808, 698]
    väljaminekud = [700, 1160, 1556, 1520, 1415, 1180, 1770,  500, 408, 505]
    
    fig = plt.figure()           # Kõigepealt loome joonist tähistava objekti
    ax = fig.add_subplot(1,1,1)  # ja lisame joonisele joonestusala.
    
    ax.plot(kuud, sissetulekud, "o-", label="Sissetulekud")               
    ax.plot(kuud, väljaminekud, "^-r", label="Väljaminekud")
    
    ax.set_ylim(0, 2000)         # Määrame y-telje nähtavuspiirkonna
    ax.set_xticks([1,2,3,4,5,6,7,8,9,10,11,12])  # ja x-telje märgid
    ax.legend()         
    
    fig.show()                   # Kuvame joonise ekraanile.

Tulpdiagramm
============
Tulpdiagrammi koostamiseks on meetod :py:meth:`bar<matplotlib.axes.Axes.bar>`, millele tuleb anda argumendiks tulpade positsioonid x-teljel, tulpade kõrgused ja tulba laius (x-telje skaalal):


.. sourcecode:: py3
    :emphasize-lines: 4,8

    import matplotlib.pyplot as plt
    
    kuud             = [ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12]
    ümbrikke_kulunud = [ 2,  6,  2,  7,  6,  2,  3,  2,  4,  4,  1, 13]
    
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    ax.bar(kuud, ümbrikke_kulunud, 0.8)
    ax.set_xticks([1,2,3,4,5,6,7,8,9,10,11,12])
    
    fig.show()
    
.. image:: images/mpl_tulp1.png

Nagu näha, määrab meetodi ``bar`` esimene argument, kuhu satuvad tulpade vasakud servad. Paremad servad satuvad tulba laiuse võrra paremale. Kui tahame tulpasid paigutada nii, et tulba kuu märgi kohale satuks tulba keskkoht, siis tuleb esimest argumenti natuke nihutada:

.. sourcecode:: py3
    :emphasize-lines: 9-11

    import matplotlib.pyplot as plt
    
    kuud             = [ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12]
    ümbrikke_kulunud = [ 2,  6,  2,  7,  6,  2,  3,  2,  4,  4,  1, 13]
    
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    
    # moodustame kuu numbrite põhjal uue listi, kus elemendid on 0.4 võrra väiksemad
    tulpade_positsioonid = [kuu - 0.4 for kuu in kuud]  
    ax.bar(tulpade_positsioonid, ümbrikke_kulunud, 0.8)
    
    ax.set_xticks([1,2,3,4,5,6,7,8,9,10,11,12])
    
    fig.show()

TODO: seleta list comprehensionit

Mitme näitaja tulpdiagramm
--------------------------
Kui me tahame tulpadena kõrvuti näha ümbrike ja kirjaklambrite kulusid, siis  tuleb lihtsalt meetodit ``bar`` välja kutsuda kaks korda. Seejuures aga tuleb sättida eri näitajate tulbad nii, et nad üksteist varjutama ei hakkaks. Samuti tuleb teha tulbad kitsamaks. Lisaks anname ``bar``-ile ``label`` argumendi, mille põhjal :py:meth:`legend()<matplotlib.axes.Axes.legend>` teeb joonisele legendi:

.. sourcecode:: py3
    :emphasize-lines: 5,14-15,18

    import matplotlib.pyplot as plt
    
    kuud                    = [ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12]
    ümbrikke_kulunud        = [ 2,  6,  2,  7,  6,  2,  3,  2,  4,  4,  1, 13]
    kirjaklambreid_kulunud  = [ 5,  2,  1,  3,  3,  0,  0,  0,  1,  2,  1,  3]
    
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    
    # moodustame kuu numbrite põhjal uue listi, kus elemendid on 0.4 võrra väiksemad
    ümbriku_tulpade_positsioonid = [kuu - 0.4 for kuu in kuud]
    ax.bar(ümbriku_tulpade_positsioonid, ümbrikke_kulunud, 0.4, label="Ümbrikke")
    
    # kirjaklambri tulpade positsioonideks kõlbavad kuu numbrid
    ax.bar(kuud, kirjaklambreid_kulunud, 0.4, label="Kirjaklambreid")
    
    ax.set_xticks([1,2,3,4,5,6,7,8,9,10,11,12])
    ax.legend()
    
    fig.show()

Kahe y-telje kasutamine
=======================
Siiani tehtud joon- ja tulpdiagrammide kombineerimine ei ole tehniliselt võttes midagi rasket -- kuna x-teljel oli kõigil juhtudel sama skaala, siis tuleb lihtsalt kõik elemendid lisada samale joonestusalale. Tuleb vaid arvestada, et rahaasjade andmetes oli meil veebruari ja märtsi kohal auk, aga kontoritarvete puhul oli ka nende kuude jaoks andmed olemas:

.. sourcecode:: py3

    import matplotlib.pyplot as plt
    
    raha_kuud      = [  1,    4,    5,    6,    7,    8,    9,   10,  11,  12]
    sissetulekud   = [710, 1200, 1445, 1690, 1350, 1223, 1470, 1200, 808, 698]
    väljaminekud   = [700, 1160, 1556, 1520, 1415, 1180, 1770,  500, 408, 505]
    
    asjade_kuud             = [ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12]
    ümbrikke_kulunud        = [ 2,  6,  2,  7,  6,  2,  3,  2,  4,  4,  1, 13]
    kirjaklambreid_kulunud  = [ 5,  2,  1,  3,  3,  0,  0,  0,  1,  2,  1,  3]
    
    fig = plt.figure()           # Kõigepealt loome joonist tähistava objekti
    ax = fig.add_subplot(1,1,1)  # ja lisame joonisele joonestusala.
    ax.set_ylim(0, 2000)         # Määrame y-telje nähtavuspiirkonna
    ax.set_xticks([1,2,3,4,5,6,7,8,9,10,11,12])  # ja x-telje märgid
    
    ax.plot(raha_kuud, sissetulekud, "o-", label="Sissetulekud")
    ax.plot(raha_kuud, väljaminekud, "^-r", label="Väljaminekud")
    
    ümbriku_tulpade_positsioonid = [kuu - 0.4 for kuu in asjade_kuud]
    ax.bar(ümbriku_tulpade_positsioonid, ümbrikke_kulunud, 0.4, label="Ümbrikke")
    ax.bar(asjade_kuud, kirjaklambreid_kulunud, 0.4, label="Kirjaklambreid")
    
    ax.legend()
    
    fig.show()                   # Kuvame joonise ekraanile.

Kahjuks see lähenemine siiski ei tööta, sest rahasummad on palju suuremad kui kontoritarvete arvud ja seetõttu viimased ei paista üldse välja. Lahenduseks on kahe erineva y-skaala kasutamine (TODO: pikem selgitus ja lingid):

.. sourcecode:: py3
    :emphasize-lines: 20-22,24-25

    import matplotlib.pyplot as plt
    
    raha_kuud      = [  1,    4,    5,    6,    7,    8,    9,   10,  11,  12]
    sissetulekud   = [710, 1200, 1445, 1690, 1350, 1223, 1470, 1200, 808, 698]
    väljaminekud   = [700, 1160, 1556, 1520, 1415, 1180, 1770,  500, 408, 505]
    
    asjade_kuud             = [ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12]
    ümbrikke_kulunud        = [ 2,  6,  2,  7,  6,  2,  3,  2,  4,  4,  1, 13]
    kirjaklambreid_kulunud  = [ 5,  2,  1,  3,  3,  0,  0,  0,  1,  2,  1,  3]
    
    fig = plt.figure()           # Kõigepealt loome joonist tähistava objekti
    ax = fig.add_subplot(1,1,1)  # ja lisame joonisele joonestusala.
    ax.set_ylim(0, 2000)         # Määrame y-telje nähtavuspiirkonna
    ax.set_xticks([1,2,3,4,5,6,7,8,9,10,11,12])  # ja x-telje märgid
    
    ax.plot(raha_kuud, sissetulekud, "o-", label="Sissetulekud")
    ax.plot(raha_kuud, väljaminekud, "^-r", label="Väljaminekud")
    
    ümbriku_tulpade_positsioonid = [kuu - 0.4 for kuu in asjade_kuud]
    ax2 = ax.twinx()
    ax2.bar(ümbriku_tulpade_positsioonid, ümbrikke_kulunud, 0.4, label="Ümbrikke")
    ax2.bar(asjade_kuud, kirjaklambreid_kulunud, 0.4, label="Kirjaklambreid")
    
    ax.legend(loc="upper left")
    ax2.legend(loc="upper right")
    
    fig.show()                   # Kuvame joonise ekraanile.

Nüüd häirib tulemuses veel see, et jooned jäävad osaliselt tulpade taha peitu, ning sissetulekute joon on ümbrike tulpadega sama värvi. Õnneks pakub matplotlib lahenduse ka neile muredele:

.. sourcecode:: py3
    :emphasize-lines: 16,27-29

    import matplotlib.pyplot as plt
    
    raha_kuud      = [  1,    4,    5,    6,    7,    8,    9,   10,  11,  12]
    sissetulekud   = [710, 1200, 1445, 1690, 1350, 1223, 1470, 1200, 808, 698]
    väljaminekud   = [700, 1160, 1556, 1520, 1415, 1180, 1770,  500, 408, 505]
    
    asjade_kuud             = [ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12]
    ümbrikke_kulunud        = [ 2,  6,  2,  7,  6,  2,  3,  2,  4,  4,  1, 13]
    kirjaklambreid_kulunud  = [ 5,  2,  1,  3,  3,  0,  0,  0,  1,  2,  1,  3]
    
    fig = plt.figure()           # Kõigepealt loome joonist tähistava objekti
    ax = fig.add_subplot(1,1,1)  # ja lisame joonisele joonestusala.
    ax.set_ylim(0, 2000)         # Määrame y-telje nähtavuspiirkonna
    ax.set_xticks([1,2,3,4,5,6,7,8,9,10,11,12])  # ja x-telje märgid
    
    ax.plot(raha_kuud, sissetulekud, "o-g", label="Sissetulekud")
    ax.plot(raha_kuud, väljaminekud, "^-r", label="Väljaminekud")
    
    ümbriku_tulpade_positsioonid = [kuu - 0.4 for kuu in asjade_kuud]
    ax2 = ax.twinx()
    ax2.bar(ümbriku_tulpade_positsioonid, ümbrikke_kulunud, 0.4, label="Ümbrikke")
    ax2.bar(asjade_kuud, kirjaklambreid_kulunud, 0.4, label="Kirjaklambreid")
    
    ax.legend(loc="upper left")
    ax2.legend(loc="upper right")
    
    # sätime joonte teljestiku tulpade omast ettepoole
    ax.set_zorder(ax2.get_zorder() + 1)
    ax.patch.set_visible(False)
    
    fig.show()                   # Kuvame joonise ekraanile.

Sektordiagramm
==============

Sektordiagrammi koostamiseks on mõeldud meetod :py:meth:`pie<matplotlib.axes.Axes.pie>`, mis võtab esimeseks argumendiks sektorite suurused ja ``labels`` argumendiks sektorite nimed:

.. sourcecode:: py3
    :emphasize-lines: 8

    import matplotlib.pyplot as plt
    
    kuud         = [  1,    4,    5,    6,    7,    8,    9,   10,  11,  12]
    sissetulekud = [710, 1200, 1445, 1690, 1350, 1223, 1470, 1200, 808, 698]
    
    fig = plt.figure()           
    ax = fig.add_subplot(1,1,1)  
    ax.pie(sissetulekud, labels=kuud)
    fig.show()

Histogramm
==========
TODO: 

Scatter-plot
============
TODO: 


Stiilid
=======
print(plt.style.available)
plt.style.use('fivethirtyeight')


Graafikute integreerimine programmidesse
========================================

:py:mod:`matplotlib.pyplot`

``matplotlib`` graafikuid saab integreerida erinevate kasutajaliidese raamistikega, sh Tkinteriga. Selleks tuleb ``Figure`` objekt luua mitte ``pyplot`` abil, vaid moodulis :py:mod:`matplotlib.figure` oleva klassi :py:class:`Figure<matplotlib.figure.Figure>` abil. Lisaks tuleb luua raamistikuspetsiifilised vidinad graafiku näitamiseks.

Järgnev näide demonstreerib pirukagraafiku lisamist Tkinteri programmi:

.. sourcecode:: py3

    import tkinter as tk
    from tkinter import ttk
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
    from matplotlib.figure import Figure
    
    def uuenda_graafik():
        ax.clear()
        
        # Simuleerin andmete uuendamist juhuslike andmete genereerimisega.
        # Reaalne programm loeks andmed kusagilt failist, sensoritest vms.
        import random
        k = 5
        suurused = random.sample([12, 45, 4, 14, 33, 32, 66, 23, 29, 7], k)
        nimed = random.sample(["Peeter", "Tiit", "Mari", "Jakob", "Teele",
                               "Kalle", "Malle", "Reet", "Lauri", "Kati"], k)
        
        ax.pie(suurused, labels=nimed)
        canvas.show()
    
    def salvesta_graafik():
        fig.savefig("graafik.pdf") # Fail ilmub jooksvasse kausta
    
    # Loon akna
    aken = tk.Tk()
    aken.title("Demo")
    
    # Loon graafikut tähistavad objektid
    fig = Figure(figsize=(5, 5), dpi=100) # 5x5 tolli
    ax = fig.add_subplot(1,1,1)
    fig.set_facecolor('white')
    
    # Loon pinna graafiku joonistamiseks
    # ja paigutan vastava Tk vidina
    canvas = FigureCanvasTkAgg(fig, master=aken)
    canvas.get_tk_widget().grid(row=0, column=0, columnspan=2)
    
    # Loon nupu andmete laadimiseks
    nupp1 = ttk.Button(aken, text="Uuenda graafik", command=uuenda_graafik)
    nupp1.grid(row=1, column=0)
    
    # Loon nupu graafiku salvestamiseks
    nupp2 = ttk.Button(aken, text="Salvesta graafik", command=salvesta_graafik)
    nupp2.grid(row=1, column=1)
    
    # Kuvan andmete esialgse seisu
    uuenda_graafik()
    
    # Alustan programmi peatsüklit
    aken.mainloop()

Rohkem infot:

* http://matplotlib.org/examples/user_interfaces/embedding_in_tk.html 
* https://pythonprogramming.net/how-to-embed-matplotlib-graph-tkinter-gui
* http://matplotlib.org/users/event_handling.html
 
Täpsem info
===========
Ülevaade võimalustest: http://matplotlib.org/users/screenshots.html
Väga hea ülevaade matplotlib mõistetest: http://matplotlib.org/faq/usage_faq.html

Hea tut?: http://www.labri.fr/perso/nrougier/teaching/matplotlib/

