import sys
sys.stdin = open("11049/input.txt","r")
input = sys.stdin.readline
INF = sys.maxsize

N = int(input()) # N: 행렬의 개수
p = list(map(int, input().split()))
for _ in range(N-1):
    p.append(list(map(int, input().split()))[1])

# print(p) [5, 3, 2, 6]

m = [[INF]*(N+1) for _ in range(N+1)]

# m[i][j] => 행렬 Aij를 계산하는데 필요한 최소한의 스칼라 곱의 수
# m[i][i] => 하나의 행렬로 구성되므로 결과를 계산하는데 스칼라 곱이 필요 
for i in range(1, N+1): 
    m[i][i] = 0

for l in range(2, N+1): # l은 체인의 길이
    for i in range(N-l+2):
        j = i + l - 1
        C = p[i-1]*p[j]
        for k in range(i, j):
            m[i][j] = min(m[i][k] + m[k + 1][j] + C*p[k], m[i][j])

print(m[1][N])