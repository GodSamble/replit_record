array=[]

for i in range(1,len(array)): #1~9
  for j in range(i,0,-1): #i+1~ 0이 될때까지 -1
    if array[j]<array[j-1]:
      array[j],array[j-1]=array[j-1],array[j]
    else:
      break

print(array)