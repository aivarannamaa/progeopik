14. Varia
==========

Erindid
------------
TODO

List comprehension
-----------------------
TODO


Kõrgemat järku funktsioonid
---------------------------------
TODO
(kopeeritud tkinteri lisast)
Nagu nägime antud praktikumi esimesest näite juures võib funktsioonile anda argumendiks ka teise funktsiooni (funktsioonile ``Button`` andsime argumendiks funktsiooni ``tervita``). Selline võte aitab tihti kirjutada üldisemat ja lühemat koodi. Näiteks defineerime funktsiooni, mis käivitab etteantud funktsiooni kaks korda, ning kasutame seda koos ühe lihtsa testfunktsiooniga:

.. sourcecode:: py3

    def topelt(f):
         # Käivita esimest korda:
         f()
         # Käivita teist korda:
         f()
     
    def tere():
         print('Tere')
         
    topelt(tere)
     
Proovige, mida selline programm teeb. NB! Viimasel real on ``tere`` kirjutatud ilma tühjade sulgudete, sest soovisime anda argumendiks funktsiooni ennast, mitte tema käivitamise tulemust. Mis oleks saanud argumendi väärtuseks, kui oleksime kirjutanud ``topelt(tere())``?

    
Edasi vaatleme väärtust tagastavate funktsioonide järjest rakendamist. Selleks defineerime funktsiooni kompositsioon, mis rakendab järjest etteantud ühekohalisi funktsioone kaasa antud argumendile x:

.. sourcecode:: python

    def kompositsioon(f, g, x):
        # g sisendiks anname väärtuse x, g poolt tagastava väärtuse
        # anname omakorda f sisendiks. Lõpuks tagastame f poolt arvutatud
        # väärtuse
        return f(g(x))
 
Näide kasutamisest:

.. sourcecode:: python

    y = kompositsioon(asin, sin, 1.0)

Programm on samaväärne järgmisega:

.. sourcecode:: python

    y = asin(sin(1.0))

Kõrgemat järku funktsioone on mugav kasutada järjendite töötlemisel. Python sisaldab sisseehitatud funktsiooni map, mis rakendab igale järjendi elemendile etteantud funktsiooni. Eespool läbi tehtud näide punktide teisendamiseks hinneteks map abil:

.. sourcecode:: py3

    punktid = [92,75,87,63]

    # Leiab punktidele vastavad hinded.
    # Igale järjendi punktid elemendile rakendame funktsiooni
    # hinne. Funktsiooni hinne poolt tagastatavad väärtused
    # korjatakse järjendisse hinded
    hinded = map(hinne, punktid)
    print hinded

    
Funktsioon map on küll sisseehitatud funktsioon, kuid tema definitsioon võiks välja näha ka järgmine:

.. sourcecode:: py3

    def map(fun, jarjend):
        # Alusta tühja järjendiga:
        tagastatavad = []
        # Iga sisendjärjendi elemendile rakenda
        # funktsiooni fun ja lisa tulemus väljundjärjendisse
        for e in jarjend:
            tagastatavad.append(fun(e))
        return tagastatavad
    
Programmeerimisstiil *funktsionaalne programmeerimine* kasutab ohtralt kõrgemat järku funktsioone.


