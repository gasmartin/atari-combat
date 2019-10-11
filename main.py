import turtle

from game_modules import objects, physics, utils

playing = True

def close_screen():
    global playing
    playing = False

screen = objects.create_screen("Atari Combat", 1300, 900)
root = screen.getcanvas().winfo_toplevel()
root.protocol("WM_DELETE_WINDOW", close_screen)

# Criar o shape do tanque comunista
utils.register_tank_shape(screen, "communist", "red")

# Criar o shape do tanque capitalist
utils.register_tank_shape(screen, "capitalist", "blue")

communist, communist_hitbox = objects.create_tank(-520, -100, "communist")
capitalist, capitalist_hitbox = objects.create_tank(520, -100, "capitalist")

communist_hitbox.dx = 5
communist_hitbox.dy = 0

capitalist_hitbox.dx = -5
capitalist_hitbox.dy = 0

communist_angle = 0
capitalist_angle = 180

def communist_turn_left():
    global communist_angle
    communist_angle += 30
    communist.left(30)
    communist_hitbox.left(30)
    physics.calculate_angle(communist_hitbox, communist_angle)

def communist_move():
    x, y = communist_hitbox.xcor(), communist_hitbox.ycor()
    communist_hitbox.goto(x + communist_hitbox.dx, y + communist_hitbox.dy)

def communist_turn_right():
    global communist_angle
    communist_angle -= 30
    communist.right(30)
    communist_hitbox.right(30)
    physics.calculate_angle(communist_hitbox, communist_angle)

def capitalist_turn_left():
    global capitalist_angle
    capitalist_angle += 30
    capitalist.left(30)
    capitalist_hitbox.left(30)
    physics.calculate_angle(capitalist_hitbox, capitalist_angle)

def capitalist_move():
    x, y = capitalist_hitbox.xcor(), capitalist_hitbox.ycor()
    capitalist_hitbox.goto(x + capitalist_hitbox.dx, y + capitalist_hitbox.dy)

def capitalist_turn_right():
    global capitalist_angle
    capitalist_angle -= 30
    capitalist.right(30)
    capitalist_hitbox.right(30)
    physics.calculate_angle(capitalist_hitbox, capitalist_angle)

screen.listen()
screen.onkeypress(communist_turn_left, "a")
screen.onkeypress(communist_move, "w")
screen.onkeypress(communist_turn_right, "d")
screen.onkeypress(capitalist_turn_left, "Left")
screen.onkeypress(capitalist_move, "Up")
screen.onkeypress(capitalist_turn_right, "Right")

while playing:
    screen.update()
