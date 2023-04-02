n = input()
w_list = input().split()
for i in w_list:
    if i in ["and", "not", "that", "the", "you"]:
        print("Yes")
        exit()

print("No")
