X = int(input())

flag = True

money = 100
i = 0
while flag:
    i += 1
    money = money + int(money*0.01)
    if money >= X:
        break
print(i)
