coin_number,won = map(int,input().split())
coin = [int(input()) for _ in range(coin_number)]
coin.sort(reverse=True)
count = 0
for i in range(coin_number):
    if won == 0:
        break
    elif coin[i] <= won:
        count += won // coin[i]
        won = won % coin[i]
    else:continue