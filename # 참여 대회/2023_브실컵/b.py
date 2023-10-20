for i in range(1, int(input()) + 1):
    n = int(input())

    if n > 4500:
        print('Case #%d: Round 1' % (i))
    elif n > 1000:
        print('Case #%d: Round 2' % (i))
    elif n > 25:
        print('Case #%d: Round 3' % (i))
    else:
        print('Case #%d: World Finals' % (i))
