a, b = map(int, input().split())

test = [False, False, False]


def testPass(sum_number):
    if sum_number == 1:
        return [True, False, False]
    elif sum_number == 2:
        return [False, True, False]
    elif sum_number == 3:
        return [True, True, False]
    elif sum_number == 4:
        return [False, False, True]
    elif sum_number == 5:
        return [True, False, True]
    elif sum_number == 6:
        return [False, True, True]
    elif sum_number == 7:
        return [True, True, True]
    else:  # 0
        return [False, False, False]


a_test = testPass(a)
b_test = testPass(b)

c_test = [False] * 3
for i in range(3):
    if a_test[i] or b_test[i]:
        c_test[i] = True
    else:
        c_test[i] = False

res = 0
if c_test[0]:
    res += 1
if c_test[1]:
    res += 2
if c_test[2]:
    res += 4

print(res)
