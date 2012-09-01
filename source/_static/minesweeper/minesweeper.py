"""
"Kivide" eemaldamiseks tee klõps vasaku hiireklahviga
Oletatava miini märgistamiseks tee klõps parema hiireklahviga.

Programm on tavapärase Minesweeperiga võrreldes primitiivsem:
- Piirkonnad, kus pole miine naabruses, ei lähe klõpsamisel tervenisti lahti,
  st. kõik ruudud tuleb ise läbi klõpsida
- Mängu eduka läbimise kohta ei tule teadet. Kasutaja peab ise märgistatud
  miinide osas arvet pidama ja ennast õigel ajal õnnitlema. 
"""

from tkinter import *
from tkinter import font, messagebox
import random

# Abifunktsioon create_layout loob juhusliku mängulaua paigutuse 
# (sh. arvutab välja iga ruudu naabruses olevate miinide arvu)
# See funktsioon on ülejäänud programmist sõltumatu, kuna ta võtab
# kogu vajamineva info argumentidena ning tagastab lihtsa 2-mõõtmelise järjendi
def create_layout(row_count, col_count, mine_count):
    # Kõigepealt vali miinidele juhuslikud positsioonid.
    # Selleks koostame listi kõikvõimalike positsioonidega:
    all_positions = []
    for x in range(col_count):
        for y in range(row_count):
            all_positions.append((x, y))
    
    # ja valime sealt juhuslikult õige arvu elemente        
    mine_positions = random.sample(all_positions, mine_count)

    # Paiguta miinid ja naabrusnumbrid mängulauda kujutavasse maatriksisse
    layout = []
    for y in range(row_count): # käi läbi kõik reanumbrid
        row = []
        for x in range(col_count): # .. ja kõik veerunumbrid
            if (x,y) in mine_positions:
                row.append("☼")
            else:
                # Sellel ruudul miini pole. Vaja arvutada, mitu pommi on naabruses
                # Asja teeb raskeks see, et mänguvälja servas olevatel ruutudel on vähem
                # naabreid, kui mänguvälja keskel
                neighbor_mine_count = 0
                
                # vasakul
                if x > 0 and (x-1, y) in mine_positions:
                    neighbor_mine_count += 1
                
                # üleval
                if y > 0 and (x, y-1) in mine_positions:
                    neighbor_mine_count += 1
                    
                # paremal
                if x < col_count+1 and (x+1, y) in mine_positions:
                    neighbor_mine_count += 1
                
                # all
                if y < row_count+1 and (x, y+1) in mine_positions:
                    neighbor_mine_count += 1
                
                # üleval-vasakul
                if y > 0 and x > 0 and (x-1, y-1) in mine_positions:
                    neighbor_mine_count += 1
                
                # üleval-paremal
                if x < col_count+1 and y > 0 and (x+1, y-1) in mine_positions:
                    neighbor_mine_count += 1
                
                # all-paremal
                if y < row_count+1 and x < col_count+1 and (x+1,y+1) in mine_positions:
                    neighbor_mine_count += 1
                    
                # all-vasakul
                if x > 0 and y < row_count+1 and (x-1, y+1) in mine_positions:
                    neighbor_mine_count += 1
                        
                row.append(neighbor_mine_count)
        layout.append(row)
    
    return layout
    
# Põhiprogramm ###################################################################
# valmista mänguväli ette
row_count = 10
col_count = 7
tile_size = 32 # ühe ruudu küljepikkus pikslites
mine_count = 10

# Tk loob programmi põhiakna
root = Tk()
root.title("Minesweeper")

# Canvas on vidin, mille peale saab joonistada, pilte laadida jne.
canvas = Canvas(root, width=col_count*tile_size, height=row_count*tile_size, highlightthickness=0)
canvas.pack()

statusbar = Label(root, text="Mängulaual on kokku %d miini" % mine_count, bd=1, relief=SUNKEN, anchor=W)
statusbar.pack(side=BOTTOM, fill=X)

big_font = font.Font(family='Helvetica', size=12, weight='bold')
#canvas.create_text(30, 50, text="Tere!", font=big_font, anchor=NW)


# Moodustame Canvas'e peale mängulaua "alumise kihi" 
layout = create_layout(row_count, col_count, mine_count)
# Paiguta miinid ja numbrid graafilisele mängulauale
for y in range(row_count): # käi läbi kõik reanumbrid
    for x in range(col_count): # .. ja kõik veerunumbrid
        tile_text = str(layout[y][x])
        canvas.create_rectangle(x*tile_size, 
                                y*tile_size,
                                x*tile_size+tile_size, 
                                y*tile_size+tile_size)
        
        # kirjuta ruudu sisse vastavalt miini sümbol või naabruses olevate miinide arv
        canvas.create_text(x*tile_size + 10, 
                           y*tile_size + 5, 
                           text=tile_text, 
                           font=big_font, 
                           anchor=NW)

# Nüüd on mängulaua alumine kiht paigas.
# Järgmiseks katame mängulaua piltidega kinni.
# Kõigepealt lae pildid sisse
plain_cover_img = PhotoImage(file="plain_cover.gif", name="plain_cover")
flagged_cover_img = PhotoImage(file="flagged_cover.gif", name="flagged_cover") # seda pilti läheb vaja hiljem

# funktsioonid right_click ja left_click seotakse allpool hiireklõpsudega
def right_click(event):
    # uurime välja, millise pildi (ruudu) peale klikiti
    item_id = event.widget.find_closest(event.x, event.y)[0]
    
    # kui tegemist on lipuga pildiga, siis vaheta pilt ilma liputa pildi vastu 
    # ning vastupidi
    if canvas.itemcget(item_id, 'image') == "plain_cover":
        canvas.itemconfig(item_id, image=flagged_cover_img)
    else:
        canvas.itemconfig(item_id, image=plain_cover_img)
    # TODO: õnnitulused, kui kõik pommid on märgistatud

def left_click(event):
    item_id = event.widget.find_closest(event.x, event.y)[0]
    # eemalda kivi
    canvas.delete(item_id)
    
    # tee selgeks, millise rea / veeruga on tegemist
    x = event.x // tile_size
    y = event.y // tile_size
    if layout[y][x] == "☼":
        messagebox.showinfo("Mäng läbi!", "Sattusid miini otsa, mäng läbi!")
        exit()



# Loo katmise pildid ("kivid") ja seosta nad hiireklõpsudega
# jäta ka kivid meelde
for y in range(row_count):
    for x in range(col_count):
        img_id = canvas.create_image(x*tile_size, y*tile_size, anchor=NW, image=plain_cover_img)
        canvas.tag_raise(img_id) 
        canvas.tag_bind(img_id, "<1>", left_click)
        canvas.tag_bind(img_id, "<3>", right_click)
        

# mainloop teeb mänguväljaku akna nähtavaks ja hakkab kasutaja tegevusi ootama
root.mainloop()


