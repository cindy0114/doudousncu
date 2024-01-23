n,finish = map(int,input().split())
l = []
ll = []
for i in range(n):
    problem = input()
    l.append(problem)
for i in l:
    if "qiandao" not in i and "easy" not in i:
        ll.append(i)
if len(ll) <= finish:
    print("Wo AK le")
else:
    print(ll[finish])