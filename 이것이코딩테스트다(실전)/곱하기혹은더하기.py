data=input()

result=int(data[0]) #result를 문자열의 첫 값으로 초기화 함

for i in range(1,len(data)): # 둘째 인덱스부터 최종 문자열까지 반복문을 돌림
  num=int(data[i]) #num이라는 올라가는 인덱스를 지정해서
  if num<=1 or result <=1: #조건문을 진행
    result+=num
  else:
    result*=num

print(result)