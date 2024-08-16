from pprint import pprint

T = 10  # 10개의 테스트 케이스

for tc in range(T):
    T_num = int(input())  # 테스트 케이스 번호
    arr = [list(map(int, input().split())) for _ in range(100)]
    # 각 행/열/대각선에서 101번째 행렬을 만들어서 값을 저장
    temp = [[0 for _ in range(101)] for _ in range(101)]
    result = 0

    # temp 행렬에 arr 행렬의 100 x 100에 대한 값 저장
    for i in range(100):
        for j in range(100):
            temp[i][j] = arr[i][j]

    # 행 별 sum 101항에 추가
    for i in range(100):
        for j in range(100):
            temp[i][100] += arr[i][j]

    # 행 별 sum 최대값 찾기
    row_max = 0
    for i in range(100):
        if row_max <= temp[i][100]:
            row_max = temp[i][100]

    # 열 별 sum 101항에 추가
    for j in range(100):
        for i in range(100):
            temp[100][j] += arr[i][j]

    # 열 별 sum 최대값 찾기
    column_max = 0
    for j in range(100):
        if column_max <= temp[100][j]:
            column_max = temp[100][j]

    # 대각선1 최대값 찾기
    diag1_max = 0
    for i in range(100):
        diag1_max += temp[i][i]

    # 대각선2 최대값 찾기
    diag2_max = 0
    for i in range(100):
        diag2_max = temp[i][99 - i]

    # 최대값 찾기
    lst_max = [row_max, column_max, diag1_max, diag2_max]
    for num in lst_max:
        if result <= num:
            result = num

    print('#%d %d' % (tc + 1, result))