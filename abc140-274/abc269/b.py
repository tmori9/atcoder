x_list = []
first_A_flag = False
first_C_flag = False
for i in range(10):
    x = list(input())
    x_list.append(x)
    if "#" in x:
        if not first_A_flag:
            A = i + 1
            first_A_flag = True
        B = i + 1
        for j, value in enumerate(x):
            if value == "#":
                if not first_C_flag:
                    C = j + 1
                    first_C_flag = True
                D = j + 1
print(f"{A} {B}")
print(f"{C} {D}")
