n = int(input())
scores = []
for i in range(n):
    scores.append(int(input()))

pass_count = len([s for s in scores if s >= 60])
excellent_count = len([s for s in scores if s >= 85])

pass_rate = int(round(pass_count / n * 100))
excellent_rate = int(round(excellent_count / n * 100))

print(str(pass_rate) + '%')
print(str(excellent_rate) + '%')
