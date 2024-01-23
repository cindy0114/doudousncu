def answer_to_mood(mood, time):
    if 0 <= time < 24:
        if mood[time] > 50:
            return f"{mood[time]} Yes"
        else:
            return f"{mood[time]} No"
    else:
        return None

if __name__ == "__main__":
    mood = list(map(int, input().split()))

    while True:
        time = int(input())
        result = answer_to_mood(mood, time)

        if result is not None:
            print(result)
        else:
            break