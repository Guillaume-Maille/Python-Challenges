import turtle

wn = turtle.Screen()
turtle.speed(0)


def square():
    for k in range(0, 4):
        turtle.forward(100)
        turtle.left(90)


for v in range(0, 10):
    for i in range(0, 4):
        turtle.left(90)
        square()
    turtle.left(18)

wn.mainloop()
