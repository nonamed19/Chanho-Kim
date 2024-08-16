T = int(input())

for tc in range(T):
    N, K = map(int, input().split())
    lst = list(map(int, input().split()))

    lst_stu = [x for x in range(1, N+1)]

    for stu in lst:
        if stu in lst_stu:
            lst_stu.remove(stu)

    print('#%d' %(tc+1), *lst_stu)