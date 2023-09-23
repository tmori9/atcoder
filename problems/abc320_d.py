n, m = map(int, input().split())

# 確定した人の判定
judge_list = [False] * n
judge_list[0] = True

# 人の2次元座標系
people_list = [[0, 0] for i in range(n)]

print(judge_list)
print(people_list)

search_list = []

for i in range(m):
    a, b, x, y = map(int, input().split())
    a -= 1
    b -= 1
    if a == 0:
        judge_list[b] = True
        people_list[b][0] = x
        people_list[b][1] = y
    elif b == 0:
        judge_list[a] = True
        people_list[a][0] = -x
        people_list[a][1] = -y
    else:
        search_list.append([a, b, x, y])
