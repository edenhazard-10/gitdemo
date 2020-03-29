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