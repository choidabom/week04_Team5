# 2775: 부녀회장이 될테야
'''
a층의 b호에 살려면 자신의 아래(a-1)층의 1호부터 b호까지 사람들의 수의 합만큼 사람들을 데려와 살아야 한다.
a층 b호 => a-1층 1 ~ b호
k층에 n호에는 몇 명이 살고 있는지? 
'''
import sys
sys.stdin = open("choidabom/부녀회장이될테야/input.txt","r")
input = sys.stdin.readline

T = int(input().rstrip())

# 아파트 하나 있어도 됨, 전역 

for i in range(T): # 테스트 케이스를 돌 때마다 초기화가 됨 
    max_f = int(input())
    max_r = int(input())

    dp = [[0 for _ in range(max_r+1)] for _ in range(max_f+1)] # 인덱스 번호 맞추기

    for i in range(max_r+1): # 0층에 i호에는 i명이 산다.
        dp[0][i] = i 

    for floor in range(1, max_f+1):
        for room in range(1, max_r+1):
            dp[floor][room] = dp[floor-1][room] + dp[floor][room-1]

    print(dp[max_f][max_r])


