T = int(input()) # 테스트 케이스 개수 T가 주어진다. (1 ≤ T ≤ 50)

for tc in range(T):
    n, m = map(int, input().split())    # 정수의 개수 N과 구간의 개수 M 주어진다. (10 ≤ N ≤ 100, 2 ≤ M ＜ N)
    lst = list(map(int, input().split()))
    num_max = 1 * m # (1 ≤ a ≤ 10000)
    num_min = 10000 * m # (1 ≤ a ≤ 10000)

    for i in range(n-m+1): # n개의 원소 중 m개의 인접한 원소 개수 범위 지정
        num_sum = 0
        for j in range(m): # m개의 인접한 원소의 합
            num_sum += lst[i+j]

        if num_sum > num_max: # max(lst)
            num_max = num_sum
        if num_sum < num_min: # min(lst)
            num_min = num_sum

    print('#%d %d' %(tc+1, num_max-num_min))