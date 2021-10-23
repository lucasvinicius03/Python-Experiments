import turtle
import math
from time import sleep

def ellipse(tur, r1, r2, angle=360):
    pyramid_base_points = []
    for a in range(angle+1):
        x = pyramid_pos[0] + (r1 * math.cos(math.radians(a)))
        y = pyramid_pos[1] + (r2 * math.sin(math.radians(a)))
        if a in pyramid_base_angles:
            pyramid_base_points.append((x, y))
        jump(tur, (x, y))
    return pyramid_base_points

def draw_pyramid(tur, pyramid_points, top):
    jump(tur, pyramid_points[0])
    for p in pyramid_points:
        tur.goto(p)
        tur.goto(pyramid_pos[0], pyramid_pos[1]+top)
        jump(t1, p)
    tur.goto(pyramid_points[0])

def jump(tur, pos):
    tur.pu()
    tur.goto(pos)
    tur.pd()

screen = turtle.Screen()
screen.tracer(0)
t1 = turtle.Turtle()
t1.hideturtle()

pyramid_base_sides = 4
pyramid_height = 200
pyramid_pos = [0, -100]
pyramid_base_angles = [x for x in range(15, 375, 360//pyramid_base_sides)]

jump(t1, pyramid_pos)
first_pyramid = ellipse(t1, 100, 25)
screen.tracer(1)
draw_pyramid(t1, first_pyramid, pyramid_height)
sleep(.3)
screen.tracer(0)

while True:
    pyramid_base = ellipse(t1, 100, 25)
    draw_pyramid(t1, pyramid_base, pyramid_height)
    for i in range(len(pyramid_base_angles)):
        pyramid_base_angles[i] += 1
        if pyramid_base_angles[i] >= 360:
            pyramid_base_angles[i] -= 360
    jump(t1, pyramid_pos)
    screen.update()
    sleep(.01)
    t1.clear()