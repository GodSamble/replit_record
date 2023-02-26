n=int(input())
roads=list(map(int,input().split())) #1234
costs=list(map(int,input().split())) #4 2 5 6

res=roads[0]*costs[0] #얘의 초기값은 고정값으로 세팅하고 추가되는 때마다 리뉴얼
#하고, 최종적으로 print(res)할 것임.
m=costs[0] # 저장고
dist=0  #

for i in range(1,n-1):
    if costs[i]<m:
      res+=m*dist
      dist=roads[i] #
      m=costs[i] #
    else:
      dist+=roads[i] #

    if i==n-2:
      res+=m*dist
print(res)