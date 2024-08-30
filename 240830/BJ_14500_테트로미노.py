from pprint import pprint
import sys

N, M = map(int, sys.stdin.readline().split())
arr_input = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
arr = [[0]*(max(N, M)+2) for _ in range(max(N, M)+2)]

for i in range(N):
    for j in range(M):
        arr[i+1][j+1] = arr_input[i][j]

result1 = 0
for i in range(1, N):
    temp_lst = []
    boundary = []
    for j in range(1, M):
        temp_lst = [arr[i][j], arr[i][j+1], arr[i+1][j], arr[i+1][j+1]]
        boundary = [arr[i-1][j], arr[i-1][j+1], arr[i][j+2], arr[i+1][j+2], arr[i+2][j+1], arr[i+2][j], arr[i+1][j-1], arr[i][j-1]]
        if min(temp_lst) < max(boundary):
            temp_lst.remove(min(temp_lst))
            temp_lst.append(max(boundary))
        result1 = max(result1, sum(temp_lst))

result2 = 0
for i in range(1, max(N, M)+1):
    for j in range(1, max(N, M)+1):
        temp_row = 0
        temp_col = 0
        for k in range(4):
            if 0 <= j+k < max(N, M)+1:
                temp_row += arr[i][j+k]
            if 0 <= j+k < max(N, M)+1:
                temp_col += arr[j+k][i]
        result2 = max(result2, max(temp_row, temp_col))

print(max(result1, result2))