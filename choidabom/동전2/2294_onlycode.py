# 2294: 동전 2
# https://tesseractjh.tistory.com/137
import sys
sys.stdin = open("choidabom/동전2/input.txt","r")
input = sys.stdin.readline

n, k = map(int, input().split())
coin = [int(input().rstrip()) for _ in range(n)] # [1, 5, 12]
dp = [10001 for _ in range(k+1)] # dp[n]은 n원을 만들기 위해 필요한 동전의 최소 개수
dp[0] = 0 # dp[0] = 0으로 초기화하여 가장 작은 가치의 동전을 선택했을 경우에도 정상적으로 dp 구함.

for i in range(1, k+1): # 값이 1부터 k가 될 때까지 반복문을 돌리면서 최소 개수를 찾으면서 k의 값을 만족할 때 최소 개수를 만족하게끔 한다. 
    for j in coin: # coin: [1, 5, 12]
        # 동전 종류가 총 3개로 1원, 5원, 8원이라면
        # dp[n] = min(dp[n-1], dp[n-5], dp[n-8]) + 1
        # 이 때, 동전의 가치는 보다 작거나 같아야 한다. 
        if i < j: continue # briefly하게 구하고자 하는 k보다 coin 값이 크면 안 되겠지? 예를 들어 6원을 구하려고 하는ep 8원을 쓰는 꼴이 되니까! 
        dp[i] = min(dp[i], dp[i-j]+1)

if dp[k] == 10001: print(-1)
else: print(dp[k])
