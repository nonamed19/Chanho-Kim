from pprint import pprint

T = int(input())  # 테스트 케이스의 개수 T

for tc in range(T):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    temp = [[0 for j in range(N)] for i in range(N)] # 합을 구하기 위해 N x N 빈 행렬 생성

    for i in range(N): # 현재 위치
        for j in range(N): # 현재 위치
            num_sum = 0
            for k in range(M): # 위치 + M만큼 loop를 돌려서 추가
                for l in range(M): # 위치 + M만큼 loop를 돌려서 추가
                    if 0 <= i+k <= N-1 and 0 <= j+l <= N-1: # N x N 배열 내로 범위 제한
                        num_sum += arr[i+k][j+l]
            temp[i][j] = num_sum

    num_max = 0
    for i in range(N):
        for j in range(N):
            if num_max <= temp[i][j]:
                num_max = temp[i][j]

    print('#%d %d' % (tc+1, num_max))