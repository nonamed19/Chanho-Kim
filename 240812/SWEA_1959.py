T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    lst1 = list(map(int, input().split()))
    lst2 = list(map(int, input().split()))
    result = 0

    if M > N: # list2가 list1보다 길이가 긴 경우,
        for j in range(M-N+1): # list2의 길이 - list1의 길이 + 1
            temp = 0
            for i in range(N): # list1의 길이
                temp += lst1[i]*lst2[i+j]
            if result < temp:
                result = temp
    elif N > M: # list1가 list2보다 길이가 긴 경우,
        for j in range(N-M+1): # list1의 길이 - list2의 길이 + 1
            temp = 0
            for i in range(M): # list2의 길이
                temp += lst2[i]*lst1[i+j]
            if result < temp:
                result = temp
    else: # list1와 list2의 길이가 같은 경우(일대일 대응)
        temp = 0
        for i in range(N):
            temp += lst1[i]*lst2[i]
        result = temp

    print('#%d %d' %(tc+1, result))