n=int(input())
#내가 구상한 i, ii 해보자!!

data=list(map(int,input().split()))
data.sort()

result=0 #총 그룹의 수 증가시키기 #0으로 초기화
cnt=0 #현재 그룹에 포함된 모험가의 수

for i in data:############ 사고력 파트
  cnt+=1
  if cnt>=i:
    result+=1
    cnt=0
  result+=1
  ######################## 사고력 파트

print(result)

###### cnt나 reulut 수치화 출력하는 답안 형태라면, 0으로 초기화 작업 반드시 해줄 것
###### 파이썬 라이브러리 '편의상' 적극 활용할 것 .sort() 같은 메소드