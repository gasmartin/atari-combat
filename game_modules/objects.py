import turtle

def create_screen(title, width, height):
    screen = turtle.Screen()
    screen.title(title)
    screen.bgcolor("#b0b85a")
    screen.setup(width=width, height=height)
    screen.tracer(0)
    return screen

def create_hitbox(x, y, color):
    hitbox = turtle.Turtle()
    hitbox.speed(0)
    hitbox.color(color)
    hitbox.shape("square")
    hitbox.shapesize(stretch_wid=3, stretch_len=4)
    hitbox.penup()
    hitbox.goto(x, y)
    return hitbox
