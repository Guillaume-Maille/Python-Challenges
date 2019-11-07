#Exercise 1

#value = 9.29

#print(f'RM{value}')

####################################################################

#Exercise 3

number = int(input("Number:"))
a = bin(number)[2::]
b = hex(number)[2::]

print(f"    Binary        Hexadecimal       Decimal\n{a:^15} {b:^15} {number:^15}")

