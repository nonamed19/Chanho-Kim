def f(N, M, K):
    time_total = 0
    time_bread = 0
    time_person = 0
    bread = 0

    while lst:
        time_total += 1 # debugging용
        time_bread += 1
        time_person += 1

        # 사람이 처음부터 들어와 있는 경우 고려
        if lst and lst[0] == 0 and K != 0:
            return 'Impossible'

        # 붕어빵 만들기
        if time_bread == M:
            bread += K
            time_bread = 0

        # 사람이 들어오는 시간 확인
        if lst and lst[0] == time_person:
            temp = 1
            while len(lst) > 1 and lst[0] == lst[1]:
                temp += 1
                lst.pop(1)
            bread -= temp
            if bread < 0:
                return 'Impossible'
            lst.pop(0)
    return 'Possible'

T = int(input())

for tc in range(T):
    N, M, K = map(int, input().split())
    lst = list(map(int, input().split())) # len(lst) == N
    lst = sorted(lst)

    print('#%d %s' %(tc+1, f(N, M, K)))