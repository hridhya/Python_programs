def shades_of_grey(n):
    hex_array = []
    if n<0 :
        return []
    for i in range(1, min(n, 254)+1):
    	s = hex(i)[2:].zfill(2)
        hex_array.append('#'+s*3)
    return hex_array
	
	
print shades_of_grey(0)