K = int(input())
lst_index = [0]*6
lst_len = [0]*6

for i in range(6):
    lst_index[i], lst_len[i] = map(int, input().split())

lst_index *= 2
lst_len *= 2

idx = 0
for i in range(6):
    if lst_index[i:i+2] == lst_index[i+2:i+4]:
        idx = i+2
        if lst_len[idx] + lst_len[idx+2] == lst_len[idx+4]:
            surface = lst_len[idx]*lst_len[idx+1]
        else:
            surface = lst_len[idx-1]*lst_len[idx]

total = 0
for i in range(6):
    temp = lst_len[i]*lst_len[i+1]
    if total < temp:
        total = temp

print((total - surface)*K)