T = 10

for tc in range(T):
    Testcase = int(input())
    N = 100  # 100 x 100 행렬
    lst = [input() for _ in range(N)]
    lst_inv = [''.join(row) for row in zip(*lst)]  # 전치된 행렬을 string으로 변환
    count = 0

    # 행과 열 동시에 탐색
    for i in range(N):
        for j in range(N):
            for k in range(N-j, 0, -1):  # 큰 길이부터 탐색
                temp1 = lst[i][j:j+k]
                temp2 = lst_inv[i][j:j+k]
                if temp1 == temp1[::-1] or temp2 == temp2[::-1]:  # 회문 확인
                    count = max(count, k)
                    break  # 더 긴 길이의 회문을 찾았으므로 종료

    print('#%d %d' % (tc + 1, count))