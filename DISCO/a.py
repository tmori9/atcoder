a,b=map(int,input().split())
sum_price = 0
if a == 1:
    sum_price += 300000
elif a == 2:
    sum_price += 200000
elif a == 3:
    sum_price += 100000

if b == 1:
    sum_price += 300000
elif b == 2:
    sum_price += 200000
elif b == 3:
    sum_price += 100000

if a == 1 and b == 1:
    sum_price += 400000

print(sum_price)
