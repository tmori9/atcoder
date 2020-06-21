x, n = map(int, input().split())
p_list = list(map(int, input().split()))

check = x
tansaku = 1
count = 0
while True:
    count += 1
    if not(check in p_list):
        print(check)
        exit()
    
    check -= tansaku
    tansaku = -tansaku
    if tansaku <0:
        tansaku -= 1
    else:
        tansaku += 1
    if count >= 500:
        exit()
