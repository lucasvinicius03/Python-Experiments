import turtle
import math
import random

def draw_square(sides):
    t1.pencolor(0, 0, 0)
    t1.fillcolor(random.randint(0,255),random.randint(0,255),random.randint(0,255))
    t1.begin_fill()
    for side in sides:
        t1.forward(side)
        t1.left(90)
    t1.end_fill()

def calculate_new_square(old_sides, internal_l1):
    triangle1 = calculate_triangle(5, adjacent=internal_l1)
    triangle2 = calculate_triangle(5, adjacent=old_sides[1]-triangle1[2])
    triangle3 = calculate_triangle(5, adjacent=old_sides[2]-triangle2[2])
    triangle4 = calculate_triangle(5, hypotenuse=old_sides[3]-triangle3[2])
    internal_l1 = triangle1[0] - triangle4[2]
    return [triangle1[0], triangle2[0], triangle3[0], triangle4[1]], internal_l1

def calculate_triangle(angle, opposite=None, adjacent=None, hypotenuse=None):
    sin = math.sin(math.radians(angle))
    cos = math.cos(math.radians(angle))
    if opposite:
        c = opposite
        a = c/sin
        b = math.sqrt(a**2 - c**2)
        return a, b, c
    elif adjacent:
        b = adjacent
        a = b/cos
        c = math.sqrt(a**2 - b**2)
        return a, b, c
    elif hypotenuse:
        a = hypotenuse
        c = a*sin
        b = math.sqrt(a**2 - c**2)
        return a, b, c

# size_of_screen = int(input('Enter screen size: '))
size_of_screen = 600

screen = turtle.Screen()
screen.title('SQUARE THINGY')
screen.setup(width=size_of_screen, height=size_of_screen)
screen.colormode(255)
t1 = turtle.Turtle()
t1.speed(8)
t1.pu()
t1.setpos((-(size_of_screen)/2)+20,(-(size_of_screen)/2)+20)
t1.pd()

sides = [size_of_screen-40, size_of_screen-40, size_of_screen-40, size_of_screen-40]
internal_l1 = size_of_screen-40

while sides[3] > 10:
    draw_square(sides)
    sides, internal_l1 = calculate_new_square(sides, internal_l1)
    t1.left(5)
screen.exitonclick()