import turtle

def create_screen(title, width, height):
    screen = turtle.Screen()
    screen.title(title)
    screen.bgcolor("#b0b85a")
    screen.setup(width=width, height=height)
    screen.tracer(0)
    return screen
