def  findingDigits(foo):
    
    for a in foo:
    	count = 0
        for i in list(str(a)):
            if int(i) != 0 and a % int(i) == 0:
                count += 1
        print count
    
    
    
    
if __name__ == '__main__':
    findingDigits([12, 1012])