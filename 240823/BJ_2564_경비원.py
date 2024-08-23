# 총 블록의 크기 x-y size
x, y = map(int, input().split())
N = int(input())

# 상점의 위치
lst = []
for i in range(N):
    lst.append(list(map(int, input().split())))

# 동근이의 위치
n, m = map(int, input().split())

result = 0
for temp in lst:
    if n == 1: # 동근이의 위치가 북쪽
        if temp[0] == 1: # 상점의 위치가 북쪽
            result += abs(temp[1]-m)
        elif temp[0] == 2: # 상점의 위치가 남쪽
            result += min((temp[1]+m+y), ((x-temp[1])+(x-m)+y))
        elif temp[0] == 3: # 상점의 위치가 서쪽
            result += temp[1]+m
        else: # 상점의 위치가 동쪽
            result += temp[1]+(x-m)

    elif n == 2: # 동근이의 위치가 남쪽
        if temp[0] == 1:  # 상점의 위치가 북쪽
            result += min((temp[1]+m+y), ((x-temp[1])+(x-m)+y))
        elif temp[0] == 2: # 상점의 위치가 남쪽
            result += abs(temp[1]-m)
        elif temp[0] == 3: # 상점의 위치가 서쪽
            result += (y-temp[1])+m
        else: # 상점의 위치가 동쪽
            result += (y-temp[1])+(x-m)

    elif n == 3: # 동근이의 위치가 서쪽
        if temp[0] == 1:  # 상점의 위치가 북쪽
            result += temp[1]+m
        elif temp[0] == 2: # 상점의 위치가 남쪽
            result += temp[1]+(y-m)
        elif temp[0] == 3: # 상점의 위치가 서쪽
            result += abs(temp[1]-m)
        else: # 상점의 위치가 동쪽
            result += min((temp[1]+m+x), ((y-temp[1])+(y-m)+x))
    
    else: # 동근이의 위치가 동쪽
        if temp[0] == 1:  # 상점의 위치가 북쪽
            result += (x-temp[1])+m
        elif temp[0] == 2: # 상점의 위치가 남쪽
            result += (x-temp[1])+(y-m)
        elif temp[0] == 3: # 상점의 위치가 서쪽
            result += min((temp[1]+m+x), ((y-temp[1])+(y-m)+x))
        else: # 상점의 위치가 동쪽
            result += abs(temp[1]-m)

print(result)