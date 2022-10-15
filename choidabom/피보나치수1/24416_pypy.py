# 24416: 알고리즘 수업 - 피보나치 수 1
# n의 피보나치 수를 재귀 호출과 동적 프로그래밍으로 구하는 알고리즘을 배ㅇ웠다.
# 재귀 호출에 비해 동적 프로그래밍이 얼마나 빠른지 확인해보자 ~~

import sys
sys.stdin = open("choidabom/24416/input.txt","r")
input = sys.stdin.readline

def recur(n):
    global ans
    if n < 3:
        ans[0] += 1
        return 1
    else:
        return recur(n-1) + recur(n-2)

def dp(n):
    global ans, dp_arr
    if n < 3: # n이 0이거나, 1이거나, 2이거나...
        return dp_arr[n]
    for i in range(3, n): # 왜 3부터 시작하는거지??? 피보나치 수열은 0, 1, 1, 2, 3, 5 이런식으로 시작 되지 때문에 
        ans[1] += 1
        dp_arr.append(dp_arr[i-1]+dp_arr[i-2])
    return dp_arr[-1]

n = int(input())
ans = [0, 1]
dp_arr = [0, 1, 1] # 피보나치 수열은 0, 1, 1, 2, 3, 5, ....

recur(n)
dp(n)
print(*ans)
