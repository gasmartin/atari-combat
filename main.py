import turtle

from game_modules import objects, physics

playing = True

def close_screen():
    global playing
    playing = False

screen = objects.create_screen("Atari Combat", 1300, 900)
root = screen.getcanvas().winfo_toplevel()
root.protocol("WM_DELETE_WINDOW", close_screen)

communist_hitbox = objects.create_hitbox(-520, -100, "red")
capitalist_hitbox = objects.create_hitbox(520, -100, "blue")

communist_angle = 0
capitalist_angle = 0

def communist_turn_left():
    global communist_angle
    communist_angle += 30
    communist_hitbox.left(communist_angle)
    physics.calculate_angle(communist_hitbox, communist_angle)

def communist_turn_right():
    global communist_angle
    communist_angle -= 30
    communist_hitbox.right(communist_angle)
    physics.calculate_angle(communist_hitbox, communist_angle)

def capitalist_turn_left():
    global capitalist_angle
    capitalist_angle += 30
    capitalist_hitbox.left(capitalist_angle)
    physics.calculate_angle(capitalist_hitbox, communist_angle)

def capitalist_turn_right():
    global capitalist_angle
    capitalist_angle -= 30
    capitalist_hitbox.right(capitalist_angle)
    physics.calculate_angle(capitalist_hitbox, communist_angle)

screen.listen()
screen.onkeypress(communist_turn_left, "a")
screen.onkeypress(communist_turn_right, "d")
screen.onkeypress(capitalist_turn_left, "Left")
screen.onkeypress(capitalist_turn_right, "Right")

while playing:
    screen.update()
