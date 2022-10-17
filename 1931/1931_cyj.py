n=int(input())
kaigi=[]
kaigi_answer=[]
for _ in range(n):
    kaigi.append(list(map(int,input().split())))
kaigi.sort()
temp=sorted(kaigi,key=lambda x: x[1])
kaigi=temp
kaigi_answer.append(kaigi[0])
for i in range(1,n):
    j = len(kaigi_answer)
    if kaigi[i][0] >= kaigi_answer[j-1][1]:
        kaigi_answer.append(kaigi[i])
print(len(kaigi_answer))