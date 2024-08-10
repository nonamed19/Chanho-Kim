from pprint import pprint

T = int(input())

for tc in range(T):
    N = 9 # 9 x 9 matrix
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 1 # 초기값을 1로 설정

    # 행, 열에 대한 조건 확인
    for i in range(N):
        row, col = [], []
        for j in range(N):
            row.append(arr[i][j])
            col.append(arr[j][i])
        # 1~9까지의 중복 확인
        for k in range(1, N+1):
            if row.count(k) != 1:
                result = 0 # 조건에 맞지 않으면 0을 출력
            if col.count(k) != 1:
                result = 0 # 조건에 맞지 않으면 0을 출력

    # 9분할된 칸에 대한 조건 확인
    for k in range(0, N-1, 3):
        for l in range(0, N-1, 3):
            sqr = []
            for i in range(N//3):
                for j in range(N//3):
                    sqr.append(arr[i+k][j+l])
            # 1~9까지의 중복 확인
            for m in range(1, N+1):
                if sqr.count(m) != 1:
                    result = 0 # 조건에 맞지 않으면 0을 출력

    print('#%d %d' %(tc+1, result))