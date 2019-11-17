import turtle

wn = turtle.Screen()
turtle.speed(0)
t = turtle.Turtle


def draw_poly(t, n, sz):
    for i in range(0, n):
        t.forward(50)
        t.left(sz)

wn.mainloop()
