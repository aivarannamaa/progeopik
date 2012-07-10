*IV. Kontrolltöö, 19.-23. september*
====================================
 
Kontrolltöös on 2 ülesannet, mis nõuavad I-III arvutipraktikumi teemade valdamist.

Seda kontrolltööd ei ole võimalik hiljem järgi teha. Kui te ei saa enda praktikumi ajal kohale tulla, siis uurige eelnevalt, kas saate teha kontrolltöö koos mõne teise rühmaga.

Teemad
------
* operatsioonid arvude ja sõnedega
* muutujad
* sisend ja väljund
* tingimuslause
* funktsioonid

NB! Esimene kontrolltöö on oluline, kuna antud teemad on aluseks kõigile järgnevatele teemadele.



Üldised nõuanded
----------------
Enne kontrolltööd:
    * Kui teil on mõned ülesanded I-III praktikumidest jäänud lahendamata, siis tehke see töö tagantjärgi ära.
    * Kui te ei tunne ennast mingi teema osas päris kindlalt, siis lahendage ka vastavad õpikuülesanded.
    * Kui miski jääb ikka segaseks, siis küsige abi praktikumijuhendajalt või kaaslastelt.

Kontrolltöö ajal:
    * **Lugege ülesanded mõttega läbi!**
    * Ärge üritage konkreetse ülesande lahendamisel kasutada kõike, mida te programmeerimisest teate. Näiteks, kui ülesande tekstis pole nõutud kasutajalt sisendi küsimist, siis järelikult pole selle ülesande lahenduses tarvis ``input`` funktsiooni kasutada.
    * Kui te ei oska ülesannet kohe algsel kujul lahendada siis lihtsustage seda, lahendage lihtsustatud variant ning kirjutage programmi vastav kommentaar. Lisaks on soovitav ära märkida ka see aspekt, mille taha te toppama jäite -- on suur võimalus, et selle kirjapanekul tuleb teile pähe õige lahendusidee.
    
Sisulised nõuanded
------------------
* Kui ülesandes mainitakse funktsiooni argumente või parameetreid, siis ärge ajage seda segamini kasutajalt andmete küsimisega (vt. :ref:`param-vs-input`). 
* Kui ülesandes öeldakse, et funktsioon peab midagi tagastama, siis ärge ajage seda segamini ``print`` funktsiooniga (vt. :ref:`return-vs-print`)
* Lugege tähelepanelikult, milline osa ülesandest käib funktsiooni definitsiooni kohta ja milline osa käib programmi "põhiosa" kohta. Näiteks, kui ülesande tekstis mainitakse kasutajalt andmete küsimist, siis see ei tähenda tingimata, et ``input`` käsku tuleks kasutada funktsiooni definitsioonis.
* Ärge ajage segamini sõneliteraali (jutumärkide või ülakomade vahel) ja muutuja nime (alati ilma jutumärkide/ülakomadeta). Seda probleemi demonstreerib järgnev programm:

  .. sourcecode:: py3
  
        nimi = input('Sisesta oma nimi: ')
        print('Tere ' + 'nimi')  # probleem! Alati kuvatakse tekst 'Tere nimi'
  
  Õige oleks nii: 
  
  .. sourcecode:: py3
  
        nimi = input('Sisesta oma nimi: ')
        print('Tere ' + nimi)    # nüüd saab Python õieti aru, et pidasite silmas muutujat
  
        
* Veenduge, et te teate, kuidas toimub muutujate kasutamine avaldistes (tehetes). Võib tekkida ekslik mulje, et nt. avaldis ``int(s)`` teisendab muutuja ``s`` täisarvuks. Tegelikult luuakse selle avaldisega hoopis uus täisarvuline väärtus aga muutuja ``s`` väärtus jääb samaks (vt. :ref:`operatsioonid-muutujatega`).
* Muutujate olemuse selgitamiseks lisati II praktikumi materjali uus lõik: :ref:`milleks-muutujad`
* ``import``-laused tuleks panna programmi algusesse. See pole Pythoni poolt range nõue, kuid oluline on see, et ``import``-lauset *ei saa* panna funktsiooni definitsiooni sisse.

Veaotsing
~~~~~~~~~
* Kontrollige, kas iga alustava sulu jaoks on olemas ka **lõpetav sulg**
* Kontrollige, kas muutujate või funktsioonide **nimed on õigesti kirjutatud**
* Kontrollige, kas funktsiooni definitsiooni päises ja tingimuslause tingimuse järel on olemas **koolon**
* Kontrollige, kas teil on **treppimine** (st. taandread) paigas
* Kontrollige, kas funktsiooni väljakutsel on **funktsiooni nime järel sulud** (olgu argumentidega või ilma)
* Kui programm annab vale tulemuse, siis **kuvage ekraanile vahetulemused**, et saada aru, millises kohas läks arvutus valeks.

Kontrolltöö korraldus
---------------------
Kummagi ülesande lahendus tuleb vormistada eraldi programmina (st. eraldi failides). Failid tuleb laadida Moodle'isse ning saata ka oma rühma juhendaja e-mailile.

Kontrolltöö ajal võib kasutada kaasavõetud materjale ja internetti. *Suhtlemine (sh. interneti teel) ei ole lubatud* (aga loomulikult võib küsida juhendajalt selgitust, kui ülesande mõte jääb segaseks). Aega on 45 minutit.