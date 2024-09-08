from pprint import pprint

def spread(X, Y):
    if arr[X][Y] >= 5:  # 현재 위치에 있는 미세먼지가 5 이상일 때 확산
        di, dj = [0, 1, 0, -1], [1, 0, -1, 0]  # 방향: 동, 남, 서, 북
        amount = arr[X][Y] // 5  # 각 방향으로 확산되는 미세먼지 양
        cnt = 0  # 확산된 방향 개수
        for k in range(4):
            ni = X + di[k]
            nj = Y + dj[k]
            if 1 <= ni <= R and 1 <= nj <= C and arr[ni][nj] != -1:  # 경계 및 공기청정기 확인
                arr[ni][nj] += amount
                cnt += 1
        arr[X][Y] -= amount * cnt  # 확산된 양만큼 현재 위치에서 차감
    return

def aircon():
    # 공기청정기 작동 로직 추가 필요
    pass


R, C, T = map(int, input().split())
arr_input = [list(map(int, input().split())) for _ in range(R)]

# 배열을 경계 포함하여 확장
arr = [[-1] * (C + 2) for _ in range(R + 2)]
for i in range(R):
    for j in range(C):
        arr[i + 1][j + 1] = arr_input[i][j]

# 확산 실행
for i in range(1, R + 1):
    for j in range(1, C + 1):
        spread(i, j)

pprint(arr)
