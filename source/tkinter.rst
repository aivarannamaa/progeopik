.. _tkinter:

*******
tkinter
*******
Selles lisas vaatleme graafilise kasutajaliidesega programmide tegemist Pythoni ``tkinter`` mooduli baasil. Esmalt kirjutame ühe lihtsa näiteprogrammi, kasutades standardseid kasutajaliidese komponente (nupud, tekstikastid). Seejärel demonstreerime, kuidas luua ``tkinter``-i ``canvas`` komponendi abil vabas vormis kasutajaliideseid (nt graafikuid, animatsioone, mänge).

Tk ja ``tkinter``
=================
Moodul ``tkinter`` (koos alammooduliga ``tkinter.ttk``) kuulub Pythoni standardvarustusse ja on seetõttu kõige mugavam graafiliste kasutajaliideste loomise vahend Pythonis. Nimetatud moodulid põhinevad levinud teegil nimega Tk, mida kasutatakse ka teistes programmeerimiskeeltes.

Käesolevas materjalis eeldame Python 3-ga kaasas olevat ``tkinter``-i versiooni 8.5. Selle versiooni olulisim eelis vanemate versioonide ees on see, et ta võimaldab luua kasutajaliideseid, mis võtavad erinevates op-süsteemides (Windows, Mac OS, Linux) vastavale platvormile omase välimuse.

.. note::


    Kuna ``tkinter`` on väga paljude võimalustega, siis siin saame demonstreerida vaid väikest osa. Paraku ei ole ka Pythoni standard-dokumentatsioon ``tkinter``-i osas piisavalt põhjalik ja seetõttu tuleks huvi korral otsida lisainfot internetist. Kuna Tk-le pandi algus juba aastal 1988, leidub nii Tk kui ``tkinter``-i kohta interetis palju materjali, millest kõik ei kajasta adekvaatselt uuemate versioonide võimalusi. Alljärgnevalt on toodud mõned paremad kohad, kust uuemate Tk versioonide kohta infot leida:

    * http://www.tkdocs.com/ -- kõige parem koht Tk ja ``tkinter``-i põhimõtete õppimiseks.  
    * http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/index.html -- eelmisest materjalist täielikum, aga eeldab, et lugeja on ``tkinter``-i põhimõtetega juba tuttav. Hea koht ``canvas``-i võimalustega tutvumiseks.


Standardsed kasutajaliidese komponendid
=======================================
Alustuseks toome ära ühe lihtsa ``tkinter``-i programmi:

.. sourcecode:: py3

    # impordi tk vidinad ja konstandid
    from tkinter import *
    from tkinter import ttk
    from tkinter import messagebox

    # see funktsioon käivitatakse nupule klõpsamisel
    def tervita():
        tervitus = 'Tere ' + nimi.get()
        messagebox.showinfo(message=tervitus)


    # loome akna
    raam = Tk() 
    raam.title("Tervitaja")
    raam.geometry("300x100")

    # loome tekstikasti jaoks sildi
    silt = ttk.Label(raam, text="Nimi")
    silt.place(x=5, y=5)

    # loome tekstikasti
    nimi = ttk.Entry(raam)
    nimi.place(x=70, y=5, width=150)

    # loome nupu
    nupp = ttk.Button(raam, text="Tervita!", command=tervita)
    nupp.place(x=70, y=40, width=150)

    # ilmutame akna ekraanile
    raam.mainloop()

Seda programmi käivitades peaksid saama ühe väikese akna, milles on tekstikast nime sisestamiseks ning nupp, mida vajutades saad nimelise tervituse.

Hakkame nüüd selle programmi sisu analüüsima.

#. Esimene ``import``-lause teeb meile kättesaadavaks ``tkinter``-i põhivahendid, teine ``import`` teeb kättesaadavaks platvormi stiiliga kasutajaliidese vidinad.

#. Funktsioon ``tervita`` on mõeldud käivitamiseks nupule klikkimise korral. Funktsiooni kehas küsitakse allpool defineeritud tekstikasti sisu (``nimi.get()``), moodustatakse selle põhjal tervitusega sõne ning näidatakse seda kasutajale väikses lisaaknas. (Selles funktsioonis oleme kasutanud ühte globaalset muutujat -- ``nimi`` pole ei funktsiooni parameeter ega lokaalne muutuja, vaid funktsioonist väljaspool defineeritud muutuja.)

#. :py:class:`Tk()<tkinter.Tk>` loob akna, millele järgmisel real määratakse pealkiri ja ülejärgmisel real mõõtmed (pikslites).

#. Järgnevalt luuakse 3 kasutajaliidese komponenti e vidinat (ingl *widget*):

    * :py:class:`ttk.Label<tkinter.ttk.Label>` loob ühe sildi (s.o vidina teksti näitamiseks). Funktsiooni esimese argumendiga näitasime, et me soovime seda silti kasutada eespool loodud aknas. Kasutades nimelist argumenti ``text``, andsime sellele sildile ka soovitud teksti. Käsk ``silt.place(...)`` paigutas loodud sildi soovitud koordinaatidele (ühikuteks on pikslid, punkt (0,0) paikneb akna sisuosa ülemises vasakus nurgas ning koordinaadid kasvavad paremale/alla liikudes).
        .. image:: images/coords.png
        
    * Järgmises plokis lõime ja seadsime paika tekstisisestuskasti (``ttk.Entry``). Selle paigutamisel näitasime ära ka soovitud laiuse.
    
    * Nupu (``ttk.Button``) loomisel määrasime argumendiga ``command`` ära, mida tuleb teha nupule klikkimise korral. Pane tähele, et argumendi väärtuseks on ainult funktsiooni nimi, mitte funktsiooni väljakutse (see oleks olnud koos tühjade sulgudega). Põhjus on selles, et me ei taha seda funktsiooni käivitada mitte nupu loomise ajal, vaid siis, kui nuppu klikitakse.

#. Viimaks käivitasime lause ``raam.mainloop()``, mis kuvab loodud akna ekraanile ja jääb ootama kasutaja tegevusi.


 
Punktid 1-5 on üldjuhul olemas igaks ``tkinter``-i programmis. Programmi sisuline olemus sõltub sellest, milliseid vidinaid aknasse paigutatakse (punkt 4) ning kuidas kasutaja tegevustele reageeritakse (punkt 2). Võimalike vidinate valimiseks uuri alustuseks lehekülge aadressil http://www.tkdocs.com/tutorial/widgets.html. Kasutaja tegevustele reageerimisel saad rakendada kogu oma programmeerimisvõtete arsenali.


Parem viis vidinate paigutamiseks
---------------------------------
Eelmist näiteprogrammi käivitades ei olnud sa võibolla rahul vidinate paigutusega ja proovisid korrigeerida etteantud koordinaate ja mõõtmeid, et kasutajaliides tuleks ilusam. Paraku on selline pikslihaaval timmimine tänamatu töö, kuna mõnes teises op-süsteemis (või ka teiste seadetega arvutis) ei pruugi sinu poolt seatud paigutus sobida. Samuti võis häirida sind see, et akna suurendamisel jäid vidinad ühte nurka pidama.

Õnneks on võimalik määrata vidinate paigutust ka natuke üldisemalt kui pikslite tasemel, lubades sellega Tk-l valida vastavalt olukorrale kõige parem konkreetne paigutus. Järgnevas programmis on vidinate paigutamiseks kasutatud ``place`` meetodi asemel ``grid`` meetodit, mis jagab kasutajaliidese mõtteliselt ruudustikuks ning paigutab iga vidina soovitud lahtrisse vastavalt argumentidele ``column`` ja ``row``.

.. sourcecode:: py3

    from tkinter import *
    from tkinter import ttk
    from tkinter import messagebox

    def tervita():
        tervitus = 'Tere ' + nimi.get()
        messagebox.showinfo(message=tervitus)


    raam = Tk() 
    raam.title("Tervitaja")
    # raam.geometry("300x100") # akna algne suurus määratakse vastavalt sisule


    # paigutame sildi ruudustiku ülemisse vasakusse lahtrisse (column ja row)
    # soovime, et sildi ümber jääks igas suunas 5 pikslit vaba ruumi (padx ja pady)
    # soovime, et silt "kleepuks" oma lahtris ülemisse vasakusse nurka (sticky)
    # N - north, W - west
    silt = ttk.Label(raam, text="Nimi")
    silt.grid(column=0, row=0, padx=5, pady=5, sticky=(N, W))

    # tekstikasti puhul soovime, et ta kleepuks nii ida- kui lääneserva külge
    # st. ta peab venima vastavalt akna suurusele
    nimi = ttk.Entry(raam)
    nimi.grid(column=1, row=0, padx=5, pady=5, sticky=(N, W, E))

    # soovime, et nupp veniks nii laiuses kui ka kõrguses
    nupp = ttk.Button(raam, text="Tervita!", command=tervita)
    nupp.grid(column=1, row=1, padx=5, pady=5, sticky=(N, S, W, E))

    # soovime, et akna suuruse muutmisel muudetakse veeru 1 ja rea 1 mõõtmeid
    # (st. veerg 0 ja rida 0 jäävad sama laiaks/kõrgeks)
    raam.columnconfigure(1, weight=1) 
    raam.rowconfigure(1, weight=1)

    # kuvame akna ekraanile
    raam.mainloop()

.. note::

    Lisaks meetoditele ``place`` ja ``grid`` võid kohata veel paigutusmeetodit ``pack``. Rohkem infot saab siit: http://www.tkdocs.com/tutorial/concepts.html#geometry .

Harjutus. Täiendatud tervitaja.
-------------------------------
Täienda eelmist programmi nii, et see võimaldaks ka perenime sisestamist ja kasutaks seda tervituses.

.. _canvas:

Tahvel (``canvas``)
===================
Üks põnevamaid Tk vidinaid on tahvel (ingl *canvas*). Tegemist on alaga, kuhu on võimalik joonistada erinevaid kujundeid, paigutada pilte vms. Järgnev näiteprogramm demonstreerib mõningaid tahvli kasutamise võimalusi:

.. sourcecode:: py3

    from tkinter import *
    from tkinter import font # vajalik teksti fondi muutmiseks

    raam = Tk()
    raam.title("Tahvel")
    tahvel = Canvas(raam, width=600, height=600, background="white")
    tahvel.grid()

    # üksik kriips (x0, y0, x1, y1)
    tahvel.create_line(30, 40, 300, 40)

    # ühendatud kriipsud (suvaline arv koordinaatide paare)
    tahvel.create_line(30,60,  300,60,  300,100,  60,100)

    # võimalik on muuta joone paksust (width) ja sisu värvi (fill)
    tahvel.create_line(30, 130, 300, 130, width=4, fill="red")

    # teistsugune joone stiil
    tahvel.create_line(30, 150, 300, 150, width=5, dash=(5, 1, 2, 1), arrow=LAST)

    # tõmbab kriipsud, ühendab otsapunktid ja värvib sisu
    # värve saab määrata ka rgb komponentidena
    # vt. http://www.colorpicker.com/
    tahvel.create_polygon(30,160,  300,160,  300,200,  60,200, fill="#95BD9D")

    # ristkülik
    tahvel.create_rectangle(30,260,  300,300)

    # ovaal
    tahvel.create_oval(30,260,  300,300, width=2, outline="blue", fill="wheat")

    # proovi liigutada hiirt selle ovaali kohale
    tahvel.create_oval(330, 330, 400, 400, fill="gray", activefill="pink")

    # kui soovid teksti esitamisel ise fonti valida, siis tuleb enne vastav font luua
    suur_font = font.Font(family='Helvetica', size=32, weight='bold')
    tahvel.create_text(30, 500, text="Tere!", font=suur_font, anchor=NW)

    raam.mainloop()


Lisainfot ``canvas``-i kohta leiab siit: http://infohost.nmt.edu/tcc/help/pubs/tkinter/canvas.html

Harjutus. Bahama lipp
---------------------

Koosta programm, mis kuvab valge taustaga graafikaakna pealkirjaga "Bahama saarte lipp" ja joonistab sinna Bahama lipu.

.. image:: images/bahama.png


Keerulisemad kujundid
---------------------
Miski ei keela tahvlile kujundite joonistamiseks kasutada tsükleid või muid Pythoni vahendeid.

Kuigi Tkinter sobib hästi graafikute joonistamiseks, tekitab mõningast ebamugavust teistmoodi koordinaatide süsteem -- oleme ju harjunud, et *y* kasvab ülespoole, mitte aga alla. Et sellest probleemist lahti saada, võtame abiks tahvli meetodi ``move``, mis võimaldab tahvlil olevaid objekte horisontaalset ja vertikaalset telge mööda ümber tõsta. Seega paigutame kõik objektid harilikku koordinaadistikku ja siis rakendame funktsiooni ``move``. 

Järgnev näiteprogramm püüab teha *y=sin(x)* graafikut:

.. sourcecode:: py3

    from tkinter import *
    from math import sin

    raam = Tk()

    w = 500 # tahvli laius
    h = 500 # tahvli pikkus
    tahvel = Canvas(raam, width=w, height=h, background="white")
    tahvel.grid()

    # vertikaalne telg
    tahvel.create_line(0, h/2, 0, -h/2, arrow=LAST)
    # horisontaalne telg
    tahvel.create_line(-w/2, 0, w/2, 0, arrow=LAST)

    punktid = []
    # genereerime graafiku punktid kujul [x0,f(x0), x1,f(x1),..., xn, f(xn)]
    for x in range(w // -2, w // 2):
        suurendus = 30
        punktid.append(x)
        y = sin(x / suurendus)
        punktid.append(y * suurendus)

    # joonistame graafiku (anname argumendid järjendina)
    tahvel.create_line(punktid, fill="red")

    # nihutame kõik objektid 250px võrra paremale ja alla
    tahvel.move(ALL, w/2, h/2)

    raam.mainloop()

Kas saadud graafik on korrektne? Miks? Leia ja paranda viga.

Piltide esitamine
-----------------
Tahvlile saab panna ka .gif, .pgm, või .ppm formaadis pilte. Järgmise näite proovimiseks salvesta programmiga samasse kausta järgmised failid:  :download:`pall.gif <downloads/pall.gif>`,
:download:`avatud.gif <downloads/avatud.gif>`,
:download:`suletud.gif <downloads/suletud.gif>`.

.. sourcecode:: py3

    from tkinter import *

    raam = Tk()
    raam.title("Tahvel")
    tahvel = Canvas(raam, width=600, height=600, background="white")
    tahvel.grid()

    # pildi kuvamisel on vaja kõigepealt laadida pilt ja panna see siis tahvlile
    pall = PhotoImage(file="pall.gif") 
    img = tahvel.create_image(450, 80, image=pall)

    # activeimage määrab pildi, mida näidatakse, kui hiirekursor on pildi kohal
    # anchor näitab, mille järgi pilt paigutatakse (antud juhul ülemise-vasaku nurga järgi)
    suletud = PhotoImage(file="suletud.gif")
    avatud = PhotoImage(file="avatud.gif")
    img = tahvel.create_image(50, 400, image=suletud, activeimage=avatud, anchor=NW)

    raam.mainloop()

Animatsioon
-----------
Olgu ülesandeks joonistada osutitega kell, mis ennast aja jooksul värskendaks.

Võrreldes eelmiste ülesannetega, kus tegemist oli sisuliselt staatiliste kujutistega, on meie praeguseks eesmärgiks uurida, kuidas võib muuta graafikaobjektide olekuid rakenduse töö ajal.

Graafikaobjektide loomisel võib neile omistada unikaalseid identifikaatoreid, mille järgi saab need hiljem tahvlil üles leida:

.. sourcecode:: py3

    id = tahvel.create_line(x0,y0,...,xn,yn)

Kasutades sellist identifikaatorit, saab näiteks objekti kustutada, nihutada või muuta tema parameetreid. Objektidega manipuleerimiseks saame kasutada järgnevaid ``canvas``-i meetodeid:

.. sourcecode:: py3

    # kustutamine
    tahvel.delete(id):
    
    # nihutamine
    tahvel.move(id, x, y):
    
    # objekti parameetrite kontrollimine
    tahvel.itemcget(id, "width")
    
    # koordinaatide uuendamine
    tahvel.coords(id, x0,y0,...,xn,yn )

Antud ülesande kontekstis huvitab meid põhiliselt viimane meetod, mille abil me saame osutite positsiooni uuendada.

Tekitame uue raami ja tahvli. Kella keskpunkt olgu tahvli keskel.

.. sourcecode:: py3

    from tkinter import *
    
    raam = Tk()
    raam.title("Kell")
    # tahvli laius
    w = 500
    # tahvli kõrgus
    h = 500
    
    tahvel = Canvas(raam, width=w, height=h, bg="white")
    
    # kella raam
    tahvel.create_oval(10,10,w-10,h-10)
    # kella keskpunkt
    tahvel.create_oval(w//2-5,h//2-5,w//2+5,h//2+5,fill="black")

Joonistame sekundiosuti (joon) ja salvestame tema id muutujasse ``sek_id``.

.. sourcecode:: py3

    sek_id = tahvel.create_line(w//2,h//2,w//2,20,fill="red")

Alustame sekundiosutist. Kuna osuti üks ots on fikseeritud kella keskel, siis meid huvitavad ainult liikuva otsa koordinaadid mingil ajahetkel *t*. Seega defineerime funktsiooni, mis etteantud sekundi jaoks tagastab vastava punkti koordinaadid *x*, *y*:

.. sourcecode:: py3

    from math import *
    
    def osutiTipp(positsioon, pikkus):
        """
        annab sekundiosuti liikuva tipu koordinaadid tavalises koordinaadistikus
        positsioon on ujukomaarv 0 ja 1 vahel    
        """
        # arvutame x koordinaadi
        x = pikkus * cos(pi/2 - positsioon *  2 * pi)

        # arvutame y koordinaadi
        y = -pikkus * sin(pi/2 - positsioon * 2 * pi)

        # tagastame uued koordinaadid
        return x, y

Järgmise sammuna loome funktsiooni, mis loeb jooksvalt aega ja uuendab sekundiosuti positsiooni.

.. sourcecode:: py3

    import time

    def uuenda():
        # loeme jooksva sekundi
        sekundid = time.localtime().tm_sec

        # saame osuti liikuva tipu koordinaadid tavalises koordinaadistikus
        tipp_x, tipp_y  = osutiTipp(sekundid / 60, w // 2 - 20)

        # teisendame need canvas-i koordinaadistikku
        keskpunkt_x = w // 2
        keskpunkt_y = h // 2
        tipp_x = keskpunkt_x + tipp_x
        tipp_y = keskpunkt_y + tipp_y

        # uuendame osuti positsiooni
        tahvel.coords(sek_id, keskpunkt_x, keskpunkt_y, tipp_x, tipp_y)

        # ootame 1 sekundi ja siis uuendame kellaaega uuesti
        raam.after(1000, uuenda)

Kutsu funktsioon *uuenda* välja enne *Tkinteri* põhitsüklisse sisenemist.

.. sourcecode:: py3

    uuenda()  
    tahvel.pack()
    raam.mainloop()

Pane kood kokku ja käivita rakendus.

Harjutus. Täiendatud kell.
--------------------------
Täienda kella. Lisa minuti- ja tunniosuti, mis samuti muudaks aja jooksul oma positsiooni.

Hiireklõpsudele reageerimine
----------------------------
Järgnevas programmis kästakse tahvlil iga hiireklõpsu peale kutsuda välja funktsioon, mis registreerib hiireklõpsu koordinaadid:

.. sourcecode:: py3

    from tkinter import *
    
    def registreeri_hiireklõps(event):
        print("Klõpsati positsioonile", event.x, event.y)
        
        klõpsud.append([event.x, event.y])
        print("Seni tehtud klõpsud:", klõpsud)
    
    raam = Tk()
    raam.title("Tahvel")
    tahvel = Canvas(raam, width=600, height=600, background="white")
    tahvel.grid()
    tahvel.bind('<1>', registreeri_hiireklõps)
    
    klõpsud = []
    
    raam.mainloop()


Klahvidele reageerimine
-----------------------
Järgmine näide demonstreerib, kuidas uuendada tahvli sisu vastavalt kasutaja tegevusele (näite proovimiseks salvesta samasse kausta :download:`juku.gif <downloads/juku.gif>`):

.. sourcecode:: py3

    from tkinter import *
    from random import randint

    # mõningad abikonstandid
    juku_sammu_pikkus = 50
    tahvli_laius = 600
    tahvli_kõrgus = 600

    # funktsioonid, mis käivitatakse vastavalt kasutaja tegevusele
    def hiireklõps_juku_peal(event):
        # liigutan Juku juhuslikku positsiooni
        uus_x = randint(0, tahvli_laius-50)
        uus_y = randint(0, tahvli_kõrgus-50)
        tahvel.coords(juku_id, uus_x, uus_y)

    def nool_üles(event):
        tahvel.move(juku_id, 0, -juku_sammu_pikkus)

    def nool_alla(event):
        tahvel.move(juku_id, 0, juku_sammu_pikkus)

    def nool_vasakule(event):
        tahvel.move(juku_id, -juku_sammu_pikkus, 0)

    def nool_paremale(event):
        tahvel.move(juku_id, juku_sammu_pikkus, 0)


    # tavaline raami ja tahvli loomine
    raam = Tk()
    raam.title("Tahvel")
    tahvel = Canvas(raam, width=tahvli_laius, height=tahvli_kõrgus, background="white")
    tahvel.grid()

    # tavaline pildi sisselugemine
    juku = PhotoImage(file="juku.gif")

    # pildi loomisel jätan meelde pildi id 
    juku_id = tahvel.create_image(100, 100, image=juku)

    # pildi id kaudu seon sellel pildil toimunud klõpsud vastava funktsiooniga
    # <1> tähistab vasakut hiireklahvi
    tahvel.tag_bind(juku_id, '<1>', hiireklõps_juku_peal)

    # seon nooleklahvid vastavate funktsioonidega
    raam.bind_all("<Up>",    nool_üles)
    raam.bind_all("<Down>",  nool_alla)
    raam.bind_all("<Left>",  nool_vasakule)
    raam.bind_all("<Right>", nool_paremale)

    raam.mainloop()

Selles näites liigutasime kasutaja tegevusele vastavalt pildi asukohta, aga sama hästi võiksime ka näiteks midagi uut joonistada, tekitada uusi pilte vms.

.. note::
    
    Aadressil http://www.tkdocs.com/tutorial/canvas.html on näide, kuidas tuvastada hiirekursori liikumist ja kasutada seda infot vaba käega joonistamise võimaldamiseks.

Mõned lisanipid
===============
Paljude objektide genereerimine tsüklis ning hiirekliki seostamine konkreetse objektiga
---------------------------------------------------------------------------------------
Järgnev näide demonstreerib, kuidas panna tahvlile hulk pilte kasutades selleks tsüklit. Selleks, et piltidele oleks võimalik ka pärastpoole ligi pääseda, salvestatakse siin piltide *id*-d abitabelisse. Näite proovimiseks salvesta samasse kausta :download:`juku.gif <downloads/juku.gif>`.

.. sourcecode:: py3

    from tkinter import *

    # see funktsioon käivitatakse piltidele klikkimisel
    def hiireklikk(event):
        # küsin selle objekti id, millele parasjagu klõpsati
        # tahvel.find_withtag(CURRENT) annab loetelu kõigi aktiivsete objektide id-dega
        # antud juhul tähendab aktiivsus seda, et selle objekti peale klikiti
        # praegu võime eeldada, et selles loetelus on vaid 1 element
        # seetõttu võtamegi sealt elemendi indeksiga 0
        pildi_id = tahvel.find_withtag(CURRENT)[0]

        # vaatan id_tabeli läbi, et saada teada, millisel positsioonil sellise id-ga pilt asub
        for i in range(3):
            for j in range(3):
                if pildi_id == id_tabel[i][j]:
                    teade = "Klikiti pildil, mis asub positsioonil " + str(i) + "," + str(j)  
                    # näitan selle teate tekstiobjekti abil
                    tahvel.itemconfigure(teksti_id, text=teade)
                    
                    # sama hästi võin teate ka lihtsalt konsooli printida
                    print(teade)


    # raami ja tahvli loomine
    raam = Tk()
    raam.title("Tahvel")
    tahvel = Canvas(raam, width=500, height=500, background="white")
    tahvel.grid()

    # pildi sisu laadimine
    pilt = PhotoImage(file="juku.gif")

    # järgnevas tsüklis loon 9 pilti ja paigutan need tahvlil 3x3 asetusse
    # lisaks salvestan piltide id-d 3x3 tabelisse (st. 2-mõõtmelisse järjendisse)
    id_tabel = []
    for i in range (3):
        id_rida = []
        for j in range(3):

            # arvutan pildi koordinaadid vastavalt veeru ja rea numbritele
            x = 170 + (j * 70)
            y = 130 + (i * 70)
            pildi_id = tahvel.create_image(x, y, image=pilt)
            
            # seon sellel pildil toimuvad klõpsud funktsiooniga "hiireklikk"
            tahvel.tag_bind(pildi_id, '<1>', hiireklikk)

            # salvestan pildi sobivale kohale järjendis
            id_rida.append(pildi_id)

        # üks rida sai valmis, lisan selle tabelisse    
        id_tabel.append(id_rida)
        

    # lõpuks loon ka ühe tekstiobjekti, mille abil saan kasutajale tekstilist infot näidata
    teksti_id = tahvel.create_text(250, 350, text="Kliki mingil pildil!")


    raam.mainloop()

Tsüklis genereerimist võib kasutada ka siis, kui on vaja palju nuppe, tekstikaste vms.

Pildi vahetamine
----------------
Eespool oli näide selle kohta, kuidas panna automaatselt pilt vahetuma, kui hiir liigub üle pildi. Vaatame nüüd üldisemat võimalust, kuidas soovi korral (nt hiireklõpsuga) vahetada pildi sisu. Näite proovimiseks salvesta samasse kausta :download:`avatud.gif <downloads/avatud.gif>` ja  :download:`suletud.gif <downloads/suletud.gif>`.

.. sourcecode:: py3

    from tkinter import *

    def vaheta_pilt(event):
        # global deklaratsioon võimaldab muuta funktsioonist väljaspool
        # defineeritud muutujat
        global näidatav_pilt

        # vahetan pildi viite
        if näidatav_pilt == suletud:
            näidatav_pilt = avatud
        else:
            näidatav_pilt = suletud

        # ... ja uuendan selle viite põhjal tahvlil oleva pildi sisu
        tahvel.itemconfigure(pildi_id, image=näidatav_pilt)


    raam = Tk()
    raam.title("Tahvel")
    tahvel = Canvas(raam, width=600, height=600, background="white")
    tahvel.grid()


    suletud = PhotoImage(file="suletud.gif")
    avatud = PhotoImage(file="avatud.gif")
    näidatav_pilt = suletud

    pildi_id = tahvel.create_image(200, 200, image=näidatav_pilt, anchor=NW)
    tahvel.tag_bind(pildi_id, '<1>', vaheta_pilt)

    raam.mainloop()
    
Hiirerullile reageerimine ja objektide suumimine
------------------------------------------------
Järgnev näide demonstreerib kahte asja -- kuidas tuvastada hiirerulli kasutamist ning kuidas muuta tahvli objektide suurust.

.. sourcecode:: py3

    from tkinter import *

    def zoom(event):
        # Linuxis toimib event.num, aga windowsis delta
        if event.num == 5 or event.delta < 0:
            # allapoole rullimine
            faktor = 0.9
        else:
            # ülespoole rullimine
            faktor = 1.1

        # event.x ja event.y annavad hiirekursori asukoha
        # skaleerin kõiki objekte selle punkti suhtes
        # (kui soovid skaleerida üksikut objekti, siis kasuta ALL asemel selle objekti id-d)
        tahvel.scale(ALL, event.x, event.y, faktor, faktor)

    raam = Tk()
    raam.title("Tahvel")
    tahvel = Canvas(raam, width=600, height=600, background="white")
    tahvel.grid()

    tahvel.create_oval(100, 100, 200, 150, fill="wheat")
    tahvel.create_oval(300, 300, 340, 340)

    juku = PhotoImage(file="juku.gif")
    tahvel.create_image(70, 70, image=juku)
    tahvel.create_image(420, 420, image=juku)

    # Windowsis tähistab hiirerullimist <MouseWheel>
    tahvel.bind_all("<MouseWheel>", zoom)
    # Linuxis toimivad "<4>" ja "<5>"
    tahvel.bind_all("<4>", zoom)
    tahvel.bind_all("<5>", zoom)

    raam.mainloop()

Kahjuks ei toimu automaatselt piltide suuruse muutmine -- täieliku efekti saamiseks tuleks ka piltide sisu vahetada suuremate vastu.

Piltide kaitsmine prügikoristuse eest
-------------------------------------
Järgnev programm näitab nupule vajutades ekraanil pilti (proovimiseks salvesta skriptiga samasse kausta :download:`juku.gif <downloads/juku.gif>`):

.. sourcecode:: py3
    
    from tkinter import *
    from tkinter import ttk
    
    raam = Tk()
    
    # teen valmis ühe pildi, mida nupuvajutusega ekraanile kuvada
    juku = PhotoImage(file="juku.gif")
    
    # pilt peab tulema selle sildi peale
    silt = ttk.Label(raam)
    silt.grid()
    
    def näita_jukut():
        silt["image"] = juku
    
    # see nupp peab pildi kuvamise välja kutsuma
    nupp = ttk.Button(text="Näita Jukut", command=näita_jukut)
    nupp.grid()
    
    
    raam.mainloop()

Kuna muutujat ``juku`` läheb vaja vaid funktsioonis ``näita_jukut``, siis oleks loomulik teha see muutuja lokaalseks muutujaks:

.. sourcecode:: py3
    :emphasize-lines: 11-12
    
    from tkinter import *
    from tkinter import ttk
    
    raam = Tk()
    
    # pilt peab tulema selle sildi peale
    silt = ttk.Label(raam)
    silt.grid()
    
    def näita_jukut():
        # teen valmis ühe pildi, mida nupuvajutusega ekraanile kuvada
        juku = PhotoImage(file="juku.gif")
        silt["image"] = juku
    
    # see nupp peab pildi kuvamise välja kutsuma
    nupp = ttk.Button(text="Näita Jukut", command=näita_jukut)
    nupp.grid()
    
    
    raam.mainloop()
    
Jama on selles, et nüüd peale nupuvajutust enam Jukut ei ilmu. Probleem on Pythoni ja Tk vahelises möödarääkimises -- Python arvab, et kui funktsioon ``näita_jukut`` oma töö lõpetab, siis lokaalsesse muutujasse ``juku`` salvestatud objekti enam vaja ei lähe ning viskab selle minema (vt https://en.wikipedia.org/wiki/Garbage_collection_%28computer_science%29). Kui ``juku`` oli globaalne muutuja, siis ei julgenud Python seda minema visata, sest globaalse muutuja kaudu võib suvaline koodi osa sellest objektist sõltuda.

Selleks, et veenda Pythonit pildi vajalikkuses, tuleks kood korraldada nii, et ka peale funktsiooni töö lõppu jääks viide pildile kusagile alles. Üks võimalus on teha globaalne piltide hulk, kuhu me salvestame kõik ``PhotoImage``-d:

.. sourcecode:: py3
    :emphasize-lines: 4,14
    
    from tkinter import *
    from tkinter import ttk
    
    pildid = set()
    raam = Tk()
    
    # pilt peab tulema selle sildi peale
    silt = ttk.Label(raam)
    silt.grid()
    
    def näita_jukut():
        # teen valmis ühe pildi, mida nupuvajutusega ekraanile kuvada
        juku = PhotoImage(file="juku.gif")
        pildid.add(juku)
        silt["image"] = juku
    
    # see nupp peab pildi kuvamise välja kutsuma
    nupp = ttk.Button(text="Näita Jukut", command=näita_jukut)
    nupp.grid()
    
    
    raam.mainloop()
    
Kommentaarid
============
.. disqus::
    :disqus_identifier: tkinter