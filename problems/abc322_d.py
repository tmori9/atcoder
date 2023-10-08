p1 = [list(input()) for i in range(4)]
p2 = [list(input()) for i in range(4)]
p3 = [list(input()) for i in range(4)]

"""
print(p1.count("#"))
print(p2.count("#"))
print(p3.count("#"))
# #の数が16個でないときはNo
if p1.count("#") + p2.count("#") + p3.count("#") != 16:
    print("NO")
    exit()
"""

# print(p1)


def calc_width_height(p):
    height = 0
    width = 0

    # heightを数える
    h_start_flag = False
    h_start = 0

    w_start = 5
    w_end = 0

    min_poly = []

    for i, one_line in enumerate(p):
        if "#" in one_line:
            min_poly.append(one_line)
            if not h_start_flag:
                h_start_flag = True
                h_start = i
            w_start = min(w_start, one_line.index("#"))
            w_end = max(w_end, len(one_line) - 1 - one_line[::-1].index("#"))
        else:
            if h_start_flag:
                height = i - h_start
                break
    width = w_end - w_start + 1

    selected_min_poly = [
        [row[i] for i in range(w_start, w_end + 1)] for row in min_poly
    ]
    # print(selected_min_poly)
    # print(h_start, height)
    # print(w_start, width)

    return height, width, selected_min_poly


height, width, min_poly = calc_width_height(p1)
print(height, width)
print(min_poly)

right_available = 4 - width
down_available = 4 - height

p_null = [["." for i in range(4)] for j in range(4)]
print(p_null)

for i in range(right_available + 1):
    for j in range(down_available + 1):
        print(j, i)
        for ii in range(i + 1):
            for jj in range(j + 1):
                p_null[jj][ii] = min_poly[jj][ii]
        print(p_null)
