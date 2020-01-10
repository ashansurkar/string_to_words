#!/usr/bin/python
import sys
import re
import nltk
from nltk.corpus import brown
# nltk.download('brown')
blacklisted_words = ['PHP','JavaScript','Microsoft','Windows','MSSQL','Healthy','Gym','Running','Authorization','Accept','Loves','Hate','Number','Token','Nails','The','A','Smaller','Bigger','Huge','Tiny']
blacklisted_words = [ i.lower() for i in blacklisted_words ]

string_first = " ".join(sys.argv[1:])
if not string_first:
    print("No string to check")
    exit()
string_first_temp = string_first.lower()

wordlist = []
for word in sorted(brown.words(),key=len,reverse=True):
    if not string_first_temp: break
    if string_first_temp and word.lower() in string_first_temp:
        string_first_temp = re.sub(word.lower(),'',string_first_temp)
        wordlist.append(word.lower())

splitwords = dict()
for w in wordlist:
    ind = string_first.lower().index(w)
    splitwords[ind] = w

newlist = []
for l, v in sorted(splitwords.items()):
    pattern = re.search(v,string_first, re.IGNORECASE)
    newlist.append(pattern.group())

print("split words :", " ".join(newlist))
for word in newlist:
    if word.lower() in blacklisted_words:
        print(word,"is blacklisted")
    else:
        print(word,"is not blacklisted")
