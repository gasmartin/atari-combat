import turtle


def create_screen(title, width, height):
    screen = turtle.Screen()
    screen.title(title)
    screen.bgcolor("#b0b85a")
    screen.setup(width=width, height=height)
    screen.tracer(0)
    return screen


def create_hitbox(x, y):
    hitbox = turtle.Turtle()
    hitbox.speed(0)
    hitbox.color("orange")
    hitbox.shape("square")
    hitbox.shapesize(stretch_wid=2, stretch_len=2)
    hitbox.penup()
    hitbox.goto(x, y)
    return hitbox


def create_tank(x, y, shape):
    hitbox = create_hitbox(x, y)
    hitbox.hideturtle()
    tank = turtle.Turtle()
    tank.speed(0)
    tank.shape(shape)
    tank.penup()
    tank.goto(x, y)
    if shape == "communist":
        tank.left(90)
    else:
        tank.right(90)
    return [tank, hitbox]
