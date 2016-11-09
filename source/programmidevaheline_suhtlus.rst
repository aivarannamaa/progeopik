***************************
Programmidevaheline suhtlus
***************************

Ükski programm pole saar -- alati sõltub sinu poolt kirjutatud programmikood mingist koodist, mis on kellegi teise poolt kirjutatud. Kõige selgemalt viitavad sellele ``import``-laused, aga ka ilma nendeta sõltub su programm Pythoni sisseehitatud funktsioonidest ja virtuaalmasina koodist. Sellest hoolimata moodustub selliste sõltuvuste puhul programmi käivitamisel suhteliselt ühtne tervik -- **operatsioonisüsteemi protsess**, mille erinevad komponendid jagavad sama mälu ning saavad vastastikku funktsioone välja kutsuda.

Selles peatükis vaatame kahte viisi, kuidas panna omavahel suhtlema programme, mis elavad **erinevates protsessides** ja võivad olla kirjutatud erinevates programmeerimiskeeltes. Alamprotsesside skeem on tehniliselt väga lihtne, aga toimib vaid ühe masina piires. Pistikute kasutamisel võivad programmid asuda ka eri arvutites, aga nende kasutamisel peab rohkemate detailidega arvestam.  


Alamprotsessid
==============
Kui programm käivitab oma töö käigus teise programmi, siis algse programmi protsessi nimetatakse selles kontekstis *ülemprotsessiks* ja uue programmi protsessi *alamprotsessiks*. Kui tegemist on konsooliprogrammiga (st. mittegraafilise programmiga), siis saab ülemprotsess kergesti alamprotsessile sisendit anda ja selle väljundit lugeda. Teisisõnu, ülemprotsess saab alamprotsessiga käituda samamoodi nagu inimkasutaja.

Käivitamine ja väljundi lugemine
--------------------------------
Võtame esimeseks näiteks konsooliprogrammi ``ping``, mis testib, kas etteantud võrguaadress on kättesaadav. Inimkasutaja kasutaks seda programmi süsteemi käsureal umbes nii:

.. sourcecode:: none

    C:\Windows\System32>ping google.com
    
    Pinging google.com [2a00:1450:4010:c05::65] with 32 bytes of data:
    Reply from 2a00:1450:4010:c05::65: time=20ms
    Reply from 2a00:1450:4010:c05::65: time=20ms
    Reply from 2a00:1450:4010:c05::65: time=20ms
    Reply from 2a00:1450:4010:c05::65: time=20ms
    
    Ping statistics for 2a00:1450:4010:c05::65:
        Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
    Approximate round trip times in milli-seconds:
        Minimum = 20ms, Maximum = 20ms, Average = 20ms  

Esimesel real on näha kasutaja poolt sisestatud käsklus ``ping google.com`` ja peale seda tulevad programmi poolt väljastatud read. Kiri ``Sent = 4, Received = 4, Lost = 0`` näitab, et saime kõigile päringutele vastuse -- seega oli Google'i avaleht sel hetkel kättesaadav.

Pythonis on alamprogramme kõige lihtsam käivitada moodulis :py:mod:`subprocess` oleva funktsiooni :func:`run<subprocess.run>` abil. Järgnev näide demonstreerib ``ping``-i käivitamist ja selle väljundi uurimist:

.. sourcecode:: py3

    import subprocess
    
    vastus = subprocess.run(["ping", "google.com"], stdout=subprocess.PIPE,
                            universal_newlines=True)
    väljund = vastus.stdout 
    
    if "0% loss" in väljund:
        print("Aadress on kättesaadav!")
    else:
        print("Mingi jama ... Täpsem info:")
        print(väljund)

Selgitus:

* Funktsiooni ``run`` esimene argument on list, mille esimeseks elemendiks on käivitatava programmi nimi. Ülejäänud elemendid on programmi argumendid.
* ``stdout=subprocess.PIPE`` näitab, et me oleme programmi väljundist huvitatud.
* ``universal_newlines=True`` toob kaasa selle, et alamprotsessiga suhtlemine käib sõnede, mitte baidijadade abil.

.. admonition:: Harjutus 

    Muuda programmi nii, et kontrollitav aadress küsitakse kasutajalt. 

Sisendi andmine
---------------
Lisaks käsurea argumentidele ootavad osad programmid infot ka *standardsisendisse*. Standardsisend on see, kust Pythoni ``input`` käsk loeb kasutaja poolt sisestatud teksti.

Oletame, et me soovime kirjutada programmi, mis kontrollib, kas tudengi poolt kirjutatud Pythoni skript töötab õigesti. Ütleme näiteks, et tudengile anti ülesanne kirjutada programm, mis küsib kasutajalt temperatuuri celsiuse skaalal ja väljastab selle fahrenheiti skaalal ümardatuna 1 komakohani. Skripti käivitamiseks ja kontrollimiseks võiksime kirjutada sellise programmi:

.. sourcecode:: py3
    :emphasize-lines: 2,12-15

    import subprocess
    import sys
    
    testid = {
        0.0 : 32.0,
        -51 : -59.8,
        39  : 102.2
    }
    
    for celsius in testid:
        fahrenheit = testid[celsius]
        sisend = str(celsius) + "\n"
    
        vastus = subprocess.run([sys.executable, "teisendus.py"],
                                input=sisend, stdout=subprocess.PIPE,
                                universal_newlines=True)
        väljund = vastus.stdout
    
        if str(fahrenheit) not in väljund:
            print("VIGA! Sisendi", celsius, "korral ei leidnud väljundist oodatud vastust.")
        else:
            print("OK")

Selgitus:

* Pythoni skriptide käivitamiseks käsureal tuleb sisestada midagi sellist: ``python skripti_nimi.py``. Seetõttu oleksime võinud proovida ka anda ``run``-i esimeseks argumendiks ``["python", "lahendus.py"]``. Jama on selles, et kõigis süsteemides ei pruugi Python olla PATH-is ja mõnes süsteemis on Pythoni interpretaatori nimi midagi muud. Seetõttu kasutasime mooduli :py:mod:`sys` muutujat :py:data:`executable<sys.executable>`, mis annab parasjagu kasutatava Pythoni interpretaatori täpse tee ja nime.
* Testsisendi teisendasime me kõigepealt sõneks ja lisasime reavahetuse (see vastab kasutajapoolsele ENTER-i vajutusele)
 

.. admonition:: Harjutus

    Salvesta samasse kausta enda *teisendus.py* ja proovi, kas testprogramm jääb sinu lahendusega hakkama.

Vigade tuvastamine
------------------
Proovi eelmist programmi käivitada ka nii, et jooksvas kaustas pole testitavat skripti. Nagu näed, jätab meie testprogramm siis mulje, et skript leidus, aga töötas valesti. Põhjus on selles, et alamprotsessis juhtuvad vead (antud juhul skripti puudumine) ei tekita viga ülemprotsessis.

Kui soovime saada lihtsalt teada, kas alamprotsess jõudis õnnelikult lõpule või mitte, siis piisab, kui uurida funktsiooni ``run`` poolt tagastatud objekti attribuuti :py:attr:`returncode<subprocess.CompletedProcess.returncode>` -- kui see on ``0``, siis on kõik korras, kõik muud väärtused on veakoodid.

Kui tahame lisaks näha ka alamprotsessis antud veateateid, siis peame programmi käivitamisel ütlema, et oleme ka veavoost huvitatud (tavaline väljund ja veateated pannakse üldiselt erinevatesse voogudesse):

.. sourcecode:: py3
    :emphasize-lines: 15,18-22

    import subprocess
    import sys
    
    testnäited = {
        0.0 : 32.0,
        -51 : -59.8,
        39  : 102.2
    }
    
    for celsius in testnäited:
        fahrenheit = testnäited[celsius]
        sisend = str(celsius) + "\n"
    
        vastus = subprocess.run([sys.executable, "lahendus.py"],
                                input=sisend, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                universal_newlines=True)
        väljund = vastus.stdout
    
        if vastus.returncode != 0:
            print("VIGA! Sisendi", celsius, "korral ebaõnnestus programmi käivitamine.",
                  "Veakood oli", vastus.returncode, "ja veavoo sisu oli järgmine:\n",
                  vastus.stderr)
        elif str(fahrenheit) not in väljund:
            print("VIGA! Sisendi", celsius, "korral ei leidnud väljundist oodatud vastust.")
        else:
            print("OK")


  
Klient-server skeem ja pistikud
===============================
Ülem- ja alamprotsessi skeem on lihtne, aga võimaluste poolest üpris piiratud -- kui me tahame teise programmi teenuseid kasutada, siis tuleb see igal kasutuskorral uuesti käivitada ja ta peab jooksma samas masinas.

Paindlikum lahendus on klient-server skeem, kus üks programm -- server e teenindaja -- on programmeeritud selliselt, et ta suudaks oma protsessi eluea jooksul abi pakkuda mitmele programmile -- kliendile. Selline lahendus võib teha süsteemi kiiremaks (programmi käivitamisele ei pea iga pöördumise korral aega kulutama) ja paindlikumaks (ühe pöördumise käigus kogutud infot saab kergesti ära kasutada teise pöördumise juures. Klient-server lahendused lubavad harilikult ka kliendi ja serveri paigutada eri masinatesse.

Kõige olulisem näide klient-server skeemist on brauser-veebiserver, kus üks veebiserveri protsess suudab oma eluaja jooksul teenindada mitut klienti (brauserit), kusjuures klientprotsess asub harilikult teises masinas.

Klient-server süsteemis moodustatakse harilikult kliendi ja serveri vahel suhtluskanal, mille otspunkte nimetatakse **pistikuteks** (ing k *sockets*). Kõikides levinud programmeerimiskeeltes on vahendid pistikute loomiseks ja nende kaudu suhtlemise korraldamiseks. Pythonis asub kõik vajalik standardteegi moodulis :py:mod:`socket`.

Server
------
Vaatame kõigepealt ühte lihtsat Pythonis kirjutatud serverit:

.. sourcecode:: py3

    # serverprogramm
    import socket
    import time
    
    # Paneme serveri kuulama porti 7482 (loodame, et see pole juba kasutuses).
    # "localhost" tähendab, et esialgu aktsepteerime vaid samast arvutist
    # tulevaid ühendusi.
    serveri_aadress=("localhost", 7842)
    kuulamise_pistik = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    kuulamise_pistik.bind(serveri_aadress)
    kuulamise_pistik.listen()
    
    # Kliendi teenindamise kood on lõpmatus tsüklis, kuna me tahame 
    # peale ühe kliendiga lõpetamist olla valmis järgmise kliendi jaoks.
    i = 1
    while True:
        print("Hakkan klienti ootama")
        suhtlemise_pistik, kliendi_aadress = kuulamise_pistik.accept()
        print("Sain just ühenduse kliendiga nr.", i)
        teade = "Tere, klient nr. " + str(i) + "! Kell on " + time.strftime("%H:%M:%S")
        suhtlemise_pistik.sendall(teade.encode("UTF-8"))
        print("Saatsin talle sellise teate:", teade)
        suhtlemise_pistik.close()
        i += 1

Serverites kasutatakse kahte tüüpi pistikuid: *kuulamispistikud* ja *suhtlemispistikud*. Antud näites luuakse funktsiooniga :py:func:`socket<socket.socket>` kõigepealt pistik, millele seejärel antakse meetodite :py:meth:`bind<socket.socket.bind>` ja :py:meth:`listen<socket.socket.listen>` abil **kuulamispistiku roll**.

.. admonition:: Serveri aadress

    Mida tähendab antud kontekstis serveri aadress? Koodist on näha, et see koosneb kahest komponendist -- hosti nimest ja pordi numbrist. Nime ``localhost`` tuleks kasutada siis, kui tahetatakse teendindada vaid samas arvutis olevaid kliente. Võrguklientide lubamiseks tuleb sinna panna arvuti nimi või IP-aadress. Selle teadasaamiseks võib kasutada funktsiooni :py:func:`socket.gethostname`.
    
    Kui mingi arvuti poole saaks pöörduda vaid IP-aadressi või hosti nime kaudu, siis saaks selles arvutis joosta vaid üks server. Selle probleemi lahendamiseks ongi serveri aadressi lisakomponendiks võetud üks number -- *pordi number*, mis eristab seda serverit teistest samas masinas jooksvatest serveritest.
    
    Numbrid, mis on väiksemad kui 1024, on reserveeritud kindlat tüüp serverite jaoks (näiteks veebiserverid kuulavad tavaliselt porti 80), seetõttu valisime oma näitesse ühe suurema numbri, mida ükski tuntud programm `ei paista kasutavat <https://en.wikipedia.org/wiki/List_of_TCP_and_UDP_port_numbers>`_.


Kui käivitad ülaltoodud programmi, siis näed, et programm jookseb kuni :py:meth:`accept<socket.socket.accept>` meetodi väljakutseni ja jääb siis ootele. Selleks, et server sellest kohast edasi jõuaks, peab mingi programm (st. klient) ühenduma porti 7482. 
Kui see juhtub, siis tagastatakse lisaks kliendi aadressile üks uus pistik -- **suhtlemispistik**, mille abil saab server kliendiga suhelda.

Antud näites seisneb suhtlus selles, et server saadab meetodi :py:meth:`sendall<socket.socket.sendall>` abil kliendile lihtsalt ühe teate. Kuna pistikuid kasutades käib suhtlus baitides, mitte sümbolites, siis teisendatakse teate tekst eelnevalt meetodiga :py:meth:`encode<str.encode>` baidijadaks (st. tüübiks ``bytes``).

.. admonition:: Terminoloogia

    Ametlikud terminid, mida professionaalid *kuulamispistiku* ja *suhtlemispistiku* asemel tegelikult kasutavad, on *serverpistik* (*server socket*) ja *klientpistik* (*client socket*). Need terminid aga pole paljude arvates hästi õnnestunud ja võivad tekitada segadust. Seetõttu räägime siin *kuulamispistikutest* ja *suhtlemispistikutest*.

Klient
------
Kust aga võtta klientprogramm, mis ühenduks näidatud porti? Me kirjutame selle ise:

.. sourcecode:: py3

    # klientprogramm
    import socket
    
    serveri_aadress=("localhost", 7842)
    suhtlemise_pistik = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    suhtlemise_pistik.connect(serveri_aadress)
    vastus = suhtlemise_pistik.recv(1024)
    print("Sain serverilt sellise vastuse:", vastus.decode("UTF-8"))

Siin luuakse jälle funktsiooni :py:func:`socket<socket.socket>` abil pistik, aga ``bind`` ja ``listen`` asemel kutsutakse välja meetod :py:meth:`connect<socket.socket.connect>`, millega määratakse sellele pistikule suhtluspistiku roll. Suhtluspistikust loetakse meetodi :py:meth:`recv<socket.socket.recv>` (lühend sõnast *receive*) abil mingi hulk baite (argument 1024 näitab, et ei soovita lugeda rohkem kui 1024 baiti), mis teisendatakse :py:meth:`decode<bytes.decode>` abil sõneks.

Kui sa nüüd käivitad klientprogrammi nii, et samal ajal serverprogramm käib, siis peaksid väljunditest nägema, et server sai oma kliendi kätte, saatis sõnumi ja jäi uut klienti ootama ning klient sai oma sõnumi kätte ja lõpetas töö.

.. admonition:: Kuidas käivitada mitut Pythoni programmi korraga?

    Mõni IDE-de (nt Thonny) lubab käivitada vaid ühte programm korraga -- teise programmi käivitamisel katkestatakse esimene programm. Sel puhul tuleks võtta kasutusele kaks IDE akent.
    
    Thonny puhul saab mitut akent lubada, kui valid Tools menüüst Options => General ja eemaldad linnukese valiku "Allow only single Thonny instance" eest). Alternatiivina võid installida endale eraldi `ametliku Pythoni distributsiooni <https://www.python.org/downloads/>`_, ning kasutada teise akna asemel sealset IDLE programmi.


``send`` ja ``recv``
====================

Kommentaarid
============
.. disqus::
    :disqus_identifier: programmidevaheline_suhtlus