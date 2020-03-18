# TASK 2 – Algorithms, arrays and pseudocode
# Declare an array to store multiple pieces of data for your activity in TASK 1. For example, a 1D array of
# STRING could store the names of students in a class.

# TASK 2.1
# Design an algorithm to search for a specific value in the array and output the array index where the
# value is found.
# Consider the differences between algorithms that search for a single rather than multiple instances of
# the value.
# Document the algorithm using:
# • structured English
# • a program flowchart
# • pseudocode.

# TASK 2.2
# Design an algorithm to manipulate data in the array, for example by sorting.
# Document the algorithm as in TASK 2.1.


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
