import turtle

wn = turtle.Screen()
tess = turtle.Turtle()
tess.shape("turtle")
tess.color("blue")
tess.stamp()
tess.pensize(5)

for i in range(12):
    tess.penup()
    tess.forward(100)
    tess.pendown()
    tess.forward(20)
    tess.penup()
    tess.forward(20)
    tess.stamp()
    tess.forward(-140)
    tess.right(30)

wn.mainloop()
