# 2098: 외판원 순회
# 1~N번까지 번호가 매겨진 도시들 있음
# 한 도시에서 출발해 N개의 도시를 모두 거쳐 다시 원래의 도시로 돌아오는 순회 여행경로를 계획, 단, 한 번 갔던 도시로는 다시 갈 수 없다. 
# 가장 적은 비용을 들이는 여행 계획

import sys
sys.stdin = open("2098/input.txt","r")
input = sys.stdin.readline
INF = sys.maxsize

N = int(input())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

dp = [[-1 for _ in range(1 << N)] for _ in range(N)]

def recursion(cur, visited):
    # 모든 노드 방문
    if visited == (1<<N)-1:
        if board[cur][0] == 0:
            return INF
        dp[cur][visited] == board[cur][0]
        return board[cur][0]

    # 메모이제이션
    if dp[cur][visited] != -1:
        return dp[cur][visited]
    
    min_dist = INF
    for i in range(N):
        if not visited & (1 << i) and board[cur][i] != 0:
            min_dist = min(min_dist, board[cur][i] + recursion(i, visited | (1 << i)))
    dp[cur][visited] = min_dist
    return min_dist

# 외판원 순회에 필요한 최소 비용 출력

print(recursion(0, 1))