m = int(input())
s1 = list(input())
s2 = list(input())
s3 = list(input())

# print(s1)
# print(s2)
# print(s3)

res = 10**9

no_ans_flag = True

for i, stop_num in enumerate(s1):
    # print(f"target = {stop_num}")
    # s2にstop_numがあるか
    # print(i)
    if stop_num in s2:
        # 複数あるindexを取得
        s2_index = [j for j, x in enumerate(s2) if x == stop_num]
        # 各要素に20を足したものを追加
        s2_index_plus_1 = [x + m for x in s2_index]
        s3_index_plus_2 = [x + m * 2 for x in s2_index]
        # 結合
        s2_index.extend(s2_index_plus_1)
        s2_index.extend(s3_index_plus_2)
        # print(s2_index)
    else:
        continue

    if stop_num in s3:
        s3_index = [j for j, x in enumerate(s3) if x == stop_num]
        # print(s3_index)
        s3_index_plus_1 = [x + m for x in s3_index]
        s3_index_plus_2 = [x + m * 2 for x in s3_index]
        s3_index.extend(s3_index_plus_1)
        s3_index.extend(s3_index_plus_2)
    else:
        continue

    for s2_i in s2_index:
        for s3_i in s3_index:
            if i == s2_i or i == s3_i or s2_i == s3_i:
                continue
            else:
                no_ans_flag = False
                res = min(res, max(set([i, s2_i, s3_i])))

if no_ans_flag:
    print(-1)
else:
    print(res)
