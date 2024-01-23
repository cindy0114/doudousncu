def count_characters(input_str):
    blank_count = digit_count = other_count = 0

    for char in input_str:
        if char.isdigit():
            digit_count += 1
        elif char.isspace():
            blank_count += 1
        else:
            other_count += 1

    return blank_count, digit_count, other_count

if __name__ == "__main__":
    input_str = input()

    blank, digit, other = count_characters(input_str)

    print(f"blank = {blank}, digit = {digit}, other = {other}")