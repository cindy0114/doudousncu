import datetime

# 获取当前日期
now = datetime.date.today()

# 获取输入日期字符串
date_str = input()

# 将输入日期字符串转换为 date 对象
input_date = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()

# 计算相隔天数
days = (input_date - datetime.date(1958, 1, 1)).days

# 输出相隔天数
print(days)
