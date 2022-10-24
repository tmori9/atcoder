import copy
k = int(input())
s = list(input())
t = list(input())

remainig_card = [k]*9
s_list = []
for n in s[:4]:
    num = int(n)
    s_list.append(num)
    remainig_card[num-1] -= 1

t_list = []
for n in t[:4]:
    num = int(n)
    t_list.append(num)
    remainig_card[num-1] -= 1


def calc_point(input_list):
    sum_point = 0
    for i in range(1, 10):
        sum_point += i*10**input_list.count(i)
    return sum_point


remainig_card_number = []
for i, n in enumerate(remainig_card):
    if n >= 1:
        remainig_card_number.append(i+1)

win_card = []
for i in remainig_card_number:
    for j in remainig_card_number:
        s_list.append(i)
        t_list.append(j)
        takahasi_point = calc_point(s_list)
        aoki_point = calc_point(t_list)
        if takahasi_point > aoki_point:
            win_card.append([i, j])
        s_list = s_list[:4]
        t_list = t_list[:4]

win_rate = 0

for taka, ao in win_card:
    after_taka = copy.deepcopy(remainig_card)
    after_taka[taka-1] -= 1
    win_rate += (remainig_card[taka-1]*after_taka[ao-1]) / \
        (sum(remainig_card)*(sum(remainig_card)-1))

print(win_rate)
