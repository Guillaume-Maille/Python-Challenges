def add_info():
    column = input("Add new info:")
    with open('Books.txt') as c:
        c1 = c.readlines()
    with open('NewBooks.txt', "w+") as f:
        lines = f.read().splitlines()
        for line in f:
            if line == lines[1]:
                f.write(c1[1] + column)
            else:
                for x in c1:
                    new_info = input("Enter new info:")
                    f.write(x + new_info)
