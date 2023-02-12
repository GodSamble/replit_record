n,m,k=map(int, input().split())
data=list(map(int,input().split()))
data.sort()

first=data[n-1] #배열 중에서 가장 큰 수
second=data[n-2] #배열 중에서 두번재로 큰 수
result=0

while True:
  for i in range(k):
    if m==0:
      break
    result+=first #반복문 돌아가는 동안 가장 큰수는 '계속' 더하기
    m-=1
  if m==0:
    break
  result += second #두번째로 큰 수를 '한 번 만' 더하기
  m-=1

print(result)