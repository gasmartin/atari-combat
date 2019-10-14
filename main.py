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

# leitura do mapa
map = utils.map_load()

# criação do layout do mapa, cada bloquinho do layout vai ficar nessa lista para serem manipulados
map_hit_boxes = objects.create_map_layout(map)

# criar o shape do tanque comunista
utils.register_tank_shape(screen, "communist", "red")

# criar o shape do tanque capitalista
utils.register_tank_shape(screen, "capitalist", "blue")

communist, communist_hitbox = objects.create_tank(-520, -100, "communist")
capitalist, capitalist_hitbox = objects.create_tank(520, -100, "capitalist")

communist_hitbox.dx = 5
communist_hitbox.dy = 0

capitalist_hitbox.dx = -5
capitalist_hitbox.dy = 0

communist_angle = 0
capitalist_angle = 180

communist_bullet = objects.create_bullet(communist.xcor(), communist.ycor(), "red")
communist_bullet.hideturtle()

capitalist_bullet = objects.create_bullet(capitalist.xcor(), capitalist.ycor(), "blue")
capitalist_bullet.hideturtle()

# tiros do tanque comunista
communist_shot = False


def shot_communist():
    global communist_shot
    if not communist_shot:
        communist_shot = True
        communist_bullet.goto(communist.xcor(), communist.ycor())
        communist_bullet.showturtle()


# tiros do tanque capitalista
capitalist_shot = False


def shot_capitalist():
    global capitalist_shot
    if not capitalist_shot:
        capitalist_shot = True
        capitalist_bullet.goto(capitalist.xcor(), capitalist.ycor())
        capitalist_bullet.showturtle()


def communist_turn_left():
    global communist_angle
    communist_angle += 22.5
    communist.left(22.5)
    physics.calculate_angle(communist_hitbox, utils.tank_speed,
                            communist_angle)


def communist_move():
    x, y = communist_hitbox.xcor(), communist_hitbox.ycor()
    communist_hitbox.goto(x + communist_hitbox.dx, y + communist_hitbox.dy)
    communist.goto(x + communist_hitbox.dx, y + communist_hitbox.dy)


def communist_turn_right():
    global communist_angle
    communist_angle -= 22.5
    communist.right(22.5)
    physics.calculate_angle(communist_hitbox, utils.tank_speed,
                            communist_angle)


def capitalist_turn_left():
    global capitalist_angle
    capitalist_angle += 22.5
    capitalist.left(22.5)
    physics.calculate_angle(capitalist_hitbox, utils.tank_speed,
                            capitalist_angle)


def capitalist_move():
    x, y = capitalist_hitbox.xcor(), capitalist_hitbox.ycor()
    capitalist_hitbox.goto(x + capitalist_hitbox.dx, y + capitalist_hitbox.dy)
    capitalist.goto(x + capitalist_hitbox.dx, y + capitalist_hitbox.dy)


def capitalist_turn_right():
    global capitalist_angle
    capitalist_angle -= 22.5
    capitalist.right(22.5)
    physics.calculate_angle(capitalist_hitbox, utils.tank_speed,
                            capitalist_angle)


# score capitalista
score_cap = 0
hud_cap = turtle.Turtle()
hud_cap.speed(0)
hud_cap.shape("square")
hud_cap.color("blue")
hud_cap.penup()
hud_cap.hideturtle()
hud_cap.goto(300, 292)  # antigo 300,262
hud_cap.write("USA {:01d}".format(score_cap), align="center",
              font=("Press Start 2P", 30, "normal"))

# score comunista
score_com = 0
hud_com = turtle.Turtle()
hud_com.speed(0)
hud_com.shape("square")
hud_com.color("red")
hud_com.penup()
hud_com.hideturtle()
hud_com.goto(-300, 292)  # antigo -300,262
hud_com.write("URSS {:01d}".format(score_com), align="center",
              font=("Press Start 2P", 30, "normal"))

# mensagem de vitoria
hud_victory = turtle.Turtle()
hud_victory.speed(0)
hud_victory.shape("square")
hud_victory.color("black")
hud_victory.penup()
hud_victory.hideturtle()
hud_victory.goto(0, 100)

# Atualizar o score do jogo
def update_score():
    global score_cap
    global score_com
    hud_cap.clear()
    hud_com.clear()
    hud_cap.write("USA {:01d}".format(score_cap), align="center",
                  font=("Press Start 2P", 30, "normal"))
    hud_com.write("URSS {:01d}".format(score_com), align="center",
                  font=("Press Start 2P", 30, "normal"))

# reiniciar o jogo
def restart():
    global score_cap
    score_cap = 0
    global score_com
    score_com = 0
    hud_cap.clear()
    hud_com.clear()
    hud_cap.write("USA {:01d}".format(score_cap), align="center",
                  font=("Press Start 2P", 30, "normal"))
    hud_com.write("URSS {:01d}".format(score_com), align="center",
                  font=("Press Start 2P", 30, "normal"))
    hud_victory.clear()


screen.listen()
screen.onkeypress(communist_turn_left, "a")
screen.onkeypress(communist_move, "w")
screen.onkeypress(communist_turn_right, "d")
screen.onkeypress(shot_communist, 'c')
screen.onkeypress(capitalist_turn_left, "j")
screen.onkeypress(capitalist_move, "i")
screen.onkeypress(capitalist_turn_right, "l")
screen.onkeypress(shot_capitalist, 'n')
screen.onkeypress(restart, "space")

while playing:

    screen.update()

    # tiro comunista
    if(communist_shot):
        physics.calculate_angle(communist_bullet, utils.bullet_speed, communist_angle)
        if communist_bullet.xcor() < 630 and communist_bullet.xcor() > -630 and \
                communist_bullet.ycor() < 200 and communist_bullet.ycor() > -250:
            communist_bullet.setx(communist_bullet.xcor() + communist_bullet.dx)
            communist_bullet.sety(communist_bullet.ycor() + communist_bullet.dy)
        else:
            communist_shot = False
            communist_bullet.goto(communist.xcor(), communist.ycor())
            communist_bullet.hideturtle()

    # tiro capitalista
    if(capitalist_shot):
        physics.calculate_angle(capitalist_bullet, utils.bullet_speed, capitalist_angle)
        if capitalist_bullet.xcor() < 630 and capitalist_bullet.xcor() > -630 and \
                capitalist_bullet.ycor() < 200 and capitalist_bullet.ycor() > -250:
            capitalist_bullet.setx(capitalist_bullet.xcor() + capitalist_bullet.dx)
            capitalist_bullet.sety(capitalist_bullet.ycor() + capitalist_bullet.dy)
        else:
            capitalist_shot = False
            capitalist_bullet.goto(capitalist.xcor(), capitalist.ycor())
            capitalist_bullet.hideturtle()

    
    if capitalist_bullet.isvisible() and physics.aabb_collision(communist_hitbox, capitalist_bullet):
        score_cap += 1
        update_score()
        capitalist_shot = False
        capitalist_bullet.goto(capitalist.xcor(), capitalist.ycor())
        capitalist_bullet.hideturtle()

    if communist_bullet.isvisible() and physics.aabb_collision(capitalist_hitbox, communist_bullet):
        score_com += 1
        update_score()
        communist_shot = False
        communist_bullet.goto(communist.xcor(), communist.ycor())
        communist_bullet.hideturtle()

    # codição de vitória
    if score_cap == 5 or score_com == 5:
        winner = 'Capitalist' if score_cap > score_com else 'Communist'
        score_cap = score_com = 0
        hud_victory.write(
            "Victory {}\nPress [Space] to restart game.".format(winner),
            align="center", font=("Press Start 2P", 30, "normal"))
