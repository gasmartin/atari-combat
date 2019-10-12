import turtle

from game_modules import objects, physics, sounds, utils

playing = True

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
