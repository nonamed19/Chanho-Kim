N = int(input())
orders = list(range(1, N + 1))  # 초기 순서 저장
numbers = list(map(int, input().split()))  # 이동해야 하는 칸의 수

arrays = [[0, 0] for _ in range(N)]
for i in range(N):
    arrays[i] = [numbers[i], orders[i]]  # [이동해야 하는 칸의 수, 초기 순서]

results = []
idx = 0  # initialization
while arrays:
    move = arrays[idx][0]
    results.append(arrays[idx][1])  # move의 순서에 따라 results에 초기 순서 저장
    arrays.pop(idx)  # move의 순서에 따라 arrays에서 element 추출

    # 종료 조건(마지막 element에 대한 계산이 완료된 경우)
    if not arrays:
        break

    # python index 로직에 따라 move가 양수인 경우와 음수인 경우를 나누어 계산해야 함.
    if move > 0:
        idx = (idx + move - 1) % len(arrays)
    else:  # elif move <= 0:
        idx = (idx + move) % len(arrays)

print(*results)