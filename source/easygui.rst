*******
EasyGui
*******

(Kirjutanud Tiina Kull)

Mis on GUI? Eks ikka graafiline kasutajaliides. Tegelikult on ka IDLE graafiline kasutajaliides, kuid esialgu võibolla harjumatu sisendi ja väljundi kasutamisega. Prooviks aga minna sammukese edasi ja hakata looma selliseid programme, milles on meie oma graafiline kasutajaliides ehk siis algatuseks hakkame kasutajaga suhtlema dialoogiakna kaudu. Selleks peab kõigepealt enda arvutisse salvestama **easygui.py** mooduli. 

EasyGui installeerimine
=======================
Lae alla **easygui.py** või zip-fail, mis sisaldab **easygui.py**-d. Vali **versioon 0.96**. Seda saad teha näiteks aadressilt: http://easygui.sourceforge.net/. Mooduli peab salvestama sinna, kust Python selle ka leiaks. Kus see asub? Koolis salvesta see samasse kataloogi, kus asuvad sul ka teised Pythonis kirjutatud programmid. Hea oleks, kui see koht on eraldi kataloog sinu isiklikus kodukataloogis.

.. note:: 
    Koduarvutis oleks sul kõige mõistlikum **easygui.py** salvestada samasse kataloogi, kus on Pythoni programm ise.

Esimene programm
================
Nüüd aga tegudele. Uuri järgmist kahte koodirida ja käivita programm.

.. sourcecode:: py3

    >>> import easygui
    >>> easygui.msgbox("Oh, ja ongi graafiline kasutajaliides")

See oli väljundi esitamine kõige lihtsama dialoogiakna kaudu. Kuid ma tahaksin, et kasutajal oleks rohkem valikuid kui lihtsalt **OK**-i vajutamine. Paljude valikunuppude saamiseks kasutatakse funktsiooni **buttonbox**:

.. sourcecode:: py3

    import easygui
    nupud = ["lühikesed","keskmised","pikad"]
    vajutati = easygui.buttonbox("Kui pikad juuksed sul on?", choices = nupud)
    easygui.msgbox("Sul on "+vajutati+" juuksed!")

Kui valikuid on rohkem kui kolm, tasub kasutada variantide nimekirjaga dialoogiakent. Seda tehakse funktsiooniga **choicebox**

.. sourcecode:: py3

    import easygui
    variandid = ["polegi","luehikesed", "keskmised","pikad"]
    vajutati = easygui.choicebox("Kui pikad juuksed sul on?", choices = variandid)
    if vajutati == None:
        easygui.msgbox("Sa ei valinud midagi!")
    elif vajutati=="polegi":
        easygui.msgbox("Sul "+vajutati+" juukseid!")
    else:
        easygui.msgbox("Sul on "+vajutati+" juuksed!")

Liiga suur?
===========
Kas pole mitte `Choiceboxi` dialoogiaken mõttetult suur? Ja seda ei saa niisama väiksemaks lohistada. Eks ole tüütu?! Sinu ülesanne on see viga parandada. Kuid niisama lihtne see ei ole, natuke tuleb algkoode muutma hakata. Kõigepealt tee lahti `easygui.py` fail, just see sama, mille sa enne oma kataloogi salvestasid. Leia sealt ``def __choicebox`` lõik kasutades menüüst Edit valikut Find ja omakorda selle alt järgmised read:

.. sourcecode:: py3

    root_width = int((screen_width * 0.8))
    root_height = int((screen_height * 0.5))

Muuda 0.8 0.4-ks ja 0.5 0.25-ks ning salvesta fail `easygui.py` peale seda. Kui see kõik on tehtud, proovi eelmist juuksepikkuse ülesannet uuesti. Kas mõjus? 

Vasta, mida tahad!
==================
Kellele ei meeldi, kui variandid on eelnevalt olemas, võib lasta kasutajal ise vastus sisestada. Kui tahetakse tekstilist vastust, siis see saadakse funktsiooniga **enterbox**, ja kui tahetakse arvulist vastust, saab alati `enterboxi` tulemuse konverteerida `int` või `float` käsuga arvuks. Kuid võib kasutada ka funktsiooni **integerbox**. Neid funktsioone kasutatakse täpselt sama moodi kui eelmisi `boxe`, kuid ilma `choice` argumendita.
**Ülesanne:** Küsi kasutajalt GUI abil sulle huvipakkuv küsimus, lase vastus sisestada ja kuva vastus koos kommentaariga GUI abil ekraanile.

.. topic:: Tasub teada!

    Kui sa tahad veel teada, mida näiteks `easygui`-ga teha saab või üleüldse oleks vaja abi mõne funktsiooni või mooduli juures, siis võib lihtsalt käsureale kirjutada `help()` ning seejärel sõna või funkstioon, nt `easygui.msgbox`. Abirežiimist saab välja lihtsalt `quit` kirjutades.


Kontrollküsimused
=================
* Millise käsuga luuakse EasyGui-s lihtne teateaken?
* Kuidas küsida kasutajalt tekstilist vastust EasyGui abil?
* Kuidas saada kasutajalt täisarvuline vastus EasyGui abil?
* Kuidas saada kasutajalt reaalarvuline vastus EasyGui abil?


Ülesanne. Aadress.
==================
Kirjuta programm, mis küsib kasutajalt kõigepealt tema nime, siis tänava nime, siis maja ja/või korteri numbri, siis linna ja riigi nime ning lõpuks postiindeksi (kõik GUI abil). Tulemuse peab programm väljastama aadressi kujul, samuti GUI abil. Tulemus peaks olema midagi sellist:

.. image:: images\easygui_aadress.png

 
