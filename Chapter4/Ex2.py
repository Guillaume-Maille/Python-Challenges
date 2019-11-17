import turtle

wn = turtle.Screen()
turtle.speed(0)
x = 20


def square(length):
    for k in range(0, 4):
        turtle.forward(length)
        turtle.left(90)


for i in range(0, 5):
    turtle.pendown()
    square(x)
    turtle.penup()
    turtle.forward(x + 10)
    turtle.left(90)
    turtle.forward(-10)
    x += 20

wn.mainloop()
