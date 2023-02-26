n = int(input())
time= list(map(int, input().split()))

time.sort() # 걸리는 시간을 오름차순으로 정렬했을 때 최솟값이 나온다
waiting = []
for i in range(n):
    waiting.append(sum(time[:i+1])) # 걸리는 시간을 인덱싱한 후 sum한 값을 waiting에 추가
    
print(sum(waiting)) # 줄 서있는 모든 사람의 waiting을 더한 값 출력