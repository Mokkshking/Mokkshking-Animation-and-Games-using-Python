
# spinner

from turtle  import *
import turtle

title('Figet Spinner')
state = {'turn':0}
def spinner ():
    'draw spinner.'
    clear()
    angle = state['turn']/10
    right(angle)
    forward(100)
    dot(100,'red')
    back(100)
    right(120)
    forward(100)
    dot(100,'green')
    back(100)
    right(120)
    forward(100)
    dot(100,'blue')
    back(100)
    right(120)
    dot(30,'gold')
    update()



def animate():
    "animate fidmet spinner."
    if state['turn']>0:
        state['turn']-=1
    spinner()
    ontimer(animate,20)



def flick():
    "flick fidget spinner."
    state['turn']+=10


setup(420,420,370,0)
hideturtle()
tracer(False)
width(20)
onkey(flick,'space')
listen()
animate()
done()







    
        
