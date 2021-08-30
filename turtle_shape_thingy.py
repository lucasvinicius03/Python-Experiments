import turtle
import math
import random

def draw_next_layer(sides):
    t1.fillcolor(random.randint(0,255),random.randint(0,255),random.randint(0,255))
    t1.begin_fill()
    for side in sides:
        t1.forward(side)
        t1.left(360/len(sides))
    t1.end_fill()

def calculate_next_layer(old_sides, internal_l1):
    triangles = [calculate_triangle(angle, b=internal_l1)]
    for side in old_sides[1:-1]:
        triangles.append(calculate_triangle(angle, b=side-triangles[-1][2]))
    triangles.append(calculate_triangle(angle, b=old_sides[-1]-triangles[-1][2], subtract=True))
    internal_l1 = triangles[0][0] - triangles[-1][2]
    new_sides = [triangle[0] for triangle in triangles]
    return new_sides, internal_l1

def calculate_triangle(angle, b=None, subtract=False):
    anglea = (num_sides-2)*180/num_sides
    if subtract:
        anglea -= angle
    angleb = 180 - angle - anglea
    a = b*math.sin(math.radians(anglea))/math.sin(math.radians(angleb))
    c = b*math.sin(math.radians(angle))/math.sin(math.radians(angleb))
    return a, b, c

def calculate_polygon(height, num_sides):
    side = height * math.sin(math.pi/num_sides)
    return side

size_of_screen = 600
height=size_of_screen-40
num_sides = 4
inradius = (height/2) * math.cos(math.pi/num_sides)
angle = 5
side = calculate_polygon(height, num_sides)
sides = [side for i in range(num_sides)]
internal_l1 = side

screen = turtle.Screen()
t1 = turtle.Turtle()

screen.title('SHAPE THINGY')
screen.setup(width=size_of_screen, height=size_of_screen)
screen.colormode(255)

t1.speed(8)
t1.pencolor(0, 0, 0)
t1.pu()
if num_sides % 2 == 0:
    t1.setpos(-side/2,-(inradius))
else:
    t1.setpos(-side/2, -((inradius+(height/2))/2))
t1.pd()

while sides[-1] > 10:
    draw_next_layer(sides)
    sides, internal_l1 = calculate_next_layer(sides, internal_l1)
    t1.left(angle)

screen.exitonclick()