from pprint import pprint
import sys

def f(head, arr):
    temp = arr[:]
    head_idx = temp.index(head)
    ### ---------------------------- ###
    temp.pop(head_idx)
    temp.pop((head_idx+1) % 5)
    ### ---------------------------- ###

    ### ---------------------------- ###
    temp_result = 0
    for i in range(3):
        temp_sum = temp[i] + temp[i+1]
        temp_result = max(temp_result, temp_sum)
    ### ---------------------------- ###
    print(temp)
    print(temp_result)
    return temp_result

N = int(input())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

result = 0
result_temp = 0
for i in range(1, 2): # head
    result_temp = 0
    for j in range(N):
        result_temp += f(i, arr[j])
    result = max(result, result_temp)

print(result)