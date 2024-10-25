while True:
    words = list(input())
    # 종료 조건
    if len(words) == 1:
        break

    queue = []
    for word in words:
        if word == '(' or word == ')' or word == '[' or word == ']':
            queue.append(word)

        if len(queue) >= 2:
            word2 = queue.pop()
            word1 = queue.pop()
            if word1 == '(' and word2 == ')':
                pass
            elif word1 == '[' and word2 == ']':
                pass
            else:
                queue.append(word1)
                queue.append(word2)

    if queue:
        print('no')
    else:
        print('yes')