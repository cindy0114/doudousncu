# 定义一个函数来计算奇数和偶数的数量
def count_odd_even(numbers):
    odd_count = 0
    even_count = 0
    for num in numbers:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return odd_count, even_count


# 输入整数数量
N = int(input().strip())
# 输入整数列表
numbers = list(map(int, input().split()))
# 调用函数并打印结果
odd, even = count_odd_even(numbers)
print(f"{odd} {even}")