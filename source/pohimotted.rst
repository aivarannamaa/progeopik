IX. Abstraktsem kokkuvõte senisest
==================================
* üldpõhimõtted
* süntaksidiagrammid
* ...



**Ülesanne 1.** Dokumentideta võõras linnas
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Kujutle end võõras linnas välisüliõpilanena. Saabudes ühiselamu juurde avastad, et ühiselamu võti, ID-kaart ja mobiiltelefon on kadunud. Kuidas lahendada olukord?

Meie igapäevaelus tuleb meil ette suuri ja väikesi ülesandeid. Mõned on lihtsad lahendada, teiste lahendamine pöörab kogu elu pahupidi (arst avastab sinu lähedasel üliharva esineva ravimatu haiguse). Mõnedele ülesannetele on olemas standardvastused, teiste korral tuleb neid alles hakata otsima. Mõned probleemid tunduvad huvitavana, mõned mitte.  
Ülesanded varieeruvad oma olemuselt matemaatilistest kuni filosoofilisteni (Mis on elu mõte?). Arvutiteaduses me tegeleme probleemidega, mille lahendust saab esitada algoritmina. 

*Algoritmiks* nimetatakse probleemi lahendamiseks vajalikku instruktsioonide hulka, mida on võimalik tõlkida arvuti jaoks arusaadavale kujule (programm) ja  mida täidab arvuti. 

Pöördume tagasi ülesande 1 juurde. Siin on ülesande püstitus puudulik. Tekib palju küsimusi, millele pole vastuseid: Kuhu need asjad kadusid? Kas need kadusid korraga? Kas need kadusid teel koju? Kas nad jäid ülikooli mõnda auditooriumi? 

Selliseid küsimusi saab esitada veel ja lahendust pole võimalik üheselt määrata.    

**Ülesanne 2.** Ruut ja ring
~~~~~~~~~~~~~~~~~~~~~~~~~~~~


Ringi sisse on joonistatud ruut, mille külje pikkus on a. Leida ringi pindala. 

.. image:: _static/l04_fig1.gif

Siin on tegemist täpselt defineeritud geomeetriaülesandega. Peale ülesandest arusaamist on vaja lahendusplaani. On vaja välja selgitada sisend (ristküliku külg) ja väljund (ringi pindala) ja kasutada sobivat tähistust.  Edasi on vaja välja selgitada seos sisendi ja väljundi vahel, mis viib lahenduseni. See võib sisaldada vahepealsete tulemuste arvutamist, nt ristküliku diagonaali arvutamist. On vaja kasutada tasandilise geomeetria põhiteadmisi (antud juhul Pythagorase teoreemi). Täiendame joonist 

.. image:: _static/l04_fig2.gif

ja esitame lahenduse kahe sammuna:

.. centered::
    :math:`d=\sqrt{a^2+a^2}=\sqrt{2}a`
    :math:`S=\frac {\pi d^2}{4}= \frac {\pi a^2}{2}`

**Ülesanne 3.** Hundi, kitse ja kapsa üle jõe viimine 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Mees peab ületama jõe paadiga, millesse mahub peale tema ainult üks kaaslane. Ta peab üle jõe viima hundi, kitse ja kapsapea. Mees peab tegutsema nii, et samal ajal, kui ta ise on paadiga jõel, ei sööks hunt ära kitse ega kits kapsapead. 

Seda tüüpi ülesanne sisaldab loogikat. Tulemuseks ei ole arvutatav väärtus nagu ülesandes 2, vaid rida käike, mis esitavad üleminekut algseisundist (kõik tegelased on ühel pool jõge) lõppseisundisse (kõik tegelased on teisel pool jõge). 

.. note::
   Leida ülesandele vähemalt üks lahendus.

**Ülesanne 4.** 
~~~~~~~~~~~~~~~
Joonisel on esitatud Pascal'i arvude kolmnurk

.. image:: _static/l04_fig4.gif

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
Toodud näited illustreerivad olukordi, mis tekivad ülesannete lahendamisel. 


Ülesande lahendamise protsess (problem solving)  
-----------------------------------------------
Ülesande lahendamise arvutil võib jagada järgmisteks etappideks:

1. Algoritmi koostamine ja esitamine.
2. Programmi koostamine mingis konkreetses programmeerimiskeeles.
3. Programmi sisestamine arvutisse.
4. Programmi testimine ja silumine.
5. Programmi käivitamine arvutis, andmete sisestamine ja tulemuse saamine arvutist.


.. index::
    single: algoritm
    
.. _algoritm:    

Algoritm
--------

Mõiste *‘algoritm’* on tuletatud 9. sajandi Pärsia matemaatiku Mohammed al-Khowarizmi nimest. Al-Khowarizmi on Algorismus (ladina keeles) - algorithm.

Esitame nüüd algoritmile täpsema definitsiooni.

**Algoritm**  on  täpselt defineeritud (arvutuslik) protseduur, mis koosneb instruktsioonide hulgast, mis saab sisendina ette mingi väärtuse või väärtuste hulga ja leiab väljundiks mingi väärtuse või väärtuste hulga. Teiste sõnadega, algoritm on protseduur, mis võtab andmed ja manipuleerib nendega, järgides ettekirjutatud samme ja leiab otsitavad väärtused.

.. image:: _static/l04_fig8.gif 

Kokkuvõtvalt, algoritm on arvutispetsialistide kõnepruugis lihtsalt protseduur. Erinevate elukutsete inimestel on erinev vorm oma töövoost ja nad nimetavad seda erinevalt. Näiteks kokk järgib protseduuri, mida nimetatakse  retseptiks. Retsept kirjeldab algoritmi, mis teisendab rea sammude abil toiduained (sisend) mingiks toiduks (väljund). Algoritm hõlmab lahenduse kogu loogikat. Seega ülesande lahendamine jaotub kaheks etapiks:

* algoritmi koostamine, mis lahendaks ülesande,
* algoritmi teisendamine programmiks.

Viimast protsessi nimetatakse programmeerimiseks ja see protsess on suhteliselt lihtsam, sest kogu loogika on juba olemas ja tuleb lihtsalt järgida kasutatava programmeerimiskeele süntaksit. Esimene etapp võib olla komistuskiviks paljudele ja seda kahel põhjusel:

* esitatakse väljakutse vaimsetele võimetele (mõtlemisele), et leida õige lahendus.
* see nõuab võimet selgesti väljendada lahenduskäik täpselt samm-sammuliste isntruktsioonidena.

Teist oskust omandatakse ja täiustatakse pidevalt läbi praktika. 
   
.. index::
    single: algoritmi omadused


Algoritmi omadused
------------------
Algoritmil on neli olulist omadust:

1. Algoritmi iga samm peab olema *täpne*, st olema ühetähenduslik.
2. Algoritm peab olema *lõplik*. Vastasel juhul me ei saa probleemile lahendust.
3. Algoritm peab olema *efektiivne*, st ta peab andma probleemile korrektse vastuse.
4. Algoritm peab olema *üldine*, st ta peab lahendama ülesande iga eksemplari. Näiteks programm, mis leiab ringi pindala, peab töötama kõigi võimalike algandmete korral antud programmeerimiskeele ja arvuti korral. 

.. index::
    single: algoritmi esitus plokkskeemina
    
.. _algoritmi esitus plokkskeemina:    

Algoritmi esitus plokkskeemina
------------------------------

Algoritmi tavaliseks esitusviisiks on nn pseudokood, mis on segu loomuliku keele sõnadest, matemaatilistest märkidest ja programmeerimiskeele võtmesõnadest. 
Algoritmi saab esitada ka graafiliselt, nt plokkskeemina. Vaatleme järgnevalt plokkskeemis kasutatavaid kujundeid:

.. index::
    single: plokkskeem
    
.. _plokkskeem:    


.. image:: _static/l04_fig9.gif 

Ringi pindala
~~~~~~~~~~~~~
1. Esitame ülesande 2 lahenduse plokkskeemina:

 .. image:: _static/l04_fig20.gif 

Siin ülesande sisendiks on ruudu külje pikkus *a*. Märgime siinjuures, et jätsime vahele diagonaali arvutamise, sest ringi pindala *S* saame arvutada otse otse ruudu külje pikkuse kaudu. 
Lahendame nüüd selle ülesande arvutil, tehes läbi ka ülesande lahendamise teised etapid. 


2. Koostame programmi, kasutades programmeerimiskeelt Python:

.. sourcecode:: py3

    from math import *

    a = int(input("Sisesta külje pikkus a: "))
    S = pi*a*a/2
    print("Kui ruudu külje pikkus on " + str(a) + ", siis ringi pindala on " +  str(S))

3. Enamasti me teostame sammud 2 ja 3 korraga, st programmi koostamise käigus sisestame selle ka arvutisse.

4. Selgub, et meie programm jääb hätta siis kui kasutaja ei sisesta midagi või sisestab külje pikkuse asemel midagi muud, nt "kuus". Seega saab öelda, et antud programm töötab vaid korrektse arvulise sisendi korral, vigase sisendi korral programmi töö lõpeb veaga.   

5. Käivitame programmi konkreetse küljepikkuse jaoks ja leiame ringi pindala.  
