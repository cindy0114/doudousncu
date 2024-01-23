import sys

def guess_number():
    n = int(input())
    left, right = 1, n
    for _ in range(25):
        mid = (left + right) // 2
        print(mid)
        sys.stdout.flush()
        ans = input()
        if ans == '<':
            right = mid - 1
        else:
            left = mid + 1
    print("! {}".format(right))

if __name__ == "__main__":
    guess_number()
