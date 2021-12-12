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
    def __init__(self, focal_length: float, cam_coords: tuple[float, float, float]=(0,0,0)) -> None:
        self.__screen = turtle.Screen()
        self.__cam_coords = cam_coords
        self.__focal_length = focal_length
        self.__points = {}
        self.__lines = []
        self.__objects = {}
        self.__turtle = BetterTurtle()
    
    def mainloop(self):
        self.__screen.mainloop()

    def setup_3d(self, focal_length: float=None, cam_coords: tuple[float, float, float]=None):
        if cam_coords and (self.__cam_coords != cam_coords):
            self.__cam_coords = cam_coords
        if focal_length and (self.__focal_length != focal_length):
            self.__focal_length = focal_length

    def move_cam(self, offset_x: float=0, offset_y: float=0, offset_z: float=0):
        self.setup_3d(cam_coords=(self.__cam_coords[0] + offset_x, self.__cam_coords[1] + offset_y, self.__cam_coords[2] + offset_z))

    def points_add(self, **points):
        for k,v in points.items():
            self.__points[k] = v
    def points_remove(self, *points):
        for x in points:
            del self.__points[x]
    def points(self):
        return self.__points

    def lines_add(self, *lines: str):
        for x in lines:
            self.__lines.append(x)
    def lines_remove(self, *lines: str):
        for x in lines:
            self.__lines.remove(x)
    def lines(self):
        return self.__lines

    def calc_projection(self, point_3d: tuple[float, float, float]) -> tuple[float, float]:
        x = (point_3d[0] - self.__cam_coords[0]) * (self.__focal_length / ((point_3d[2]/10) - self.__cam_coords[2]))
        y = (point_3d[1] - self.__cam_coords[1]) * (self.__focal_length / ((point_3d[2]/10) - self.__cam_coords[2]))
        return (x, y)

    def draw_frame(self):
        self.__screen.tracer(0)
        self.__turtle.clear()
        for x in self.__lines:
            self.__turtle.jump(self.calc_projection(self.__points[x[0]]))
            self.__turtle.goto(self.calc_projection(self.__points[x[1]]))
        self.__screen.tracer(1)

if __name__ == '__main__':
    view = 50
    screen3d = Screen3D(view)
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
    screen3d.lines_add('ab', 'bc', 'cd', 'da')
    screen3d.lines_add('ef', 'fg', 'gh', 'he')
    screen3d.lines_add('ae', 'bf', 'cg', 'dh')
    while True:
        for x in range(30):
            sleep(.03)
            screen3d.draw_frame()
            screen3d.move_cam(10, 0, 0)
        for x in range(60):
            view -= 1
            sleep(.03)
            screen3d.draw_frame()
            screen3d.move_cam(-10, 0, 0)
        for x in range(30):
            view += 1
            sleep(.03)
            screen3d.draw_frame()
            screen3d.move_cam(10, 0, 0)