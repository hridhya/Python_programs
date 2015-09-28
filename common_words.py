def common_words(list_1, list_2) :
	result = []
	##result=[word for word in list_1 if word in list_2]
	for word in list_1.split() :
		if word in list_2.split() :
			result.append(word)
	return result
	
if __name__ == '__main__':
	list_1 = raw_input("Enter your first string ")
	list_2 = raw_input("Enter your second string ")
	print common_words(list_1, list_2)

