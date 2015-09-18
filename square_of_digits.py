def square_of_digits(num) :
	new_num = ''
	copy_num = num
	while(num>0):
		copy_num = num%10
		square = copy_num**2
		new_num += str(square)
		num = num/10
	return new_num

print square_of_digits(9119)