class hash_map(object):

	aMap = []
	
	def __init__(self, table_size):
		self.table_size = table_size
		for i in range(0, self.table_size):
			self.aMap.append([])
	
    	
	def put(self, key,value):
		if key is None or value is None :
			raise ValueError('Please pass a valid key/value')
		hash_location = hash(key) % len(self.aMap)
		self.aMap[hash_location].append(value)
	
	def get(self, key):
		if key is None :
			raise ValueError('Please pass a valid key')
		hash_location = hash(key) % len(self.aMap)
		return self.aMap[hash_location]
		


if __name__ == '__main__':

	hashmap1 = hash_map(100)
	key,value = raw_input('Please enter a key and value... ').split() 
	hashmap1.put(key, value)
	Key = raw_input('Please enter a key whose value is to be checked... ')
	print hashmap1.get(Key)