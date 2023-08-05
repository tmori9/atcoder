import math

n = int(input())
a_list = list(map(int, input().split()))

a_list = sorted(a_list)

lower_value = 0
upper_value = 2 * 10**5
if sum(a_list) % len(a_list) == 0:  # 割り切れる
    lower_value = sum(a_list) // len(a_list)
    upper_value = sum(a_list) // len(a_list)
else:
    lower_value = math.floor(sum(a_list) / len(a_list))
    upper_value = math.ceil(sum(a_list) / len(a_list))

# print(lower_value)
# print(upper_value)

lower_diff = 0
upper_diff = 0
for a in a_list:
    if a < lower_value:
        lower_diff += lower_value - a
    if upper_value < a:
        upper_diff += a - upper_value

# print(lower_diff)
# print(upper_diff)
print(max(lower_diff, upper_diff))
