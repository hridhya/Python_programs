### iterate over a list and pull element indices at the same time####

###Use enumerate###
my_list = ['a', 'b', 'c']

for i, char in enumerate(my_list):
    print i, char
    
    
    
print list(enumerate(my_list))