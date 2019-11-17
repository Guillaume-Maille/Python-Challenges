import turtle

wn = turtle.Screen()
turtle.speed(0)


def star():
    for k in range(9):
        turtle.right(144)
        turtle.forward(100)


for i in range(5):
    star()
    turtle.penup()
    turtle.forward(350)
    turtle.right(144)
    turtle.pendown()

wn.mainloop()
