n = int(input())
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))

result_value = min(b_list) - max(a_list)
if result_value < 0:
    print(0)
else:
    print(result_value + 1)
