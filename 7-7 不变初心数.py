a = int(input())
def chuxin(x):
    global xin
    f = 0
    for i in range(3,10):
        num = str(x*i)
        sum1 = 0
        for j in num:
            sum1 += int(j)
        if sum1==xin:
            #print(sum1)
            f += 1
            continue
        else:
            break
    if f == 7:
        return True
    else:
        return False
while a:
    a -= 1
    a1 = int(input())
    b1 = str(a1*2)
    xin = 0
    for i in b1:
        xin += int(i)
    if chuxin(a1):
        print(xin)
    else:
        print("NO")