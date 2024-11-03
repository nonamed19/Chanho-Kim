def cantor(strings, N):
    # 모든 선의 길이가 1일때 까지 반복
    if N == 1:
        print(*strings, end = '')
        return

    # 각 선(문자열)을 3등분 하고, 가운데 문자열을 공백으로 바꾼다.
    start, end = int(N * (1/3)), int(N * (2/3))
    for i in range(start, end):
        strings[i] = ' '

    cantor(strings[:start], N/3)
    cantor(strings[start:end], N/3)
    cantor(strings[end:], N/3)
    return


while True:
    try:  # 입력을 여러 줄로 이루어져 있다.
        N = 3 ** int(input())  # -가 3**N개 있는 문자열에서 시작
        strings = ['-'] * N
        cantor(strings, N)
        print()
    except:  # 파일의 끝에서 입력을 멈춘다.
        break