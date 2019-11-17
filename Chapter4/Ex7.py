import turtle

wn = turtle.Screen()
turtle.speed(0)


def sum_to(n):
    x = 0
    for i in range(0, n + 1):
        x += i
    print(x)


sum_to(10)

wn.mainloop()
