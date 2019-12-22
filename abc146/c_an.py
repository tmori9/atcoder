A, B, X = map(int, input().split())
 
 
def get_digit(num):
    digits = 0
    while num > 0:
        num //= 10
        digits += 1
    return digits
 
 
def can_buy(num):
    digits = get_digit(num)
    return True if A * num + B * digits <= X else False
 
 
def can_buy(digits):
    return True if A * (10 ** (digits - 1)) + B * digits <= X else False
 
 
ans_digits = 10
while ans_digits > 0 and (not can_buy(ans_digits)):
    ans_digits -= 1
 
if ans_digits == 0:
    print(0)
    exit()
elif ans_digits == 10:
    print(10 ** 9)
    exit()
 
Xrest = X - B * ans_digits
ans = min(Xrest // A, 10 ** ans_digits - 1) 
 
print(ans)