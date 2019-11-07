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
