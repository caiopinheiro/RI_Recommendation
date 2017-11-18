#!/usr/bin/env python
# -*- coding: utf-8 -*-

from nltk.tokenize import RegexpTokenizer
from stop_words import get_stop_words
from nltk.stem.porter import PorterStemmer
from gensim import corpora, models
import gensim
import csv
import pprint

tokenizer = RegexpTokenizer(r'[a-zA-Z]+')
en_stop = get_stop_words('en')
p_stemmer = PorterStemmer()
doc_set = []

print('Started reading')
with open('arquivo.csv', 'r', encoding='utf-8', errors='replace') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    count = 0
    for row in spamreader:
        doc_set.append(row[10] + ' ' + row[19] + ' ' + row[24] + ' ' + row[25])
        
        count += 1
        if count == 1000:
            break

print('End reading')
texts = []
for i in doc_set:
    raw = i.lower()
    tokens = tokenizer.tokenize(raw)
    stopped_tokens = [i for i in tokens if not i in en_stop]
    stemmed_tokens = [p_stemmer.stem(i) for i in stopped_tokens]
    texts.append(stemmed_tokens)

dictionary = corpora.Dictionary(texts)
# pprint.pprint(dictionary.token2id)

corpus = [dictionary.doc2bow(text) for text in texts]

ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=10, id2word = dictionary, passes=20)
# print(ldamodel.print_topics())

count = 0
for user_info in doc_set:
    # print(user_info)

    stopped_tokens = []
    stemmed_tokens = []
    corpus = []

    raw = user_info.lower()
    tokens = tokenizer.tokenize(raw)
    stopped_tokens = [i for i in tokens if not i in en_stop]
    stemmed_tokens = [p_stemmer.stem(i) for i in stopped_tokens]
    #dictionary = corpora.Dictionary([stemmed_tokens])
    corpus = [dictionary.doc2bow(text) for text in [stemmed_tokens]]
    
    print('User ' + str(count))
    for topic in ldamodel[corpus]:
        pprint.pprint(topic)
    count += 1
