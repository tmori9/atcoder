n, m = map(int, input().split())
s_list = [int(input()) for i in range(n)]  # 文字列S
t_list = [int(input()) for i in range(m)]  # 文字列T

t_set = set(t_list)

count = 0
for s in s_list:
    s = str(s)
    selected = int(s[-3:])
    if selected in t_set:  # 効率化のため、setで存在確認
        count += 1

print(count)
