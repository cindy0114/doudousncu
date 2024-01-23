num=[int(i) for i in input().split()]
#n0:答题数量，n1：答题人数
for i in range(num[1]):
    temp = [i for i in input()]
    s = ''
    for i in temp:
        if i == 'y':
            s += '0'
        if i == 'n':
            s += '1'
    s=int(s,2)
    print(s + 1)