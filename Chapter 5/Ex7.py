import turtle
wn = turtle.Screen()
tess = turtle.Turtle()
xs = [48, 117, 200, 240, 160, 260, 220]
wn.bgcolor("lightgreen")
tess.color("blue", "red")
tess.pensize(3)


def draw_bar(t, height):
    t.begin_fill()
    t.left(90)
    t.forward(height)
    t.write("  " + str(height))
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()
    t.penup()
    t.forward(10)
    t.pendown()


for a in xs:
    draw_bar(tess, a)
