def dfs(graph,v,visited):
  visited[v]=True
  print(v,end=' ')
  for i in graph[v]:
    if not visited[i]:
      dfs(graph,i,visited)

graph=[
  [],
  [2,3,8], #1 -> 2,3,8
  [1,7],   #2 -> 1,7
  [1,4,5],
  [3,5],
  [3,4],
  [7],
  [2,6,8],
  [1,7]    #8->1,7 의 뜻을 지님!
           #리스트 자료형으로 표현 한 것.
]

visited=[False]*9
dfs(graph,1,visited)