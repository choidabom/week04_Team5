# 함수로 하는게 훠얼씬 빠르다. 69372kb 412ms
import sys
sys.stdin = open("1904/input.txt","r")
input = sys.stdin.readline
n = int(input())
dp = [0] * 1000001
dp[1] = 1
dp[2] = 2
for i in range(3, n+1):
    dp[i] = (dp[i-1] + dp[i-2]) % 15746
print(dp[n])