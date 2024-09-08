def score_max(cnt):
    global result
    if cnt == 9:
        start, score = 0, 0
        for inning in arr:
            b1, b2, b3, out = 0, 0, 0, 0
            while out <= 2:
                p = player[start]
                if inning[p] == 0: # 아웃
                    out += 1
                elif inning[p] == 1: # 1루타
                    score += b3
                    b1, b2, b3 = 1, b1, b2
                elif inning[p] == 2: # 2루타
                    score += b2 + b3
                    b1, b2, b3 = 0, 1, b1
                elif inning[p] == 3: # 3루타
                    score += b1 + b2 + b3
                    b1, b2, b3 = 0, 0, 1
                else: # 홈런
                    score += b1 + b2 + b3 + 1
                    b1, b2, b3 = 0, 0, 0

                start += 1
                start %= 9

        result = max(result, score)
        return

    for i in range(9):
        if visited[i]:
            continue

        visited[i] = 1 # 현재 위치 저장
        player[i] = cnt
        score_max(cnt + 1)
        visited[i] = 0 # 탐색 후 위치 삭제
        player[i] = 0


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
player = [0 for _ in range(9)]
visited = [0 for _ in range(9)]
player[3], visited[3] = 0, 1 # 4번 타자의 타순은 0번으로 고정

result = 0
score_max(1)
print(result)