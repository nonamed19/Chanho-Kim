from collections import deque

def bfs(queue, target):
    while queue:
        now, iter = queue.popleft()
        if now[0] == target[0] and now[1] == target[1]: # 현재 위치와 목표 위치가 동일한 경우
            return iter

        for i in range(8):
            ni = now[0] + di[i]
            nj = now[1] + dj[i]
            if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj]:
                visited[ni][nj] = True
                queue.append(([ni, nj], iter + 1))

    return -1


T = int(input())

for tc in range(T):
    N = int(input())  # N x N 크기의 체스판
    now = list(map(int, input().split()))
    target = list(map(int, input().split()))

    queue = deque()
    queue.append((now, 0))  # 현재 위치 및 탐색 횟수 queue에 저장

    visited = [[False] * N for _ in range(N)]
    visited[now[0]][now[1]] = True

    di, dj = [-2, -1, 1, 2, 2, 1, -1, -2], [1, 2, 2, 1, -1, -2, -2, -1]
    result = bfs(queue, target)

    print(result)