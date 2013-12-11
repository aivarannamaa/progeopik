Moodulid ja skoop
*****************
.. note::

    See peatükk on senistest hoopis tehnilisem. Siiski, esimene osa "Lokaalsed ja globaalsed muutujad" kuni alamteemani "Ametlik terminoloogia: skoop" on vajalik ja jõukohane materjal kõigile.
    
    Kui sellele järgnev materjal (alates teemaga "Nimeruumid") jääb teile segaseks, siis ärge heitke veel meelt -- programmeerida saab ka ilma seda mõistmata. Samas, kui kavatsete programmeerimist tõsiselt võtta, siis on varem või hiljem ikkagi soovitav kõik selle peatüki teemad endale selgeks teha.
    
Miks hoiab Python funktsiooni sees defineeritud muutujaid ülejäänud muutujatest eraldi? Kuidas leiab Python muutuja nime põhjal muutuja väärtuse? Miks on vaja teatud funktsioone (nt. ``sin``) enne kasutamist *importida*? Mis asi ikkagi on moodul? 

Selles peatüki tegelastega olete õigupoolest juba tuttavad -- käsitleme Pythoni muutujaid, funktsioone ja mooduleid aga seda veidi teise nurga alt kui seni. Nimelt võtame me need mõisted "pulkadeks" lahti, uurime natuke ja paneme uuesti kokku, lootuses, et taoline analüüs aitab Pythoni tööpõhimõtetest paremini aru saada. Lõpuks näeme, et Pythoni tööpõhimõtted toetavad programmide loomist osade kaupa. 


Lokaalsed ja globaalsed muutujad
================================
.. note::
    
    Siin on esitatud pisut lihtsustatud mudel Pythoni muutujate haldamise süsteemist. Täpsemalt saab lugeda näiteks Pythoni ametlikust dokumentatsioonist: http://docs.python.org/3/reference/executionmodel.html#naming-and-binding
     
Nagu 4. peatükis (:ref:`lokaalsed-muutujad`) mainitud, on kõik funktsiooni definitsiooni sees kasutusele võetud muutujad **lokaalsed**, st. neid pole võimalik funktsioonist väljaspool kasutada. Taoline korraldus on mugav, kuna nii ei pea programmeerija funktsiooni kirjutamisel muretsema kellegi teise (või tema enda) poolt kusagil mujal kasutatud muutujate kogemata ülekirjutamise pärast. Kui kogu vajaminev info tuleb funktsiooni sisse parameetrite kaudu ja tulemused tagastatakse ``return`` lausega, siis võib funktsiooni kirjutamisel kogu ülejäänud programmi ära unustada ja keskenduda ainult käesolevale alamülesandele.

Samas, mõnikord on kasulik, kui me saaksime ka funktsiooni sees otse "välise maailmaga" suhelda, lugedes ja/või kirjutades funktsioonist väljaspool olevaid muutujaid e. **globaalseid muutujaid**.

.. note::

    Taoline otsesuhtlus oleks põhjendatud näiteks siis, kui välisest maailmast on vaja palju sisendeid ja nende argumentidena saatmine läheks väga tüütuks, või kui vajadus välismaailmaga suhtlemiseks ilmneb alles peale seda, kui funktsiooni on juba paljudes kohtades välja kutsutud ja uue parameetri lisamine oleks väga tülikas.

Kui meil on vaja globaalse muutuja väärtust ainult lugeda, siis pole vaja midagi erilist teha -- me lihtsalt kasutame vajaliku muutuja nime funktsiooni sees:

.. sourcecode :: py3
    
    def lekita_saladus():
        print(avalik_saladus)
        
    avalik_saladus = "Käsi peseb kätt"

    lekita_saladus()

Kui me aga üritaksime globaalse muutuja väärtust muuta, siis jääksime hätta:

.. sourcecode :: py3
        
    def muuda_saladust():
        avalik_saladus = "Hunt hunti ei murra"
    
    
    avalik_saladus = "Käsi peseb kätt"
    muuda_saladust()
    
    # kontrollime, kas saladus on muudetud
    print(avalik_saladus)

Programm kuvas meile ekraanile ikka esialgse saladuse (``"Käsi peseb kätt"``). Asi oli selles, et funktsiooni sees loob (esmakordne) omistamine vaikimisi uue lokaalse muutuja -- see, et ka funktsioonist väljaspool on sama nimega muutuja olemas, Pythonile korda ei lähe. Antud näites tekitati funktsiooni käivitamisel uus lokaalne muutuja ``avalik_saladus``, mille väärtuseks sai ``"Hunt hunti ei murra"``. Kuna lokaalne muutuja oli sama nimega nagu globaalne muutuja, siis pole meil võimalik funktsioonis ``muuda_saladus`` globaalset muutujat isegi lugeda (öeldakse, et lokaalne muutuja *varjab* samanimelise globaalse muutuja). Kuna ``print`` lause on funktsioonist väljaspool, siis tema näeb globaalset muutujat, mille väärtust pole keegi puutunud.

Selleks, et funktsiooni sees saaks globaalset muutujat muuta, tuleb selleks Pythonile soovi avaldada, märkides võtmesõnaga ``global`` funktsiooni alguses ära vastavate muutujate nimed:

.. sourcecode :: py3
    :emphasize-lines: 2
        
    def muuda_saladust():
        global avalik_saladus
        avalik_saladus = "Hunt hunti ei murra"
    
    
    avalik_saladus = "Käsi peseb kätt"
    muuda_saladust()
    
    # kontrollime, kas saladus on muudetud
    print(avalik_saladus)


Ametlik terminoloogia: *skoop*
------------------------------
Funktsiooni "sisemuse" ja "välismaailma" tähistamiseks on tegelikult olemas spetsiaalsed terminid -- **lokaalne skoop** (ing. k *local scope*) ja **globaalne skoop** (*global scope*). *Lokaalne skoop* tähistab seda *piirkonda programmi tekstis*, mis jääb mingi konkreetse funktsiooni definitsiooni sisse. Iga funktsiooni definitsioon moodustab omaette lokaalse skoobi. Kõik, mis jääb funktsioonide definitsioonidest väljapoole, on *globaalne skoop* (see väide on pisut lihtsustatud, aga praeguseks siiski piisavalt täpne).

Kui räägitakse mingist konkreetsest muutujast, siis võidakse ka öelda, et "sellel muutujal on *<lokaalne või globaalne>* skoop" (see tähendab sama mis "see muutuja on *<lokaalne või globaalne>*").

Nimeruumid
----------
Mingi funktsiooni sees kasutusele võetud (st. lokaalsete) muutujate kogumit nimetatakse selle funktsiooni **lokaalseks nimeruumiks** (*local namespace*). Kõigist mingi skripti e. mooduli globaalsest muutujatest moodustub vastava mooduli **globaalne nimeruum** (*global namespace*). Kõige tähtsamad Pythoni funktsioonid (nt. ``len``, ``str``, ``sum``) on koondatud omaette nimeruumi, mida nimetatakse **sisseehitatud nimeruumiks** (*builtin namespace*).

Nimeruumide abil haldab Python muutujaid ja nende väärtusi programmi jooksutamise ajal. Nimeruumi võib kujutada ette kaheveerulise tabelina, mis seab mingi muutuja nimele vastavusse mingi väärtuse. Näitena toome ühe lihtsa programmi ja sellele vastava globaalse nimeruumi, nagu see näeks välja programmi lõppu jõudes:

.. sourcecode:: py3
    
    x = 3
    sõna = "tere"
    x += 1

+----------+------------+
| Nimi     | Väärtus    |
+==========+============+
| x        | 4          |
+----------+------------+
| sõna     | "tere"     |
+----------+------------+

Nimeruumide kasutamine
----------------------
Sisseehitatud nimeruum luuakse Pythoni interpretaatori käivitamisel ja see püsib Pythoni mälus kuni interpretaatori sulgemiseni. 

Skripti/mooduli globaalne nimeruum luuakse skripti käivitamisel/mooduli laadimisel (st. esmakordsel importimisel) ja see püsib mälus (tavaliselt) kuni programmi sulgemiseni. Konktreetse skripti/mooduli käivitamise/laadimise alguses on tema nimeruum tühi. Uued kirjed tekivad ja olemasolevate kirjete väärtused muutuvad omistamislausete käivitamisel. Funktsioon ``globals()`` annab selle nimeruumi sisu tavalise Pythoni sõnastikuna.

Funktsiooni nimeruum luuakse igal funktsiooni väljakutsel uuesti ja see kustutakse, kui funktsioon lõpetab. Funktsiooni käivitamisel täidetakse nimeruum juba ette funktsioonis defineeritud muutujate nimedega, va. need nimed, mis on mainitud võtmesõna ``global`` järel. Väärtuste lahtrid jäetaks esialgu tühjaks. Funktsiooni täitmise käigus lokaalsesse nimeruumi enam uusi kirjeid ei teki, omistamislaused muudavad ainult olemasolevate kirjete väärtuse veergu (kui omistatakse globaalsetesse muutujatesse, siis muudetakse vastava mooduli globaalset nimeruumi).  Funktsioon ``locals()`` annab selle nimeruumi sisu sõnastikuna.

Mingis avaldises esineva muutuja väärtustamiseks kasutab Python järgnevat skeemi:

    #. kui avaldis asub funktsiooni kehas ja kui funktsiooni lokaalses nimeruumis leidub otsitav nimi, siis kasutatakse vastavat väärtust
    #. vastasel juhul otsitakse väärtust kõigepealt mooduli globaalsest nimeruumist
    #. kui globaalses nimeruumis vastet ei leidu, siis otsitakse sisseehitatud nimeruumist
    #. kui ka sisseehitatud nimeruumis vastet ei leidu, siis antakse veateade (``NameError``).

Moodulid
========
Pythoni moodulitega tutvusite juba 1. peatükis, kus öeldi, et teatud matemaatiliste funktsioonide kasutamiseks on need vaja kõigepalt ``math`` moodulist *importida*, näiteks:

.. sourcecode:: py3

    >>> from math import sqrt
    >>> sqrt(4.0)
    2.0

Teises peatükis tutvustati ``import``-lausest ka teist varianti, kus imporditi *moodul* ise ja soovitud funktsiooni kasutati koos mooduli nimega:

.. sourcecode:: py3

    >>> import math
    >>> math.sqrt(4.0)
    2.0

Tuleb välja, et just selle variandi kaudu jõuame natuke lähemale moodulite olemusele!

Hakkame näidet lähemalt uurima. Näite teine rida tundub väga sarnane mingi *meetodi* kasutamisele. Vaatame näiteks sõnemeetodi ``count`` kasutamist:

.. sourcecode:: py3

    >>> lause = "tere vana kere!"
    >>> lause.count("e")
    4
    
Mõlemal juhul on kõigepealt kirjutatud mingi nimi (vastavalt ``math`` või ``lause``), siis punkt, siis veel mingi nimi (``sqrt`` ja ``count``) ja lõpuks sulgudes mingi argument. Ilmselt juba teate, et ``lause`` on antud näites *muutuja* ning nagu iga muutuja, tähistab ta mingit *väärtust* e. *objekti* (selles peatükis kasutame mõlemaid termineid). Kas antud näidete *süntaktilise* sarnasuse järgi võib järeldada, et ka ``math`` avaldises ``math.sqrt(4.0)`` on muutuja? Kui jah, siis mis on selle muutuja väärtus?

Siiani oleme muutuja väärtust uurinud kas ``print`` käsu abil või siis käsureal. Proovime järgi:

.. sourcecode:: py3

    >>> import math
    >>> math
    <module 'math' (built-in)>
    
Käsurida andis meile vastuse -- ``math``-il on tõepoolest väärtus!

Moodul kui väärtus/objekt
-------------------------
Tuleb välja, et ``import`` lause tekitab programmi uue muutuja, mille väärtuseks on samanimelises programmifailis sisalduvate funktsioonidefinitsioonide (ja teiste definitsioonide) kogum. Kuna sõna *moodul* kasutatakse ka programmifaili tähistamiseks, siis on tavaks ``import`` lausega tekitatud väärtust nimetada *mooduli objektiks*. 

.. note::

    Erinevalt siiani nähtud väärtustest (nagu näiteks arvud või sõnastikud), paistab mooduli objekt Pythoni käsurealt vaadates väga veider (``<module 'math' (built-in)>``) -- lubatud definitsioonide kogumit pole kusagil näha. Asi on selles, et osade moodulite jaoks ei ole head viisi, kuidas neid ekraanil näida, seetõttu näidatakse vaikimisi moodulite kohta alati vaid lühike kirjeldus. 

Nagu teame, on igal Pythoni väärtusel/objektil mingi tüüp, mis määrab ära, mida sellega teha saab. Uurime järgi, mis on mooduli objekti tüüp:

.. sourcecode:: py3

    >>> import math
    >>> type(math)
    <class 'module'>
    
Saime teada, et tegemist on tüübiga ``module``. Arve saab liita ja korrutada, sõnesid saab teisendada suurtähtedeks jne. Mida saab teha ``module`` tüüpi objektiga?

Nagu mainitud, on moodul mingite definitsioonide kogum, seega võib arvata, et moodulilt saab küsida mingit definitsiooni. Nii see on -- mingi moodulis sisalduva definitsiooni kasutamiseks tuleb kirjutada moodulit tähistava muutuja nimi, punkt ja definitsiooni nimi. Seega, kui te olete mõnes oma programmis kasutanud avaldist ``math.pi``, siis meie uue terminoloogia järgi võite öelda, et küsisite mooduli objektilt ``math`` defintsiooni ``pi`` väärtust.

.. note::

    Loodetavasti juba märkasite seost mooduli objekti ning eespool kirjeldatud mooduli globaalse nimeruumi vahel. Tegemist on tõepoolest sama info kahe erineva esitusega.

Kuidas jääb aga avaldisega ``math.sqrt(4.0)``? See avaldis on veid keerulisem, sest siin on kasutatud funktsiooni definitsiooni, aga ``pi`` oli lihtsalt mingi arv. Tuleb välja, et me võime selle avaldise veel osadeks võtta:

.. sourcecode:: py3

    >>> import math
    
    >>> math.sqrt
    <built-in function sqrt>
    
    >>> type(math.sqrt)
    <class 'builtin_function_or_method'>

Nagu näha, õnnestus meil küsida definitsiooni ``sqrt`` väärtus ilma argumenti mainimata. Justnagi mooduli objekti puhul, on tegemist väärtusega, mida ei ole lihtne ekraanil näidata, sellepärast näitabki käsurida ainult lühikest kirjeldust. Oluline on see, et nii kirjeldus, kui väärtuse tüübi küsimine kinnitavad, et definitsiooni sisuks on funktsioon (nimetatakse ka *funktsiooni objekt*).

Siiani olete harjunud funktsiooni mainima ainult koos argumendiga. Samas, kui järgi mõelda, siis on täiesti loomulik, et iga funktsioon on ka *ise* olemas, konkreetsetest argumentidest sõltumatult. 

Nagu juba tavaks saanud, küsime ka funktsioonitüüpi väärtuse puhul -- mida sellega teha saab? Vastust olete juba eelnevates peatükkides kohanud -- funktsiooni saab *välja kutsuda* e. *käivitada*, kirjutades tema järele sulud ja sinna sisse 0 või rohkem argumenti. Seejuures pole oluline, kust ja kuidas me selle funktsioonitüüpi väärtuse saime. Selle demonstreerimiseks on järgnevas näites küsitud ``math`` mooduli käest mõned funktsioonid ja tehtud nendega kõikvõimalikke trikke:

.. sourcecode:: py3

    >>> import math
    
    >>> # salvestame uude muutujasse
    >>> funktsioon = math.sqrt 
    >>> funktsioon(4.0)
    2.0
    
    >>> # alamaavaldiste ümber võib panna sulge, järelikult peaks järgnev töötama:
    >>> (math.sqrt)(4.0)
    2.0
    
    >>> # proovime salvestada funktsiooni objektid järjendisse
    >>> järjend = [math.sqrt, math.sin, math.cos]
    >>> järjend[0]
    <built-in function sqrt>
    >>> järjend[0](4.0)
    2.0
    >>> järjend[1](0.5)
    0.479425538604203
    >>> järjend[2](0.5)
    0.8775825618903728    

Tänu Pythoni sellisele lähenemisele funktsioonidele saamegi väga lihtsalt öelda, mida mooduli objektiga saab teha -- sellelt saab nime järgi küsida mingit väärtust (mis peab olema eelnevalt moodulis defineeritud). See, kas antud väärtus on mingi lihtne objekt (nagu sõne või täisarv) või midagi keerulisemat (nt. funktsioon), ning kuidas seda väärtust kasutada on juba küsija mure.

.. topic:: from math import sin, cos

    Tuleb välja, et meie uute teadmiste abil on seda ``import``-lause varianti (kus imporditakse otse mooduli komponente) võimalik ümber kirjutada mooduli enda importimise kaudu. Järgnevad kaks programmilõiku on samaväärsed:
    
    .. sourcecode:: py
    
        from math import sin, cos
        ...
        
    .. sourcecode:: py
    
        import math
        sin = math.sin
        cos = math.cos
        del math # del eemaldab näidatud (so. import lause poolt tekitatud) muutuja
        ...
    

Isetehtud moodulid
------------------
Pythoni installeerimisel tuleb kaasa suur hulk nn. standardmoodule, mis paigutatakse kindlatesse kaustadesse, kust ``import``-lause nad üles leiab. Neile lisaks on aga väga lihtne luua ka oma mooduleid -- tegelikult saab igat skripti, mida te siiani olete kirjutanud, kasutada Pythoni moodulina.

Kui te tahate ühte oma moodulitest kasutada teises skriptis, siis on kõige kindlam, kui salvestate mõlemad failid samasse kausta. Salvestage järgnev näide faili nimega ``demomoodul.py``:

.. sourcecode:: py3

    eriline_arv = 42

    def korruta(x):
        return x * eriline_arv
        
    def tervita():
        print("Tervitused demomoodulist")
    

Samasse kausta salvestage (suvalise nimega) järgnev skript ja käivitage see:

.. sourcecode:: py3

    import demomoodul # mooduli nimeks saab failinimi ilma laiendita
    
    print(demomoodul.eriline_arv)
    print(demomoodul.korruta(2))
    demomoodul.tervita()

Nendes skriptides, mida te kavatsete kasutada moodulina (st. importida mõnes teises skriptis) võiks sisalduda ainult definitsioonid. Nagu näitest näha on Pythonis kaks viisi definitsioonide kirjutamiseks -- uute funktsioonide defineerimiseks kasutatakse ``def`` konstruktsiooni ja lihtsamate definitsioonide jaoks võrdusmärki. 

Mooduli sisu uurimine
---------------------
Nagu öeldud, saab mooduli objektilt küsida mingile nimele vastavat väärtust. Kas see kirjeldus meenutab teile ühte teist Pythoni andmetüüpi? Loodetavasti mäletate, et ka Pythoni sõnastikus sai mingi võtme järgi küsida sellega seotud väärtust. Moodulit võib tegelikult vaadelda justkui teatud kitsendustega sõnastikku -- võti antakse punktiga, mitte kantsulgudes ja võti peab alati olema mingi nimi.

Erinev on ka moodulis sisalduvate nimede loetlemine -- selleks tuleb kasutada funktsiooni ``dir``:

.. sourcecode:: py3

    >>> import math
    >>> dir(math)
    ['__doc__', '__name__', '__package__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2',
     'atanh', 'ceil', 'copysign', 'cos', 'cosh', 'degrees', 'e', 'erf', 'erfc', 'exp',
     'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'hypot',
     'isfinite', 'isinf', 'isnan', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'modf',
     'pi', 'pow', 'radians', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'trunc']


Objektid ja attribuudid
=======================
Me alustasime moodulite uurimist kõrvutades moodulis oleva funktsiooni ja sõnemeetodi kasutamist. Tuleb välja, et kõigil Pythoni väärtustel on sarnasus moodulitega -- neilt saab nime järgi küsida mingi nende komponendi (või aspekti) väärtust. Samuti saab kasutada ``dir`` funktsiooni tuvastamaks, milliste nimedega komponente mingil objektil on.

Proovime näiteks arvudega:

.. sourcecode:: py3

    >>> x = 1.25
    >>> dir(x)
    ['__abs__', '__add__', '__bool__', '__class__', '__delattr__', '__divmod__', '__doc__',
     '__eq__', '__float__', '__floordiv__', '__format__', '__ge__', '__getattribute__',
     '__getformat__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__int__',
     '__le__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__pos__',
     '__pow__', '__radd__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__',
     '__rfloordiv__', '__rmod__', '__rmul__', '__round__', '__rpow__', '__rsub__',
     '__rtruediv__', '__setattr__', '__setformat__', '__sizeof__', '__str__', '__sub__',
     '__subclasshook__', '__truediv__', '__trunc__', 'as_integer_ratio', 'conjugate',
     'fromhex', 'hex', 'imag', 'is_integer', 'real']
     
    >>> x.as_integer_ratio
    <built-in method as_integer_ratio of float object at 0x02C6E130>
    >>> type(x.as_integer_ratio)
    <class 'builtin_function_or_method'>
    >>> x.as_integer_ratio()
    (5, 4)
    
    >>> (2.0).is_integer()
    True
    >>> (2.1).is_integer()
    False    
    
Allkriipsudega nimesid käsitleb Python spetsiaalselt (neid kasutatakse siis kui antud väärtus esineb operaatori ees).

Kui me tahame väärtuse juures rõhutada seda, et tema "komponente" saab nime järgi küsida, siis nimetame teda **objektiks**. Vastavaid komponente nimetatakse **attribuutideks**.

Nagu näha, on nii arvudel, kui moodulitel funktsioonitüüpi attribuute. Moodulite puhul nimetatakse neid lihtsalt funktsioonideks, ülejäänud objektide juures eelistatakse terminit *meetod*. Meetodit võib võtta kui funktsiooni, mis on spetsialiseeritud ühe konkreetse objekti jaoks:

.. sourcecode:: py3

    >>> esimene = "tere"
    >>> teine = "maailm"
    
    >>> esimese_sõna_täheloendur = esimene.count
    >>> teise_sõna_täheloendur = teine.count
    
    >>> esimese_sõna_täheloendur("e")
    2
    >>> teise_sõna_täheloendur("e")
    0


Modulaarsus
===========
Paljude tänapäeva programmide taga on meeletu hulk koodi -- pole lootustki, et keegi suudaks näiteks Microsoft Wordi või Linuxi tuuma kogu koodi olulisi detaile ühekorraga hoomata. Seetõttu rakendatakse keeruliste tarkvaralahenduste loomisel juba eespool mainitud "jaga ja valitse" printsiipi -- ülesanne ja sellele vastav lahendus jagatakse osadeks, millest igaüks keskendub mingile konkreetsele lõigule koguülesandest. Kui sedasi saadud alamülesanded on ikka liiga keerulised, siis jagatakse need omakorda veel osadeks jne, kuni saadakse paraja suurusega ülesanded, mida programmeerija suudab oma peas piisava täpsusega "töödelda".

Ülesannet ei saa siiski jagada osadeks suvalisest kohast -- on oluline, et alamülesanded ja neile vastavad lahendused (st. programmiosad) sõltuksid üksteisest võimalikult vähe, vastasel juhul peab programmeerija ikkagi mõtlema mitmele ülesandele korraga. Kuigi lõpuks tuleb need suhteliselt iseseisvad programmiosad ikkagi panna koos töötama (vastasel juhul poleks tegemist ühe süsteemi komponentidega), tuleb osade arendamisel kasuks, kui me ei pea eriti ülejäänud süsteemi peale mõtlema.

Kui mingi süsteemi (nt. tarkvara) komponentidest rääkides tahetakse rõhutada just nende suhtelist sõltumatust, siis nimetatakse neid komponente üldiselt *mooduliteks*. Konkreetse programmeerimiskeele puhul võib sellel sõnal olla ka kitsam tähendus (nagu veendusite eespool Pythoni näitel). Kui süsteemi ülesehitusel on edukalt kasutatud sõltumatuid komponente, siis nimetatakse seda süsteemi *modulaarseks*. Modulaarset süsteemi saab kergemini täiendada ja muuta, kuna pole karta, et mingi väike muudatus ühes kohas võib põhjustada mingi ettenägematu probleemi kusagil mujal.

Kaks põhilist mehhanismi modulaarsuse saavutamiseks on funktsioonid ja objektid. Programmeerimiskeeled on valdavalt üles ehitatud selliselt, et see mis toimub funktsiooni sees, on selle funktsiooni siseasi -- see võimaldab vajadusel funktsiooni sisu ümber kirjutada, ilma et see põhjustaks ootamatusi ülejäänud süsteemis. See on ka põhjus, miks Python hoiab lokaalseid muutujaid teistest muutujatest eraldi. Objektid lisavad siia juurde veel võimaluse kasutada samamoodi "privaatseid" aga pikema elueaga muutujaid, millele pääsevad ligi ainult teatud hulk funktsioone ja mida neis funktsioonides on võimalik seetõttu palju muretumalt kasutada. See osa ei ole paraku Pythonis eriti hästi lahendatud.





