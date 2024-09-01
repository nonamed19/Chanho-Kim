arr = [list(map(int, input().split())) for _ in range(19)]
dir = [[0,1],[1,0],[1,1], [1,-1]]
def five(arr):
    for i in range(19):
        for j in range(19):
            if arr[i][j] > 0 : #돌이 있는 경우
                col = arr[i][j]  # 돌 색 저장 1 or 2
                for di, dj in dir : # 순회
                    ni, nj = i, j
                    cnt = 0 # 오목 수
                    o = []  # 오목 돌 위치 저장
                    while 0<=ni<19 and 0<=nj<19 and arr[ni][nj] == col : # 범위를 벗어나거나 같은 돌이 아닌 경우 중단
                        cnt += 1
                        o += [(nj, ni)] # 나중에 j를 기준으로 정렬해야하므로 j먼저 저장
                        ni, nj = ni + di, nj + dj
                    ni, nj = i, j # 반대 방향으로 다시(육목방지)
                    while 0<=ni<19 and 0<=nj<19 and arr[ni][nj] == col :
                        cnt += 1
                        o += [(nj, ni)]
                        ni, nj = ni - di, nj - dj
                    if cnt-1 == 5: # i,j 중복이므로 cnt -1
                        print(col)
                        o.sort()
                        print(o[0][1]+1, o[0][0]+1)
                        return
    print(0) # 오목이 없는 경우
    return
five(arr)