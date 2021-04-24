"""
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN, ROUND_FLOOR
x = Decimal(input())
print(Decimal(str(x)).quantize(Decimal('0'), rounding=ROUND_FLOOR))
"""
x = input()

search_index = x.find('.')

if search_index == -1:
    print(x)
else:
    print(x[:search_index])
