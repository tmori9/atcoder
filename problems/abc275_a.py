n = int(input())
h_list = list(map(int, input().split()))

max_value = max(h_list)
max_index = h_list.index(max_value)
print(max_index + 1)
