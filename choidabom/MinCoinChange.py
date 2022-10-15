'''
https://colab.research.google.com/github/NoCodeProgram/CodingTest/blob/main/dynamicProgramming/minCoinChange.ipynb#scrollTo=HLzCpCagAnR7
Min Coin Change
문제: 주어진 동전 coins로 금액의 합 amount를 만들기 위한 최소한의 동전의 갯수는 몇 개인가?
[2, 3, 5] sum = 11

5*1 + 3*2 + 2*0 = 11, 3
5*1 + 3*0 + 2*3 = 11, 3
5*0 + 3*3 + 2*1 = 11, 4
5*0 + 3*1 + 2*4 = 11, 5
이런 문제를 처음 보더라도 다이나믹 프로그래밍에 익숙하다면 subproblems으로 나눌 수 있다.

[Top down 방식의 코드]
F(11) = Min(F(9), F(8), F(6)) + 1
F(n) = Min(F(n-2), F(n-3), F(n-5)) + 1

[Bottom Up 방식의 코드]
array를 만든다. 
F(0) = 0
F(1) = -1
F(2) = 1
F(3) = 1
F(4) = Min(F(2), F(1), F(-1)) + 1 = Min(1, -1, -1) + 1 = 1 + 1 = 2
F(5) = Min(F(3), F(2), F(0)) + 1 = Min(1, 1, 0) + 1 = 1 + 1 = 2
.....
=> 시간 복잡도: O(k*n), 공간 복잡도: O(n)
'''

# 이 코드에서 dp_arr의 인덱스는 가격(동전)의 역할을 하고, 
# dp_arr의 value, 값은 동전의 최소 갯수의 역할음 함. 

def coinChange(coins, amount):
    MAX_COST = 999999999
    dp_arr = [-1] * (amount+1) # dp_arr는 -1로 초기화 한다. 해당하는 값이 없으면 -1을 통해 거를 수 있도록
    dp_arr[0] = 0 # ???? 0원은 소용이 없기 때문에 인덱스 0은 0으로 초기화

    for idx in range(amount+1): 
        if dp_arr[idx] != -1: # 값이 -1이 아니면 continue/왜냐면 지금 초기화를 -1로 해줬기 때문에 
            continue

        crnt_min = MAX_COST 
        for coin in coins:
            last_idx = idx - coin
            if last_idx < 0:    # 마지막 인덱스가 0보다 작으면 
                continue        # 가장 가까운 for문으로 다시 넘어감
            last_cost = dp_arr[last_idx]
            if last_cost == -1:
                continue
            cost = last_cost + 1
            crnt_min = min(cost, crnt_min)
    
        dp_arr[idx] = -1 if crnt_min == MAX_COST else crnt_min

    return dp_arr[amount]
                
print(coinChange(coins=[2, 3, 5], amount = 10))
