import math

a, b = map(int, input().split())

if a <= b and b <= 999 and a >= 100:
    for c in range(a, b+1):
        f = c // 100
        g = (c // 10) % 10
        h = c % 10
        if c == math.pow(f, 3) + math.pow(g, 3) + math.pow(h, 3):
            print(c)
else:
    print("Invalid Value.")
