import sys

def queue(stack, M):
    global cnt
    while stack[-1] > M:
        stack.pop()
        cnt += 1
    if stack[-1] < M:
        stack.append(M)
        cnt += 1


N, P = map(int, sys.stdin.readline().split())
stack = [[0] for _ in range(7)]
cnt = 0

for _ in range(N):
    S, M = map(int, sys.stdin.readline().split())
    queue(stack[S], M)

print(cnt)