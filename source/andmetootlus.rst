.. _andmetootlus:

************
Andmetöötlus
************

Andmete visualiseerimine ``matplotlib`` abil
============================================

Graafikute integreerimine teistesse programmidesse
--------------------------------------------------

``matplotlib`` graafikuid saab integreerida erinevate kasutajaliidese raamistikega, sh Tkinteriga. Selleks tuleb ``Figure`` objekt luua mitte ``pyplot`` abil, vaid moodulis ``matplotlib.figure`` oleva konstruktoriga (http://matplotlib.org/api/figure_api.html#matplotlib.figure.Figure). Lisaks tuleb luua raamistikuspetsiifilised vidinad graafiku näitamiseks.

Järgnev näide demonstreerib pirukagraafiku lisamist Tkinteri programmi:

.. sourcecode:: py3

    import tkinter as tk
    from tkinter import ttk
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
    from matplotlib.figure import Figure
    
    def uuenda_graafik():
        ax.clear()
        
        # Simuleerin andmete uuendamist juhuslike andmete genereerimisega.
        # Reaalne programm loeks andmed kusagilt failist, sensoritest vms.
        import random
        k = 5
        suurused = random.sample([12, 45, 4, 14, 33, 32, 66, 23, 29, 7], k)
        nimed = random.sample(["Peeter", "Tiit", "Mari", "Jakob", "Teele",
                               "Kalle", "Malle", "Reet", "Lauri", "Kati"], k)
        
        ax.pie(suurused, labels=nimed)
        canvas.show()
    
    def salvesta_graafik():
        fig.savefig("graafik.pdf") # Fail ilmub jooksvasse kausta
    
    # Loon akna
    aken = tk.Tk()
    aken.title("Demo")
    
    # Loon graafikut tähistavad objektid
    fig = Figure(figsize=(5, 5), dpi=100) # 5x5 tolli
    ax = fig.add_subplot(1,1,1)
    fig.set_facecolor('white')
    
    # Loon pinna graafiku joonistamiseks
    # ja paigutan vastava Tk vidina
    canvas = FigureCanvasTkAgg(fig, master=aken)
    canvas.get_tk_widget().grid(row=0, column=0, columnspan=2)
    
    # Loon nupu andmete laadimiseks
    nupp1 = ttk.Button(aken, text="Uuenda graafik", command=uuenda_graafik)
    nupp1.grid(row=1, column=0)
    
    # Loon nupu graafiku salvestamiseks
    nupp2 = ttk.Button(aken, text="Salvesta graafik", command=salvesta_graafik)
    nupp2.grid(row=1, column=1)
    
    # Kuvan andmete esialgse seisu
    uuenda_graafik()
    
    # Alustan programmi peatsüklit
    aken.mainloop()

Rohkem infot:

* http://matplotlib.org/examples/user_interfaces/embedding_in_tk.html 
* https://pythonprogramming.net/how-to-embed-matplotlib-graph-tkinter-gui
* http://matplotlib.org/users/event_handling.html
 

Täpsem info
-----------
Ülevaade võimalustest: http://matplotlib.org/devdocs/users/screenshots.html
Väga hea ülevaade matplotlib mõistetest: http://matplotlib.org/faq/usage_faq.html

NumPy
=====

Pylab
=====
TODO: