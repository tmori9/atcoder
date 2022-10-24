import copy
n, x, y = map(int, input().split())
a_list = list(map(int, input().split()))

left_right = set()
up_down = set()

result_left_right_set = set()
result_up_down_set = set()

for i, v in enumerate(a_list):
    #print(f"{i=}, {v=}")
    if i == 0:
        left_right.add(v)
    else:
        if i == len(a_list) - 1 or i == len(a_list) -2:
            #print("最後から2個以内")
            if i % 2 == 0:
                temp_set = copy.copy(left_right)
                for j in temp_set:
                    result_left_right_set.add(j+v)
                    result_left_right_set.add(j-v)
                if len(left_right) == 0:
                    result_left_right_set.add(v)
                    result_left_right_set.add(-v)
            else:
                temp_set = copy.copy(up_down)
                for j in temp_set:
                    result_up_down_set.add(j+v)
                    result_up_down_set.add(j-v)
                if len(up_down) == 0:
                    result_up_down_set.add(v)
                    result_up_down_set.add(-v)
            continue


        if i % 2 == 0:
            temp_set = copy.copy(left_right)
            for j in temp_set:
                left_right.add(j+v)
                left_right.add(j-v)

            if len(left_right) == 0:
                left_right.add(v)
        else:
            temp_set = copy.copy(up_down)
            for j in temp_set:
                up_down.add(j+v)
                up_down.add(j-v)
            
            if len(up_down) == 0:
                up_down.add(v)
                up_down.add(-v)
        

if len(result_left_right_set) == 0: # N =2 のとき
    result_left_right_set.add(a_list[0])

#print(f"{left_right=}, {up_down=}")
#print(f"{result_left_right_set=}, {result_up_down_set=}")

if x in result_left_right_set and y in result_up_down_set:
    print("Yes")
else:
    print("No")