import os
import pandas as pd
import numpy as np
import collections
import matplotlib.pyplot as plt

if("reload" not in globals()):
    reload = True
    
if(reload):
    db = pd.read_excel('recipeInfo/recipeInfo.xls',encoding='utf8')
    
    db2 = db.dropna(subset=['ingredients_bag-of-words'],axis=0)
    ds_bag = db2['ingredients_bag-of-words'].apply(lambda x :[s for s in x.split(' ') if s.isalpha()])
    
    reload = False
    
    
unique_words = collections.Counter()
for recipe_words in ds_bag.values:
    unique_words.update(recipe_words)

sorted_words = dict()

for key in unique_words:
    if(unique_words[key] in sorted_words):
        sorted_words[unique_words[key]].append(key)
    else:
        sorted_words[unique_words[key]] = [key]
        
nb_words = {i:len(sorted_words[i]) for i in sorted_words}

plt.figure()
x = list(nb_words.keys())
y = list(nb_words.values())
plt.plot(x,y,'.')
plt.xlabel('Number of occurences')
plt.ylabel('Number of distincts words')
plt.show()

nb_words_sort = sorted(list(nb_words.items()))
cum_distinct = [nb_words_sort[0]]
for (i,nb) in nb_words_sort[1:]:
    cum_distinct.append((i,nb + cum_distinct[-1][1]))
    
plt.figure()
x = [ind for (ind,val) in cum_distinct]
y = [val for (ind,val) in cum_distinct]
plt.plot(x,y)
plt.xlabel("Number of occurences")
plt.ylabel("Cumulative number of distinct words")
plt.show()


words_by_occ = []
for i in nb_words:
    words_by_occ.append((i,nb_words[i]*i))

words_by_occ.sort()

cum_words = [words_by_occ[0]]
for (i,nb) in words_by_occ[1:]:
    cum_words.append((i,nb+cum_words[-1][1]))

plt.figure()
x = [ind for (ind,val) in cum_words]
y = [val/cum_words[-1][-1]*100 for (ind,val) in cum_words]
plt.plot(x,y)
plt.xlabel("Number of occurences")
plt.ylabel("Cumulative number of words (in %)")
plt.show()