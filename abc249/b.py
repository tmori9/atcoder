s = input()
s_list = list(s)

lower_flag = False
upper_flag = False
tyohuku_flag = True
count_s = []
for str in s_list:
    if str.isupper():
        upper_flag = True
    if str.islower():
        lower_flag = True
    if str in count_s:
        tyohuku_flag = False
    count_s.append(str)

if upper_flag and lower_flag and tyohuku_flag:
    print("Yes")
else:
    print("No")
