import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.color("blue")

def koch(t, n, size):
    order = 0
    if n == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
           koch(t, order -1, size/3)
           t.left(angle)


def new_fractal(n):
    order = 0
    if n == 0:
        koch(tess, 2, 200)
        tess.left(-120)
    else:
        for i in range(order):
            new_fractal(0)

new_fractal(3)

wn.exitonclick()
