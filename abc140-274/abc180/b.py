import math
n = int(input())
x_list = list(map(int, input().split()))

result_sum = 0
result_double = 0
che_list = []
for i in x_list:
    che_list.append(abs(i))
    result_sum += abs(i)
    result_double += abs(i)*abs(i)

print(result_sum)
print(math.sqrt(result_double))
print(max(che_list))
