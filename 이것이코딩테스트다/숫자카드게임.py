n,m=map(int,input().split())

result=0
row_min=[]

for i in range(n):
  row=list(map(int,input().split()))
  row_min.append(min(row))
result=max(row_min)

print(result)