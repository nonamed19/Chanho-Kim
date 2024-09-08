N, M = map(int, input().split())
cut = int(input())

row = [0, M]
col = [0, N]
for _ in range(cut):
    A, B = map(int, input().split())
    if A == 0: # 가로로 자르는 점선
        row.append(B)
    else: # A == 1: # 세로로 자르는 점선
        col.append(B)
row.sort()
col.sort()

width, height = 0, 0
for i in range(len(row)-1):
    width = max(width, row[i+1] - row[i])
for i in range(len(col) - 1):
    height = max(height, col[i+1] - col[i])

result = width * height
print(result)