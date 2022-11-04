import turtle
from time import sleep
import random
t = turtle.Turtle()
s = t.getscreen()
s.colormode(255)
s.bgcolor(255, 255, 255)
t.hideturtle()
t.speed(0)
t.penup()
t.goto(-100, 100)
t.pendown()
bg_1 = 100
bg_2 = 50
bg_3 = 10
d_1 = 1
d_2 = 1
d_3 = 1

def eye(int):
    global bg_1
    global bg_2
    global bg_3
    global d_1
    global d_2
    global d_3
    for x in range(6):
        blue = random.randint(0, 255)
        red = random.randint(0, 255)
        green = random.randint(0, 255)
        t.color(red, green, blue)
        t.begin_fill()
        t.circle(int / (x + 1))
        # t.right(170)
        t.end_fill()
        if d_1 == 1:
            if bg_1 > 0:
                bg_1 -= 2
            else:
                d_1 = -1
        else:
            if bg_1 < 100:
                bg_1 += 2
            else:
                d_1 = 1
        if d_2 == 1:
            if bg_2 > 0:
                bg_2 -= 5
            else:
                d_2 = -1
        else:
            if bg_2 < 100:
                bg_2 += 5
            else:
                d_2 = 1
        if d_3 == 1:
            if bg_3 > 0:
                bg_3 -= 1
            else:
                d_3 = -1
        else:
            if bg_3 < 100:
                bg_3 += 1
            else:
                d_3 = 1
        s.bgcolor(bg_1, bg_2, bg_3)

for x in range(100):
    eye((x + 1) * 5)
    t.penup()
    t.fd(x * 10)
    t.right(95)
    t.pendown()

sleep(6)
