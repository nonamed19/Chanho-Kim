import sys

def heappush(num):
    arr.append(num)
    idx = len(arr) - 1
    while idx > 0:
        parent = (idx - 1) // 2
        if arr[parent] < arr[idx]: # 부모노드가 자식노드보다 더 작은 경우
            arr[parent], arr[idx] = arr[idx], arr[parent]
            idx = parent
        else: # if arr[parent] > arr[idx]
            break

def heappop():
    if not arr:
        return 0

    max_num = arr[0]
    num_last = arr.pop()
    if arr:
        arr[0] = num_last
        idx = 0

        while True:
            left = 2 * idx + 1
            right = 2 * idx + 2
            maximum = idx

            if left < len(arr) and arr[left] > arr[maximum]:
                maximum = left
            if right < len(arr) and arr[right] > arr[maximum]:
                maximum = right
            if maximum == idx:
                break # maximum node를 찾은 경우

            arr[idx], arr[maximum] = arr[maximum], arr[idx]
            idx = maximum

    return max_num


N = int(sys.stdin.readline())
arr = []

for i in range(N):
    num = int(sys.stdin.readline())

    if num == 0:
        print(heappop())
    else:  # if num != 0:
        heappush(num)