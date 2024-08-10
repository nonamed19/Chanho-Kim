T = int(input())  # 케이스 개수 T ( 1 ≤ T ≤ 50 )

for tc in range(T):
    N = int(input())  # 카드 장수 ( 5 ≤ N ≤ 100 )
    lst = list(map(int, input()))
    temp = [0] * 10 # count를 위한 빈 리스트 생성
    num_max, num_idx = 0, 0

    for i in range(N): # 카드가 등장한 횟수만큼 count += 1 수행
        temp[lst[i]] += 1

    for j in range(10): # max(temp) 및 그 index j 추출
        if temp[j] >= num_idx:
            num_idx = temp[j]
            num_max = j

    print('#%d %d %d' % (tc+1, num_max, num_idx))