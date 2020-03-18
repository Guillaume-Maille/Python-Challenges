# TASK 4 – Algorithm modification
# Additional information needs to be saved for each book, such as a publication date.
# An additional task is needed to create a new file from the original file. The task will prompt the user to
# input the additional information for each book.
# Consider possible validation of the additional information.
# Write program code for the additional task c.


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
