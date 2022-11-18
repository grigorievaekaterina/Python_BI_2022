#!/usr/bin/env python
# coding: utf-8

# In[428]:


import re


# ### Task 1

# In[429]:


pattern_1 = r"(ftp[.][\w+|.|/|#]*)"
ftps = open('ftps.txt', 'w')
with open("references.txt") as input_file:
    line = "line"
    while len(line) != 0:
        line = input_file.readline()
        match = re.findall(pattern_1, line)
        if match != []:
            c += len(match)
            ftps.write('\n'.join(match))
ftps.close()            


# ### Task 2-5

# In[430]:


import seaborn as sns


# In[431]:


#all numbers from the text will be written here
numbers = ''

#all with-a-words will be here
a_words = ''

#all sentences with ! end will be here
exc_sentences = ''

#all unique words and len-s will be here
unique_len = {}
unique_words = set()

with open("2430AD.txt") as input_file:
    line = "line"
    while len(line) != 0:
        line = input_file.readline()
        
        #numbers
        match_num = re.findall(r"(\d+)", line)
        if match_num != []:
            numbers += '\n'.join(match_num) + '\n'
        
        #all words with a
        match_a = re.findall(r"[a-zA-Z]*[a][a-zA-Z]*", line)
        if match_a != []:
            a_words += '\n'.join(match_a) + '\n'
        

        #all sentences with !
        s = re.sub(r'\s+', ' ', line)
        for s in re.split(r'(?<=[.!?…])', s):
            match_exc = re.findall(r'[^"^ ].*[!].*', s)
            if match_exc != []:
                exc_sentences += "\n".join(match_exc) + '\n'

        #unique words
        words = re.findall(r"\w+", line.lower())        
        if words != []:
            for w in words:
                if w not in unique_words:
                    unique_words.add(w)
                    if len(w) not in unique_len.keys():
                        unique_len.update({len(w): 1})
                    else:
                        unique_len[len(w)] += 1


# In[432]:


print(numbers)


# In[433]:


print(a_words)


# In[434]:


print(exc_sentences)


# In[435]:


#barplot for unique
for key in list(unique_len.keys()):
    unique_len[key] = unique_len[key]/len(unique_words)
        
sns.barplot(x = list(unique_len.keys()), y = list(unique_len.values()))


# ### Task 6

# In[436]:


s = input().split()
output = ''
for w in s:
    syllables = re.findall(r"[БбВвГгДдЖжЗзЙйКкЛлМмНнПпРрСсТтФфХхЦцЧчШшЩщЬьЪь]*[АаЕеËëИиОоУуЫыЭэЮюЯя]",  w)
    for syl in syllables:
        output += syl+'к'+syl[-1].lower()
    output += ' '
print(output)


# ### Task 7

# In[437]:


def find_n_words_sentences(text, number):
    output = []
    regex = re.compile(r'[.|!|?|…]')
    sentences = filter(lambda x: x, [x.strip() for x in regex.split(text)])
    for s in sentences:
        words = re.split(r" ", s)
        if len(words) == number:
            output.append(tuple(words))
    return output


# In[438]:


#example
find_n_words_sentences("Здесь три слова. Здесь тоже три", 3)


# In[ ]:




