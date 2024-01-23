def count_chars(s):
    letter = 0
    blank = 0
    digit = 0
    other = 0
    for c in s:
        if c.isalpha():
            letter += 1
        elif c.isspace() or c == ' ':
            blank += 1
        elif c.isdigit():
            digit += 1
        else:
            other += 1
    return letter, blank, digit, other

N = int(input())
s = input()
letter, blank, digit, other = count_chars(s)
print("letter =", letter, "blank =", blank, "digit =", digit, "other =", other)
