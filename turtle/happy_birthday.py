import turtle
from random import randint
from time import sleep

def tur_pos(x, y):
    t1.pu()
    t1.goto(x, y)
    t1.pd()

def writer(text, pos):
    tur_pos(*pos)
    t1.write(text, font=('arial', 30, 'bold'), align='center')

def draw_balloon(size):
    t1.begin_fill()
    t1.circle(size)
    t1.end_fill()
    t1.rt(90)
    t1.fd(size*2)
    t1.lt(90)

def next_frame(balloons):
    for balloon in balloons:
        t1.color('black', balloon[1])
        balloon[0][1] = balloon[0][1] + 10
        tur_pos(balloon[0][0], balloon[0][1])
        draw_balloon(20)
        if balloon[0][1] > window[1]/2:
            del balloons[0]
    writer(happy_birthday, (0,40))
    writer(name, (0,-40))
    sleep(0.03)
    sn.update()
    t1.clear()

def create_balloon(balloons, color):
    balloons.append(([randint(-int(window[0]/2), int(window[0]/2)), -int(window[1]/2)], color))

sn = turtle.Screen()
sn.tracer(0)
window = (sn.window_height(), sn.window_width())

t1 = turtle.Turtle()
t2 = turtle.Turtle()
t1.hideturtle()
t2.hideturtle()
t1.pensize(1)

happy_birthday = 'HAPPY BIRTHDAY'
name = 'JHON DOE'

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
balloons = []

while True:
    create_balloon(balloons, colors[randint(0,5)])
    for frame in range(5):
        next_frame(balloons)