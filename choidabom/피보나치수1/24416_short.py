import sys
sys.stdin = open("choidabom/24416/input.txt","r")
input = sys.stdin.readline

n=int(input())
a,b=0,1
for i in range(n):a,b=b,a+b
print(a,n-2)