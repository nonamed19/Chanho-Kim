from pprint import pprint

N, K = map(int, input().split())
arr = [list(0 for _ in range(7)) for _ in range(2)]

for i in range(N):
    Gender, Grade = map(int, input().split())
    arr[Gender][Grade] += 1

result = 0
for i in range(2):
    for j in range(7):
        while arr[i][j] > 0:
            arr[i][j] -= K
            result += 1

print(result)