import turtle
s = turtle.getscreen()
t = turtle.Turtle()
t.speed(0)
t.pensize(2)
t.color("gray")
t.speed(0) # 1:slowest, 3:slow, 5:normal, 10:fast, 0:fastest
def eye(origin_x, origin_y):
  t.penup()
  t.setpos(origin_x, origin_y)
  t.pendown()
  rotation = 20
  for i in range(3):
    for x in range(100):
      t.forward(x/2)
      t.right(45)
    restart(origin_x, origin_y)
    t.right(rotation)
    rotation += 90

def restart(x, y):
  t.penup()
  t.setpos(x, y)
  t.pendown()

eye(-100, 100)
eye(50, 100)
