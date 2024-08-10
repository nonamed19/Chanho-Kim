from pprint import pprint

T = int(input()) # 총 테스트 케이스의 개수 T

for tc in range(T):
    # 세로 길이 N은 5 이상 15 이하의 정수이다. (5 ≤ N ≤ 15)
    # 단어의 길이 K는 2 이상 N 이하의 정수이다. (2 ≤ K ≤ N)
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    count = 0

    # 행 탐색
    for i in range(N):
        for j in range(N-K+1):
            num_sum = 0
            for k in range(K):
                num_sum += arr[i][j+k] # i번째부터 i+K만큼 떨어진 위치의 배열 합(0이면 빈칸)
            if j == 0: # 가장 왼쪽
                if num_sum == K and arr[i][j+K] == 0: # 가장 왼쪽에서 K까지는 1이고, j+K칸은 0인 경우
                    count += 1
            elif 1 <= j < N-K: # 중간
                if num_sum == K and (arr[i][j-1] + arr[i][j+K] == 0): # j-1과 j+K는 1이고 그 사이는 0인 경우
                    count += 1
            elif j == N-K: # 가장 오른쪽
                if num_sum == K and arr[i][j-1] == 0: # 가장 오른쪽에서 K까지는 1이고, j-K칸은 0인 경우
                    count += 1

    # 열 탐색
    for j in range(N):
        for i in range(N-K+1):
            num_sum = 0
            for k in range(K):
                num_sum += arr[i+k][j] # j번째부터 j+K만큼 떨어진 위치의 배열 합(0이면 빈칸)
            if i == 0:
                if num_sum == K and arr[i+K][j] == 0: # 가장 위에서 K까지는 1이고, i+K칸은 0인 경우
                    count += 1
            elif 1 <= i < N-K:
                if num_sum == K and (arr[i-1][j] + arr[i+K][j] == 0): # i-1과 i+K는 1이고 그 사이는 0인 경우
                    count += 1
            elif i == N-K:
                if num_sum == K and arr[i-1][j] == 0: # 가장 아래에서 K까지는 1이고, i-K칸은 0인 경우
                    count += 1

    print('#%d %d' %(tc+1, count))
