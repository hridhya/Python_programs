def  findingDigits(num):
	sum = 0
	
	n = num
	while n>0 :
			
		copy_num = n%10
			
		if num%copy_num == 0 :
			sum+=1
		n = n/10
			
	return sum

foo = [122, 12]
for num in foo:	
	print findingDigits(num)