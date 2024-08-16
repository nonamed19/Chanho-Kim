T = int(input()) # 테스트 케이스 개수 T (1<=T<=50)

for tc in range(T):
    N = int(input()) # 정수의 개수 N (10<=N<=100)
    arr = list(map(int, input().split())) # N개의 정수 ai (1<=ai<=100)
    result = [0] * 10

    # arr 선택 정렬
    for i in range(N-1):
        idx_min = i
        for j in range(i+1, N):
            if arr[idx_min] > arr[j]:
                idx_min = j
        arr[i], arr[idx_min] = arr[idx_min], arr[i]

    for i in range(10):
        if i % 2 == 0: # 짝수번째 요소(큰 값부터)
            result[i] = arr[-1-(i//2)]
        else: # 홀수번째 요소(작은 값부터)
            result[i] = arr[i//2]

    print(f'#{tc+1} {" ".join(map(str, result))}')