def flipBits(a):
   return ~a & 0xffffffff 
 
if __name__ == '__main__':
    n = int(raw_input())
    for i in range(0,n):
        a = int(raw_input())
        print flipBits(a)
        