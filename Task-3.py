word = 'pythonist'
dict_ = {x:word.count(x) for x in word}
for s in dict_:
    print(f'Символ "{s}" встречается в строке - {dict_[s]}')