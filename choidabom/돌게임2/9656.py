import sys
sys.stdin = open("choidabom/돌게임2/input.txt","r")
'''
상근 시작 / 창영 시작
짝수이면 상근이가 무조건 win?

'''
N = int(input()) # 돌의 수 
if N % 2 == 0:
    print("SK") # 상근 win ??
else:
    print("CY") # 창영 win
