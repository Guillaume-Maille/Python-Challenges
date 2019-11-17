def gen():
    c = 0
    x = input("7 Bits:")
    eoo = input("even or odd?")
    for i in range(7):
        if x[i] == '1':
            c += 1
    if eoo == "even":
        if c % 2 == 0:
            print(f"0{x}")
        if c % 2 > 0:
            print(f"1{x}")
    if eoo == "odd":
        if c % 2 == 0:
            print(f"1{x}")
        if c % 2 > 0:
            print(f"0{x}")


def check():
    c = 0
    x = input("8 Bits:")
    eoo = input("even or odd?")
    for i in range(8):
        if x[i] == '1':
            c += 1
    if eoo == "even":
        if c % 2 == 0:
            print('Data is valid')
        else:
            print('ERROR! Invalid data')
    if eoo == "odd":
        if c % 2 == 0:
            print('ERROR! Invalid data')
        if c % 2 > 0:
            print('Data is valid')


p = input("Would you ike to check parity or generate parity?('check' or 'gen')")
if p == 'check':
    check()
if p == 'gen':
    gen()
