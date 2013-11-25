*********************
Tehnilised teemad
*********************

Python 2 vs. Python 3
----------------------
Kuigi antud kursuses kasutame ainult Python 3-e, on paljud tuntud Pythoni programmid ja teegid kirjutatud Python 2-s. Täpsemat infot Python 3 ja Python 2 erinevuste kohta leiab aadressilt http://docs.python.org/release/3.0.1/whatsnew/3.0.html, aga siin toome välja mõned olulisemad punktid:

* Python 2-s toimib operaator ``/`` pisut teisiti -- kui mõlemad operandid on täisarvud, siis teostatakse täisarvuline jagamine (nii nagu ``//`` puhul Python 3-s). Kui soovid Python 2-s teha täisarvudega "tavalist" jagamist (`3 / 2 = 1,5`), siis tuleb vähemalt üks operandidest teha murdarvuks, nt. ``3 / 2.0`` või ``x / float(y)``.
* Pythoni 2-s kasutatakse kahte erinevat täisarvutüüpi: `int` tähistab seal 32-bitiseid täisarve ning `long` tähistab piiramata suurusega täisarve. Tüüp `int` Python 3-s vastab tüübile `long` Python 2-s.
* Python 2-s võib ``print`` käsu argumendi anda ilma sulgudeta, nt. ``print "tere"``
* Python 2-s üritab ``input`` käsk sisestatud teksti tõlgendada avaldisena (nt. arvu või muutujana). Teksti sisestamiseks on seal eraldi käsk ``raw_input``.

Pythoni programmi pakendamine *exe*-failiks
-------------------------------------------
Nõue, et Pythoni programmide käivitamiseks peab süsteemi olema paigaldatud Pythoni interpretaator, võib olla mõnikord tülikas, näiteks, kui soovid oma programmi jagada mõne sõbraga, kes arvutitest palju ei taipa.

Õnneks on loodud vahendeid, mis pakendavad Pythoni programmi koos selle käivitamiseks vajaliku infrastruktuuriga ühte *jooksutatavasse* (ing. k. *executable*) faili (e. `exe`-faili). Taolist faili saab topeltklõpsuga käivitada ka süsteemides, kus Pythonit pole paigaldatud. Tuleb vaid arvestada, et saadud `exe`-fail on mõne megabaidi suurune ka siis, kui programm on "Tere maailm!".

Taolistest pakendajatest tundub hetkel kõige parem *cx_Freeze*. Selle allalaadimiseks ja kasutusjuhiste lugemiseks mine aadressile http://cx-freeze.sourceforge.net/.

