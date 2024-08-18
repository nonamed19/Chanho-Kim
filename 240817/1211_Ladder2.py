for _ in range(10):
    tc = int(input()) # 테스트 케이스의 번호
    N = 100 # N x N 행렬
    arr_input = [list(map(int, input().split())) for _ in range(N)]
    result = []

    # 좌-우가 0으로 둘러 쌓이고 102 x 100 크기의 arr_input 정보가 담긴 행렬 생성
    arr = [[0]*(N+2) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            arr[i][j+1] = arr_input[i][j]

    for j in range(1, N+1): # 100 x 102 행렬로 만들었기 때문에 range(1, N+1)
        if arr[0][j] == 1:
            now_i, now_j, start_j, cnt = 1, j, j-1, 0  # 시작 위치 탐색, 100 x 102 행렬로 만들었기 때문에 j-1
            while 1 <= now_i < N and 1 <= now_j < N+2:
                ### 오른쪽에 길이 있는 경우
                if arr[now_i][now_j+1] == 1 and now_j+1 < N+2:
                    while arr[now_i][now_j+1] == 1:
                        now_j += 1
                        cnt += 1

                ### 왼쪽에 길이 있는 경우
                elif arr[now_i][now_j-1] == 1 and 1 <= now_j-1:
                    while arr[now_i][now_j-1] == 1:
                        now_j -= 1
                        cnt += 1

                ### 아래로 내려 가는 경우
                now_i += 1
                cnt += 1

            result.append([cnt, start_j])

    print('#%d %d' %(tc, sorted(result)[0][1]))