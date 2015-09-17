def sum_of_n(n) :
	sum = 0
	lst = []
  # your code goes here
	if n>0 :
		for i in range(0,n+1) :
			sum+=i
			lst.append(sum)
	
	
	else :
		for i in range(0, abs(n)+1) :
			sum+=i
			lst.append(-sum)
			
	return lst
			

  