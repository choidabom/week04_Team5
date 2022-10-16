# 24416: 알고리즘 수업 - 피보나치 수 1
# n의 피보나치 수를 재귀 호출과 동적 프로그래밍으로 구하는 알고리즘을 배ㅇ웠다.
# 재귀 호출에 비해 동적 프로그래밍이 얼마나 빠른지 확인해보자 ~~

import sys
sys.stdin = open("choidabom/24416/input.txt","r")
input = sys.stdin.readline

cnt1 = 0 
cnt2 = 0

def fib(n): # 재귀 함수: 함수 내에서 자기 자신을 호출하는 함수 
    global cnt1
    cnt1 += 1
    if n == 1 or n == 2: # n이 3이상일 경우, else로 건너뜀
        cnt1 -= 1
        return 1
    else:
        return fib(n-1) + fib(n-2)

def fibonacci(n):
    global cnt2
    f[1], f[2] = 1, 1
    for i in range(3, n+1):
        cnt2 += 1
        f[i] = f[i-1] + f[i-2]
    return f[n]

f = [0 for _ in range(41)]
n = int(input())
fib(n)
fibonacci(n)
print(cnt1+1, cnt2)

