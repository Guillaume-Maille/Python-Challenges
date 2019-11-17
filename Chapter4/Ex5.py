import turtle

wn = turtle.Screen()
turtle.speed(0)
x = 0
y = 90

for s in range(30):
    for i in range(4):
        x += 2
        turtle.forward(x)
        turtle.left(y)

wn.mainloop()
