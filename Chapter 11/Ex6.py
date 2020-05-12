def scalar_mult(s, v):
    x = []
    for value in range(len(v)):
        x.append(s * v[value])
    print(x)


a = [1, 2, 3, 4, 5]

scalar_mult(8, a)
