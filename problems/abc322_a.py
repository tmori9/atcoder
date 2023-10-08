n = int(input())
s = input()

# print(s.find("ABC"))
if s.find("ABC") == -1:
    print(-1)
else:
    print(s.find("ABC") + 1)
