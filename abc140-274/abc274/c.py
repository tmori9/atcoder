n = int(input())
a_list = list(map(int, input().split()))


result_list = [0]*(len(a_list)*2 +1)

sort_idx_list = list(sorted(enumerate(a_list), key=lambda x: x[1]))

for (idx, value) in sort_idx_list:
    #print(f"{idx=}, {value=}")
    parent_idx = (idx+1)*2 -1
    #print(f"{parent_idx=}")
    result_list[parent_idx] = result_list[value-1] + 1
    result_list[parent_idx+1] = result_list[value-1] + 1
#print(result_list)
for i in result_list:
    print(i)