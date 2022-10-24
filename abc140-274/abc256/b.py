n = int(input())
a_list = list(map(int, input().split()))
a_list.reverse()
sum_num = 0

for i, count in enumerate(a_list):
    sum_num += count
    if sum_num >= 4:
        break

if sum(a_list) <= 3:
    print(0)
else:
    print(len(a_list) - i)
