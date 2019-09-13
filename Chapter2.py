#   comment

w1 = "All"
w2 = "work"
w3 = "and"
w4 = "no"
w5 = "play"
w6 = "makes"
w7 = "Jack"
w8 = "a"
w9 = "dull"
w10 = "boy."

print(w1, w2, w3, w4, w5, w6, w7, w8, w9, w10)

################################################################################

print(6 * (1 - 2))

################################################################################

bruce = 6
print(bruce + 4)

################################################################################

p = 10000
n = 12
r = 0.08


t = int(input("How many years will the money be compounded for?"))

print(p*(1+r/n)**n*t)

################################################################################

print(5 % 2, 9 % 5, 15 % 12, 12 % 15, 6 % 6, 0 % 7)

################################################################################

ct = int(input("What is the current time (In hours (24hr)):"))
hw = int(input("In how many hours would you like the alarm to go off?"))
x = 0

t = ct + hw
if t > 24:
    x = (t / 24)
    if x > 0.99999999999999999999999999999999999999999:
        print("Alarm will go off at", t % 24, "in", t // 24, "day(s).")
    else:
        print("Alarm will go off at", t, "today.")
else:
    if x > 0.99999999999999999999999999999999999999999:
        print("Alarm will go off at", t % 24, "in", x, "day(s).")
    else:
        print("Alarm will go off at", t, "today.")
