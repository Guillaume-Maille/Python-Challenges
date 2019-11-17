xs = [83, 75, 74.9, 70, 69.9, 65, 60, 59.9, 55, 50, 49.9, 45, 44.9, 40, 39.9, 2, 0]


def grade(m):
    if m >= 75:
        print('First')
    elif 70 <= m < 75:
        print('Upper Second')
    elif 60 <= m < 70:
        print('Second')
    elif 50 <= m < 60:
        print('Third')
    elif 45 <= m < 50:
        print('F1 Supp')
    elif 40 <= m < 45:
        print('F2')
    elif m < 40:
        print('F3')


for i in range(xs):
    grade(i)
