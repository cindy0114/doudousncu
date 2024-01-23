n, c = input().split()  # 输入正方形边长和组成正方形边的字符
n = int(n)

# 计算需要输出的行数（四舍五入取整）
m = (n + 1) // 2

# 按行输出正方形边
for i in range(m):
    row = c * n
    print(row)
