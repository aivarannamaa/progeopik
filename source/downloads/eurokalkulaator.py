from tkinter import *
from tkinter import ttk

euro_krooni_kurss = 15.6466

# valmistan ette funktsioonid, mida käivitatakse, kui vastava lahtrisse midagi tipitakse
def arvuta_eurod_kroonideks(event):
    arvuta(euro_lahter, euro_tulemus, euro_krooni_kurss, "EEK")

def arvuta_kroonid_eurodeks(event):
    arvuta(krooni_lahter, krooni_tulemus, 1 / euro_krooni_kurss, "EUR")

def arvuta(kust, kuhu, kurss, tulemuse_symbol):
    tekst = kust.get()
    try:
        summa = round(float(tekst),2)
        kuhu['text'] = "%.2f %s " % (summa * kurss, tulemuse_symbol)
    except Exception as e:
        # kui float'iks teisendamine ei õnnestunud, siis jõutakse siia
        kuhu['text'] = "???"

# Tk teeb akna
root = Tk()
root.title("Eurokalkulaator")

# LabelFrame teeb piirjoone ja pealkirjaga ala
vasak_pool = ttk.LabelFrame(root, text=" EUR -> EEK ")
vasak_pool.grid(row=0, column=0, padx=10, pady=8)

# sisestuslahter ja tulemuse widget lähevad LabelFrame'i sisse
euro_lahter = ttk.Entry(vasak_pool, width=10)
euro_lahter.grid(row=0, column=0, padx=5, pady=5)

# pane lahtris klahvi ülestõstmisele reageerima eespool tehtud funktsioon
euro_lahter.bind("<KeyRelease>", arvuta_eurod_kroonideks)

euro_tulemus = ttk.Label(vasak_pool, text="", width=15)
euro_tulemus.grid(row=0, column=1, padx=5, pady=5)


# sama lugu parema poolega
parem_pool = ttk.LabelFrame(root, text=" EEK -> EUR ")
parem_pool.grid(row=1, column=0, padx=10, pady=(0,8))

krooni_lahter = ttk.Entry(parem_pool, width=10)
krooni_lahter.grid(row=0, column=0, padx=5, pady=5)
krooni_lahter.bind("<KeyRelease>", arvuta_kroonid_eurodeks)

krooni_tulemus = ttk.Label(parem_pool, text="", width=15)
krooni_tulemus.grid(row=0, column=1, padx=5, pady=5)

# mainloop jälgib kasutaja tegevust 
# ja kutsub registreeritud sündmuste korral välja vastavad funktsioonid
root.mainloop()