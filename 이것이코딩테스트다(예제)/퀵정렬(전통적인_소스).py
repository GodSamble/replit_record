array=[5,7,9,0,3,1,6,2,4,8]

def quick_sort(array,start,end):
  if start >= end: #원소 1개 되면 종료
    return

  pivot=start #첫번째 원소로 피벗잡기
  left = start+1
  right = end
  while left<=right:
      #피벗보다 큰 데이터 찾을 때까지 반복
      while left <=end and array[left]<=array[pivot]:
          left +=1
      #피벗보다 작은 데이터를 찾을 때까지 반복
      while right > start and array[right] >=array[pivot]:
          right -=1
      if left>right: #엇갈렷으면 작은 데이터와 피벗 교체
        array[right],array[pivot] = array[pivot],array[right]
      else:          #엇갈리지 않은채라면 작은 데이터와 큰 데이터 교체
        array[left],array[right]=array[right],array[left]

  quick_sort(array,start,right-1) # 기존 파티션의 왼쪽에서 한 번 더!
  quick_sort(array,right+1,end)   # 기존 파티션의 오른쪽에서 한 번 더!

quick_sort(array,0,len(array)-1)
print(array)