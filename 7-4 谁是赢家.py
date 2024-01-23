n=[int(i) for i in input().split()]
s=input()
if s.count(str(n.index(max(n))))>0:
    if n.index(max(n))==0:
        print('The winner is a: %s + %d'%(n[0],s.count('0')))
    else:
        print('The winner is b: %s + %d'%(n[1],s.count('1')))
else:
    if n.index(min(n))==0:
        print('The winner is a: %s + %d'%(n[0],s.count('0')))
    else:
        print('The winner is b: %s + %d'%(n[1],s.count('1')))
