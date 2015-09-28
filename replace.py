def replace_all(text, dic):
    for k, v in dic.items():
        text = text.replace(k, v)
    return text
 

my_text = 'Hello everybody.'
reps = {'H':'|-|', 'e':'3', 'o':'0'}
 
txt = replace_all(my_text, reps)
print txt  