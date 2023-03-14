n, q = map(int, input().split())

count = [0] * n  # イエローカード: +1, レッドカード: +2
for _ in range(q):
    event_num, target = map(int, input().split())
    if event_num == 1:
        count[target - 1] += 1
    elif event_num == 2:
        count[target - 1] += 2
    else:
        if count[target - 1] >= 2:
            print("Yes")
        else:
            print("No")
