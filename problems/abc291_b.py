from statistics import mean

n = int(input())  # 合計人数は 5*n
score_list = list(map(int, input().split()))

score_list = sorted(score_list)  # 昇順ソート

accurary_point = score_list[n:-n]
print(mean(accurary_point))
