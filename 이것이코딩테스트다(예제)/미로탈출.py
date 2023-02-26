from collection import deque

#이차원 리스트로 맵에 관한 정보 입력받기
n,m=map(int,input().split())
graph=[]
for i in range (n):
  graph.append(map(int,input()))
  
#이동할 네 방향 정의
dx=[-1,1,0,0]
dy=[0,0,-1,1]

#dfs 구현
def bfs(x,y):
  queue=deque()
  queue.append((x,y))

  #queue가 빌 때 까지 while문을 통해 구현
  while queue:
    x,y=queue.popleft()
    
    #현재위치에서 네 방향으로의 위치 확인
    for i in range(4):
      nx=x+dx[i]
      ny=y+dy[i]
      #미로찾기 맵을 벗어난 경우 무시
      if nx<0 or ny<0 or nx>=n or ny>=m:
        continue
      #벽인 경우 무시
      if graph[nx][ny]==0:
        continue
      #해당 노드를 처음 방문 시에만, 최단거리로 등록
      if graph[nx][ny]==1:
        graph[nx][ny]=graph[x][y]+1
        queue.append((nx,ny))
  #가장 오른쪽 아래까지의 최단거리 반환
  return graph[n-1][m-1]

print(bfs(0,0))