def f():
    di = [0, 0, 1] # 오른쪽, 왼쪽, 아래
    dj = [1, -1, 0]
    lst_start = []

    # 시작점 찾기
    for j in range(N):
        if arr[0][j] == 1:
            lst_start.append([1, j])

    for i in range(len(lst_start)):
        now_i, now_j = lst_start[i][0], lst_start[i][1]
        print(now_i, now_j)
        while True:
            # 오른쪽에 길이 있는 경우
            if arr[now_i][now_j+dj[0]] == 1 and now_j+dj[0] < N:
                now_j += dj[0]
                continue
                # while now_j != 0:
                #     now_j += dj[0]
                #     print(now_i, now_j)
                #     if now_j + dj[0] == 0 or now_j + dj[0] == N-1:
                #         break

            # 왼쪽에 길이 있는 경우
            elif arr[now_i][now_j+dj[1]] == 1 and 0 <= now_j+dj[1]:
                while now_j != 0:
                    if now_j + dj[1] == 0 or now_j + dj[1] == 0:
                        break
                    now_j += dj[1]
                    print(now_i, now_j)
                now_j -= dj[1]

            # 아래로 가는 길이 있는 경우
            if arr[now_i+di[2]][now_j] == 1 and now_i+di[2] < N:
                now_i += di[2]
                print(now_i, now_j)

            if arr[now_i][now_j] == 2:
                return True

T = 1 # 10으로 바꿔야 함

for tc in range(10):
    Testcase = int(input())
    N = 10 # 100 x 100 행렬
    arr = [list(map(int, input().split())) for _ in range(N)]

    print(f())