n = int(input())
x = [list(input()) for i in range(n)]

result_list = []
for i, all_result in enumerate(x):
    win = 0
    for result in all_result:
        if result == "o":
            win += 1
    result_list.append([i + 1, win])


sorted_result_list = sorted(result_list, key=lambda x: x[1], reverse=True)

ans = []
for i in sorted_result_list:
    ans.append(i[0])
# リストを空白区切りで出力
print(*ans)
