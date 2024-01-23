n = int(input())
for i in range(n):
    day, t = input().split()
    if day != '0':
        hi, mi = map(int, t.split(':'))
        tot_min = 24 * 60 * (int(day) - 1) + 60 * hi + mi  # 将地球人的时间全部转化为分钟
        tot_min //= 2  # 地球人总时间/2就是外星人的时间
        d = tot_min // (24 * 60) + 1  # 将总分钟拆成小时和天数
        tot_min %= 24 * 60
        he = tot_min // 60
        me = tot_min % 60
    else:
        d, he, me = 0, *map(int, t.split(':'))

    print(d, end=' ')
    print('{:02d}:{:02d}'.format(he, me))