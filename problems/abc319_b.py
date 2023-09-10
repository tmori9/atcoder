n = int(input())

for i in range(n + 1):
    if i == 0:
        print("1", end="")
        continue
    # nの約数を求める
    candidate = []
    for j in range(1, 10):
        if n % j == 0:
            candidate.append(j)
    no_flag = True
    for num in candidate:
        if i % (n // num) == 0:
            print(num, end="")
            no_flag = False
            break
    if no_flag:
        print("-", end="")
print()
