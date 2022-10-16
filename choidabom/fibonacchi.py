# O(2^n)의 시간복잡도를 가지는 피보나치 수열 구현
def fib_naive(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        fib = fib_naive(n-1) + fib_naive(n-2)
        return fib

# O(n)의 시간복잡도를 가지는 recursive DP 
# Top down 방식의 dynamic programming solution 
# 이러한 recursive 방법의 큰 문제는 큰 숫자를 구하고자 하면 recursion limit이 발생
fib_arr = [0, 1]
def fib_recur_dp(n):
    if n < len(fib_arr):
        return fib_arr[n]
    else:
        fib = fib_recur_dp(n-1) + fib_recur_dp(n-2)
        fib_arr.append(fib)
        return fib

# Bottom  down 방식의 dynamic programming solution 
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    fib_arr = [0, 1]
    for i in range(2, n+1):
        num = fib_arr[i-1] + fib_arr[i-2]
        fib_arr.append(num) 
    return fib_arr[n]
