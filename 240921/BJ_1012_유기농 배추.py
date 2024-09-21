from collections import deque

def bfs(x, y):
    queue = deque()
    queue.append([x, y])
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()

        for i in range(4):  # 4방향 탐색
            ni = x + di[i]
            nj = y + dj[i]
            if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj] and arr[ni][nj] == 1:
                queue.append([ni, nj])
                visited[ni][nj] = True
    return


T = int(input())

for _ in range(T):
    N, M, K = map(int, input().split())

    arr = [[0]*M for _ in range(N)]
    for _ in range(K):
        CABBAGE_x, CABBAGE_y = map(int, input().split())
        arr[CABBAGE_x][CABBAGE_y] = 1

    di, dj = [0, 1, 0, -1], [1, 0, -1, 0] # 4방향 탐색
    visited = [[False]*M for _ in range(N)]
    result = 0

    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1 and not visited[i][j]:
                bfs(i, j)
                result += 1

    print(result)


### ------------------------------------------------------------------------------------------------ ###
# 배추가 2500개까지 놓여질 수 있기 때문에 DFS로 풀면 recursion error 발생함

# def dfs(x, y):
#     visited[x][y] = True
#     for i in range(4):  # 4방향 탐색
#         ni = x + di[i]
#         nj = y + dj[i]
#         if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj] and arr[ni][nj] == 1:
#             dfs(ni, nj)
#
#
# T = int(input())
#
# for _ in range(T):
#     N, M, K = map(int, input().split())
#
#     arr = [[0]*M for _ in range(N)]
#     for _ in range(K):
#         CABBAGE_x, CABBAGE_y = map(int, input().split())
#         arr[CABBAGE_x][CABBAGE_y] = 1
#
#     di, dj = [0, 1, 0, -1], [1, 0, -1, 0] # 4방향 탐색
#     visited = [[False]*M for _ in range(N)]
#     result = 0
#
#     for i in range(N):
#         for j in range(M):
#             if arr[i][j] == 1 and not visited[i][j]:
#                 dfs(i, j)
#                 result += 1
#
#     print(result)