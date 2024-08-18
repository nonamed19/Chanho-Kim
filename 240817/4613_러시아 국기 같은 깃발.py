T = int(input())

for tc in range(T):
    N, M = map(int, input().split()) # N x M 행렬
    arr = [list(input()) for _ in range(N)]
    result = 50*50 # 변경 가능한 모든 가지수(max. 50 x 50 행렬)

    for i in range(1, N):              # [WHITE]
        for j in range(1, N):          # [BLUE]
            for k in range(1, N):    # [RED]
                if i + j + k == N:
                    arr_temp = []
                    count = 0
                    # 가능한 모든 행렬을 생성한다
                    for _ in range(i):
                        arr_temp.append(['W']*M)
                    for _ in range(j):
                        arr_temp.append(['B']*M)
                    for _ in range(k):
                        arr_temp.append(['R']*M)

                    # 변경해야 하는 가지수를 count해서 최소값을 출력
                    for l in range(N):
                        for m in range(M):
                            if arr[l][m] != arr_temp[l][m]:
                                count += 1
                    result = min(result, count)

    print('#%d %d' %(tc+1, result))