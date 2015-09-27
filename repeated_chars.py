##Number of repeated letters i a string
def repeat(check_str):

	count = {}
	for letter in check_str:
		if count.has_key(letter):
			count[letter] += 1
		else:
			count[letter] = 1
			
	for key in count:
		if count[key] > 1:
			print key, count[key]
			
if __name__ == '__main__':
	str = raw_input("Enter your string ")
	repeat(str.strip())	
	