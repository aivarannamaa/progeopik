import os
from tkinter import *
from tkinter import ttk, filedialog, messagebox

def vali_kaust():
    kausta_nimi = filedialog.askdirectory()
    kausta_lahter.delete(0)
    kausta_lahter.insert(0, kausta_nimi)

def naita_infot():
    kausta_nimi = kausta_lahter.get().strip()
    laiend = laiendi_lahter.get().strip()
    
    if kausta_nimi == "" or laiend == "":
        messagebox.showerror("Probleem", "Kõigepealt vaja valida/sisestada laiend ja kaust")
        return
     
    failinimed = os.listdir(kausta_nimi)
    print(len(failinimed))
    
    failide_arv = 0
    kogumaht = 0
    
    for failinimi in failinimed:
        if failinimi[-(len(laiend)+1):] == "." + laiend:
    
            täisnimi = kausta_nimi + "\\"+ failinimi
            
            suurus = os.stat(täisnimi).st_size
            suurus_mb = round(suurus / 1024 / 1024, 1)
            
            print(failinimi + ", " + str(suurus_mb) + "MB")
            
            failide_arv = failide_arv + 1
            kogumaht = kogumaht + suurus
    
    kogu_mb = round(kogumaht / 1024 / 1024, 1)
    print("Kokku oli " + str(failide_arv) + " faili, kogumahuga " + str(kogu_mb) + "MB")

# alljärgnev kood sätib paika kasutajaliidese elemendid
root = Tk()
root.title("Failide info")
root.geometry("500x550")

laiendi_silt = ttk.Label(root, text="Laiend", justify=LEFT)
laiendi_silt.grid(row=0, column=0, sticky=NSEW, padx=5, pady=5)

laiendi_lahter = ttk.Entry(root, width=5)
laiendi_lahter.insert(0, "mp3")
laiendi_lahter.grid(row=0, column=1, sticky=W, padx=5, pady=5)

kausta_silt = ttk.Label(root, text="Kaust", justify=LEFT)
kausta_silt.grid(row=1, column=0, sticky=NSEW, padx=5)

kausta_lahter = ttk.Entry(root)
kausta_lahter.grid(row=1, column=1, sticky=EW, padx=5)

kausta_nupp = ttk.Button(root, text="...", command=vali_kaust, width=3)
kausta_nupp.grid(row=1, column=2, padx=5)

start_nupp = ttk.Button(root, text="Näita infot", command=naita_infot)
start_nupp.grid(row=2, column=0, columnspan=3, sticky=NSEW, padx=5, pady=5)

tabel = ttk.Treeview(root, columns=('nimi', 'suurus'))
tabel.grid(row=3, column=0, columnspan=3, sticky=NSEW, padx=5)
tabel.column('nimi', width=400, anchor=W)
tabel.column('suurus', width=50, anchor=W)
tabel.heading('nimi', text='Nimi', anchor=W)
tabel.heading('suurus', text='Suurus', anchor=W)
tabel['show'] = 'headings'

statusbar = Label(root, text="", bd=1, relief=SUNKEN)
statusbar.grid(row=4, column=0, columnspan=3, sticky=NSEW, padx=5, pady=5)

root.columnconfigure(1, weight=1)
root.rowconfigure(3, weight=1)

root.mainloop()


