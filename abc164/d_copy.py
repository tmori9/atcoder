s = input()

if len(s) <= 3:
    print(0)
    exit()

result_sum = 0
for i in range(len(s)):
    for j in range(len(s)-i-1):
        pass
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

print()
