import matplotlib.pyplot as plt

kuud         = [  1,    4,    5,    6,    7,    8,    9,   10,  11,  12]
sissetulekud = [710, 1200, 1445, 1690, 1350, 1223, 1470, 1200, 808, 698]
väljaminekud = [700, 1160, 1556, 1520, 1415, 1180, 1770,  500, 408, 505]

fig = plt.figure()           
ax = fig.add_subplot(1,1,1)  

# Salvestame jooned muutujatesse, et oleks pärast võimalik vahet teha,
# kummale joonele klõpsati.
# Lisame ka picker argumendi, mis näitab kui lähedale peab klõpsama,
# et klõpsu seostatakse joonega
[sissetulekute_joon] = ax.plot(kuud, sissetulekud, "o-", label="Sissetulekud", picker=3)               
[väljaminekute_joon] = ax.plot(kuud, väljaminekud, "^-r", label="Väljaminekud", picker=3)

ax.set_xlabel("Kuud")      
ax.set_ylim(0, 2000)        
ax.set_xticks([1,2,3,4,5,6,7,8,9,10,11,12]) 
ax.legend()         

# defineerime funktsiooni, mis peaks klõpsudele reageerima
def on_pick(event):
    thisline = event.artist
    xdata = thisline.get_xdata()
    ydata = thisline.get_ydata()
    index = event.ind[0]
    kuu_nr = xdata[index]
    summa = ydata[index]
    
    if thisline == sissetulekute_joon:
        näitaja = "sissetulek"
    else:
        näitaja = "väljaminek"
        
    print(str(kuu_nr) + ". kuu " + näitaja + " oli " + str(summa))

# registreerime funktsiooni klõpsudele reageerima
cid = fig.canvas.mpl_connect('pick_event', on_pick)

fig.show()                   