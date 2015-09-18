def candies(s):
	sum = 0
	if len(s) <= 1 :
		return -1
	max_candy = max(s)
	for n in s :
		extra = max_candy-n
		sum+=extra
	return sum
print candies([4])###result = 9