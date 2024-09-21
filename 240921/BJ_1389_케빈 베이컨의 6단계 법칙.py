from collections import deque

def KevinBacon(self):
    lst_tem = [0] * N # 케빈 베이컨의 수를 저장하는 list

    for target in range(1, N+1):
        if target != self:
            lst_tem[target-1] = bfs(self, target)

    return sum(lst_tem)


def bfs(start, target):
    queue = deque()
    queue.append([start, 1])  # 맨 처음으로 탐색하는 지점 저장
    visited = [False] * (N+1)
    visited[start] = True

    while queue:
        node, dist = queue.popleft()

        if node == target:
            return dist

        for friend in lst_adj[node]:
            if not visited[friend]:
                visited[friend] = True
                queue.append([friend, dist + 1])


N, M = map(int, input().split())
lst_adj = list([] for _ in range(N + 1))

for i in range(1, M+1):
    A, B = map(int, input().split())
    lst_adj[A].append(B)
    lst_adj[B].append(A)

lst_cnt = [0] * N
for i in range(1, N+1):
    lst_cnt[i-1] = KevinBacon(i)

print(lst_cnt.index(min(lst_cnt)) + 1)