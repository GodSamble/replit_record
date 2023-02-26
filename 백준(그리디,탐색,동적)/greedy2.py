import sys
n=int(sys.stdin.readline())

time=[[0]*2 for _ in range(n)] #time=[] #n개 [0][0]으로 초기화
for i in range(n):
    s,e=map(int,sys.stdin.readline().split())
    time[i][0]=s #시작시간 [열][행] -> [세로 가로]
    time[i][1]=e #끝나는시간
    
time.sort(key=lambda x:(x[1],x[0])) #

cnt=1 #
end_time=time[0][1]
for i in range(1,n):
    if time[i][0]>=end_time:
        cnt+=1
        end_time=time[i][1]
print(cnt)