from math import cos, radians, sin

def calculate_angle(turtle, speed, degrees):
    dx = speed * cos(radians(degrees))
    dy = speed * sin(radians(degrees))
    turtle.dx = round(dx, 2)
    turtle.dy = round(dy, 2)