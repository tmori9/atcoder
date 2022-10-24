N=int(input())
List=[int(i) for i in input().split()]

bou_half = sum(List)/2

bou_sum = 0
for i in List:
    bou_sum += i
    if bou_sum == bou_half:
        print(0)
        exit()
    if bou_sum > bou_half:
        if bou_sum - bou_half < bou_half - bou_sum + i: # 中心が右より
            print(int((bou_sum - bou_half) // 0.5))
            exit()
        else: 
            print(int((bou_half - bou_sum +i) // 0.5))
            exit()
