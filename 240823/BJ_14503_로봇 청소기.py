from pprint import pprint

def f(r, c, d):
    # delta : 반시계방향 90 deg 회전
    di = [-1, 0, 1, 0]
    dj = [0, -1, 0, 1]

    cnt = 0
    while True:
        # 현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소한다.
        if arr[r][c] == 0:
            arr[r][c] = -1
            cnt += 1

        # 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우,
        # 반시계 방향으로 90 deg 회전한다.
        for _ in range(4):
            d += 1
            ni = r + di[d%4]
            nj = c + dj[d%4]
            if arr[ni][nj] == 0:
                # 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진한다.
                r, c = ni, nj  # 새로운 방향 설정
                break

        # 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우,
        else:
            # 바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 한 칸 후진하고 1번으로 돌아간다.
            if arr[r+di[(d+2)%4]][c+dj[(d+2)%4]] != 1:
                r, c = r+di[(d+2)%4], c+dj[(d+2)%4]
            else:
                return cnt

N, M = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
d = 4 - d

print(f(r, c, d))