import turtle
import time

from game_modules import objects, physics, sounds, utils

playing = True

def close_screen():
    global playing
    playing = False


screen = objects.create_screen("Atari Combat", utils.SCREEN_WIDTH, utils.SCREEN_HEIGHT)
root = screen.getcanvas().winfo_toplevel()
root.protocol("WM_DELETE_WINDOW", close_screen)

# leitura do mapa
map = utils.map_load()

# criação do layout do mapa, cada bloquinho do
# layout vai ficar nessa lista para serem manipulados
map_hit_boxes = objects.create_map_layout(map)

# criação o shape do tanque comunista
utils.register_tank_shape(screen, "communist", "red")
# criação o shape do tanque capitalista
utils.register_tank_shape(screen, "capitalist", "blue")

communist, communist_hitbox = objects.create_tank(-520, 210, "communist")
capitalist, capitalist_hitbox = objects.create_tank(520, -100, "capitalist")

communist_hitbox.dx = 5
communist_hitbox.dy = 0

capitalist_hitbox.dx = -5
capitalist_hitbox.dy = 0

communist_angle = 0
capitalist_angle = 180

def random_spawn(tank, tank_hitbox, side, spinning = False):
    if side == "left":
        x_min, x_max = -650, 0
    else:
        x_min, x_max = 0, 650

    tank_is_colliding = True

    while tank_is_colliding:
        tank_hitbox.goto(utils.generate_random_location(x_min, x_max))

        tank_is_colliding = False

        for hitbox in map_hit_boxes:
            tank_is_colliding |= physics.aabb_collision(hitbox,
                                                            tank_hitbox)

    tank.goto(tank_hitbox.xcor(), tank_hitbox.ycor())

random_spawn(communist, communist_hitbox, "left")
random_spawn(capitalist, capitalist_hitbox, "right")

communist_bullet = objects.create_bullet(communist.xcor(),
                                         communist.ycor(), "red")
communist_bullet.hideturtle()

capitalist_bullet = objects.create_bullet(capitalist.xcor(),
                                          capitalist.ycor(), "blue")
capitalist_bullet.hideturtle()


def shot_communist():
    if not communist_bullet.isvisible():
        communist_bullet.goto(communist.xcor(), communist.ycor())
        communist_bullet.showturtle()


def shot_capitalist():
    if not capitalist_bullet.isvisible():
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

    communist_will_collide = False

    communist_next_hitbox = communist_hitbox.clone()
    communist_next_hitbox.goto(x + communist_hitbox.dx, y +
                               communist_hitbox.dy)

    communist_will_collide |= physics.aabb_collision(communist_next_hitbox,
                                                     capitalist_hitbox)
    for hitbox in map_hit_boxes:
        communist_will_collide |= physics.aabb_collision(hitbox,
                                                         communist_next_hitbox)

    if not communist_will_collide:
        communist_hitbox.goto(x + communist_hitbox.dx, y + communist_hitbox.dy)
        communist.goto(x + communist_hitbox.dx, y + communist_hitbox.dy)
    else:
        del communist_next_hitbox


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

    capitalist_will_collide = False

    capitalist_next_hitbox = capitalist_hitbox.clone()
    capitalist_next_hitbox.goto(x + capitalist_hitbox.dx, y +
                                capitalist_hitbox.dy)

    capitalist_will_collide |= physics.aabb_collision(capitalist_next_hitbox,
                                                      communist_hitbox)
    for hitbox in map_hit_boxes:
        capitalist_will_collide |= physics.aabb_collision(
                                   hitbox, capitalist_next_hitbox)

    if not capitalist_will_collide:
        capitalist_hitbox.goto(x + capitalist_hitbox.dx, y +
                               capitalist_hitbox.dy)
        capitalist.goto(x + capitalist_hitbox.dx, y + capitalist_hitbox.dy)
    else:
        del capitalist_next_hitbox


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
hud_victory.color("black", "red")
hud_victory.penup()
hud_victory.hideturtle()
hud_victory.goto(0, -5)


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

    random_spawn(communist, communist_hitbox, "left")
    random_spawn(capitalist, capitalist_hitbox, "right")

    update_score()

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


while playing:

    screen.update()

    # Lógica do tiro comunista
    if communist_bullet.isvisible():
        x, y = communist_bullet.xcor(), communist_bullet.ycor()
        physics.calculate_angle(communist_bullet, utils.bullet_speed,
                                communist_angle)
        communist_bullet.goto(x + communist_bullet.dx, y + communist_bullet.dy)

        for hitbox in map_hit_boxes:
            if physics.aabb_collision(hitbox, communist_bullet):
                utils.reset_bullet(communist_bullet, communist.xcor(),
                                   communist.ycor())

        if physics.aabb_collision(capitalist_hitbox, communist_bullet):
            score_com += 1
            update_score()
            utils.reset_bullet(communist_bullet, communist.xcor(),
                               communist.ycor())

    # Lógica do tiro capitalista
    if capitalist_bullet.isvisible():
        x, y = capitalist_bullet.xcor(), capitalist_bullet.ycor()
        physics.calculate_angle(capitalist_bullet, utils.bullet_speed,
                                capitalist_angle)
        capitalist_bullet.goto(x + capitalist_bullet.dx, y +
                               capitalist_bullet.dy)

        for hitbox in map_hit_boxes:
            if physics.aabb_collision(hitbox, capitalist_bullet):
                utils.reset_bullet(capitalist_bullet, capitalist.xcor(),
                                   capitalist.ycor())

        if physics.aabb_collision(communist_hitbox, capitalist_bullet):
            score_cap += 1
            update_score()
            utils.reset_bullet(capitalist_bullet, capitalist.xcor(),
                               capitalist.ycor())

    # codição de vitória
    if score_cap == 5 or score_com == 5:
        screen.ontimer(restart, 4000)
        winner = 'Capitalist' if score_cap > score_com else 'Communist'
        score_cap = score_com = 0
        hud_victory.write(
            "Victory {}\nAguarde o jogo será reiniciado.".format(winner),
            align="center", font=("Press Start 2P", 30, "normal"))
