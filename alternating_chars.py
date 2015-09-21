if __name__ == '__main__':
    t = input()
    for i in range(t):
        s = raw_input()
        del_count = 0
        lst = []
        for i in range(1,len(s)):
            if s[i]==s[i-1]:
                del_count+=1
        print del_count    