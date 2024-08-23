N = 4
lst = [0]*N
arr = [[0]*100 for _ in range(100)]
result = 0

for i in range(N):
    lst[i] = list(map(int, input().split()))

for s in range(N):
    for i in range(lst[s][0], lst[s][2]):
        for j in range(lst[s][1], lst[s][3]):
            arr[i][j] = 1

for i in range(len(arr)):
    result += arr[i].count(1)

print(result)