n, k = map(int, input().split())
p_list = list(map(int, input().split()))

new_list = sorted(p_list)
new_list = new_list[:k]
print(sum(new_list))