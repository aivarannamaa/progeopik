*Interaktsioon*
===============================
Mõned ideed, kuidas teha õpik interaktiivsemaks


Automaatne tagasiside programmidele
--------------------------------------
* TODO uuri Viopet
* tehniliselt poleks eriti keeruline ka ise teha (standard-Pythoni jooksutamine minimaalsete õigustega kasutaja all).
* Filipp Ivanovi töö (Pythoni filter) on siin asjakohane võimaldades kindlamat turvalisust ning lahendusruumi kitsendamist.

Kas arvestada tulemusi hindamisel? See võib tekitada kiusatuse petta.


Teksti märgendamine ja kommenteerimine
-----------------------------------------
Tudeng võiks saada teha teksti "enda omaks":

* sõnade highlight'imisega (nähtav talle ja õppejõududele)
* oma kokkuvõtte ja kommentaaride kirjutamisega iga teema lõpus olevasse tekstikasti.

Vaevatasuks võiks genereerida talle lehekülje, kus on tema märkused kokku võetud(?).

Lisaks võiks olla võimalus kirjutada teksti kohta avalikke kommentaare:

* parandused 
* selgitused kaastudengitele
* ...

Avalehel võiks olla viimaste kommentaaride logi. See teeks õpiku "sotsiaalsemaks" ja loodetavasti tekitaks rohkem huvi selle külastamise ja lugemise vastu.

Heaks näiteks on O'Reilly Open Feedback Publishing System, http://ofps.oreilly.com/, nt. http://ofps.oreilly.com/titles/9781449398583/chap1_id35940135.html või Scala parendamise ettepanekud Google Docs'is, nt https://docs.google.com/document/d/1NdxNxZYodPA-c4MLr33KzwzKFkzm9iW9POexT9PkJsU/edit?hl=en_US (märkused on dokumendi teises pooles).



Autentimine
~~~~~~~~~~~~~~
Isiklike täienduste tegemiseks/nägemiseks on vaja kasutaja autentida. Mõned võimalikud variandid:

* UT konto põhjal
* Google'i konto põhjal
* Facebook'i konto põhjal

"Tehtud"-linnukeste süsteem
------------------------------
Tudeng saab märkida iga ülesande juures, kas ta sai sellega hakkama või mitte (kui kasutada automaattestimist, siis ilmub see lahenduse esitamisega). See on mõeldud enesemotivatsiooni tõstimiseks, mitte hindamiseks. Materjali avalehel näeb tudeng kokkuvõtet, kui palju ülesandeid on tal lahendatud (rohelise märgiga) ja kui palju jäänud lahendamata (punase märgiga). Loodetavasti tekitab see paljudel tudengitel tungi muuta kõik punased märgid roheliseks. Igatahes paljud professionaalsed arendajad on automaattestide jooksutamisel sellist tungi enda juures täheldanud. 

Võimalikud edasiarendused:

    * Avalik üldistatud ülesannete lahendamise statistika üle kogu kursuse (tõenäoliselt motiveerib tugevamaid ja keskmisi, aga võib masendada nõrgemaid)
    * "Aumärkide" andmine (vt. stackoverflow badges), nt. kui tudengil läks peatüki ülesannete lahendamiseks vaja vähem, kui 3 vihjet või uuesti proovimist, siis näeb ta selle peatüki saavutuste juures mingit lisamärki. Teine aumärk võiks olla ülesannete õigeks ajaks (nt. enne loengut) lahendamise eest.
    * Kui logida lahenduste esitamise ajad ning kõik kordusesitused, siis saaks hea ülevaate sellest, millised teemad on raskemad ja millised kergemad.

