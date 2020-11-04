from PIL import Image
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import jieba
import numpy as np
from collections import Counter

text = open('禮運大同.txt', "r",encoding="utf-8").read()  
 
jieba.set_dictionary('dictionary/dict.txt.big.txt')
with open('dictionary/stopWord_cloud.txt', 'r', encoding='utf-8-sig') as f: 

    stops = f.read().split('\n')   
terms = []  
for t in jieba.cut(text, cut_all=False):  
    if t not in stops:  
        terms.append(t)
diction = Counter(terms)

font = "鋼筆體W2.TTC"

mask = np.array(Image.open("joestar.png"))  
#wordcloud = WordCloud(font_path=font) 
wordcloud = WordCloud(background_color="white",mask=mask, font_path=font)  
wordcloud.generate_from_frequencies(diction)  


plt.figure(figsize=(10,10))
plt.imshow(wordcloud)
plt.axis("off")
plt.show()

wordcloud.to_file("news_Wordcloud.png")  
