from itertools import combinations

N = int(input())
arr = []
members = []

for i in range(N):
    arr.append(list(map(int, input().split())))
    members.append(i)

team1 = list(combinations(members, N//2))

lst = []
for i in team1:
    team2 = list(combinations(i, 2))
    tmp = 0
    for j in team2:
        tmp += arr[j[0]][j[1]] + arr[j[1]][j[0]]
    lst.append(tmp) # lst : [(0, 1)], [(0, 2)], [(0, 3)], [(1, 2)], [(1, 3)], [(2, 3)]

result = 100
for i in range(len(lst)//2):
    tmp = abs(lst[i] - lst[len(lst)-i-1])
    result = min(result, tmp)

print(result)