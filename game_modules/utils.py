import turtle

ball_speed = 5
tank_speed = 3


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
