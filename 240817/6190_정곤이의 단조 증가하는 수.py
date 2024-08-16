T = int(input())

for tc in range(T):
    N = int(input())
    lst = list(map(int, input().split()))
    result = -1
    validation = 0

    for i in range(N-1):
        for j in range(i+1, N):
            temp = str(lst[i] * lst[j])

            lst_temp = []
            for k in range(len(temp)):
                lst_temp.append(int(temp[k]))

            # 곱한 숫자가 1자리 수이면서 result보다 클 때
            if len(lst_temp) == 1 and result < lst_temp[0]:
                result = lst_temp[0]

            # 곱한 숫자가 2자리 이상이면서 result보다 클 때
            m = 0
            while m < len(lst_temp) - 1:
                if lst_temp[m] > lst_temp[m+1]:
                    break
                if m == len(lst_temp) - 2:
                    num_temp = 0
                    for l in range(len(lst_temp)):
                        num_temp += lst_temp[-1-l]*10**l
                    if result < num_temp:
                        result = num_temp
                    break
                m += 1

    print('#%d %d' %(tc+1, result))