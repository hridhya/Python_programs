if __name__ == '__main__':
	t = input()
	for _ in xrange(t):
		black,white = map(int, raw_input().split())
        x, y, z = map(int, raw_input().split())
        if x>y and x>z :
            print white*y + black*(y+z)
        elif y>x and y>z:
            print black*x + white*(x+z)
        else :
            print black*x + white*y
        
	   