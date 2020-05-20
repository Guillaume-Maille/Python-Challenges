def getgrades(x):
    c = 0
    studentgrades = [34, 56, 87, 45, 76, 9, 79, 90, 100, 23, 47, 78, 67, 98, 92, 73]
    for i in studentgrades:
        c += 1
        print(c)
        if x == i:
            print("position", c)
            break


getgrades(90)
