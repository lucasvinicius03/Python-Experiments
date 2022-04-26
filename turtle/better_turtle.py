import turtle
from math import radians, sin, cos
from time import sleep

class BetterTurtle(turtle.Turtle):
    def jump(self, x: tuple[float, float], y: float=None):
        self.penup()
        self.goto(x, y)
        self.pendown()

    def calc_circle(self, radius_x, radius_y, inclination, angle):
        if not radius_y: radius_y = radius_x
        inclination_radians, angle_radians = radians(inclination), radians(angle)
        inclination_sin, angle_sin = sin(inclination_radians), sin(angle_radians)
        inclination_cos, angle_cos = cos(inclination_radians), cos(angle_radians)
        x = (radius_x * angle_cos * inclination_cos) - (radius_y * angle_sin * inclination_sin)
        y = (radius_x * angle_cos * inclination_sin) + (radius_y * angle_sin * inclination_cos)
        return (x, y)

    def ellipsis(self, radius_x: float, radius_y: float=None, inclination=0, extent=360, steps=90):
        current_angle = 0
        self.jump(self.calc_circle(radius_x, radius_y, inclination, current_angle))
        for _ in range(steps):
            current_angle += 360/steps
            if current_angle <= extent:
                self.goto(self.calc_circle(radius_x, radius_y, inclination, current_angle))

class Screen3D():
    def __init__(self, focal_length, cam_coords=(0,0,0)) -> None:
        self.__screen = turtle.Screen()
        self.__focal_length = focal_length
        self.__points = {'cam': cam_coords}
        self.__orig_points = {'cam': cam_coords}
        self.__lines = []
        self.__turtle = BetterTurtle()
        self.__turtle.hideturtle()
    
    def mainloop(self):
        self.__screen.mainloop()

    def setup_3d(self, focal_length=None, cam_coords=None):
        if cam_coords and (self.__points['cam'] != cam_coords):
            self.__points['cam'] = cam_coords
        if focal_length and (self.__focal_length != focal_length):
            self.__focal_length = focal_length

    def move_cam(self, offset):
        self.setup_3d(cam_coords=self.point_translate(self.__points['cam'], offset))

    def points_add(self, **points):
        for k,v in points.items():
            self.__points[k] = v
            self.__orig_points[k] = v
    def points_remove(self, *points):
        for x in points:
            del self.__points[x]
            del self.__orig_points[x]
    def point_translate(self, point, translation):
        x, y, z = point
        x += translation[0]
        y += translation[1]
        z += translation[2]
        return (x, y, z)
    def points(self):
        return self.__points

    def lines_add(self, *lines):
        for line in lines:
            self.__lines.append(line)
    def lines_remove(self, *lines):
        for x in lines:
            self.__lines.remove(x)
    def lines(self):
        return self.__lines

    def object_rotate(self, obj, rotation, origin=None):
        sin_x, cos_x = sin(radians(rotation[0])), cos(radians(rotation[0]))
        sin_y, cos_y = sin(radians(rotation[1])), cos(radians(rotation[1]))
        sin_z, cos_z = sin(radians(rotation[2])), cos(radians(rotation[2]))
        if not origin:
            origin_x = sum(self.__points[point][0] for point in obj)/len(obj)
            origin_y = sum(self.__points[point][1] for point in obj)/len(obj)
            origin_z = sum(self.__points[point][2] for point in obj)/len(obj)
            origin = (origin_x, origin_y, origin_z)
        for point in obj:
            x, y, z = self.point_translate(self.__points[point], (-origin[0], -origin[1], -origin[2]))
            x2, y2, z2 = x, y, z
            if rotation[0]:
                y2 = (y * cos_x) - (z * sin_x)
                z2 = (y * sin_x) + (z * cos_x)
                y, z = y2, z2
            if rotation[1]:
                x2 = (x * cos_y) + (z * sin_y)
                z2 = (z * cos_y) - (x * sin_y)
                x, z = x2, z2
            if rotation[2]:
                x2 = (x * cos_z) - (y * sin_z)
                y2 = (x * sin_z) + (y * cos_z)
                x, y = x2, y2
            self.__points[point] = self.point_translate((x, y, z), origin)

    def calc_projection(self, point_3d: tuple[float, float, float]) -> tuple[float, float]:
        x = (point_3d[0] - self.__points['cam'][0]) * (self.__focal_length / (point_3d[2] - self.__points['cam'][2]))
        y = (point_3d[1] - self.__points['cam'][1]) * (self.__focal_length / (point_3d[2] - self.__points['cam'][2]))
        return (x, y)

    def draw_frame(self):
        self.__screen.tracer(0)
        for t in turtle.turtles():
            if isinstance(t, BetterTurtle):
                t.clear()
        for x in self.__lines:
            self.__turtle.jump(self.calc_projection(self.__points[x[0]]))
            self.__turtle.goto(self.calc_projection(self.__points[x[1]]))
        self.__screen.tracer(1)
    def draw_frame_sync(self, *steps):
        for t in turtle.turtles():
            if isinstance(t, BetterTurtle):
                t.clear()
        for lines in steps:
            self.__screen.tracer(0)
            tur = {line:{'t':BetterTurtle()} for line in lines}
            for line in lines:
                tur[line]['t'].jump(self.calc_projection(self.__points[line[0]]))
                tur[line]['t'].hideturtle()
                tur[line]['t'].setheading(tur[line]['t'].towards(self.calc_projection(self.__points[line[1]])))
                tur[line]['m'] = tur[line]['t'].distance(self.calc_projection(self.__points[line[1]]))*0.01
            for x in range(100):
                for line in lines:
                    tur[line]['t'].forward(tur[line]['m'])
                    self.__screen.update()
            self.__screen.tracer(1)
        


if __name__ == '__main__':
    import random
    screen3d = Screen3D(500, (0,0,250))
    point0 = (-125, -125, 1000)
    lengthx = 500
    lengthy = 500
    lengthz = 500
    screen3d.points_add(a=point0,
                        b=(point0[0]+(lengthx/2), point0[1], point0[2]), 
                        c=(point0[0]+(lengthx/2), point0[1], point0[2]+(lengthz/2)), 
                        d=(point0[0], point0[1], point0[2]+(lengthz/2)))
    screen3d.points_add(e=(point0[0], point0[1]+(lengthy/2), point0[2]), 
                        f=(point0[0]+(lengthx/2), point0[1]+(lengthy/2), point0[2]), 
                        g=(point0[0]+(lengthx/2), point0[1]+(lengthy/2), point0[2]+(lengthz/2)), 
                        h=(point0[0], point0[1]+(lengthy/2), point0[2]+(lengthz/2)))
    screen3d.lines_add(('a', 'b'), ('b', 'c'), ('c', 'd'), ('d', 'a'))
    screen3d.lines_add(('e', 'f'), 'fg', ('g', 'h'), 'he')
    screen3d.lines_add('ae', 'bf', 'cg', 'dh')

    screen3d.points_add(i=(400,0,1000), j=(800, 0, 1000), k=(800, 0, 1400), l=(400, 0, 1400))
    screen3d.lines_add('ij', 'jk', 'kl', 'li')

    test = 0
    if test == 0:
        screen3d.object_rotate('abcdefgh', (random.randint(0,360), random.randint(0,360), random.randint(0,360)))
        screen3d.object_rotate('ijkl', (random.randint(0,360), random.randint(0,360), random.randint(0,360)))
        screen3d.draw_frame_sync(('ab', 'ad', 'ae', 'ij', 'il'), ('bc', 'bf', 'dc', 'dh', 'ef', 'eh', 'jk', 'lk'), ('cg', 'fg', 'hg'))
        sleep(.5)
        while True:
            screen3d.draw_frame()
            screen3d.object_rotate('abcdefgh', (5,5,5))
            screen3d.object_rotate('ijkl', (5,5,5))
            sleep(.03)
    elif test == 1:
        while True:
            for x in range(30):
                sleep(.03)
                screen3d.draw_frame()
                screen3d.move_cam((10,0,0))
            for x in range(60):
                view -= 1
                sleep(.03)
                screen3d.draw_frame()
                screen3d.move_cam((-10,0,0))
            for x in range(30):
                view += 1
                sleep(.03)
                screen3d.draw_frame()
                screen3d.move_cam((10,0,0))