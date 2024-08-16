from pprint import pprint

T = 10

for tc in range(T):
    N = int(input())
    arr = [list(input()) for _ in range(8)]
    count = 0

    # 행 탐색
    for i in range(8):
        for j in range(8-N+1):
            lst = list(arr[i][x] for x in range(j, j+N))

            for k in range(N//2):
                if lst[k] != lst[-1-k]:
                    break   # 회문이 아닌 경우
            else:
                count += 1

    # 열 탐색
    for j in range(8):
        for i in range(8-N+1):
            lst = list(arr[x][j] for x in range(i, i+N))

            for k in range(N//2):
                if lst[k] != lst[-1-k]:
                    break   # 회문이 아닌 경우
            else:
                count += 1

    print('#%d %d' %(tc+1, count))