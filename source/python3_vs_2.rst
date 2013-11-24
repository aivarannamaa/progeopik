*********************
Python 3 vs. Python 2
*********************
Kuigi antud kursuses kasutame ainult Python 3-e, on paljud tuntud Pythoni programmid ja teegid kirjutatud Python 2-s. Täpsemat infot Python 3 ja Python 2 erinevuste kohta leiab aadressilt http://docs.python.org/release/3.0.1/whatsnew/3.0.html, aga siin toome välja mõned olulisemad punktid:

* Python 2-s toimib operaator ``/`` pisut teisiti -- kui mõlemad operandid on täisarvud, siis teostatakse täisarvuline jagamine (justnagu ``//`` puhul Python 3-s). Kui soovid Python 2-s teha täisarvudega "tavalist" jagamist (`3 / 2 = 1,5`), siis tuleb vähemalt üks operandidest teha murdarvuks, nt. ``3 / 2.0`` või ``x / float(y)``.
* Pythoni 2-s kasutatakse kahte erinevat täisarvutüüpi: `int` tähistab seal 32-bitiseid täisarve ning `long` tähistab piiramata suurusega täisarve. Tüüp `int` Python 3-s vastab tüübile `long` Python 2-s.
* Python 2-s võib ``print`` käsu argumendi anda ilma sulgudeta, nt. ``print "tere"``
* Python 2-s üritab ``input`` käsk sisestatud teksti tõlgendada avaldisena (nt. arvu või muutujana). Teksti sisestamiseks on seal eraldi käsk ``raw_input``.