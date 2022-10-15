# recursion fibonacci와 dp fibonacci를 의사코드 그대로 구현하게 되면 
# 재귀 함수를 호출하고 반복하는 과정에서 많은 연산을 필요로 하게 되어 시간 초과가 발생하다.
# so, dp로 구현하는 부분에서도 불필요한 반복이 요구된다. 
# 따라서 이를 해결하기 위해서는 그리디한 방법(Greedy Algorithm)으로 해결해야함.
# https://lbdiaryl.tistory.com/292

import sys
sys.stdin = open("choidabom/24416/input.txt","r")
input = sys.stdin.readline

def fib(n):
    a, b = 1, 1
    for i in range(n-2):
        a, b = b, a+b
    return b

# dp로 구현한 fibonacci 함수 같은 경우,
# 3에서 n+1까지 반복할 때의 횟수만 알면 되기 때문에 이를 n-2로 바꾸어 해결하는 것이 가능하다. 
def fibonacchi(n):
    return n-2

n = int(input())
print(f'{fib(n)} {fibonacchi(n)}')