# 15881: PenPineappleApplePen
# 사과, 파인애플, 펜이 일렬로 세워져있다.
# 순서를 바꾸지 않고 옆에 있는 물건끼리 연결했을 때 펜-파인애플-애플-펜이 몇 개나 많들 수 있을찌?
# 사과 A, 파인애플 P, 펜 p /펜-파인애플-애플-펜 => pPAp
import sys
sys.stdin = open("choidabom\PenPineappleApplePen\input.txt","r")
input = sys.stdin.readline

n = int(input())
inputs = input()

cnt = 0
ans = []
for i in range(len(inputs)):
    ans.append(inputs[i])
    if ''.join(ans[-4:]) == 'pPAp':
        cnt += 1
        ans = []
print(cnt)