p = 10000
n = 12
r = 0.08


t = int(input("How many years will the money be compounded for?"))

print(p*(1+r/n)**n*t)
