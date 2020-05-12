def add_vectors(u, v):
    x = []
    for value in range(len(u)):
        x.append(u[value] + v[value])
    print(x)


a = [1, 2, 3, 4, 5]
b = [5, 4, 3, 2, 1]

add_vectors(a, b)
