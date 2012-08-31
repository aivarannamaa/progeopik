"""
ikoon http://www.rw-designer.com/icon-set/minesweeper
"""

from tkinter import *
from tkinter import font
import random

# valmista m�nguv�li ette
row_count = 15
col_count = 10
tile_size = 32

root = Tk()
root.title("Minesweeper")

# Canvas on vidin, mille peale saab joonistada, pilte laadida jne.
canvas = Canvas(root, width=col_count*tile_size, height=row_count*tile_size, highlightthickness=0)
canvas.pack()

statusbar = Label(root, text="siia tulevad mängu sõnumid", bd=1, relief=SUNKEN, anchor=W)
statusbar.pack(side=BOTTOM, fill=X)

big_font = font.Font(family='Helvetica', size=12, weight='bold')
#canvas.create_text(30, 50, text="Tere!", font=big_font, anchor=NW)

# vali välja miinide positsioonid
all_positions = []
for x in range(col_count):
    for y in range(row_count):
        all_positions.append((x, y))

mine_positions = random.sample(all_positions, row_count * col_count // 7)

# Paiguta miinid ja numbrid mängulauale
# lisaks salvestame mängulaua info ka eraldi massiivi (layout), kust seda on lihtsam kontrollida
layout = []
for y in range(row_count): # käi läbi kõik reanumbrid
    row = []
    for x in range(col_count): # .. ja kõik veerunumbrid
        if (x,y) in mine_positions:
            row.append("☼")
            tile_text = "☼"
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
            if neighbor_mine_count > 0:
                tile_text = str(neighbor_mine_count)
            else:
                tile_text = ""
            
            
        canvas.create_rectangle(x*tile_size, 
                                y*tile_size,
                                x*tile_size+tile_size, 
                                y*tile_size+tile_size)
        
        # kirjuta ruudu sisse vastavalt miini sümbol või naabruses olevate miinide arv
        canvas.create_text(x*tile_size + 10, 
                           y*tile_size + 5, 
                           text=tile_text, 
                           font=big_font, 
                           anchor=NW,
                           justify=CENTER)


# nüüd on mängulaua alumine kiht paigas.
# Kui järgnev kood välja kommenteerida, siis saab kontrollida, kas numbrid on õiged

# Katame mängulaua piltidega kinni. Piltidele klõpsides saab märkida miine või võtta "kive" lahti
# Kõigepealt lae pildid sisse
cover_img = PhotoImage(file="cover.gif", name="cover")
flag_img  = PhotoImage(file="flag.gif", name="flag") # seda pilti läheb vaja hiljem

# loome funktsioonid, mida käivitatakse piltidele klõpsamise korral
def right_click(event):
    # uurime välja, millise pildi (ruudu) peale klikiti
    item_id = event.widget.find_closest(event.x, event.y)[0]
    
    # kui tegemist on lipuga pildiga, siis vaheta pilt ilma liputa pildi vastu 
    # ning vastupidi
    if canvas.itemcget(item_id, 'image') == "cover":
        canvas.itemconfig(item_id, image=flag_img)
    else:
        canvas.itemconfig(item_id, image=cover_img)
    
    # TODO: õnnitulused, kui kõik pommid on märgistatud

def left_click(event):
    item_id = event.widget.find_closest(event.x, event.y)[0]
    canvas.delete(item_id)
    # TODO: game over kui vajutati pommi peale


for y in range(row_count):
    for x in range(col_count):
        img_id = canvas.create_image(x*tile_size, y*tile_size, anchor=NW, image=cover_img)
        canvas.tag_raise(img_id)
        canvas.tag_bind(img_id, "<1>", left_click)
        canvas.tag_bind(img_id, "<3>", right_click)
        

root.mainloop()


