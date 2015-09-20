def Virus(n):
    if (n < 3):
        return "-1"
     
    threes = n//3
    fives = 0
     
    while threes >=0:
        rem = n - threes*3
        if rem % 5 == 0:
            fives = rem/5
            break
        threes -= 1
         
    if threes <= 0 and fives == 0:
        return "-1"
     
    return "555"*threes + "33333"*fives
 
if __name__ == '__main__':
    N = int(raw_input())
    for i in range(N):
        n = int(raw_input())
        print Virus(n)