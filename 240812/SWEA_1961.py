from pprint import pprint

def rotate(N, arr):
    for i in range(N):
        temp1, temp2, temp3 = [], [], []
        for j in range(N):
            temp1.append(arr[-1-j][i])
            temp2.append(arr[N-1-i][N-1-j])
            temp3.append(arr[j][N-1-i])
        print(''.join(temp1), end = ' ')
        print(''.join(temp2), end = ' ')
        print(''.join(temp3), end = ' ')
        print(end = '\n')

T = int(input())

for tc in range(T):
    N = int(input())
    arr = [list(map(str, input().split())) for _ in range(N)]

    print('#%d' %(tc+1))
    rotate(N, arr)