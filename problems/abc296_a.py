n = int(input())
s = list(input())

pre = ""
for i, s_str in enumerate(s):
    if pre == s_str:
        print("No")
        exit()
    pre = s_str
print("Yes")
