import re


def calculate_gpa(scores):
    score_dict = {
        '优秀': 4.5,
        '良好': 3.5,
        '中等': 2.5,
        '及格': 1.5,
        '不及格': 0
    }
    gpa_sum = 0
    total_credits = 0

    for i in range(2, len(scores)):
        if i % 2 == 0:
            try:
                score = float(scores[i])
                credit = float(re.findall(r'\d+\.\d+', scores[i + 1])[0])  # 提取成绩后面的数字
                gpa_sum += score_dict.get(scores[i - 1], 0) * credit
                total_credits += credit
            except ValueError:

                pass

    if total_credits == 0:
        return "无有效成绩"

    gpa = round(gpa_sum / total_credits, 2)
    return gpa


input_str = input("请输入学生信息：")
input_list = re.split(r'\s+', input_str.strip())
student_id = input_list[0]
student_name = input_list[1]
scores = input_list[2:]

gpa = calculate_gpa(scores)
output_str = f"{student_id},{student_name},{gpa}"
print(output_str)
