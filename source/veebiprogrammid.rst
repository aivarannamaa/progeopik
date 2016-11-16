***************
Veebiprogrammid
***************

Veebiprogramm on programm, millega saab suhelda `HTTP <https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol>`__ protokolli abil -- näiteks veebibrauserit kasutades. 

Programmidevahelise suhtluse peatükis on :ref:`näide, kus primitiivsete vahenditega pannakse kokku lihtne veebiprogramm/veebiserver <lihtne_veebiserver>`. See on küll hea võrguprogrammeerimise harjutus ning selgitab hästi HTTP põhimõtteid, aga nii madalal tasemel programmeerides kulub kahjuks enamus auru tehniliste nüansside ja protokolli järgmisele, eriti kui tahta töökindlat ja turvalist tulemust. Seetõttu on enamasti mõistlik jätta serverite kirjutamine selle ala spetsialistide hooleks ning kirjutada oma programm veidi kõrgemal abstraktsioonitasemel, kus ei pea muretsema vastuse päise formaadi, päringu parsimise jms pärast.

Selles peatükis uurimegi kuidas kirjutada programme WSGI toega veebiserverite jaoks, mis kannavad paljude tehniliste detailide eest ise hoolt.

Kõigepealt käsitleme põgusalt WSGI spetsifikatsiooni ennast, aga kuna ka see on enamus ülesannete jaoks liiga madala tasemega, siis liigume kiiresti edasi populaarse veebiraamistiku `Flask <http://flask.pocoo.org/>`__ juurde, mis peidab WSGI detailid mugavama ja sõbralikuma liidese taha.

Lõpuks tutvustame ühte mugavat võimalust oma veebiprogramm pilve peale tõsta ja kogu internetile kättesaadavaks teha.

.. note::

    Selles peatükis eeldatakse lugejalt HTTP ja HTML-i olemuse tundmist. Vajadusel vii end nende teemadega algtasemel kurssi. HTTP osas piisab esialgu :ref:`ülalpool viidatud näitest <lihtne_veebiserver>`, HTML-liga tutvumiseks soovitame `W3Schools juhendit <http://www.w3schools.com/html/>`__.


WSGI
====
`WSGI <https://en.wikipedia.org/wiki/Web_Server_Gateway_Interface>`__ on spetsifikatsioon, mis paneb paika kuidas suhtlevad omavahel WSGI toega veebiserverid ja Pythonis kirjutatud veebiprogrammid või -raamistikud. Konkreetsemalt -- kuidas veebiserver edastab veebiprogrammile päringu info ja kuidas programm edastab veebiserverile vastuse info.

Selle spetsifikatsiooni järgi peab veebiprogrammis olema teatud kujuga funktsioon, mida veebiserver iga päringu korral välja kutsub ja mille ülesandeks on koostada antud päringule sobiv vastus.

Näide
-----
Vaatame ühte lihtsat WSGI programmi. Salvesta faili *veebiprogramm.py* järgnev kood:

.. sourcecode:: py3

    # veebiprogramm.py
    import time
    
    def application(environ, start_response):
        vastuse_shabloon = """
            <html>
                <head>
                    <title>Tere!</title>
                </head>
                <body>
                    <h1>Tere, kallis klient!</h1>
                    <p>{}</p>
                </body>
            </html>"""
    
        if environ["QUERY_STRING"] == "kellaaeg":
            vastuse_keha = vastuse_shabloon.format(time.strftime("%H:%M:%S"))
        elif environ["QUERY_STRING"] == "kuupaev":
            vastuse_keha = vastuse_shabloon.format(time.strftime("%Y-%m-%d"))
        else:
            vastuse_keha = vastuse_shabloon.format("Kuidas, palun?")
    
        start_response('200 OK', [('Content-Type', 'text/html; charset=utf-8')])
        return [vastuse_keha.encode("UTF-8")]

Selle näite põhjal saab kõik olulised WSGI põhimõtted välja tuua:

* Nagu näha, ei ole programmis kusagil juttu võrgust, pistikutest, portidest ega muust taolisest -- WSGI järgi on kõik see serveri mure. Veebiprogramm peab oskama lihtsalt koostada etteantud päringule sobiva vastuse.
* WSGI funktsiooni nimeks pannakse tavaliselt ``application`` (aga võib kasutada ka muud nime. Seda peab lihtsalt serveri konfigureerimisel arvestama.)
* Funktsioonil peab olema kaks parameetrit. 
* **Esimese parameetri** väärtuseks annab veebiserver sõnastiku, mis sisaldab muuhulgas infot päringu kohta. Näiteks element võtmega ``"QUERY_STRING"`` annab selle osa URL-ist, mis jääb küsimärgist paremale. Ülejäänud elementide kohta saad lugeda `siit <http://wsgi.readthedocs.io/en/latest/definitions.html>`__.
* **Teine parameeter** on funktsioon, mida tuleb kutsuda välja vastuse päise saatmiseks. Nagu näitest näha, on sel funktsioonil kaks parameetrit -- vastuse `staatuskood <https://en.wikipedia.org/wiki/List_of_HTTP_status_codes>`__ ja päise elementide list.
* Funktsioon peab **tagastama** vastuse keha. HTTP vastuse keha on baitide jada, seepärast on antud näites sõne kodeeritud UTF-8 abil baitideks. Selleks, et veebiprogramm saaks keha mugavalt mitme jupina koostada, on lepitud kokku, et tagastusväärtus on list, mille elemendid on baidijadad, mis kokku moodustavad vastuse keha. Kuna antud näites on keha koostatud ühes jupis, siis tagastatakse üheelemendiline list. (Mõnedes WSGI näidetes  kasutatakse ``return``-i asemel ``yield``-i -- see tähendab, et autor on soovinud listi asemel tekitada `generaatori <https://jeffknupp.com/blog/2013/04/07/improve-your-python-yield-and-generators-explained/>`__.)   

Käivitamine
-----------
Ülaltoodud näite testimiseks oleks meil vaja mingit WSGI toega veebiserverit. Õnneks on Pythoni standardteegis moodul :py:mod:`wsgiref.simple_server`, mille abil saame testimiseks sobiva serveri kergesti kokku klopsida:

.. sourcecode:: py3

    # server.py
    from wsgiref.simple_server import make_server
    from veebiprogramm import application # impordime meie veebiprogrammi ...
    
    # ... ja paneme selle serveris jooksma
    server = make_server('localhost', 8080, application)
    server.serve_forever()

Käivita serveri skript veebiprogrammiga samas kaustas ja katseta oma brauseris järgnevaid aadresse:

* http://localhost:8080/
* http://localhost:8080/?kuupaev
* http://localhost:8080/?kellaaeg
* http://localhost:8080/pildid/maasikas.jpg

.. admonition:: if __name__ == "__main__"

    Võimalik, et sa oled näinud kusagil sellise struktuuriga WSGI näidet:
    
    .. sourcecode:: py3
    
        def application(environ, start_response):
            ...
        
        if __name__ == "__main__":
            from wsgiref.simple_server import make_server
            server = make_server('localhost', 8080, application)
            server.serve_forever()
    
    Sellises programmis on lihtsalt veebiprogrammi ja testserveri kood pandud kokku ühte faili. ``if __name__ == "__main__"`` tagab selle, et seda moodulit saab kasutada kahel moel:
    
    * Kui seda imporditakse, siis muutuja ``__name__`` väärtuseks on mooduli nimi (nt. ``"veebiprogramm"`` ja seetõttu serveri koodi ei käivitata.
    * Kui aga see fail käivitada Pythoni skriptina, siis ``__name__`` väärtuseks saab ``"__main__"`` ja lisaks WSGI funktsiooni defineerimisele käivitatakse ka server.

Flask
=====
TODO: http://flask.pocoo.org/

Programmi avalikustamine
========================

TODO: https://www.pythonanywhere.com


Alternatiivid
=============

``http.server``
---------------
Väga lihtsa veebiprogrammi puhul võib WSGI asemel kaaluda Pythoni standardteegis oleva mooduli :py:mod:`http.server` kasutamist. Sealsete klassidega saab kergesti luua hädapärase veebiserveri ja veebiprogrammi kombinatsiooni.

Django
------
`Django <https://www.djangoproject.com/>`__ on ilmselt kõige tuntum Pythoni veebiraamistik, mis pakub kõike seda, mida Flask pluss veel palju muud -- näiteks põhjalikku andmebaasi kasutamise tuge, programmi osade eraldamise ja taaskasutamise võimalust jne. 


Kommentaarid
============

.. disqus::
    :disqus_identifier: veebiprogrammid