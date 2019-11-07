def count_letters(string, ch):
    count = 0
    for c in string:
        if c == ch:
            count += 1
    return count


count_letters('Guillaume', 'l')
