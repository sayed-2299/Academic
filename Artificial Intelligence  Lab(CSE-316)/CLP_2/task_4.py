import pprint
import string

text="Dictionary Items Dictionary items are ordered, changeable, and do not allow duplicates. Dictionary items are presented in key: value pairs, and can be referred to by using the key name."

text=text.lower()
text=text.translate(str.maketrans('', '', string.punctuation))
words=text.split()

dictionary={}
for word in words:
    if word in dictionary:
        dictionary[word]+=1
    else:
        dictionary[word]=1
print(dictionary)
