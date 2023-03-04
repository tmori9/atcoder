s = list(input())

for i, s_i in enumerate(s):
    if s_i.isupper():
        print(i + 1)
        break
