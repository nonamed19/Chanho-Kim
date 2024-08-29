def f():
    for i in range(1, N+1):
        for j in range(1, N+1):
            if arr[i][j] == 1:
                for k in range(4):
                    cnt = 0
                    for l in range(5):
                        ni = i + di[k] * l
                        nj = j + dj[k] * l
                        if 0 <= ni <= N and 0 <= nj <= N and arr[ni][nj] == 1:
                            cnt += 1
                    if cnt == 5:
                        if 0 <= i - di[k] < N+2 and 0 <= j - dj[k] < N+2 and 0 <= ni + di[k] < N+2 and 0 <= nj + dj[k] < N+2:
                            if arr[i - di[k]][j - dj[k]] != 1 and arr[ni + di[k]][nj + dj[k]] != 1:
                                return 1, i, j

            elif arr[i][j] == 2:
                for k in range(4):
                    cnt = 0
                    for l in range(5):
                        ni = i + di[k] * l
                        nj = j + dj[k] * l
                        if 0 <= ni <= N and 0 <= nj <= N and arr[ni][nj] == 2:
                            cnt += 1
                    if cnt == 5:
                        if 0 <= i - di[k] < N+2 and 0 <= j - dj[k] < N+2 and 0 <= ni + di[k] < N+2 and 0 <= nj + dj[k] < N+2:
                            if arr[i - di[k]][j - dj[k]] != 2 and arr[ni + di[k]][nj + dj[k]] != 2:
                                return 2, i, j
    return 0


N = 19
arr_input = [list(map(int, input().split())) for _ in range(N)]
arr = [[0]*(N+2) for _ in range(N+2)]

for i in range(N):
    for j in range(N):
        arr[i+1][j+1] = arr_input[i][j]

di = [-1, 0, 1, 1]
dj = [1, 1, 1, 0]

result = f()

if result:
    print(result[0])
    print(result[1], result[2])
else:
    print(0)