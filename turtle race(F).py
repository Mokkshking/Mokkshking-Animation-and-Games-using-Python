import pyttsx3
from turtle import *
from random import *
import turtle
import time

# SCREEN SETUP
setup(800, 500)
title("Turtle Race")
bgcolor("forestgreen")
speed(0)

# HEADING
penup()
goto(-100, 205)
color("white")
write("TURTLE RACE", font=("Arial", 20, "bold"))

# DIRT
goto(-350, 200)
pendown()
color("salmon1")
begin_fill()
for i in range(2):
    forward(700)
    right(90)
    forward(400)
    right(90)
end_fill()

# FINISH LINE
gap_size = 20
shape("square")
penup()

# WHITE SQUARES ROW 1
color("white")
for i in range(10):
    goto(250, (170 - (i * gap_size * 2)))
    stamp()

# WHITE SQUARES ROW 2
for i in range(10):
    goto(250 + gap_size, ((210 - gap_size) - (i * gap_size * 2)))
    stamp()

# BLACK SQUARES ROW 1
color("black")
for i in range(10):
    goto(250, (190 - (i * gap_size * 2)))
    stamp()

# BLACK SQUARES ROW 2
for i in range(10):
    goto(251 + gap_size, ((190 - gap_size) - (i * gap_size * 2)))
    stamp()
    

# first player details 
player_1 = Turtle() 
player_1.color('red') 
player_1.shape('turtle')
player_1.shapesize(1.5)
   
# first player proceeds to racing track 
player_1.penup() 
player_1.goto(-300,150) 
player_1.pendown() 
   
 
  
# second player details 
player_2 = Turtle() 
player_2.color('blue') 
player_2.shape('turtle') 
player_2.shapesize(1.5)

# second player enters in the racing track 
player_2.penup() 
player_2.goto(-300,50) 
player_2.pendown() 
   
 
  
# third player details 
player_3 = Turtle() 
player_3.shape('turtle') 
player_3.color('green') 
player_3.shapesize(1.5)

# third player enters in the racing track 
player_3.penup() 
player_3.goto(-300,-50) 
player_3.pendown() 

  
# fourth player details 
player_4 = Turtle() 
player_4.shape('turtle') 
player_4.color('cyan') 
player_4.shapesize(1.5)

# fourth player enters in the racing track 
player_4.penup() 
player_4.goto(-300,-150) 
player_4.pendown() 


# PAUSE FOR 1 SECOND BEFORE RACING
time.sleep(1)

# move the turtles
while player_1.xcor() <= 245 and player_2.xcor() <= 245 and player_3.xcor() <= 245 and player_4.xcor() <= 245:
     player_1.forward(randint(1,2))
     player_2.forward(randint(1,2))
     player_3.forward(randint(1,2))
     player_4.forward(randint(1,2))

# to choose winner

if player_1.xcor() > player_2.xcor() and player_1.xcor() > player_3.xcor() and player_1.xcor() > player_4.xcor():
    Win = "RED TURTLE WINS"
    player_1.shapesize(2.5)

    
elif player_2.xcor() > player_1.xcor() and player_2.xcor() > player_3.xcor() and player_2.xcor() > player_4.xcor():
    Win = "BLUE TURTLE WINS"
    player_2.shapesize(2.5)
    
    
elif player_3.xcor() > player_1.xcor() and player_3.xcor() > player_2.xcor() and player_3.xcor() > player_4.xcor():
    Win = "GREEN TURTLE WINS"
    player_3.shapesize(2.5)
    
   
else:
     Win = "CYAN TURTLE WINS"
     player_4.shapesize(2.5)

shape("classic")
penup()
goto(-165,-200)
color("black") 
write( Win, font=("Arial", 20, "bold"))
hideturtle()
# to anounce the winner
engine=pyttsx3.init()
engine.say(Win)
engine.runAndWait()

     
