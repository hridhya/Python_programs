import math
if __name__ == '__main__':
    
    text = raw_input().replace(" ", "")
    columns = int(math.ceil(math.sqrt(len(text))))
    for c in range(columns):
        print text[c::columns],