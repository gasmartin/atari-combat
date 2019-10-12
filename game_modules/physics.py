from math import cos, radians, sin
import turtle

ball_speed = 5
tank_speed = 1

def calculate_angle(turtle, degrees):
    dx = tank_speed * cos(radians(degrees))
    dy = tank_speed * sin(radians(degrees))
    turtle.dx = round(dx, 2)
    turtle.dy = round(dy, 2)

def calculate_angle_shot(degrees):
    dx = 100 * cos(radians(degrees))
    dy = 100 * sin(radians(degrees))
    return [dx, dy]
