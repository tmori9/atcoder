s = list(input())
# print(s)


def is_palindrome(s):
    return s == s[::-1]


res = 0
for start_i in range(len(s)):
    for end_i in range(start_i, len(s)):
        if is_palindrome(s[start_i : end_i + 1]):
            res = max(res, len(s[start_i : end_i + 1]))

print(res)
