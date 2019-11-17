def even_sum(x):
    n = 0
    for i in x:
        if i % 2 == 0:
            n += i
    print(n)


v = [1, 2, 3, 4, 5, 6, 7, 8, 9]

even_sum(v)
