from pprint import pprint

T = int(input())

for tc in range(T):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    result = 0

    # 위쪽
    step = 1
    for i in range(0, N//2):
        for j in range(1, step+1):
            if j == 1:
                result += arr[i][N//2]
            else:
                result += arr[i][N//2-j+1]
                result += arr[i][N//2+j-1]
        step += 1

    # 중간
    for i in range(N//2, N//2+1):
        for j in range(N):
            result += arr[i][j]

    # 아래쪽
    step = 1
    for i in range(N-1, N//2, -1):
        for j in range(1, step+1):
            if j == 1:
                result += arr[i][N//2]
            else:
                result += arr[i][N//2-j+1]
                result += arr[i][N//2+j-1]
        step += 1

    print('#%d %d' %(tc+1, result))