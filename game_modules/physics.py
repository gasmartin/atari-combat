from math import cos, radians, sin
import turtle


def calculate_angle(turtle, speed, degrees):
    dx = speed * cos(radians(degrees))
    dy = speed * sin(radians(degrees))
    turtle.dx = round(dx, 2)
    turtle.dy = round(dy, 2)


def calculate_angle_shot(degrees):
    dx = 100 * cos(radians(degrees))
    dy = 100 * sin(radians(degrees))
    return [dx, dy]

# Paredes e balas (não mudam de angulo)
def aabb_collision(rect, rect2):
    rx, ry = rect.xcor(), rect.ycor()
    rx2, ry2 = rect2.xcor(), rect2.ycor()

    rect_sizes = rect.shapesize()[:2]
    rect_half_height = rect_sizes[0] * 10
    rect_half_width = rect_sizes[1] * 10

    rect2_sizes = rect2.shapesize()[:2]
    rect2_half_height = rect2_sizes[0] * 10
    rect2_half_width = rect2_sizes[1] * 10

    return rx < rx2 + rect2_half_width and rx + rect_half_width > rx2 \
            and ry < ry2 + rect2_half_height and ry + rect_half_height > ry2
