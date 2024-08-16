T = int(input())

for tc in range(T):
    N, K = map(int, input().split())
    lst = sorted(list(map(int, input().split())))

    result = 0
    for i in range(K):
        result += lst[-1-i]

    print('#%d %d' %(tc+1, result))