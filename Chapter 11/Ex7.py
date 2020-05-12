def dot_product(u, v):
    x = []
    y = 0
    for value in range(len(u)):
        x.append(u[value] * v[value])
        y += x[value]
    print(y)


a = [1, 2, 3, 4, 5]
b = [5, 4, 3, 2, 1]

dot_product(a, b)
