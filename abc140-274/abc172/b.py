s = input()
t = input()

sum_num = 0
for i in range(len(s)):
    if not(s[i] == t[i]):
        sum_num += 1

print(sum_num)