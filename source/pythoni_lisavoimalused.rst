Lisa. Pythoni lisavõimalused
==============================


Tingimusavaldis
---------------
Lisaks ``if``-*lausele* on Pythonis olemas ka ``if``-*avaldis* e. *tingimusavaldis*. Selle olemust on kõige lihtsam selgitada näitega:

.. sourcecode:: py3

    >>> a = 1
    >>> b = 2
    >>> 'suurem' if a > b else 'väiksem'
    'väiksem'

Ka ``if``-avaldise juures kasutatakse võtmesõnu ``if`` ja ``else``, aga nende paigutus on erinev -- tõesele tingumusele vastav haru kirjutatakse ``if``-i ette ja väärale tingimusele vastav haru kirjutatakse ``else`` järele, koolonit ega treppimist ei kasutata. Oluline on veel see, et erinevalt tingimuslausest, ei käi tingimusavaldise harudesse mitte laused vaid avaldised. Tingimusavaldise väärtus võetakse ühest või teisest harust, vastavalt tingimusele. See asjaolu tingib ka selle, et mõlemad harud peavad olema antud.

Toome siinkohal veel ühe näite tingimusavaldise kasutamise kohta:

.. sourcecode:: py3

    def neto(bruto):
        return bruto if bruto <= 144 else (bruto - 144) * 0.79 + 144

Tingimusavaldise asemel saab alati kasutada tingimuslauset ...
    
.. sourcecode:: py3

    def neto(bruto):
        if bruto <= 144:
            vastus = bruto
        else:
            vastus = (bruto - 144) * 0.79 + 144
            
        return vastus

... aga mõnikord saab tingimusavaldisega oma idee lihtsalt kompaktsemalt kirja panna.


.. note:: 

    Ära aja segamini ka tingimusavaldist ja loogilist avaldist. Loogiline avaldis on avaldis, mille tüüp on ``bool``. Tingimusavaldis on avaldis, milles on kasutatud äsja tutvustatud valikuskeemi, tingimusavaldise tüüp tavaliselt *ei ole* ``bool``.

.. note::

    Kui sulle siiski tundub, et tingimusavaldis teeb sinu jaoks asjad liiga segaseks, siis võid seda rahumeeli ignoreerida. Alati saab hakkama ka ainult tingimuslausega. Mitmes populaarses programmeerimiskeeles isegi pole tingimusavaldist.
