T = int(raw_input())
for i in range (0,T):
    A,B,C1 = [int(x) for x in raw_input().split(' ')]
    n = w = A/B
    while (w >= C1):
        ne = w/C1
        n += ne
        w %= C1
        w += ne
    answer = n 
    # write code to compute answer
    print answer