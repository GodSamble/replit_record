data=input() #asdf1as4edf2sdf6
result=[] #문자열리스트
value=0 #

for x in data:
  if x.isalpha():
    result.append(x)
  else:
    value+=int(x)

  result.sort()

  if value!=0:
    result.append(str(value))

print('',join(result))