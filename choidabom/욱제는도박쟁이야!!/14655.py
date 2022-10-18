# 14655: 욱제는도박쟁이야!!
# 동전 뒤집기 
# 첫 번째 라운드에서는 동전에 표시된 값들의 합이 최대가 되도록 뒤집어야 하고, 
# 두 번째 라운드에서는 동전에 표시된 값들의 합이 최소가 되도록 뒤집어야 한다.
# (첫 번째 라운드 동전 값의 합) - (두 번째 라운드 동전 값의 합) = 해당 플레이어가 게임에서 획득한 점수
# 이 점수가 최대가 되는 플레이어가 바로 게임의 승자이다. 
import sys
sys.stdin = open("choidabom/욱제는도박쟁이야!!/input.txt","r")
input = sys.stdin.readline

N = int(input())
first = list(map(int, input().split(' ')))
second = list(map(int, input().split(' ')))

print(first)
print(second)