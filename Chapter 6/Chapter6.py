import sys

def absolute_value(x):
    if x < 0:
        return -x
    return x


def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)


def test_suite():
    """ Run the suite of tests for code in this module (this file).
    """
    test(turn_clockwise("N") == "E")
    test(turn_clockwise("W") == "N")


####################################################################

#1)

#NOT WORKING


def turn_clockwise(p):
    cl = ['N', 'E', 'S', 'W']
    for i in range(0, 4):
        if p == cl[i]:
            x = i + 1
    if x == 5:
        print('N')
    else:
        print(cl[x])

turn_clockwise('N')

test_suite()
