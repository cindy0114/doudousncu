n = int(input())
lst = []
for i in range(n):
    a = input().split()
    lst.append(a)
for i in range(n//2):
    for j in range(n - 1, 0, -1):
        if lst[j][0] != lst[i][0]:
            print(lst[i][1],lst[j][1])
            lst.remove(lst[j])
            n = n-1
            break