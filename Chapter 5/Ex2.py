ad = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

dn = int(input('Starting day number:'))
l = int(input('Length of stay:'))

if dn + l % 7 <= 7:
    print('Day of return:', ad[dn + l % 7])
else:
    print('Day of return:', ad[dn + l % 7 - 7])
