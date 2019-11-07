import turtle

wn = turtle.Screen()
tess = turtle.Turtle()
tess.speed(0)

for i in range(0, 3):
    tess.forward(50)
    tess.right(120)

for i in range(0, 4):
    tess.forward(50)
    tess.right(90)

for i in range(0, 6):
    tess.forward(50)
    tess.right(60)

for i in range(0, 8):
    tess.forward(50)
    tess.right(45)

wn.mainloop()
