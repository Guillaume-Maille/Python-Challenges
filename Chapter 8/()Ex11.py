import string

def subcount(substring, string):
    if string.find(substring) > -1:
        for i in string:
            x = i
            print(string[x:].find(substring))


subcount('a', 'aba')
