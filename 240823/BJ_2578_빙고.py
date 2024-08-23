def f():
    for s in range(N*N):
        for i in range(N):
            for j in range(N):
                if arr[i][j] == lst[s]:
                    check[i][j] += 1
                    if bingo(check):
                        return s+1


def bingo(arr):
    call = 0
    cnt_diag, cnt_inv_diag = 0, 0
    for i in range(N):
        cnt_row, cnt_column = 0, 0
        for j in range(N):
            if arr[i][j] == 1:
                cnt_row += 1
                if cnt_row == 5:
                    call += 1
            if arr[j][i] == 1:
                cnt_column += 1
                if cnt_column == 5:
                    call += 1
        if arr[i][i] == 1:
            cnt_diag += 1
            if cnt_diag == 5:
                call += 1
        if arr[-1-i][i] == 1:
            cnt_inv_diag += 1
            if cnt_inv_diag == 5:
                call += 1
    if call >= 3:
        return True
    return False


N = 5

# 빙고판 저장
arr = [list(map(int, input().split())) for _ in range(N)]
check = [[0]*N for _ in range(N)]

lst = []
# 사회자가 부르는 숫자 저장
for i in range(N):
    temp = list(map(int, input().split()))
    for num in temp:
        lst.append(num)

print(f())