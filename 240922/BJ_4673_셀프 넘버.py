def self_number(N, num):
    if num >= N: # pruning : 10000 이상의 숫자는 확인 불요
        return

    num_str = str(num)
    for i in range(len(num_str)):
        num += int(num_str[i])

    if num in lst:
        lst.remove(num)
    else:
        return # pruning : 일전에 이미 처리한 값

    self_number(N, num)


N = 10000 # to be 10,000 at submission
lst = list(range(1, N+1)) # 1 ~ 10,000까지의 숫자

for number in range(1, N+1):
    self_number(N, number) # self number가 아닌 수를 lst에서 제거

for number in lst:# self number만 남은 lst
    print(number) # self number를 한 줄에 하나씩 출력