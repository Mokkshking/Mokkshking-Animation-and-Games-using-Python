# heart
from turtle import *
import turtle
import time
turtle.speed(5)
turtle.bgcolor("black")
title('Thank You Heart')

penup()
goto(-180,-200)
color("#e4af00") # golden color
write(" THANK YOU ", font=("Arial", 50, "bold"))
goto(30,-80)
pendown()
def curve():
    for i in range(200):
        turtle.right(1)
        turtle.forward(1)

turtle.color("pink", "red")        

turtle.begin_fill()
turtle.left(140)
turtle.forward(111.65)
curve()

turtle.left(120)
curve()
turtle.forward(111.65)
turtle.end_fill()
turtle.hideturtle()






