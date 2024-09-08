def f(N, M, cnt):
    global result, result_lst

    if M < 0: # f(N-2)가 음수가 되는 순간 재귀 종료
        if result < cnt:
            result = cnt
            return True
        else:
            return False

    result_lst.append(M) # 재귀 중 f(N-1)의 값을 저장
    return f(M, N-M, cnt + 1) # f(N-2) = f(N) - f(N-1)를 수행하는 재귀함수


N = int(input())

result = 0
for num in range(N + 1):
    result_lst = [N] # f(N)의 값은 먼저 저장하고 cnt = 1으로 시작
    if f(N, num, 1):
        elements = result_lst

print(result)
print(*elements)