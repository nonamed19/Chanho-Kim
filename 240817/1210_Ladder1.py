T = 10 # 10개의 테스트 케이스

for tc in range(T):
    N = int(input()) # 테스트 케이스의 번호
    arr = [list(map(int, input().split())) for _ in range(100)]

    start = 0
    for j in range(100):
        if arr[99][j] == 2:
            loc_j = j # 57
    
    loc_i = 99
    while loc_i > 0:
        if (loc_j > 0) and (arr[loc_i][loc_j-1] == 1):
            while (loc_j > 0) and (arr[loc_i][loc_j-1] == 1):
                loc_j -= 1
        elif (loc_j < 99) and (arr[loc_i][loc_j+1] == 1):
            while (loc_j < 99) and (arr[loc_i][loc_j+1] == 1):
                loc_j += 1
        if (loc_i > 0) and (arr[loc_i-1][loc_j] == 1):
            loc_i -= 1

    print('#%d %d' %(N, loc_j))
