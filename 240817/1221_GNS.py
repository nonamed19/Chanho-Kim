T = int(input()) # 테스트 케이스의 개수

for tc in range(T):
    L, N = input().split()
    N = int(int(N)/3) # 문자열의 길이 N 100≤N≤10000
    lst_alp = list(input().split())

    # list in ALPHABET to list in NUMBER
    lst_num = []
    for num in lst_alp:
        if num == 'ZRO': lst_num.append(0)
        elif num == 'ONE': lst_num.append(1)
        elif num == 'TWO': lst_num.append(2)
        elif num == 'THR': lst_num.append(3)
        elif num == 'FOR': lst_num.append(4)
        elif num == 'FIV': lst_num.append(5)
        elif num == 'SIX': lst_num.append(6)
        elif num == 'SVN': lst_num.append(7)
        elif num == 'EGT': lst_num.append(8)
        else: lst_num.append(9)

    # counting numbers of each NUMBER
    cnt = [0] * 10
    for num in lst_num:
        cnt[num] += 1

    # sorting in ascending direction(counting sort)
    result_num = []
    for i in range(len(cnt)):
        result_num += [i] * cnt[i]

    # list in NUMBER to list in ALPHABET
    result = []
    for num in result_num:
        if num == 0: result.append('ZRO')
        elif num == 1: result.append('ONE')
        elif num == 2: result.append('TWO')
        elif num == 3: result.append('THR')
        elif num == 4: result.append('FOR')
        elif num == 5: result.append('FIV')
        elif num == 6: result.append('SIX')
        elif num == 7: result.append('SVN')
        elif num == 8: result.append('EGT')
        else: result.append('NIN')

    print('#%d' %(tc+1))
    print(*result)