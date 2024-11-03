while True:
    words = list(input())
    # 종료 조건(온점 하나만 input으로 들어오는 경우)
    if len(words) == 1:
        break

    queue = []
    for word in words:
        # character가 소괄호 / 대괄호인 경우 queue에 삽입
        if word == '(' or word == ')' or word == '[' or word == ']':
            queue.append(word)

        # 소괄호 / 대괄호가 queue에 삽입된 후 가장 최근에 삽입된 character와 짝이 맞는지 확인
        if len(queue) >= 2:
            word2 = queue.pop()
            word1 = queue.pop()
            if word1 == '(' and word2 == ')':  # 소괄호인 경우 queue에서 pop()
                pass
            elif word1 == '[' and word2 == ']':  # 대괄호인 경우 queue에서 pop()
                pass
            else:  # 소괄호 & 대괄호인 경우 queue에 다시 삽입
                queue.append(word1)
                queue.append(word2)

    if queue:  # queue에 element가 남아있는 경우 짝이 맞지 않다는 것을 의미
        print('no')
    else:  # queue에 element가 남아있지 않는 경우 모든 짝이 맞다는 것을 의미
        print('yes')