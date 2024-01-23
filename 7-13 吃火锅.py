a = []
b = []
c = []
while 1:
    c = input()
    if c == '.':  # 遇到符合'.'结束输入
        break
    else:
        a.append(c)

sum = 0
print(len(a))  # 第一行输出消息总条数
for i in a:
    if 'chi1 huo3 guo1' in i:
        sum += 1
        b.append(a.index(i))  # 判断有吃火锅则记录位置

if len(b) == 0:  # 无吃火锅摔脸
    print('-_-#')
else:
    print(b[0] + 1, sum)  # 第一次出现的位置和出现多少条