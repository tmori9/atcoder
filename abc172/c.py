n, m, c  = map(int, input().split())
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))

# まずはAの本棚を全部よみ、一つずつBの数値をあげる
check_list = []
read_time = 0
a_index = 0
for i, value in enumerate(a_list):
    a_index = i + 1
    read_time += value
    if read_time > c: # タイムを超えたら
        read_time -= value
        a_index -= 1
        break
    

read_book = a_index  # Aの読んだ本
b_index = 0
a_read_book_list = a_list[:read_book]
a_read_book_list.reverse()

for i,value in enumerate(a_read_book_list):
    check_list.append(len(a_read_book_list)-i)

"""
flag_last = False
for i, value in enumerate(a_read_book_list):
    while read_time <= c:
        if b_index >= len(b_list):
            flag_last = True
            break
        read_time += b_list[b_index]
        b_index += 1

    if flag_last == False:
        read_time -= b_list[b_index]
        b_index -= 1

    flag = False

    check_list.append(len(a_read_book_list)-i+b_index)
    read_time -= value # Aから一冊取る
"""
print(che)

if len(check_list) == 0:
    print(0)
else:
    print(max(check_list))