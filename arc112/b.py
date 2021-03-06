b, used = map(int, input().split())

# 到達可能の判定

if b > 0:  # 正 0の場合要検討
    if b*2 <= used:
        # 到達可能
        print(used+abs(b)*2 - 1)
        exit()
    else:
        if used == 0:  # 特殊解
            print(1)
            exit()

        elif used == 1:  # 特殊解
            print(2)
            exit()
        else:
            print(used*2 - 1)
            exit()

if b <= 0:
    if abs(b)*2 + 1 <= used:
        # 到達可能
        print(used+abs(b)*2)
        exit()
    else:
        if used == 0:  # 特殊解
            print(1)
            exit()
        elif used == 1:  # 特殊解
            print(2)
            exit()
        else:
            print(used*2 - 1)
            exit()
