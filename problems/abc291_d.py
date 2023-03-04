n = int(input())
card_number = [list(map(int, input().split())) for i in range(n)]

for i, (omote, ura) in enumerate(card_number):
    if i == 0:
        pre_omote = omote
        pre_ura = ura
        continue
    if pre_omote == omote:
        count = 2 ** (n - 2)
    if omote == ura:
        count = 2 ** (n - 2)
    if pre_ura == omote:
        count = 2 ** (n - 2)
    if pre_ura == ura:
        count = 2 ** (n - 2)
