#2차원 리스트 90도 회전 => 이건 별도로 메모해둬서 요긴하게 사용해야함. 자주 이용되는 기법이므로 따로 빼서 적어둘 것.
def rotate_a_matrix_by_90_degree(a):
    n= len(a)
    m= len(a[0])
    result = [[0]*n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][n-i-1]=a[i][j]
    return result

# 자물쇠의 중간 부분이 모두 1인지 확인
def check(new_lock):
    lock_length = len(new_lock) // 3
    for i in range(lock_length,lock_length*2):
        for j in range(lock_length, lock_length*2):
            if new_lock[i][j]!=1:
                return False
    return True

def solution(key,lock):
    n=len(lock)
    m=len(key)
    #자물쇠의 크기를 기존의 3배로 변환
    new_lock=[[0]*(n*3) for _ in range(n*3)]
    for i in range(n):
        new_lock[i+n][j+n]=lock[i][j]

    #4가지 방향에 대해서 확인
for rotation in range(4):
    key= rotate_a_matrix_by_90_degree(key)
    for x in range(n*2):
        for y in range(n*2):
            for i in range(m):
                for j in range(m):
                    new_lock[x+i][y+j]+=key[i][j]

        if check(new_lock)==True:
            return True
        for i in range(m):
            for j in range(m):
                new_lock[x+i][y+j]-=key[i][j]

return False

#난이도 어려운 관계로
#이코테 해설 보고 클론함
#기본기 다지고 다시 풀 것!

#let's start!