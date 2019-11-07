import turtle


def spin(t, sz):
    b.speed(0)
    b.hideturtle()
    b.pencolor("gold")
    i = sz + 1
    f = 0
    while True:
        f += 0.355
        t.forward(f)
        t.left(i)


b = turtle.Turtle()
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Turtle functions")
b.speed(0)


spin(b, 45)
wn.mainloop()
