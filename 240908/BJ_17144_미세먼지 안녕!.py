from pprint import pprint

def spread(arr):
    di, dj = [0, 1, 0, -1], [1, 0, -1, 0]
    arr_temp = [[0]*C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if arr[i][j] >= 5: # 해당 칸의 크기가 5 이상일때만 확산이 일어남
                amount = arr[i][j] // 5 # 각 방향으로 확산되는 미세먼지 양
                cnt = 0 # 확산되는 미세먼지의 방향
                for k in range(4):
                    ni = i + di[k]
                    nj = j + dj[k]
                    if 0 <= ni < R and 0 <= nj < C:
                        if arr[ni][nj] != -1:
                            arr_temp[ni][nj] += amount # 확산되는 양은 따로 계산해야함
                            cnt += 1
                arr[i][j] -= (amount * cnt)

    for i in range(R):
        for j in range(C):
            arr[i][j] += arr_temp[i][j] # 확산되는 양은 따로 계산해야함
    return

def aircon(arr):
    upper = location[0] # aircon 상단
    for i in range(upper-1, 0, -1): # 아래 -> 위
        arr[i][0] = arr[i-1][0]
    for j in range(C-1): # 왼쪽 -> 오른쪽
        arr[0][j] = arr[0][j+1]
    for i in range(upper): # 위 -> 아래
        arr[i][C-1] = arr[i+1][C-1]
    for j in range(C-1, 1, -1): # 오른쪽 -> 왼쪽
        arr[upper][j] = arr[upper][j-1]
    arr[upper][1] = 0

    lower = location[1] # aircon 하단
    for i in range(lower+1, R-1): # 위 -> 아래
        arr[i][0] = arr[i+1][0]
    for j in range(C-1): # 왼쪽 -> 오른쪽
        arr[R-1][j] = arr[R-1][j+1]
    for i in range(R-1, lower, -1): # 아래 -> 위
        arr[i][C-1] = arr[i-1][C-1]
    for j in range(C-1, 1, -1): # 오른쪽 -> 왼쪽
        arr[lower][j] = arr[lower][j-1]
    arr[lower][1] = 0


R, C, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(R)]

location = []
for i in range(R):
    if -1 in arr[i]:
        location.append(i)

for _ in range(T):
    spread(arr)
    aircon(arr)

result = 0
for i in range(R):
    result += sum(arr[i])
print(result + 2)