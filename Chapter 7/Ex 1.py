def odd_count(x):
    n = 0
    for i in x:
        if i % 2 != 0:
            n += 1
    print(n)


v = [1, 2, 3, 4, 5, 6, 7, 8, 9]

odd_count(v)
