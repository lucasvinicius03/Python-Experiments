import turtle
from time import sleep

fps = 30
gravity = 10/fps
force = 5

screen = turtle.Screen()
turs = [turtle.Turtle(), turtle.Turtle()]

screen.tracer(0)

turs[0].color('black', 'red')
for tur in turs:
    tur.pensize(2)
    tur.hideturtle()
turs[0].goto(-150,150)
turs[1].goto(-150,160)
turs[1].clear()

for x in range(50):
    for tur in turs:
        tur.goto(tur.pos()[0] + force, tur.pos()[1] + gravity)
    turs[0].clear()
    turs[0].begin_fill()
    turs[0].circle(20)
    turs[0].end_fill()
    screen.update()
    gravity -= 10/fps
    sleep(1/fps)

screen.exitonclick()