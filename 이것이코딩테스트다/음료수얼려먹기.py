#몇 곱하기 몇인지 입력받기
n,m=map(int,input().split())

#2차원 리스트 식으로 맵 정보 사용자로부터 입력받기
graph=[]
for i in range(n):
  graph.append(list(map(int,input())))

#DFS 사용
def dfs(x,y):
  #좌표의 값이 유의미한 값을 입력받았는지 거르기
  if x<=-1 or x>=n or y<=-1 or y>=m:
    return False
  #방문하지 않은 곳은 0 -> 1로 바꾸기
  if graph[x][y]==0:
    graph[x][y]=1
    #해당 좌표에 대하여 상하좌우의 위치를 재귀적으로 호출
    dfs(x - 1, y)
    dfs(x, y - 1)
    dfs(x + 1, y)
    dfs(x, y + 1)       
    return True       
  return False
  
#아이스크림의 개수
result=0

#맵의 모든 좌표를 순회
for i in range(n):
  for j in range(m):
    if dfs(i,j)==True:
      result+=1
      
print(result)