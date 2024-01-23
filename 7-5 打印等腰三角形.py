n, char = input().split()
n = int(n)

for i in range(1, n + 1):
    print(" " * (n - i) + char * (2 * i - 1))
