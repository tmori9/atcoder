N=int(input())
S = list(input())

result = []
for s in S:
    result.append(chr((ord(s) -65 + N) % 26 + 65))

for s in result:
    print(s, end="")
