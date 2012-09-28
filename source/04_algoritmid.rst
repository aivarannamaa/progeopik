4. Algoritm ja plokkskeem
==========================

Selles peatükis teeme väikese pausi uute Pythoni konstruktsioonide õppimisse ning vaatame juba läbitud teemasid veidi teise nurga alt.

Peale antud teema läbimist oskate:

    * selgitada algoritmi mõistet;
    * lihtsamate ülesannete korral esitada probleemi täpse püstituse, st välja selgitada algandmed ja nõutava tulemuse;
    * leida antud ülesande lahendamiseks kohased põhitegevused ja esitada nende täitmise järjekorra;
    * esitada lihtsamate ülesannete lahendust plokkskeemina.


Ülesanded ja nende lahendamine
--------------------------------------
Meie igapäevaelus tuleb ette suuri ja väikesi ülesandeid või probleeme. Mõned on lihtsad lahendada, teiste lahendamine pöörab kogu elu pahupidi (nt. arst avastab teie lähedasel ravimatu haiguse). Mõnedele ülesannetele on olemas standardvastused, teiste korral tuleb neid alles hakata otsima. Mõned probleemid tunduvad huvitavana, mõned mitte. Ülesanded varieeruvad oma olemuselt matemaatilistest kuni filosoofilisteni (nt. Mis on elu mõte?). 

Vaatame nüüd mõnesid ülesandeid, millega võite kokku puutuda.


Näide 1. Dokumentideta võõras linnas
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Kujutlege end võõras linnas välisüliõpilanena. Saabudes ühiselamu juurde avastate, et ühiselamu võti, ID-kaart ja mobiiltelefon on kadunud. Kuidas lahendada olukord?

.. admonition:: Kommentaar 

    Antud ülesande püstitus tekitab palju küsimusi: kuhu need asjad võisid kaduda? Kas nad kadusid korraga? Millal nad viimati olemas olid? Kas ülikooli ruumidesse pääseb veel sisse, et neid sinna otsima minna? Selliseid küsimusi saab esitada veel ja seetõttu oleks väga raske lahendust üheselt määrata. Me võiksime ju proovida formuleerida kaotatud asjade leidmiseks mingi "retsepti" aga tõenäoliselt nõuab selle situatsiooni lahendamine ka *loovust*, st. oskust toimida ettenägematus olukorras.

Näide 2. Ruut ja ring
~~~~~~~~~~~~~~~~~~~~~~~~~~~~


Ringi sisse on joonistatud ruut, mille külje pikkus on a. Leida ringi pindala. 

.. image:: images/ring_ruut1.gif

.. admonition:: Kommentaar

    Siin on tegemist täpselt defineeritud geomeetriaülesandega. Peale ülesandest arusaamist on vaja lahendusplaani. On vaja välja selgitada sisend (ristküliku külg) ja väljund (ringi pindala) ja kasutada sobivat tähistust.  Edasi on vaja välja selgitada seos sisendi ja väljundi vahel, mis viib lahenduseni. See võib sisaldada vahepealsete tulemuste arvutamist, nt ristküliku diagonaali arvutamist. On vaja kasutada tasandilise geomeetria põhiteadmisi (antud juhul Pythagorase teoreemi). Täiendame joonist 

    .. image:: images/ring_ruut2.gif

    ja esitame lahenduse kahe sammuna:

    .. centered::
        :math:`d=\sqrt{a^2+a^2}=\sqrt{2}a`
        :math:`S=\frac {\pi d^2}{4}= \frac {\pi a^2}{2}`

Näide 3. Hundi, kitse ja kapsa üle jõe viimine 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Mees peab ületama jõe paadiga, millesse mahub peale tema ainult üks kaaslane. Ta peab üle jõe viima hundi, kitse ja kapsapea. Mees peab tegutsema nii, et samal ajal, kui ta ise on paadiga jõel, ei sööks hunt ära kitse ega kits kapsapead. 

Leida ülesandele vähemalt üks lahendus.

.. admonition:: Kommentaar
    
    Seda tüüpi ülesanne sisaldab loogikat. Tulemuseks ei ole arvutatav väärtus nagu ülesandes 2, vaid rida käike, mis esitavad üleminekut algseisundist (kõik tegelased on ühel pool jõge) lõppseisundisse (kõik tegelased on teisel pool jõge). 


Näide 4. Pascal'i kolmnurk 
~~~~~~~~~~~~~~~~~~~~~~~~~~~
Joonisel on esitatud Pascal'i arvude kolmnurk

.. image:: images/l04_fig4.gif

Äärmistel kohtadel on arv 1. Ülejäänute korral on väärtuseks kahe lähima arvu summa arvule vahetult ülemisel real. Kuidas arvutada kombinatsioonide arvu *n* elemendist *k* kaupa

.. centered::
    :math:`C_{k}^n=\frac {n!(n - k)!}{k!}`
    

kus 

.. centered::
    :math:`n!=1\cdot 2 \cdot 3 \cdot \ldots \cdot n`

kasutades Pascali kolmnurka?
Kuidas on Pascali kolmnurga arvud seotud kordajatega valemis  

.. centered::
    :math:`(x + y)^n`

peale valemi lahtikirjutamist?  



.. index::
    single: algoritm
    
.. _algoritm:    

Algoritm
---------
Ülalpool toodud näited illustreerivad olukordi, mis tekivad ülesannete lahendamisel. Arvutiteaduses tegeleme me probleemidega, mille lahendust saab esitada `algoritmina`. 

**Algoritmiks** nimetatakse probleemi lahendamiseks vajalikku instruktsioonide hulka, mida *mehhaaniliselt* (st. ilma loovust rakendamata) järgides on võimalik jõuda soovitud tulemuseni. Algoritmi kohta öeldakse tihti ka lihtsalt *protseduur*.

Algoritmil on neli olulist omadust:

1. Algoritmi iga samm peab olema *täpne*, st olema ühetähenduslik.
2. Algoritm peab olema *lõplik*. Vastasel juhul me ei saa probleemile lahendust.
3. Algoritm peab olema *efektiivne*, st ta peab andma probleemile korrektse vastuse.
4. Algoritm peab olema *üldine*, st ta peab lahendama ülesande iga eksemplari. Näiteks ringi pindala leidmise algoritm peab sobima kõigi võimalike algandmete jaoks.


Algoritme kasutatakse erinevate elukutsete juures. Näiteks kokk järgib algoritmi, mida nimetatakse retseptiks. Retsept kirjeldab protsessi, mis teisendab rea sammude abil toiduained (sisend) mingiks toiduks (väljund). 
 
.. note::

    Sõna *‘algoritm’* on tuletatud 9. sajandi Pärsia matemaatiku Mohammed al-Khowarizmi nimest. Tema nime ladinapärane kuju on *Algorismus*.



Algoritm ja arvuti
~~~~~~~~~~~~~~~~~~~~~~~~
Kuna algoritmi järgimine ei nõua loovust, siis on algoritme võimalik tõlkida arvuti jaoks arusaadavale kujule (programm) ja seega saab neid vajadusel käivitada arvutil. Sellest vaatenurgast võiksime anda algoritmile ka järgneva, veidi kitsama definitsiooni:

*Algoritm on täpselt defineeritud (arvutuslik) protseduur, mis koosneb instruktsioonide hulgast, millele antakse sisendina ette mingi väärtus või väärtuste hulk ja mis leiab väljundiks mingi väärtuse või väärtuste hulga. Teiste sõnadega, algoritm on protseduur, mis võtab andmed ja manipuleerib nendega, järgides ettekirjutatud samme ja leiab otsitavad väärtused.* 

.. image:: images/l04_fig8.gif 


Algoritmi loomine
~~~~~~~~~~~~~~~~~~~~~~~~~~
Iga algoritmi saab kergesti kohandada selliseks, et tema *rakendamiseks* sobib masin. Seevastu algoritmide *loomiseks* on vaja midagi enamat.

Esimeses peatükis oli juttu programmeerimise olemusest. Sama kehtib ka algoritmide loomise juures -- tegemist on loomingulise protsessiga, kus läheb vaja samaaegselt konkreetsust (täpsust) ja üldistusvõimet (abstraktset mõtlemist). Algoritmide loomine on üks põhilisi tegevusi programmeerimise juures. Piisavalt täpselt formuleeritud algoritmi esitamine arvutiprogrammina on küllaltki lihtne, tuleb vaid jälgida vastava programmeerimiskeele sõnavara ja reegleid. 

Kuidas aga formuleerida algoritmi? Mõned ütlevad, et programmeerimine ja algoritmide loomine ongi üks ja sama. Tavapärases kõnepruugis siiski tehakse algoritmil ja programmil vahet: algoritm esitab mingi ülesande lahenduskäiku ilma tehnilistesse detailidesse laskumata (aga siiski ühetähenduslikult), programm on aga tavaliselt mõeldud mingi konkreetse masina (sh virtuaalse masina) juhtimiseks ja seetõttu võib sisaldada nüansse, mis on olulised vaid selle masina kasutamise korral.

Kaasaegsetes programmeerimiskeeltes (nt Python) ei ole masina nüanssidele eriti vaja mõelda, seetõttu kasutatakse programmeerimiskeeli juba algoritmide väljatöötamise faasis. Vahel on aga siiski mugavam panna algoritm esialgu kirja kuidagi teisiti, näiteks *pseudokoodina* (so. loomuliku keele ja matemaatiliste sümbolite segu) või mingi visuaalse *skeemina*. Järgnevalt uurimegi lähemalt ühte algoritmide skemaatilise esitamise viisi.

   


.. index::
    single: algoritmi esitus plokkskeemina
    
.. _plokkskeem:    

Plokkskeem
--------------------------------
Üks levinud graafiline notatsioon algoritmide esitamiseks on *plokkskeem*. Vaatleme järgnevalt plokkskeemis kasutatavaid kujundeid:

.. index::
    single: plokkskeem
    

.. image:: images/l04_fig9.gif 


Kartulisalati tegemise plokkskeem
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Alustame praktilisest näitest - lihtsast kartulisalati valmistamisest, mille võib esitada järgmise plokkskeemina:

.. image:: images/l05_fig1.gif

Üksi salatit valmistades on meil võimalik lisada kartuleid ühekaupa ja hapukoort ühe lusikatäie kaupa, samal ajal kontrollides, kas vajalik kogus on juba lisatud:

.. image:: images/l05_fig2.gif


Korraldame loendamist pliiatsi ja paberiga, märkides igal lisamisel paberile ühe kriipsu. Peale kartulite lisamist kustutame kriipsud paberilt, et saaks loendada hapukurkide lisamist:

.. image:: images/l05_fig3.gif

Arvutis me kasutamine loendamiseks muutujaid, hoides nendes näiteks loendamise jooksvat seisu. Loendamise algul peame loenduri seisu nullima.  


.. image:: images/l05_fig4.gif

OLetame, et meil on juba olemas käsklused (funktsioonid), mis rakendamisel annavad meile vajaliku asja või toiduaine:

* ``tühiKauss()`` annab tühja kausi, 
* ``uusHapukurk()`` annab uue hapukurgi, 
* ``uusKartul()`` annab uue kartuli, 
* ``splKoort()`` annab supilusikatäie hapukoort,
* ``noaotsagaSoola()`` annab noa otsatäie soola, 
* ``maitseSisu()`` annab tagasi soolasuse maitse *m*, mille parajust saab hiljem kontrollida. 

Samuti oletame, et me saame kasutada olemasolevaid protseduure, millele asju ette andes tehakse ära mingi töö:

* ``lisaTükeldatult(a, k)`` lisab  aine *a* tükeldatult kaussi *k*, 
* ``segaSisu(k)`` segab kausis *k* olevad ained kokku.

Kasutades neid käsklusi, saame kartulisalati tegemise esitada järgmisel kujul:
 
.. image:: images/l05_fig5.gif

Lihtsustame oma plokkskeemi selliselt, et anname uue kartuli, hapukurgi, supilusikatäie hapukoore ja noaotsatäie soola võtmise otse lisamise käsklustele, sest meil ei ole neid eraldi muutujates vaja rohkem kasutada:


.. image:: images/l05_fig6.gif


Ülesande lahendamise protsess
-----------------------------------------------
Ülesande lahendamise arvutil võib jagada järgmisteks etappideks:

    #. Algoritmi koostamine ja esitamine.
    #. Programmi koostamine mingis konkreetses programmeerimiskeeles.
    #. Programmi sisestamine arvutisse.
    #. Programmi testimine ja silumine.
    #. Programmi käivitamine arvutis, andmete sisestamine ja tulemuse saamine arvutist.

Teeme need etapid läbi ringi pindala ülesande näitel:

    #. Esitame algoritmi plokkskeemina:

        .. image:: images/l04_fig20.gif 

        Siin ülesande sisendiks on ruudu külje pikkus *a*. Märgime siinjuures, et jätsime vahele diagonaali arvutamise, sest ringi pindala *S* saame arvutada otse otse ruudu külje pikkuse kaudu. 

    #. Koostame programmi, kasutades programmeerimiskeelt Python:

        .. sourcecode:: py3

            from math import *

            a = int(input("Sisesta külje pikkus a: "))
            S = pi*a*a/2
            print("Kui ruudu külje pikkus on " + str(a) + ", siis ringi pindala on " +  str(S))

    #. Enamasti me teostame sammud 2 ja 3 korraga, st programmi koostamise käigus sisestame selle ka arvutisse.
    #. Selgub, et meie programm jääb hätta siis kui kasutaja ei sisesta midagi või sisestab külje pikkuse asemel midagi muud, nt "kuus". Seega saab öelda, et antud programm töötab vaid korrektse arvulise sisendi korral, vigase sisendi korral programmi töö lõpeb veaga.   
    #. Käivitame programmi konkreetse küljepikkuse jaoks ja leiame ringi pindala.  

Robotkilpkonn
--------------

.. image:: images/l04_fig10.gif 

Edasiseks harjutamiseks võtame appi ühe virtuaalse robotkilpkonna, mis suudab etteantud keskkonnas liikuda ja reageerida veel mõnedele lihtsatele käskudele. Oletame, et robotkilpkonn liigub ristkülikukujulisel mänguväljakul, mille mõõtmed pole teada:

 .. image:: images/l04_fig11.gif 
 
Kilpkonn oskab sooritada järgmiseid tegevusi:

 .. image:: images/l04_fig12.gif  
 
Harjutus 1. Kolm sammu edasi ja ümberpöörd
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 Robotkilpkonn asub näoga seina poole selliselt, et seinani on vähemalt 3 sammu. Kilpkonnal on vaja liikuda kolm sammu edasi ja pöörata näoga tuldud tee suunas (pöörata ümber).   

.. image:: images/l04_fig13.gif  

Lahenduse võib esitada järgmise plokkskeemina:

.. image:: images/l04_fig14.gif  

Harjutus 2. Kui võimalik, kolm sammu  edasi ja ümberpöörd 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Robotkilpkonn asub näoga seina poole ja ei ole teada, mitu sammu on seinani. Kilpkonnal on vaja liikuda kolm sammu edasi ja pöörata näoga tuldud tee suunas (pöörata ümber). Kui seinani on vähem kui kolm sammu, siis liikuda seinani ja pöörata ümber. 

.. image:: images/l04_fig15.gif  

Nüüd on lahendus juba veidi keerulisem:  

.. image:: images/l04_fig16.gif  

Harjutus 3. Ring ümber mänguväljaku 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Kilpkonn asub ruudustiku vasakus ülemises nurgas näoga paremale. Ruutude arv ei ole teada. Kilpkonnal on vaja läbi käia suurim ring ja jõuda esialgsesse positsiooni tagasi. Koostada plokkskeem.  

.. image:: images/l04_fig17.gif  

Harjutus 4. Liikumine takistusest mööda
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Kilpkonn asub ruudustiku suvalisel ruudul. Ruutude arv ei ole teada. Ruudustikul võib olla sirge vahesein, mille otsad ei ulatu ruudustiku servani. Kilpkonnal on vaja liikuda ruudustiku selle välisseinani, mille poole ta näoga on. Koostada plokkskeem.  

.. hint:: 
    Antud ülesande korral võib olla olukord, kus takistus asub roboti ees

    .. image:: images/l04_fig18.gif  

    või siis ei asu

    .. image:: images/l04_fig19.gif  

.. note:: 

    Laadides alla väikese programmi, on võimalik kilpkonna liikumist modelleerivate plokkskeemide koostamist testida ka arvuti abil: http://www.physicsbox.com/indexrobotprogen.html


.. _triibuliseks:

Harjutus 5. Põranda värvimine triibuliseks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Oletame, et kilpkonnal on lisaks veel käsk ``värvi()``, mille saamisel värvib ta selle ruudu, kus ta parasjagu asub, tumedaks. Programmi alguses asub kilpkonn juhuslikul ruudul näoga põhja suunas. Ruudustik on ristkülikukujuline, ilma takistusteta. Ruudustiku täpne suurus pole teada.

Koostage plokkskeem, mis paneb kilpkonna värvima põrandat põhja-lõuna suunas triibuliseks -- alustada tuleks lääneservast, järgmine veerg põrandaruute peab jääma värvimata, ülejärgmine tuleb jälle värvida jne.

NB! proovige programmi läbi mängida nii paaritu- kui paarisarvulise laiusega ruudustiku korral.

Olge valmis, et see plokkskeem tuleb eelmistest omajagu suurem.

.. hint::

    Ülesande lahendamiseks tuleks valida kõigepealt strateegia, kuidas robotkilpkonn liigub ruudustikul. Üheks võimaluseks on variant, kus kilpkonn värvib ühe triibu ja liigub tuldud teed tagasi. Ta kordab värvimist järgmisel värvitaval veerul (üks veerg tuleb jätta vahele, et tulemus oleks triibuline). 
    

Pykkar
-----------------------
Kui tegite eelnevate harjutuste plokkskeemid paberile, siis saite sedasi esitatud algoritme "käivitada" vaid enda peas. Nagu teada, on inimene aga ekslik ja seetõttu võisid mõned vead algoritmides jääda märkamatuks. 

Nüüd on teil võimalus teisendada oma skeemid Pythoni koodiks ja näha roboti liikumist oma ekraanil. Kõigepealt laadige alla moodul :download:`pykkar.py <downloads/pykkar.py>` ja salvestage see oma töökausta.

Nüüd salvestage samasse kausta järgnev näiteskript ja käivitage see:

.. sourcecode:: py3

    from pykkar import *
    
    # create_world võtab argumendiks mitmerealise sõne, mis esitab
    # roboti "maailma"
    # Trellid tähistavad seinu, nooleke tähistab robotit
    # (noole suund tähistab roboti suunda)
    create_world("""
    ########
    #  >   #
    #      #
    #      #
    #      #
    #      #
    ########
    """)

    samme_jäänud = 3
    while samme_jäänud > 0:
        if is_wall(): # ei lase robotil vastu seina põrgata
            break
        else:
            step() # robot liigub ühe ruudu võrra edasi
            samme_jäänud -= 1
    
    # pöörame ringi
    right()
    right()

Loodetavasti nägite programmi käivitamisel umbes sellist pilti:

.. image:: images/pykkar.png

Justnagu plokkskeemi robot, mõistab ka Pykkar liikuda ühe sammu edasi (``step()``), pöörata 90° paremale (``right()``), värvida enda all olevat ruutu (``paint()``) ning kontrollida, kas ta ees on sein (``is_wall()``). 

Antud näiteprogramm vastab umbkaudselt eespool toodud harjutusele "2. Kui võimalik, kolm sammu  edasi ja ümberpöörd" (lahendus on küll natuke üldisem). Muutke programmis roboti algset asukohta ja katsetage, kas programm toimib õieti ka siis, kui seinani on vähem, kui 3 sammu.

Harjutus 6. Plokkskeemi kohandamine Pythoni programmiks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Kirjutage nüüd eespool antud robotiülesanded ümber Pythoni programmideks, kasutades moodulit ``pykkar``.


Lisalugemist
------------

Kuna algoritmi koostamine on ülesande lahendamise kõige olulisem osa, siis on ülesannete lahendusprotsessi uuritud ka süstemaatiliselt. Üheks selle ala klassikuks võib lugeda Ungari matemaatikut George Pólyat, kes uuris ülesande lahendamise protsessi lähemalt ja avaldas oma kuulsa raamatu "Kuidas seda lahendada?". Oma raamatus toob ta välja neli etappi, millega ülesande lahendajal tuleb kokku puutuda. Esitame siinkohal tema kuulsa tsitaadi:

.. index::
    single: Pólya
    
.. _Pólya:    

George Pólya:

*Suur avastus lahendab suure probleemi, kuid väike avastus on olemas iga probleemi lahenduses. Sinu probleem võib olla tagasihoidlik, kuid kui see esitab väljakutse sinu uudishimule ja toob mängu sinu leiutaja omadused. Kui sa seda lahendad omaenda vahenditega, võid kogeda pingutust ja nautida avastuse triumfi. Sellised kogemused võivad vastuvõtlikus eas tekitada vajaduse vaimse töö järele ja jätta jälje terveks eluks.*

George Pólya selgitab oma raamatus ülesande lahendamise nelja etappi, mida soovitame ka antud kursuse ülesannete korral hoolikalt järgida. 

1. Ülesandest arusaamine
~~~~~~~~~~~~~~~~~~~~~~~~
* Mis on otsitavaks? Mis on antud? Milles seisnevad ülesande tingimused?
* Kas tingimusi on võimalik üldse rahuldada? Kas tingimused on otsitava tulemi määramiseks piisavad? Kas nende hulgas on ülearuseid? Kas tingimused on vastuolulised?
* Valmista joonis. Võta kasutusele sobiv tähistus.

2. Lahendamise idee ja sellele vastava plaani koostamine
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* Kas tead mõnd teist antud ülesandega seonduvat ülesannet?
* Vaatle otsitavat! Püüa meenutada mõnda tuntud ülesannet, milles on sama või sarnane otsitav.
* Kas on võimalik seda ülesannet ära kasutada? Kas peab sisse tooma mingi abielemendi, mis võimaldaks varem lahendatud ülesannet ära kasutada?
* Kas saab ülesannet teisiti sõnastada? Veel teisiti? Pöördu tagasi definitsiooni juurde.
* Kui sa ei suuda antud ülesannet lahendada, siis proovi lahendada kõigepealt mõni temaga seonduv ja võib-olla lihtsam ülesanne. Või üldisem ülesanne? Või erijuht? Või sarnane ülesanne? Jättes osa tingimustest kõrvale, kuivõrd on otsitav siis määratud?
* Kas kasutasid kõiki andmeid? Kas kasutasid kõiki tingimusi? Kas arvestasid kõiki ülesandes sisalduvaid mõisteid?

3. Lahendusplaani täitmine
~~~~~~~~~~~~~~~~~~~~~~~~~~
* Veendu iga sammu õigsuses.

4. Tagasivaade
~~~~~~~~~~~~~~
* Kas saad kontrollida tulemust? Kas saad kontrollida lahenduskäiku?
* Kas saad tulemust teisiti leida?
* Kas tulemus või lahenduskäik on kasutatav mõne teise ülesande korral?




