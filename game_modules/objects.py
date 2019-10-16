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
    hitbox.shapesize(stretch_wid=3, stretch_len=3)
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


def create_bullet(x, y, color):
    bullet = turtle.Turtle()
    bullet.speed(0)
    bullet.shape("square")
    bullet.shapesize(stretch_wid=0.5, stretch_len=0.5)
    bullet.color(color)
    bullet.penup()
    bullet.goto(x, y)
    return bullet


def create_map_layout(map):
    # valores iniciais de onde começa a tela, tanto o x quanto o y
    x_ini = -640
    y_ini = 280  # antigo 280

    # variaveis que eu vou manipular pra posicionar as caixinhas
    x = x_ini
    y = y_ini

    # linhas e colunas do mapa
    rows = len(map)
    columns = len(map[0])

    # criando a lista de caixinhas
    hit_boxes = []
    for i in range(0, rows):
        for j in range(0, columns):
            if map[i][j] == '0':
                hitbox = create_hitbox(x, y)
                hitbox.shapesize(2, 2)
                hit_boxes.append(hitbox)
            x += 19.8  # to colocando um pouco menos que 20
            # pq senão passa da tela
        x = x_ini
        y -= 14.3  # é quebrado assim pq eu não to pegando a
        # tela toda, to deixando um espaço pro placar

    return hit_boxes
