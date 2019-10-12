from math import cos, radians, sin

ball_speed = 5
tank_speed = 2

def calculate_angle(turtle, degrees):
    dx = tank_speed * cos(radians(degrees))
    dy = tank_speed * sin(radians(degrees))
    turtle.dx = round(dx, 2)
    turtle.dy = round(dy, 2)