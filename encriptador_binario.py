abc="abcdefghijklmnopqrstuvwxz "
ABC=abc.upper()
#print(abc)
#print(ABC)
list_abc=[]
dict_abcdario={}
dict_bin={}
for letter in abc:
    list_abc.append(letter)
for letter in ABC:
    list_abc.append(letter)
#print(list_abc)
for value in list_abc:
    dict_abcdario[value]=ord(value)
    dict_bin[value]=bin(ord(value))
#print(dict_abcdario)
#print(dict_bin)
txt="Anita lava la Tina"
list_txt=[]
for c in txt:
    list_txt.append(dict_bin[c])
txtbin="".join(list_txt)
#print(list_txt)
print(txtbin)