import itertools
N, M, Q = map(int, input().split())
List = [list(map(int, input().split())) for i in range(Q)]

comb = list(itertools.combinations_with_replacement(list(range(1, M+1)), N))

max_point = 0
point_cont = 0
for pt in comb:
    point_cont = 0
    for list_pt in List:
        if pt[list_pt[1]-1] - pt[list_pt[0]-1] == list_pt[2]:
            point_cont += list_pt[3]
    if max_point <= point_cont:
        max_point = point_cont

print(max_point)
