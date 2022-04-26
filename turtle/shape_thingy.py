import turtle
import math
import random

def draw_next_layer(distance=None, old_points=None):
    t1.fillcolor(random.randint(0,255),random.randint(0,255),random.randint(0,255))
    t1.begin_fill()
    new_points = []
    if distance:
        for x in range(num_sides):
            walk(distance, new_points)
            t1.left(360/num_sides)
    elif old_points:
        t1.goto(old_points[0])
        for x in old_points[1:]:
            t1.setheading(t1.towards(x))
            distance = t1.distance(x)
            walk(distance, new_points)
    t1.end_fill()
    new_points.append(new_points[0])
    screen.update()
    return new_points, distance

def calculate_polygon(height, num_sides):
    side = height * math.sin(math.pi/num_sides)
    return side

def walk(distance, points):
    percent = distance/100*offset
    t1.forward(percent)
    points.append(t1.pos())
    t1.forward(distance-percent)

size_of_screen = 600
height=size_of_screen-40
num_sides = 10
inradius = (height/2) * math.cos(math.pi/num_sides)
offset= 10
side = calculate_polygon(height, num_sides)

screen = turtle.Screen()
t1 = turtle.Turtle()

screen.title('SHAPE THINGY')
screen.setup(width=size_of_screen, height=size_of_screen)
screen.colormode(255)

t1.speed(0)
screen.tracer(0)
t1.pencolor(0, 0, 0)
t1.pu()
if num_sides % 2 == 0:
    t1.goto(-side/2,-(inradius))
else:
    t1.goto(-side/2, -((inradius+(height/2))/2))
t1.pd()

points, side = draw_next_layer(distance=side)
while side > 20:
    points, side = draw_next_layer(old_points=points)

screen.exitonclick()