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
for i in range(len(d)):
    t[d[i]]=e[i]
print(f(txt),g(word),newfrequency,a,d,e,t)
plt.bar(d,e,label=u"关键词",color="b")
plt.xlabel(u"单词",FontProperties=font)
plt.ylabel(u"词频",FontProperties=font)
plt.title(u"关键词表",FontProperties=font)
plt.legend(prop=font)
plt.show()
import tkinter as tk
import tkinter.messagebox
simpleword=tk.Tk()
simpleword.title('虚假的word')
top=tk.Tk()
def choose():
    tk.messagebox.showinfo(title='显示原文',message=word)
Choose=tk.Button(simpleword,text='显示原文',command=choose).pack()
def showfrequency():
    tk.messagebox.showinfo(title='展示词频',message=t)
Showfrequency=tk.Button(simpleword,text='展示词频',command=showfrequency).pack()
def keyword():
    tk.messagebox.showinfo(title='展示关键词',message=d)
Keyword=tk.Button(simpleword,text='展示关键词',command=keyword).pack()
simpleword.mainloop()
      