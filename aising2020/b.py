aa = int(input())
a_list = list(map(int, input().split()))

result_sum = 0
for i, n in enumerate(a_list):
    i += 1  

    if i % 2 == 1 and n % 2 == 1:
        result_sum += 1 

print(result_sum)