s = input()
four_list = set()
five_list = set()
six_list = set()
seven_list = set()

a = 1
while True:
    check_int = 2019 * a
    str_len = len(str(check_int))
    if str_len == 4:
        four_list.add(str(check_int))
    elif str_len == 5:
        five_list.add(str(check_int))
    elif str_len == 6:
        six_list.add(str(check_int))
    elif str_len == 7:
        seven_list.add(str(check_int))
    a += 1
"""
print(four_list)
print(five_list)
print(six_list)
"""
if len(s) <= 3:
    print(0)
    exit()

result_sum = 0
for i in range(len(s)-3):
    # print(s[i:4+i])
    if s[i:4+i] in four_list:
        result_sum += 1

if len(s) <= 4:
    print(result_sum)
    exit()

for i in range(len(s)-4):
    if s[i:5+i] in five_list:
        result_sum += 1

if len(s) <= 5:
    print(result_sum)
    exit()

for i in range(len(s)-5):
    if s[i:6+i] in four_list:
        result_sum += 1

print(result_sum)
