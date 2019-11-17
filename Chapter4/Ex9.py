import turtle

wn = turtle.Screen()
turtle.speed(0)


def star():
    for k in range(9):
        turtle.right(144)
        turtle.forward(100)


star()

wn.mainloop()
