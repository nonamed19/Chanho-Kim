N = int(input())
lst = list(map(int, input().split()))

key = lst[0]
cnt_plus = 0
cnt_minus = 0
result = 0
for num in lst:
    if num > key:
        cnt_plus += 1
        cnt_minus = 1
        if cnt_plus >= result:
            result = cnt_plus
    elif num < key:
        cnt_plus = 1
        cnt_minus += 1
        if cnt_minus >= result:
            result = cnt_minus
    else:
        cnt_plus += 1
        cnt_minus += 1
        if max(cnt_plus, cnt_minus) >= result:
            result = max(cnt_plus, cnt_minus)
    key = num
