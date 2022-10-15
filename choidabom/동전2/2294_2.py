# 2294: 동전 2
# https://tesseractjh.tistory.com/137

import sys
sys.stdin = open("choidabom/2294/input.txt","r")
input = sys.stdin.readline

n, k = map(int, input().split()) # n가지 종류의 동전, 가치의 합 k원
coin = [int(input().rstrip()) for _ in range(n)] # 코인을 담을 1차원 배열

dp = [10001 for _ in range(k+1)]  # 각 값마다 필요한 최소 코인 갯수를 저장할 dp 배열
dp[0] = 0 # 가장 작은 가치의 동전을 선택했을 경우에도 정상적으로 dp를 구할 수 있다. 
for i in range(1, k+1): # 1부터 가치의 합 k까지 check~!
    for j in coin: # coin = [1, 5, 12]
        if i < j: continue # 예를 들어 dp[6]을 구할 때 8원은 포함할 수 없기 때문이다.
        dp[i] = min(dp[i], dp[i-j] + 1)

if dp[k] == 10001:
    print(-1)
else:
    print(dp[k])

# dp[n]은 n원을 만들기 위해 필요한 동전의 최소 개수를 나타낸다.
# a원짜리 동전을 포함해서 n원을 만든다고 했을 때, dp[n] = dp[n-a] +1 이라고 할 수 있다. 
# 예를 들어, 3원짜리 동전을 하나 선택해서 10원을 만드는 동전의 최소 개수는 dp[7]
# dp[7](7원을 만드는 동전의 최소 개수) +1(3원짜리 동전 1개)
# 그런데 어떤 동전을 포함할 때가 가장 적은 수의 동전이 필요한지 알려면 모든 동전에 대해 위 과정을 거쳐야 한다.
# 예를 들어 동전 종류가 총 3개로 1원, 5원, 8원이라면
# dp[n] = min(dp[n-1], dp[n-5], dp[n-8]) + 1이 성립한다.
# 단, 이 때 동전의 가치는 n보다 작거나 같아야 한다.
# 예를 들어 dp[6]을 구할 때 8원은 포함할 수 없기 때문이다.

