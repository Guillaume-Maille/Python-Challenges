def is_rightangled(a, b, c):
    if (a**2 + b**2)**0.5 - c < 0.00001:
        print('True')
    else:
        print('False')
