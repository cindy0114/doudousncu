import math

a, b, c, d = map(int, input().split())

m = abs(c - a)
n = abs(d - b)

print(m + n)
