# l1~l4代表1~4号轮子的胎压，l5是最低报警胎压，l6是胎压差阈值
l1,l2,l3,l4,l5,l6 = map(int,input().split(' '))
l = [l1,l2,l3,l4]
e = [] # 存储出错的轮胎胎压
maxl = max(l)
for i in l:
    if i < l5:
        e.append(i)
    else:
        if maxl - i > l6:
            e.append(i)
if len(e) == 0:
    print('Normal')
elif len(e) == 1:
    print('Warning: please check #%d!'%(l.index(e[0]) + 1))
else:
    print('Warning: please check all the tires!')