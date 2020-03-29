#大学计算机基础大作业
txt=open("小白鼠文章.txt", "r").read().splitlines()
stopword=open("停用词表.txt", "r").read().splitlines()
from matplotlib.font_manager import FontProperties
font = FontProperties(fname='C:\Windows\Fonts\simkai.ttf')
import matplotlib.pyplot as plt
import re
frequency={}
newfrequency={}
a=[]
b=[]
d=[]
e=[]
meaningless_words=["and","or","a","is","the","in","to","are","am","on","for","but","so","of","can"]
def f(s):
    for c in txt:
        c = re.sub(r'[.?!,""/]', ' ', c)
        c=c.lower()
        word=c.split(" ")
        word=[x for x in word if x != '']
        total_number=len(word)
        single_word=set(word)
        for c in single_word:
            frequency_word=word.count(c)
            frequency[c]=frequency_word
        return total_number, word,frequency
total_number,word,frequency=f(txt)
single_word=set(word)
def g(s):
    for c in meaningless_words:
        while c in word:
            word.remove(c)
        while c in stopword:
            word.remove(c)
    return word
newword=g(word)
for c in newword:
    count=newword.count(c)
    newfrequency[c]=count
for c in single_word:
    count=newword.count(c)
    a.append(count)
    a.sort()
b=a[-6:]
Min=min(b)
for c in single_word:
    count=newword.count(c)
    if count>=Min:
        d.append(c)
for c in d:
    e.append(newfrequency[c])
t={}
        