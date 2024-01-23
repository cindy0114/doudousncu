def find_ability(k, l, w):
    def check(mid):
        for i in range(k):
            for j in range(1 << (k - i - 1)):
                if mid > l[i][j]:
                    return False
        return True

    left, right = 1, 10 ** 9
    while left < right:
        mid = (left + right) // 2
        if check(mid):
            right = mid
        else:
            left = mid + 1

    if left == w:
        return "No Solution"
    else:
        return [left] + find_ability(k - 1, l, w)

k = int(input())
l = []
for _ in range(k):
    l.append([int(x) for x in input().split()])
w = int(input())
result = find_ability(k, l, w)
print(" ".join(str(x) for x in result))
