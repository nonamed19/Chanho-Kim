#1 시간 초과 - 수학식으로 풀어야 함

w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())

dir = [1, 1] # 초기 이동방향

for i in range(t):
    if p + dir[0] > w or q + dir[1] > h or p + dir[0] < 0 or q + dir[1] < 0:
        if (p == w and q == h) or (p == 0 and q == 0):
            dir[0] *= -1
            dir[1] *= -1
        elif p == w or p == 0:
            dir[0] *= -1
        elif q == h or q == 0:
            dir[1] *= -1
    p += dir[0]
    q += dir[1]

    print(p, q)