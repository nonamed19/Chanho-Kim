def merge_sort(A, p, r, K):
    if p < r:
        q = abs((p + r) // 2)       # q는 p, r의 중간 지점
        merge_sort(A, p, q, K)      # 전반부 정렬
        merge_sort(A, q + 1, r, K)  # 후반부 정렬
        merge(A, p, q, r, K)        # 병합


def merge(A, p, q, r, K):
    global count, result
    i, j, t = p, q + 1, 0
    tmp = [0] * (r - p + 1)

    while i <= q and j <= r:
        if A[i] <= A[j]:
            tmp[t] = A[i]
            i += 1
        else:
            tmp[t] = A[j]
            j += 1
        t += 1

    while i <= q:       # 왼쪽 배열 부분이 남은 경우
        tmp[t] = A[i]
        i += 1
        t += 1

    while j <= r:       # 오른쪽 배열 부분이 남은 경우
        tmp[t] = A[j]
        j += 1
        t += 1

    for i in range(t):  # 결과를 A[p..r]에 저장
        A[p + i] = tmp[i]
        count += 1

        if count == K:  # 배열 A에 K 번째 저장 되는 수를 출력
            result = A[p + i]


N, K = map(int, input().split())
numbers = list(map(int, input().split()))
count, result = 0, -1

merge_sort(numbers, 0, N - 1, K)

print(result)