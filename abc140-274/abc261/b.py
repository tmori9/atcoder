n = int(input())
match_list = [[j for j in input()] for i in range(n)]

incorrect = False

for i, line in enumerate(match_list):
    for j, value in enumerate(line):
        if value == "W":
            # 不正解
            if not match_list[j][i] == "L":
                incorrect = True
                break
        elif value == "L":
            # 不正解
            if not match_list[j][i] == "W":
                incorrect = True
                break
        elif value == "D":
            # 不正解
            if not match_list[j][i] == "D":
                incorrect = True
                break

if incorrect:
    print("incorrect")
else:
    print("correct")
