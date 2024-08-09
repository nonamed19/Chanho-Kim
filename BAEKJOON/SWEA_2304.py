from pprint import pprint

N = int(input())
lst, lst_sorted = [], []
lst_x, lst_y = [], []

for i in range(N):
    lst.append(list(map(int, input().split())))

for i in range(N):
    lst_x.append(lst[i][0])
    lst_y.append(lst[i][1])

lst_x_sorted = sorted(lst_x)
lst_y_sorted = sorted(lst_y)

H_max = lst_y_sorted[N-1]
for i in range(N):
    if lst[i][1] == H_max:
        L_H_max = lst[i][0]

for i in range(N):
    lst_sorted.append([lst_x_sorted[i], lst[lst_x.index(lst_x_sorted[i])][1]])

validation = 1
while validation != 0:
    validation = 0
    for i in range(1, len(lst_sorted)-1):
        if lst_sorted[i-1][1] >= lst_sorted[i][1] and lst_sorted[i][1] <= lst_sorted[i+1][1]:
            lst_sorted.pop(i)
            validation += 1
            break

result = 0
for i in range(len(lst_sorted)-1):
    width = lst_sorted[i+1][0]-lst_sorted[i][0]
    height = min(lst_sorted[i+1][1], lst_sorted[i][1])
    area = width*height
    result += area

result += H_max*1 # 제일 높은 높이 1칸 추가

print(result)