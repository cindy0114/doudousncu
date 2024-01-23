a,b = map(int,input().split())
s = a*b
s = str(s)
s = s[::-1]
s = s.lstrip("0")
print(s)
