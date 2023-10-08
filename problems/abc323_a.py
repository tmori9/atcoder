s = list(map(int, input()))
for i, num in enumerate(s):
    if i == 0:
        continue
    if i % 2 == 1:
        if num == 1:
            print("No")
            exit()
print("Yes")
