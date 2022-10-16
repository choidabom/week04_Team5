# 9625: BABBA
'''
화면 - A
버튼 1 - B
버튼 2 - BA
3 - BAB
4 - BABBA

(0, 1)
(1, 1)
(1, 2)

'''
import sys
sys.stdin = open("choidabom/BABBA/input.txt","r")
input = sys.stdin.readline
K = int(input())
dp = [[] for _ in range(K+1)]
dp[0] = [1, 0] 
for i in range(1, K+1):
    A = dp[i-1][0]
    B = dp[i-1][1]
    # dp[i][0] = B
    # dp[i][1] = A + B 
    dp[i] = [B, A+B]

print(*dp[K])
