N = int(input())
orders = list(range(1, N + 1))
numbers = list(map(int, input().split()))

arrays = [[0, 0] for _ in range(N)]
for i in range(N):
    arrays[i] = [numbers[i], orders[i]]

results = []
idx = 0  # initialization
while arrays:
    move = arrays[idx][0]
    results.append(arrays[idx][1])
    arrays.pop(idx)

    # 종료 조건(마지막 element에 대한 계산이 완료된 경우)
    if not arrays:
        break

    if move > 0:
        idx = (idx + move - 1) % len(arrays)
    else:  # elif move <= 0:
        idx = (idx + move) % len(arrays)

print(*results)