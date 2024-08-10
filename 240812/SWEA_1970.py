T = int(input())

for tc in range(T):
    change = int(input())
    money = [10, 50, 100, 500, 1000, 5000, 10000, 50000]
    money_inv = sorted(money, reverse = True)
    result = [0]*8

    for i in range(len(money_inv)):
        temp = change//money_inv[i]
        if temp >= 1:
            change -= money_inv[i]*temp
            result[i] += temp

    print('#%d' %(tc+1))
    print(*result)