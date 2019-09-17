import turtle
wn = turtle.Screen()

####################################################################

#1)

#ad = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

#def day():
#    x = int(input('What is your number?'))
#    print(ad[x])

#day()

####################################################################

#2)

#ad = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

#dn = int(input('Starting day number:'))
#l = int(input('Length of stay:'))

#if dn + l % 7 <= 7:
#    print('Day of return:', ad[dn + l % 7])
#else:
#    print('Day of return:', ad[dn + l % 7 - 7])

####################################################################

#3)

#a <= b

#a < b

#not a < 18 and day != 3

#not a < 18 and day == 3

####################################################################

#4)

#T

#F

#F

#F

####################################################################

#5)

#T

#T

#T

#T

#T

#T

#F

#T

####################################################################

#6)

#xs = [83, 75, 74.9, 70, 69.9, 65, 60, 59.9, 55, 50, 49.9, 45, 44.9, 40, 39.9, 2, 0]

#def grade(m):
#    if m >= 75:
#        print('First')
#    elif 70 <= m < 75:
#        print('Upper Second')
#    elif 60 <= m < 70:
#        print('Second')
#    elif 50 <= m < 60:
#        print('Third')
#    elif 45 <= m < 50:
#        print('F1 Supp')
#    elif 40 <= m < 45:
#        print('F2')
#    elif m < 40:
#        print('F3')

#for i in range(xs):
#    grade(i)

####################################################################

#7)

#def draw_bar(t, height):
#    t.begin_fill()
#    t.left(90)
#    t.forward(height)
#    t.write("  " + str(height))
#    t.right(90)
#    t.forward(40)
#    t.right(90)
#    t.forward(height)
#    t.left(90)
#    t.end_fill()
#    t.penup()
#    t.forward(10)
#    t.pendown()


#wn.bgcolor("lightgreen")

#tess = turtle.Turtle()
#tess.color("blue", "red")
#tess.pensize(3)

#xs = [48,117,200,240,160,260,220]

#for a in xs:
#    draw_bar(tess, a)

####################################################################

#8)

#def draw_bar(t, height):
#    if height >= 200:
#        tess.color("blue", "red")
#    elif 100 <= height < 200:
#        tess.color("blue", "yellow")
#    elif height < 100:
#        tess.color("blue", "green")
#    t.begin_fill()
#    t.left(90)
#    t.forward(height)
#    t.write("  " + str(height))
#    t.right(90)
#    t.forward(40)
#    t.right(90)
#    t.forward(height)
#    t.left(90)
#    t.end_fill()
#    t.penup()
#    t.forward(10)
#    t.pendown()


#wn.bgcolor("lightgreen")

#tess = turtle.Turtle()
#tess.color("blue", "red")
#tess.pensize(3)

#xs = [48,117,200,240,160,260,220]

#for a in xs:
#    draw_bar(tess, a)

####################################################################

#9)

#def draw_bar(t, height):
#    t.begin_fill()
#    t.left(90)
#    if height < 0:
#        t.forward(height)
#        t.penup()
#        t.forward(-15)
#        t.write("  " + str(height))
#        t.forward(15)
#        t.pendown()
#        t.right(90)
#        t.forward(40)
#        t.right(90)
#        t.forward(height)
#    else:
#        t.forward(height)
#        t.write("  " + str(height))
#        t.right(90)
#        t.forward(40)
#        t.right(90)
#        t.forward(height)
#    t.left(90)
#    t.end_fill()
#    t.penup()
#    t.forward(10)
#    t.pendown()


#wn.bgcolor("lightgreen")

#tess = turtle.Turtle()
#tess.color("blue", "red")
#tess.pensize(3)

#xs = [-48, 117, -200, -240, 160, -260, 220]

#for a in xs:
#    draw_bar(tess, a)

####################################################################

#10)

#def find_hypot(s1, s2):
#    print((s1**2 + s2**2)**0.5)

#find_hypot()

####################################################################

#11)

#def is_rightangled(a, b, c):
#    if (a**2 + b**2)**0.5 - c < 0.00001:
#        print('True')
#    else:
#        print('False')

#is_rightangled()

####################################################################

#12)

#def is_rightangled(x, y, z):
#    if x > y and z:
#        a = z
#        b = y
#        c = x
#    elif y > z and x:
#        a = z
#        b = x
#        c = y
#    elif z > x and y:
#        a = y
#        b = x
#        c = z
#    if (a**2 + b**2)**0.5 - c < 0.00001:
#        print('True')
#   else:
#        print('False')

#is_rightangled()

####################################################################

#13.

#import math
#a = math.sqrt(2.0)
#print(a, a*a)
#print(a*a == 2.0)

####################################################################

wn.mainloop()
