.. _lisapaketid:

**************************
Lisapakettide paigaldamine
**************************

Lisaks sellele, et Pythonil on mahukas standardteek, on talle loodud ka väga palju lisapakette erinevate ülesannete lahendamiseks.

.. admonition:: Miks eraldi teema?

    Lihtsatel juhtudel piisaks teise programmeerija poolt loodud moodulite kasutamiseks sellest, kui kopeerida vastavad py-failid enda skriptiga samasse kausta. Kui aga need moodulid sõltuvad kolmanda programmeerija moodulitest, siis läheb asi juba veidi tülikaks. Seetõttu on iga populaarsete programmeerimiskeele jaoks loodud mingi mehhanism, mis teeb lisapakettide publitseerimise, leidmise ja paigaldamise lihtsamaks.

Pythoni lisapaketinduse keskmeks on `PyPi <https://pypi.python.org/pypi>`__ -- Python Package Index. Tegemist on andmebaasiga, kuhu lisapakettide loojad saavad enda paketid koos kirjeldusega üles laadida ning kust pakettide kasutajad saavad pakette alla laadida ja enda arvutisse paigaldada. Pakettide loomise kohta leiad infot `Python Packaging Guide <https://packaging.python.org/>`__'ist, aga siin vaatame kuidas olemasolevaid pakette kasutada.

pip
===
``pip`` (Linuxi ja Mac-i puhul ka ``pip3``) on käsurea programm, mis oskab PyPi-st pakette alla tõmmata ja sinu arvutisse installida. Kui pakett sõltub veel mõnest paketist, siis installitakse ka see jne.

Uuemate Pythoni versioonidega (ja ka Thonnyga) on ``pip`` enamasti kaasas, seega ``pip``-i enda paigaldamise pärast ei ole sul tõenäoliselt vaja muretseda. Küll aga on vaja teada kuidas ``pip``-i käivitada.

Üldine käivitusjuhis
--------------------
OP-süsteemi käsurea avamise juhendit vaata jaotusest :ref:`python_op_systeemi_kasureal`.

Kui käsk ``pip`` on PATH-is, siis piisab uue paketi installimiseks käsust kujul ``pip install <paketi nimi>`` või ``pip3 install <paketi nimi>``  (nt. ``pip install pygame``). Vastasel juhul tuleb näidata käsu ``pip`` asukoht, nt. ``C:\Python34\Scripts\pip install pygame``.

Paketi eemaldamiseks on ``pip``-is alamkäsk ``unistall`` -- nt. ``pip uninstall pygame``.

.. admonition:: Tähelepanu mitme Pythoni installatsiooni korral!

    Erinevatele Pythoni versioonidega tulevad kaasa ka erinevad ``pip``-id. Seega, kui sul on installitud mitu Pythoni versiooni (nt. versioon 2.7 ja 3.5), siis  tuleks enne ``pip`` käsu kasutamist veenduda, et sa kasutad õiget versiooni, et installitav pakett jõuaks ikka õige interpretaatori juurde. Seda, millise interpretaatoriga käsk ``pip`` seotud on, saab kontrollida käsuga ``pip --version``. 

pip-i käivitamine Thonnys
-------------------------
Kui süsteemi käsurida avada Thonny kaudu (`Tools → Open system shell`), siis mitme interpretaatori ja PATH-i pärast muretsema ei pea, sest Thonny suudab käsurea seadistada nii, et lühikese nimega on kättesaadav õige ``pip``.


Kommentaarid
============
.. disqus::
    :disqus_identifier: lisapaketid