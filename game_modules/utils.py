from random import randint
import turtle

bullet_speed = 10
tank_speed = 5

SCREEN_WIDTH = 1300 
SCREEN_HEIGHT = 750

def map_load(map_name):
    map = open(map_name).readlines()
    return map


def register_tank_shape(screen, name, color):
    shape = turtle.Shape("compound")

    tank = turtle.Turtle(visible=False)
    tank.speed('fastest')
    tank.penup()

    tank.goto(-30, 30)

    tank.begin_poly()
    tank.goto(15, 30)
    tank.goto(15, 15)
    tank.goto(5, 15)
    tank.goto(5, 5)
    tank.goto(30, 5)
    tank.goto(30, -5)
    tank.goto(5, -5)
    tank.goto(5, -15)
    tank.goto(15, -15)
    tank.goto(15, -30)
    tank.goto(-30, -30)
    tank.goto(-30, -15)
    tank.goto(-15, -15)
    tank.goto(-15, 15)
    tank.goto(-30, 15)
    tank.goto(-30, 30)
    tank.end_poly()

    shape.addcomponent(tank.get_poly(), color)

    screen.register_shape(name, shape)

def generate_random_location(x_min, x_max):
    x_min = x_min + 30
    x_max = x_max - 30
    y_min = -280
    y_max = 210
    return (randint(x_min, x_max), randint(y_min, y_max))

def reset_bullet(bullet, x, y):
    bullet.goto(x, y)
    bullet.hideturtle()

def error():
    print("Azedou irmão, tu fez foi alguma merda ai, shutting down bitch")
