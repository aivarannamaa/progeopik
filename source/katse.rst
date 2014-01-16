Katsetused
****************
blaa

Esimene
=========

blaa

Parameetrid
===========
Nagu näha, on funktsioonid suureks abiks, kui sama käskude komplekti tahetakse programmis käivitada mitmes kohas. Samas, täpselt sama tegevuse kordamist on vaja siiski üpris harva. Tihemini on vaja teha midagi sarnast, kuid teatud väikese nüansiga, mis võib erinevatel kordadel varieeruda. Sellise nüansi väljatoomiseks on võimalik funktsioonile lisada **parameetreid**. Järgnevas näiteprogrammis on defineeritud funktsioon kasutaja tervitamiseks. Varieeruv nüanss e. parameeter on antud juhul tervitatava nimi:

.. sourcecode:: python

    def tere(nimi):
        print("Tere " + nimi + "!")
        print("Kuidas läheb?")
        
    tere("Kalle")
    tere("Malle")
    
Funktsiooni ``tere`` definitsiooni päises on lisaks funktsiooni nimele näidatud ära ka parameeter nimega "nimi". Parameetri näol on sisuliselt tegu spetsiaalse lokaalse muutujaga, mille väärtus sõltub sellest, kuidas funktsioon parasjagu välja kutsuti. Kui funktsioon kutsutakse välja avaldisega ``tere("Kalle")``, siis saab muutuja ``nimi`` väärtuseks ``"Kalle"``, ``tere("Malle")`` puhul on väärtuseks ``"Malle"``. Funktsiooni sisemine masinavärk töötab mõlemal juhul samamoodi – ta võtab parameetri väärtuse (misiganes see juhtub olema) ning lisab selle tervitusele. Kuna aga väärtused on kahel juhul erinevad, on ka tulemus erinev.

Parameetritega saab teha funktsiooni universaalsemaks -- teatud detailid jäetakse funktsiooni väljakutsuja otsustada. Ilma parameetriteta funktsioon on justkui rätsep, kes teeb alati samasuguseid ülikondi, parameetreid võiks aga võrrelda tellija mõõtude ja muude soovidega, mida rätsep oma tegevuses arvesse võtab.

.. topic:: Kas sõnad *parameeter* ja *argument* on sünonüümid?

    Mitte päris. Parameetrid ja argumendid on ühe mündi kaks erinevat poolt. Argument on funktsiooni väljakutses antud *avaldis*, millest saab vastava parameetri *väärtus*. Parameetrid on seotud funktsiooni definitsiooniga, argumendid on seotud funktsiooni väljakutsega. Parameetrid on üldised, argumendid on konkreetsed. Meie viimases näites on ``nimi`` funktsiooni ``tere`` parameeter, aga sõneliteraal ``"Kalle"`` on vastav argument funktsiooni väljakutses.
    
    .. note::    
        Parameetri vs. argumendi asemel võib mõnikord kohata ka väljendeid `formaalne parameeter` vs. `tegelik parameeter`.  

.. topic:: Harjutus. Parametriseeritud ``ruut``
    :class: exercise done
    :name: parametriseeritud_ruut

    Täiusta eespool defineeritud ruudu joonistamise funktsiooni nii, et ruudu küljepikkuse saab määrata funktsiooni väljakutsel. Kasuta loodud funktsiooni, joonistades mitu erineva suurusega ruutu.
    
    .. note::
    
        Järgnevas vihjes on antud harjutuse näitelahendus, ära seda enne vaata, kui oled ise proovinud!
    
    .. hint::
        :class: solution    
        
        .. sourcecode:: py3
        
            from turtle import *
            
            def ruut(kylg):
                i = 0
                while i < 4:
                    forward(kylg)
                    left(90)
                    i += 1
            
            ruut(100)
            
            # liigume kuskile mujale
            up()
            forward(200)
            down()
            
            # väiksem ruut
            ruut(20)
            
            exitonclick()
    


``return`` vs. ``print``
------------------------

.. todo::

    Vaata üle, kas see on optimaalne selgitus. Paljudel on sellega ikka probleeme.
    Äkki selgitad liiga segaselt?


Eelnevalt märkisime, et funktsiooni parameetrid ja ``input`` on olemuselt sarnased, kuna mõlemad on seotud sisendi saamisega, kuid parameetrid on paindlikumad, kuna täpne sisendi saamise viis jäetakse lahtiseks.

Analoogselt võime võrrelda ``print`` ja ``return`` käskusid -- mõlemad on seotud väljundi andmisega, kuid ``return`` on paindlikum, kuna täpne tulemuse kasutamise viis jäetakse lahtiseks.

Uuri kahte järgnevat programmi, kus mõlemas on defineeritud funktsioon ringi pindala arvutamiseks. Mõlemal juhul on meie eesmärgiks arvutada mingi ringi pindala ning kuvada tulemus ekraanile ja kirjutada faili. 

+----------------------------------------------+----------------------------------------------+
|.. sourcecode:: py3                           |.. sourcecode:: py3                           |
|                                              |                                              |
|    from math import pi                       |    from math import pi                       |
|                                              |                                              |
|    def ringi_pindala(raadius):               |    def ringi_pindala(raadius):               |
|        print("Pindala on", pi * raadius**2)  |        return pi * raadius**2                |
|                                              |                                              |
|                                              |    x = ringi_pindala(16.5)                   |
|    ringi_pindala(16.5)                       |    print("Pindala on", x)                    |
|                                              |                                              |  
|    # Salvestame tulemuse ka faili ...        |    # salvestame tulemuse ka faili            |
|    # Probleem: kuidas saada tulemust         |    f.open("tulemus.txt")                     |
|    # ekraanilt kätte?                        |    f.write("Tulemus: " + str(x))             |
|                                              |    f.close()                                 |
+----------------------------------------------+----------------------------------------------+
    
Kui sooviksime arvutuse tulemust näidata ainult ekraanil, siis tehniliselt võttes pole vahet, kas me teeme ``print``-i funktsiooni sees või väljaspool. Erinevus tuleb sisse, kui me soovime tulemust veel kuskil kasutada näiteks faili koostamisel või mingites järgnevates arvutustes -- meie esimeses programmis olev funktsioon siis enam ei sobi. Teises variandis on funktsioon defineeritud üldisemana ja seetõttu saab seda kasutada rohkemates situatsioonides.

.. todo::

    Kaugus: Kuidas sulle meeldiks see, kui sa tahad arvutada sin(0.5) ja selle asemel, et Python tagastaks 0.479425538604203, kirjutab ta su ekraanile "Selle arvu siinus on 0.479425538604203"? Ilmselt on sin funktsiooni praegusel kujul siiski kasulikum. Samamoodi oleks kasulikum, kui sinu funktsioon "kaugus", mitte ei prindiks ekraanile mingi jutu, vaid tagastaks ainult selle arvu mida küsitakse. Küsija ise siis vaatab, mis ta tulemusega edasi teeb -- võibolla prindib ekraanile, võibolla teeb midagi muud.


.. note::
    
    Antud teemas võib segadus tekkida Pythoni käsurea kasutamisel -- kui kirjutada sinna avaldis ``sqrt(2)``, siis tulemus ilmub ikkagi ekraanile, kuigi me ei kasutanud ``print`` käsku. Kas see tähendab, et ka funktsioon ``sqrt`` kuvab vastuse ekraanile? Ei, tegelikult kuvab Pythoni käsurida ``sqrt`` käest saadud vastuse ekraanile omal algatusel, ``sqrt`` ei tea sellest midagi. 

.. topic:: Harjutus. Kuu nimed
    :class: exercise
    :name: kuu_nime_funktsioon
    
    .. include:: exercises/kuu_nime_funktsioon.py
        :start-after: """
        :end-before: """  

    

Harjutus. Kahest suurim => kolmest suurim
-----------------------------------------

.. note::

    Vahel öeldakse, et laiskus on programmeerija puhul voorus. Sellega mõeldakse tegelikult seda, et hea programmeerija otsib alati võimalusi, kuidas mingi uue koodi kirjutamise asemel delegeerida võimalikult palju tööd juba olemasolevale koodile. Käesolev harjutus üritab seda mõtteviisi propageerida.

Kõigepealt defineeri funktsioon ``kahest_suurim``, mis tagastab kahest argumendiks antud arvust suurima. 

Seejärel küsi programmi põhiosas kasutajalt *kolm* arvu, ning kuva ekraanile neist suurim. Proovi seejuures delegeerida võimalikult palju tööd äsja loodud funktsioonile.

.. hint::

    ``kahest_suurim(a, kahest_suurim(b, c))``
        



``return`` lõpetab funktsiooni töö
----------------------------------
Senistes näidetes oli ``return``-lause funktsiooni kehas kõige viimane lause (või siis viimane lause ``if``-lause harus). Tegelikult ei pea ``return`` olema tingimata funktsiooni lõpus. Järgnevas absoluutväärtuse arvutamise funktsiooni näites kasutatakse ``return``-i kahes kohas -- funktsiooni lõpus ja tingimuslause sees:

.. sourcecode:: py3

    def absoluut(x):
        if x < 0:
            return -x
        
        return x

Kumb neist ``return``-idest siis ikkagi kehtib? Sellele vastamiseks peame teadma, et ``return`` lause käivitamine lõpetab alati funktsiooni töö. Seega, kui kutsume antud funktsiooni välja negatiivse argumendiga, siis käivitub esimene ``return`` ja ``if``-lausele järgnevat rida üldse ei vaadatagi. Kui aga ``if`` lause tingimus osutub vääraks, siis ``if``-lause keha ei vaadata ja Python jätkab sellega, mis tuleb peale ``if``-lauset (s.o. teine ``return```).

Selline võimalus kasutada ``return``-i funktsiooni keskel ei ole tegelikult eriti oluline -- alati saab funktsiooni panna kirja nii, et seal on täpselt üks ``return`` lause ja see paikneb funktsiooni lõpus.

.. note::

    ``return``-lausest on olemas ka variatsioon, kus avaldise osa on hoopis ära jäetud, st. kogu lause koosneb ainult võtmesõnast ``return``. Seda varianti kasutatakse siis, kui tahetakse funktsiooni töö lõpetada ilma mingit väärtust tagastamata.



