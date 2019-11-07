xs = [12, 10, 32, 3, 66, 17, 42, 99, 20]

for i in range(0, 9):
    print(xs[i])

for i in range(0, 9):
    print(xs[i])
    print(int(xs[i]**2))

total = 0

for i in range(0, 9):
    total += xs[i]
print(total)
