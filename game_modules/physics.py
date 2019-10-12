from math import cos, radians, sin
import turtle


def calculate_angle(turtle, speed, degrees):
    dx = speed * cos(radians(degrees))
    dy = speed * sin(radians(degrees))
    turtle.dx = round(dx, 2)
    turtle.dy = round(dy, 2)


def calculate_angle_shot(degrees):
    dx = 100 * cos(radians(degrees))
    dy = 100 * sin(radians(degrees))
    return [dx, dy]
