K = int(input())
result_n = 0

def runrun(num):
    list_run = list(str(num))
    for j in range(0, len(list_run)-1):
        if abs(int(list_run[j]) - int(list_run[j+1])) > 1:
            return False
    return True

check = 0
for i in range(1, K+1):
    result_n+= 1
    result_list = list(str(result_n))
    if runrun(result_n):
        continue
    else:
        dan_num = 1
        for j in range(len(result_list)-1):
            if int(result_list[j]) + 1 == int(result_list[j+1]):
                dan_num += 1
            else:
                dan_num = 1
        top_dan = len(result_list)-dan_num
        for l, k in enumerate(result_list):
            if l < top_dan:
                continue
            else:
                pass
        result_list[top_dan] = int(result_list[top_dan])+1
print(result_n)
print(dan_num)

### not complete
        