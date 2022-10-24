card=[list(map(int,input().split())) for i in range(3)]
N=int(input())
target_list=[int(input()) for i in range(N)]

for i, line in enumerate(card):
    for j, pt in enumerate(line):
        if pt in target_list:
            card[i][j] = 1 # マークあり
        else:
            card[i][j] = 0 #マークなし

result = False
# 横
for l in card:
    if l.count(1) == 3:
        result = True

# 縦
for l in list(zip(*card)):
    if l.count(1) == 3:
        result = True

# 斜め
if card[1][1] == 1: #真ん中にマークあり
    if card[0][0] == 1 and card[2][2] == 1:
        result = True
    if card[0][2] == 1 and card[2][0] == 1:
        result = True

if result:
    print("Yes")
else:
    print("No")
