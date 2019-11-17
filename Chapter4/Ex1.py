import turtle

wn = turtle.Screen()
turtle.speed(0)


def square():
    for o in range(0, 4):
        turtle.forward(10)
        turtle.left(90)


for u in range(0, 5):
    square()
    turtle.penup()
    turtle.forward(20)
    turtle.pendown()

wn.mainloop()
