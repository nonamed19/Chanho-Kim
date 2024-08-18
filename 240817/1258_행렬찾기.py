from pprint import pprint

T = int(input())

for tc in range(10): # in range(T)
    N = int(input())
    arr_input = [list(map(int, input().split())) for _ in range(N)]
    lst = [] # 0이 아닌 a x b 행렬의 크기를 담을 리스트

    # index error 방지를 위해 상하좌우를 0으로 채우기(N+2 x N+2 행렬)
    arr = [[0]*(N+2) for _ in range(N+2)]
    for i in range(N):
        for j in range(N):
            arr[i+1][j+1] = arr_input[i][j]

    for i in range(1, N+1):
        for j in range(1, N+1):
            if arr[i][j] != 0 and arr[i-1][j] == 0 and arr[i][j-1] == 0:
                start_i, start_j = i, j
                ni, nj = i, j
                while arr[i][nj+1] != 0:
                    nj += 1
                while arr[ni+1][j] != 0:
                    ni += 1
                end_i, end_j = ni, nj

                lst.append([(end_i-start_i+1)*(end_j-start_j+1), end_i-start_i+1, end_j-start_j+1])

    lst = sorted(lst)
    print('#%d %d' %(tc+1, len(lst)), end = ' ')
    for i in range(len(lst)):
        print(*lst[i][1:3], end = ' ')
    print()

