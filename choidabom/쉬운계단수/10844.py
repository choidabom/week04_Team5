# 10844: 쉬운 계단 수
# https://velog.io/@ready2start/Python-%EB%B0%B1%EC%A4%80-10844-%EC%89%AC%EC%9A%B4-%EA%B3%84%EB%8B%A8-%EC%88%98
# 인접한 모든 자리의 차이가 1 => 계단수
# N이 주어질 때, 길이가 N인 계단 수 총 몇 개? => 갯수를 묻는다.
# 정답을 1000000000으로 나눈 나머지 출력

import sys
sys.stdin = open("choidabom/쉬운계단수/input.txt","r")

N = int(input())
# 문제 조건에서 0으로 시작할 수는 없다고 했기에
# 한 자리 수일 때는 0은 0, 나머지는 1로 초기화해줌
dp = [[0]*10 for _ in range(N+1)]
dp[1] = [0] + [1] * 9 # 만약 N이 1일 때 9가 출력되어야함.
# print(dp)

for i in range(2, N+1): # 2
    # 0으로 끝나는 경우
    dp[i][0] = dp[i-1][1]
    # 9로 끝나는 경우
    dp[i][9] = dp[i-1][8]

    for j in range(1, 9):
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

print(sum(dp[N])%1000000000)