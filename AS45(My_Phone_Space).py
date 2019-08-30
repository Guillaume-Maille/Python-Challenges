# You would like to show people how much space images take up on their phone to help them decide how much space they need.
# This needs to take into different resolutions
# https://docs.google.com/forms/d/e/1FAIpQLSfR1DK0HBOTJ_wcTUHqivIi-MGhELTTblj-jxC7NYRyeiUESw/viewform?entry.761381367=AS45&entry.408774996

x = 0

while x == 0:
    r = int(input("Image resolution:"))
    print()
    l = int(input("Image length:"))
    print()
    w = int(input("Image width:"))
    print()
    c = int(input("Colour depth:"))
    N = (w*r*l*r)
    A = (N*c) / 8
    print("Image size:", A, "Bytes")
    print()
    yn = input("Would you like to calculate the size of another image?(YES/NO)")
    if yn == 'YES':
        ()
    else:
        x = 1
