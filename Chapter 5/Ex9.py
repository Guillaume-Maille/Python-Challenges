import turtle

wn = turtle.Screen()
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.color("blue", "red")
tess.pensize(3)
xs = [-48, 117, -200, -240, 160, -260, 220]


def draw_bar(t, height):
    t.begin_fill()
    t.left(90)
    if height < 0:
        t.forward(height)
        t.penup()
        t.forward(-15)
        t.write("  " + str(height))
        t.forward(15)
        t.pendown()
        t.right(90)
        t.forward(40)
        t.right(90)
        t.forward(height)
    else:
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
