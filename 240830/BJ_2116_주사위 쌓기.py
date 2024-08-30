import sys

def f(head, arr):
    temp = arr[:]
    lst = []
    head_idx = temp.index(head)
    tail_idx = 0

    if head_idx == 0 or head_idx == 5:
        if head_idx == 0:
            tail_idx = temp[5]
        else:
            tail_idx = temp[0]
        lst = temp[1:5]
    elif head_idx == 1 or head_idx == 3:
        if head_idx == 1:
            tail_idx = temp[3]
        else:
            tail_idx = temp[1]
        lst = [temp[0]] + [temp[2]] + temp[4:6]
    elif head_idx == 2 or head_idx == 4:
        if head_idx == 2:
            tail_idx = temp[4]
        else:
            tail_idx = temp[2]
        lst = temp[0:2] + [temp[3]] + [temp[5]]

    return tail_idx, max(lst)


N = int(input())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

result = 0
result_temp = 0
for i in range(1, 7): # head
    result_temp = 0
    head_idx = i
    for j in range(N):
        tail_idx, sum_temp = f(head_idx, arr[j])
        result_temp += sum_temp
        head_idx = tail_idx
    result = max(result, result_temp)

print(result)