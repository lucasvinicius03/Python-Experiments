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
    triangles = [calculate_triangle(angle, adjacent=internal_l1)]
    for side in old_sides[1:-1]:
        triangles.append(calculate_triangle(angle, adjacent=side-triangles[-1][2]))
    triangles.append(calculate_triangle(angle, hypotenuse=old_sides[-1]-triangles[-1][2]))
    internal_l1 = triangles[0][0] - triangles[-1][2]
    new_sides = [triangle[0] for triangle in triangles[:-1]]
    new_sides.append(triangles[-1][1])
    return new_sides, internal_l1

def calculate_triangle(angle, adjacent=None, hypotenuse=None):
    cos = math.cos(math.radians(angle))
    if adjacent:
        b = adjacent
        a = b/cos
    elif hypotenuse:
        a = hypotenuse
        b = a*cos
    c = math.sqrt(a**2 - b**2)
    return a, b, c

size_of_screen = 600
num_sides = 4
sides = [size_of_screen-40 for i in range(num_sides)]
internal_l1 = size_of_screen-40
angle = 5

screen = turtle.Screen()
t1 = turtle.Turtle()

screen.title('SQUARE THINGY')
screen.setup(width=size_of_screen, height=size_of_screen)
screen.colormode(255)

t1.speed(8)
t1.pencolor(0, 0, 0)
t1.pu()
t1.setpos((-(size_of_screen)/2)+20,(-(size_of_screen)/2)+20)
t1.pd()

while sides[3] > 10:
    draw_next_layer(sides)
    sides, internal_l1 = calculate_next_layer(sides, internal_l1)
    t1.left(angle)

screen.exitonclick()