import turtle
import time

from game_modules import objects, physics, sounds, utils

playing = True

shot1 = turtle.Turtle()
shot1.hideturtle()

shot2 = turtle.Turtle()
shot2.hideturtle()

def close_screen():
    global playing
    playing = False

screen = objects.create_screen("Atari Combat", 1300, 900)
root = screen.getcanvas().winfo_toplevel()
root.protocol("WM_DELETE_WINDOW", close_screen)

# leitura do mapa, rlx que eu vou modularizar, queria dar commit logo, quem reclamar vai ter que sair no soco cmg
arq = open("mapa.txt","r")
mapa = []
linha = arq.readline()
while(linha):
    mapa.append(linha.rstrip())
    linha = arq.readline()
arq.close()

#valores iniciais de onde começa a tela, tanto o x quanto o y
x_ini = -640
y_ini = 250
 #variaveis que eu vou manipular pra posicionar as caixinhas
x = x_ini 
y = y_ini

#linhas e colunas do mapa
linhas = len(mapa)
colunas = len(mapa[0]) 

#criando a lista de caixinhas
hit_boxes = []
for i in range(0,90):
    for j in range(0,130):
        if mapa[i][j] == '0':
            hit_boxes.append(objects.create_hitbox(x,y))
        x += 9.88
    x = x_ini
    y -= 6.8

# Criar o shape do tanque comunista
utils.register_tank_shape(screen, "communist", "red")

# Criar o shape do tanque capitalista
utils.register_tank_shape(screen, "capitalist", "blue")

communist, communist_hitbox = objects.create_tank(-520, -100, "communist")
capitalist, capitalist_hitbox = objects.create_tank(520, -100, "capitalist")

communist_hitbox.dx = 5
communist_hitbox.dy = 0

capitalist_hitbox.dx = -5
capitalist_hitbox.dy = 0

communist_angle = 0
capitalist_angle = 180

# Tiros do tanque comunista

communist_shot = False
communist_shot_init = False
communist_trash_shot = False
def shot_communist():
    global communist_shot
    global communist_shot_init
    global communist_trash_shot
    communist_shot = True
    communist_shot_init = True
    communist_trash_shot = True

# Tiros do tanque capitalista

capitalist_shot = False
capitalist_shot_init = False
capitalist_trash_shot = False
def shot_capitalist():
    global capitalist_shot
    global capitalist_shot_init
    global capitalist_trash_shot
    capitalist_shot = True
    capitalist_shot_init = True
    capitalist_trash_shot = True

def communist_turn_left():
    global communist_angle
    communist_angle += 22.5
    communist.left(22.5)
    communist_hitbox.left(22.5)
    physics.calculate_angle(communist_hitbox, utils.tank_speed, communist_angle)

def communist_move():
    x, y = communist_hitbox.xcor(), communist_hitbox.ycor()
    communist_hitbox.goto(x + communist_hitbox.dx, y + communist_hitbox.dy)
    communist.goto(x + communist_hitbox.dx, y + communist_hitbox.dy)

def communist_turn_right():
    global communist_angle
    communist_angle -= 22.5
    communist.right(22.5)
    communist_hitbox.right(22.5)
    physics.calculate_angle(communist_hitbox, utils.tank_speed, communist_angle)

def capitalist_turn_left():
    global capitalist_angle
    capitalist_angle += 22.5
    capitalist.left(22.5)
    capitalist_hitbox.left(22.5)
    physics.calculate_angle(capitalist_hitbox, utils.tank_speed, capitalist_angle)

def capitalist_move():
    x, y = capitalist_hitbox.xcor(), capitalist_hitbox.ycor()
    capitalist_hitbox.goto(x + capitalist_hitbox.dx, y + capitalist_hitbox.dy)
    capitalist.goto(x + capitalist_hitbox.dx, y + capitalist_hitbox.dy)

def capitalist_turn_right():
    global capitalist_angle
    capitalist_angle -= 22.5
    capitalist.right(22.5)
    capitalist_hitbox.right(22.5)
    physics.calculate_angle(capitalist_hitbox, utils.tank_speed, capitalist_angle)

screen.listen()
screen.onkeypress(communist_turn_left, "a")
screen.onkeypress(communist_move, "w")
screen.onkeypress(communist_turn_right, "d")
screen.onkeypress(shot_communist, 'z')
screen.onkeypress(shot_capitalist, 'm')
screen.onkeypress(capitalist_turn_left, "Left")
screen.onkeypress(capitalist_move, "Up")
screen.onkeypress(capitalist_turn_right, "Right")

#score capitalista
score_cap = 0
hud_cap = turtle.Turtle()
hud_cap.speed(0)
hud_cap.shape("square")
hud_cap.color("blue")
hud_cap.penup()
hud_cap.hideturtle()
hud_cap.goto(300,262)
hud_cap.write("USA {:01d}".format(score_cap), align= "center",
                font=("Press Start 2P", 30, "normal"))

#score comunista
score_com = 0
hud_com = turtle.Turtle()
hud_com.speed(0)
hud_com.shape("square")
hud_com.color("red")
hud_com.penup()
hud_com.hideturtle()
hud_com.goto(-300,262)
hud_com.write("URSS {:01d}".format(score_com), align= "center",
                font=("Press Start 2P", 30, "normal"))

while playing:

    screen.update()

    # tiro comunista
    if(communist_shot):
        if(communist_trash_shot):
            shot1.hideturtle()
            communist_trash_shot = False
        if(communist_shot_init):
            shot1 = turtle.Turtle()
            shot1.speed(0)
            shot1.shape("circle")
            shot1.color("red")
            shot1.penup()
            shot1.turtlesize(1)
            shot1.setx(communist.xcor())
            shot1.sety(communist.ycor())
            communist_shot_init = False
        shot1.dx, shot1.dy = physics.calculate_angle_shot(communist_angle)
        if(shot1.xcor() < 630 and shot1.xcor() > -630 and shot1.ycor() < 200 and shot1.ycor() > -250):
            shot1.setx(shot1.xcor() + shot1.dx)
            shot1.sety(shot1.ycor() + shot1.dy)
        else:
            communist_shot = False
            shot1.hideturtle()
    # tiro capitalista

    if(capitalist_shot):
        if(capitalist_trash_shot):
            shot2.hideturtle()
            capitalist_trash_shot = False
        if(capitalist_shot_init):
            shot2 = turtle.Turtle()
            shot2.speed(0)
            shot2.shape("circle")
            shot2.color("blue")
            shot2.penup()
            shot2.turtlesize(1)
            shot2.setx(capitalist.xcor())
            shot2.sety(capitalist.ycor())
            capitalist_shot_init = False
        shot2.dx, shot2.dy = physics.calculate_angle_shot(capitalist_angle)
        if(shot2.xcor() < 630 and shot2.xcor() > -630 and shot2.ycor() < 200 and shot2.ycor() > -250):
            shot2.setx(shot2.xcor() + shot2.dx)
            shot2.sety(shot2.ycor() + shot2.dy)
        else:
            capitalist_shot = False
            shot2.hideturtle()
