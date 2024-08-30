# i 의미 : i번째 부분집합
for i in range(1 << len(arr)):
    for idx in range(len(arr)):
        # i & (i << idx)
        # - i번째 부분집합에 idx 요소가 포함되어 있나요 ?
        if i & (1 << idx):
            print(arr[idx], end = ' ')
    print()