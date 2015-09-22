if __name__ == '__main__':
    t = input()
    for i in xrange(t):
        N, K = [int(i) for i in raw_input().split()]
        A = map(int, raw_input().split())
        for x in A:
            if x <= 0:
                K -= 1
        if K <= 0:
                print "NO"
        else:
            print "YES"