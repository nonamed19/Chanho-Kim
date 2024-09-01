import sys

def bfs(x, y):
    visited = [[0]*M for _ in range(N)]
    queue = [[x, y]]
    visited[x][y] = 1 # 방문 처리
    while queue:
        j, i = queue.pop(0)
        for k in range(4):
            ni, nj = i + di[k], j + dj[k]
            if 0 <= ni < M and 0 <= nj < N and visited[nj][ni] == 0 and arr[nj][ni] != 0:
                visited[nj][ni] = visited[j][i] + 1
                queue.append([nj, ni])
    return visited[N-1][M-1]


N, M = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

print(bfs(0,0))