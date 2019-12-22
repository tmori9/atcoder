import copy

H,W,K=map(int,input().split())
List=[list(input()) for i in range(H)]
result = copy.deepcopy(List)
int_n = 1
for i, line in enumerate(List):
    for j, point in enumerate(line):
        if point == '#':
            result[i][j] = int_n
            int_n += 1
print(result)

for i, line in enumerate(List):
    for j, point in enumerate(line):
        print(i, j, point)
        itigo = 0
        if point == '.':
            # 同じ行のイチゴを見る(一番近く)
            if '#' in List[i][:j]:
                itigo += 1
            if '#' in List[i][j:]:
                itigo += 1

            # 同じ列のイチゴを見る（一番近く）
            if '#' in [row[j][:i] for row in List]:
                itigo += 1
            if '#' in [row[j][i:] for row in List]:
                itigo += 1
            
            if itigo == 1:
                