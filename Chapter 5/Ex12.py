def is_rightangled(x, y, z):
    if x > y and z:
        a = z
        b = y
        c = x
    elif y > z and x:
        a = z
        b = x
        c = y
    elif z > x and y:
        a = y
        b = x
        c = z
    if (a**2 + b**2)**0.5 - c < 0.00001:
        print('True')
    else:
        print('False')
