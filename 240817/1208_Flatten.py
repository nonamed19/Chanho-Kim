T = 10 # 총 10개의 테스트 케이스

for tc in range(T):
    N = int(input()) # 덤프 횟수는 1이상 1000이하
    lst = list(map(int, input().split())) # 가로 길이는 항상 100

    for _ in range(N+1):
        num_max = 1     # 모든 위치에서 상자의 높이는 1이상 100이하
        num_min = 100   # 모든 위치에서 상자의 높이는 1이상 100이하
        idx_max = 0
        idx_min = 0

        for j in range(100):
            if lst[j] > num_max: # 제일 높은 위치의 index 추출
                num_max = lst[j]
                idx_max = j
            if lst[j] < num_min: # 제일 낮은 위치의 index 추출
                num_min = lst[j]
                idx_min = j

        lst[idx_max] -= 1 # 제일 높은 위치의 값 -1
        lst[idx_min] += 1 # 제일 낮은 위치의 값 +1

    print('#%d %d' %(tc+1, num_max - num_min))