n, m = map(int, input().split())
a_list = list(map(int, input().split()))
x = [list(input()) for i in range(n)]
# print(x)

current_ponts = []
for i, contest in enumerate(x):
    total_point = i + 1
    for j, result in enumerate(contest):
        if result == "o":
            total_point += a_list[j]
    current_ponts.append(total_point)
# print(current_ponts)

max_point = max(current_ponts)

# 点数の高い順番のインデックスのリスト
important_task = [
    i[0] for i in sorted(enumerate(a_list), key=lambda x: x[1], reverse=True)
]
# print(important_task)

for i, contest in enumerate(x):
    point = current_ponts[i]
    have_to_solve = 0
    if point == max_point:
        print(0)
    else:
        for task in important_task:
            if x[i][task] == "x":
                point += a_list[task]
                have_to_solve += 1
            if point > max_point:
                print(have_to_solve)
                break
