# 2098: 외판원 순회
# 1부터 N번까지 도시, 외판원 => 한 도시에서 출발해 N개의 도시를 모두 거쳐 다시 원래의 도시로 돌아오는 순회 여행 경로 계획, 단 한 번 갔던 도시로는 다시 못 감
# 각 도시간 이동 비용 행렬 W[i][j] => 즉 도시 i에서 도시 j로 가기 위한 비용 
# W[i][j]와 W[j][i]는 다름, W[i][i] = 0, W[i][j]=0인 경우도 있을 수 있음
# N과 비용 행렬 주어졌을 때, 가장 적은 비용을 들이는 외판원의 순회 여행 경로를 구하시오. 

import sys
sys.stdin = open("2098/input.txt","r")
input = sys.stdin.readline
print = sys.stdout.write
sys.setrecursionlimit(10**8)
INF = sys.maxsize

# x: 현재 위치
# visited: 현재 위치를 포함해서 방문한 이력
def dfs(x, visited):
    # 이미 인자로 받은 visited 정보와 함께 x에 온 이력이 있는지 
        # 있다면 0(초기값)이 아닐 것 => 최소 비용이 이미 dp에 담겨 있을 것
        # 없다면 0(초기값)일 것 => if 조건에 맞지 않음 
    if dp[x][visited]:
        return dp[x][visited]

    # 모든 노드를 방문했는지 
        # 했다면 마지막 노드(현재 노드==x)에서 0(시작점)으로 돌아갈 방법이 있는지
    if visited == (1<<N)-1:
        if graph[x][0]:
            return graph[x][0]
        return INF

    # 위의 if문들의 조건에 모두 맞지 않아 여기까지 왔다는 것은 
    # 인자로 주어진 visited 정보로 x라는 노드에 처음 방문했다는 의미
        # 주어진 visited를 통해 방문한 적 없는 노드가 무엇인지 알고
        # 그곳들을 방문했을 때의 최소 비용을 알아내야 함
    min_cost = INF
    for i in range(1, N):
        # 현재 위치(x)에서 i로 가는 방법이 없거나
        # 이미 i 노드를 방문한 이력이 visited에 담겨 있다면 
        if not graph[x][i] or visited & (1<<i):
            continue

        # dfs로 방문하지 않은 노드들을 방문해줘야 함
        # visited | (1<<i)로 i번째 노드까지 방문했다는 것을 표시하고
        # graph[x][i]에 더해줌으로써 x -> i로 갈 때 필요한 비용을 더함
        tmp = dfs(i, visited|(1<<i)) + graph[x][i]

        # 최소 비용을 알고 싶기 때문에
        # 현재 위치 x에서 방문하지 않은 노드를 방문하는 여러가지 방법들 중 최소 비용으로 min_cost를 갱신함
        if tmp < min_cost:
            min_cost = tmp
    dp[x][visited] = min_cost
    return min_cost

N = int(input())
graph = [tuple(map(int, input().split())) for _ in range(N)]

# 1<<N == 1*2^N ????????????????? => 1*2^4 = 16
dp = [[0]*(1<<N) for _ in range(N)]


print(f'{dfs(0, 1)}')
