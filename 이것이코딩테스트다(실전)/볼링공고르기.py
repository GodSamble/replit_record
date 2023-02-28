n,m=map(int,input().split())# 5 3
data=list(map(int,input().split()))

array=[0]*11 #0<=m<=10 으로 명시되어 있기 때문에 ->'문제 명시된 걸로 초기화 범위 잡아두는 거 메모!'

for x in data: #각 무게에 해당하는 볼링공 개수 카운트 ->'이러한 방식으로 해당 값의 카운트 반복횟수 알 수 있구나!'
  array[x]+=1

result=0

for i in range(n-1):
    for j in range(i+1, n):
        if data[i] != data[j]:
            result += 1

print(result)