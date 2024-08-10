from pprint import pprint

T = int(input()) # 테스트 케이스 개수 T (1 ≤ T ≤ 50)

for tc in range(T):
    N = int(input()) # 칠할 영역의 개수 N (2 ≤ N ≤ 30)
    temp = [[0 for j in range(10)] for i in range(10)]
    temp_red = [[0 for j in range(10)] for i in range(10)]
    temp_blue = [[0 for j in range(10)] for i in range(10)]
    arr_red, arr_blue = [], []
    count_red, count_blue = 0, 0
    result = 0

    # 입력 받는 리스트의 4번째 원소가 1이면 arr_red, 2이면 arr_blue
    for i in range(N):
        arr = list(map(int, input().split())) # (0 ≤ r1, c1, r2, c2 ≤ 9)
        if arr[4] == 1: # RED
            arr_red.append(arr[0:4])
            count_red += 1
        elif arr[4] == 2: # BLUE
            arr_blue.append(arr[0:4])
            count_blue += 1

    # 빨간색 영역에 대해 temp_red의 행렬을 1로 채움
    iter_red = 0
    while count_red > 0:
        for i in range(arr_red[iter_red][0], arr_red[iter_red][2]+1):
            for j in range(arr_red[iter_red][1], arr_red[iter_red][3]+1):
                if temp_red[i][j] == 0:
                    temp_red[i][j] += 1
        iter_red += 1
        count_red -= 1

    # 파란색 영역에 대해 temp_blue의 행렬을 1로 채움
    iter_blue = 0
    while count_blue > 0:
        for i in range(arr_blue[iter_blue][0], arr_blue[iter_blue][2]+1):
            for j in range(arr_blue[iter_blue][1], arr_blue[iter_blue][3]+1):
                if temp_blue[i][j] == 0:
                    temp_blue[i][j] += 1
        iter_blue += 1
        count_blue -= 1

    # temp_red와 temp_blue의 행렬을 순회하며 둘다 1인 구간에 대해 result += 1
    for i in range(10):
        for j in range(10):
            if temp_red[i][j] == 1 and temp_blue[i][j] == 1:
                result += 1

    print('#%d %d' %(tc+1, result))