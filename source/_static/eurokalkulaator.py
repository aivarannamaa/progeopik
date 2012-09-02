from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Eurokalkulaator")

def arvuta_eurod_kroonideks(event):
    print(euro_lahter.get())

def arvuta_kroonid_eurodeks(event):
    pass

# vasak pool 
euro_pealkiri = ttk.Label(root, text="Eurod kroonideks")
euro_pealkiri.grid(row=0, column=0, columnspan=2)

euro_lahter = ttk.Entry(root, width=10)
euro_lahter.grid(row=1, column=0)
euro_lahter.bind("<KeyPress>", arvuta_eurod_kroonideks)

euro_tulemus = ttk.Label(root, text="", width=10)
euro_tulemus.grid(row=1, column=1)

# parem pool
krooni_pealkiri = ttk.Label(root, text="Kroonid eurodeks")
krooni_pealkiri.grid(row=0, column=2, columnspan=2)

krooni_lahter = ttk.Entry(root, width=10)
krooni_lahter.grid(row=1, column=2)

krooni_tulemus = ttk.Label(root, text="", width=10)
krooni_tulemus.grid(row=1, column=3)



root.mainloop()