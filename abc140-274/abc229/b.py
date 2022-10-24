a, b = map(int, input().split())

result_plus = a + b
result_list = []
while result_plus > 0:
    result_list.append(result_plus % 10)
    result_plus //= 10
result_list.reverse()

a_list = []
while a > 0:
    a_list.append(a % 10)
    a //= 10
a_list.reverse()

b_list = []
while b > 0:
    b_list.append(b % 10)
    b //= 10
b_list.reverse()


if len(a_list) < len(result_list):
    for i in range(len(result_list) - len(a_list)):
        a_list.insert(0, 0)

if len(b_list) < len(result_list):
    for i in range(len(result_list) - len(b_list)):
        b_list.insert(0, 0)


for i, res in enumerate(result_list):
    if not a_list[i] + b_list[i] == res:
        print("Hard")
        exit()
print("Easy")
