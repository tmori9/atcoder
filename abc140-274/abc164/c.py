N = int(input())
str_list = set()

for i in range(N):
    n = input()
    if n in str_list:
        continue
    else:
        str_list.add(n)
print(len(str_list))
