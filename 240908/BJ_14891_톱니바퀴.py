def calculate(num, dir, visited):
    def turn_cw(gear):
        gear.insert(0, gear.pop())
        return

    def turn_ccw(gear):
        gear.append(gear.pop(0))
        return

    visited[num] = 1 # 탐색 여부 저장

    if num < 4 and visited[num + 1] == 0: # 우측 톱니바퀴 계산
        if gear_lst[num][2] != gear_lst[num + 1][-2]:
            calculate(num + 1, -dir, visited)
    if num > 1 and visited[num - 1] == 0: # 좌측 톱니바퀴 계산
        if gear_lst[num - 1][2] != gear_lst[num][-2]:
            calculate(num - 1, -dir, visited)

    if dir == 1: # clockwise
        turn_cw(gear_lst[num])
    else: # dir == -1: # counter-clockwise
        turn_ccw(gear_lst[num])
    return


gear_lst = [0] + [list(map(int, input())) for _ in range(4)]

N = int(input())
for _ in range(N):
    visited = [0] * 5
    num, dir = map(int, input().split())
    calculate(num, dir, visited)

result = 0
for i in range(1, 5):
    result += gear_lst[i][0]*(2**(i-1))
print(result)