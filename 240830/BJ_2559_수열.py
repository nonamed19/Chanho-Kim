# 1. 시간 초과

N, K = map(int, input().split())
lst = list(map(int, input().split()))

temp = sum(lst[:K])
result = temp

for i in range(N-K):
    temp = temp - lst[i] + lst[i+K]
    if result < temp:
        result = temp

print(result)