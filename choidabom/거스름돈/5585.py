# 5585: 거스름돈
# 500엔, 100엔, 50엔, 10엔, 5엔, 1엔
# 언제나 거스름돈 개수가 가장 적게 잔돈을 줌
import sys
sys.stdin = open("choidabom/거스름돈/input.txt","r")
input = sys.stdin.readline

# 타로가 지불할 돈
pay = int(input())
money_list = [500, 100, 50, 10, 5, 1]
left = 1000 - pay
ans = 0

for money in money_list:
    if money > left: # money가 left(남은 돈)보다 크면 못 거슬러 주니깐 continue
        continue
    else:
        q = left // money
        r = left % money
        ans += q
        if r == 0: break
        else:
            left -= q * money
print(ans)
