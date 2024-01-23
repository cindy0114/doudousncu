# 输入单词
word = input()

# 统计每个字母出现的次数
count = [0] * 26  # 共有 26 个小写英文字母
for c in word:
    count[ord(c) - ord('a')] += 1

# 找到出现次数最多的字母
max_count = max(count)
max_index = count.index(max_count)
max_char = chr(max_index + ord('a'))

# 输出结果
print(max_char)
print(max_count)
