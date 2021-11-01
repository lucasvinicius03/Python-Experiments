import turtle
import math
from time import sleep

def calculate_points(pos, r1, r2, angles):
    points = []
    for a in angles:
        x = pos[0] + (r1 * math.cos(math.radians(a)))
        y = pos[1] + (r2 * math.sin(math.radians(a)))
        points.append((x, y))
    return points

def draw_pyramid(tur, draw=False):
    y_points = calculate_points(pyramid_pos, 0, pyramid_height//2, pyramid_y_angles)
    x_points = calculate_points(y_points[1], pyramid_width, pyramid_width*math.cos(math.radians(pyramid_y_angles[1])), pyramid_x_angles)
    if draw: 
        screen.tracer(1)
    jump(tur, x_points[0])
    for p in x_points:
        tur.goto(p)
        tur.goto(y_points[0])
        jump(t1, p)
    tur.goto(x_points[0])
    screen.tracer(0)

def jump(tur, pos):
    tur.pu()
    tur.goto(pos)
    tur.pd()

screen = turtle.Screen()
t1 = turtle.Turtle()
t1.hideturtle()

pyramid_base_sides = 4
pyramid_height = 200
pyramid_width = 100
spin_x = True
spin_y = True
pyramid_pos = [0, 0]
pyramid_x_angles = [x for x in range(15, 375, 360//pyramid_base_sides)]
pyramid_y_angles = [80, 260]

draw_pyramid(t1, True)

while True:
    draw_pyramid(t1)
    if spin_x:
        for i in range(len(pyramid_x_angles)):
            pyramid_x_angles[i] += 1
            if pyramid_x_angles[i] >= 360:
                pyramid_x_angles[i] -= 360
    if spin_y:
        for i in range(len(pyramid_y_angles)):
            pyramid_y_angles[i] += 1
            if pyramid_y_angles[i] >= 360:
                pyramid_y_angles[i] -= 360
    screen.update()
    sleep(.01)
    t1.clear()