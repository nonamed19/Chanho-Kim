for _ in range(10):
    tc = int(input())
    N = 100 # 100 x 100 행렬
    lst = [input() for _ in range(N)] # list(str)으로 받기
    lst_inv = [''.join(x) for x in zip(*lst)] # 전치행렬 in str
    count = 0

    # 행렬 탐색
    for i in range(N): # i = N
        for j in range(N): # i = N
            for k in range(1, N-j+1):
                temp1 = lst[i][j:j+k] # 행 palindrome 확인
                temp2 = lst_inv[i][j:j+k] # 열 palindrome 확인
                if temp1 == temp1[::-1] or temp2 == temp2[::-1]:
                    count = max(count, k)

    print('#%d %d' %(tc, count))