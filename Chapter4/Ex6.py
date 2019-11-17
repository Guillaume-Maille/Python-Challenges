import turtle

wn = turtle.Screen()
turtle.speed(0)


def draw_poly(n, sz):
    for i in range(0, n):
        turtle.forward(50)
        turtle.left(sz)


def draw_equitriangle(sz):
    draw_poly(3, sz)


draw_equitriangle(120)

wn.mainloop()
