from pprint import pprint

T = 10

for tc in range(T):
    Testcase = int(input())
    N = 100 # 100 x 100 행렬
    arr = [list(input()) for _ in range(N)]
    count = 0

    # 행 탐색
    for i in range(N):
        for j in range(N):
            M = j + 1  # length of palindrome
            while M < N:
                for k in range(N-M+1):
                    lst = list(arr[i][x] for x in range(j, M))
                    for l in range(len(lst)//2):
                        # print(lst)
                        if lst[l] != lst[-1-l]:
                            break   # 회문이 아닌 경우
                        else:
                            if count < len(lst):
                                count = len(lst)
                M += 1

    # # 열 탐색
    # for j in range(8):
    #     for i in range(8-N+1):
    #         lst = list(arr[x][j] for x in range(i, i+N))
    #
    #         for k in range(N//2):
    #             if lst[k] != lst[-1-k]:
    #                 break   # 회문이 아닌 경우
    #         else:
    #             count += 1
    #
    print('#%d %d' %(tc+1, count))