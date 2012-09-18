## Monte Carlo meetodil pi arvutamine - demo
## Gerli Viikmaa 18.09.2012

## Juhend:
## Kui ruut ja ring on joonistatud, tekib iga kliki peale dot
## ning shellis kuvatakse loendused ning arvutatud pi
## NB! Kui liiga kiiresti vajutada, tuleb vahel joon dot-i asemel
##     Kui eriti kiiresti vajutada, tuleb must joon (varvimata)

from turtle import *
from random import seed, uniform

seed()

def square(side):
    for i in range(4):
        fd(side)
        left(90)

radius = 250
circlecounts = 0
allcounts = 0

def draw_random_dot(x, y, lim=radius):
    global circlecounts, allcounts
    x=uniform(-lim, lim)
    y=uniform(-lim, lim)
    setpos(x, y)
    if x*x+y*y<=lim*lim:
        col="green"
        circlecounts += 1
    else:
        col="red"
    allcounts += 1
    dot(5, col)
    # pi on 7 komakohaga (%.7f), tohib muuta:
    print ("Kokku: %d, Ringis: %d, pi=%.7f" % 
           (allcounts, circlecounts, 4*circlecounts / allcounts))

speed(8) # joonista ruut aeglasemalt

up()
fd(radius)
left(90)
bk(radius)
down()

square(2*radius)
fd(radius)
speed(10) # speed(0) on eriti kiire (kui 10 aeglane on)
circle(radius)
up()

getscreen().onclick(draw_random_dot)
mainloop()

