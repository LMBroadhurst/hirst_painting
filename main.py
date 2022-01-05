# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract("image.png", 30)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

# print(rgb_colors)

import turtle as t
from turtle import Screen
import random

color_list = [(34, 108, 167), (245, 77, 36), (112, 163, 211), (153, 57, 85), (219, 156, 94), (201, 60, 27),
              (24, 133, 55), (246, 204, 84), (190, 151, 47), (225, 119, 152), (46, 53, 121), (221, 68, 97),
              (113, 199, 156), (147, 37, 30), (253, 202, 0), (91, 113, 192), (74, 40, 32), (248, 153, 143),
              (111, 41, 49), (155, 212, 203), (53, 174, 163), (38, 31, 67), (154, 210, 219), (43, 33, 45),
              (35, 55, 46), (99, 93, 2)]


# Get turtle into the bottom corner of the page with required settings


painter = t.Turtle()
painter.hideturtle()
painter.penup()
painter.setposition(-200, -200)
painter.pensize(7)
painter.speed(0)
t.colormode(255)

# Draw a simple circle in a random color


def draw_spot():
    painter.color(random.choice(color_list))
    painter.dot(30)


# Draw a line of spots


def line_of_spots():
    for _ in range(10):
        draw_spot()
        painter.forward(50)


# Draw the whole painting


def whole_painting():
    y = -200
    for _ in range(10):
        line_of_spots()
        y += 50
        painter.setposition(-200, y)


whole_painting()
screen = Screen()
screen.exitonclick()
