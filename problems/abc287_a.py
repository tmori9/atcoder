n = int(input())
s_list = [input() for i in range(n)]  # 文字列S

for_count = 0
against_count = 0
for i in s_list:
    if i == "For":
        for_count += 1
    else:
        against_count += 1

if for_count >= against_count:
    print("Yes")
else:
    print("No")
