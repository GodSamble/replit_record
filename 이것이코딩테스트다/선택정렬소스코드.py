array=[7,5,9,0,3,1,6,2,4,8]

for i in range(array):
  min_index=i
  for j in range(i+1,len(array)):
    min_index=j
    array[i],array[min_index]=array[min_index],array[i] #스와프
#대입연산자를 기점으로 대칭이 되게 반대로 적어주면 스와프가 일어남.

print(array)