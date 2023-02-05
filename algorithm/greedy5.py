n=int(input())
roads=list(map(int,input().split()))
costs=list(map(int,input().split()))

res=roads[0]*costs[0]
m=costs[0]
dist=0

