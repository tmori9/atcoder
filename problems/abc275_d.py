intput_n = int(input())

# dp = [0] * 10000000
# dp[0] = 1
# dp_bool = [False] * 10000000
# dp_bool[0] = True

dp_dict = dict()
dp_dict[0] = 1


def f_d(n):
    if n == 0:
        return 1
    first = n // 2
    second = n // 3
    if not dp_dict.get(first) == None and not dp_dict.get(second) == None:
        dp_dict[n] = dp_dict[first] + dp_dict[second]
        return dp_dict[n]
    else:
        return f_d(second) + f_d(first)


a = f_d(intput_n)
print(a)
