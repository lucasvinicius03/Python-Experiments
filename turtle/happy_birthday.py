import turtle
from random import randint
from time import sleep

def tur_pos(tur, pos):
    tur.pu()
    tur.goto(pos)
    tur.pd()

def writer(text, pos):
    tur_pos(t2, pos)
    t2.write(text, font=('arial', 30, 'bold'), align='center')

sn = turtle.Screen()
sn.tracer(0)
height = sn.window_height()
width = sn.window_width()

t1 = turtle.Turtle()
t2 = turtle.Turtle()
t1.hideturtle()
t2.hideturtle()

happy_birthday = 'happybirthdayonyourlanguage'
name = 'personsname'

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

while True:
    for x in range(20):
        t1.color('black', colors[randint(0,5)])
        balloon = (randint(0 - int(height / 2), int(height / 2)),
            randint(0 - int(width / 2), int(width / 2)))
        tur_pos(t1, balloon)
        t1.begin_fill()
        t1.circle(20)
        t1.end_fill()
        t1.rt(90)
        t1.forward(40)
        t1.lt(90)
    writer(happy_birthday, (0,40))
    writer(name, (0,-40))
    sn.update()
    t1.clear()
    t2.clear()
    sleep(0.5)