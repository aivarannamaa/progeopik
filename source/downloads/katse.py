from turtle import *

def ruut(kylg):
    i = 0
    while i < 4:
        forward(kylg)
        left(90)
        i += 1

ruut(100)

# liigume kuskile mujale
up()
forward(200)
down()

# väiksem ruut
ruut(20)

exitonclick()
