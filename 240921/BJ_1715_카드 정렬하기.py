import sys


def heappush(num):
    arr.append(num)
    idx = len(arr) - 1
    while idx > 0:
        parent = (idx - 1) // 2
        if arr[parent] > arr[idx]: # 부모노드가 자식노드보다 더 큰 경우
            arr[parent], arr[idx] = arr[idx], arr[parent]
            idx = parent
        else: # if arr[parent] < arr[idx]
            break


def heappop():
    min_num = arr[0]
    num_last = arr.pop()
    if arr:
        arr[0] = num_last
        idx = 0

        while True:
            left = 2 * idx + 1
            right = 2 * idx + 2
            minimum = idx

            if left < len(arr) and arr[left] < arr[minimum]:
                minimum = left
            if right < len(arr) and arr[right] < arr[minimum]:
                minimum = right
            if minimum == idx:
                break # minimum node를 찾은 경우

            arr[idx], arr[minimum] = arr[minimum], arr[idx]
            idx = minimum

    return min_num


N = int(input())
arr = []

for i in range(N):
    num = int(sys.stdin.readline())
    heappush(num)

result = 0
for i in range(N-1):
    A, B = heappop(), heappop()
    heappush(A + B)
    result += A + B

print(result)