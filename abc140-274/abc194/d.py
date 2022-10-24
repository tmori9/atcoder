from decimal import Decimal
n = int(input())

bunbo = n**(n-1)

print(Decimal(bunbo)/(n-1))
