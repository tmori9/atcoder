import collections
n = int(input())
a_list = list(map(int, input().split()))

cout_list = collections.Counter(a_list)

set_list = list(set(a_list))
sum_num = 0
for i in range(1, len(set_list)):
    for j in range(0, i):
        first_num = set_list[i]
        second_num = set_list[j]
        sum_num += (first_num-second_num)**2 * \
            cout_list[first_num]*cout_list[second_num]

print(sum_num)
