__author__ = 'Viral'

import csv
import re
import nltk.corpus
from nltk import word_tokenize

reviews = []
tokenized = []
imp_words = []
file = open('test1.csv')
freader = csv.reader(file, quotechar = '"')

for row in freader:
    if (row[1] == 'English' and int(row[2]) <=2):
        reviews.append(row[6])

stopwords = nltk.corpus.stopwords.words('english')

for review in reviews:
    tokenized.append(word_tokenize(review))

#print(tokenized)

for x in tokenized:
    imp_words.append([word for word in x if word.lower()
                      not in stopwords and word.isalpha()])
#print(imp_words)


file1 = open('criteria.csv')
freader = csv.reader(file1, quotechar = '"')

counter = 0

for review_line in imp_words:
  for review_word in review_line:
    file1 = open('criteria.csv')
    freader = csv.reader(file1, quotechar = '"')
    counter = 0
    for row in freader:
        counter1 = 0
        if counter < 1:
                counter += 1
                continue
        for criteria_word in row:
            if criteria_word != '':
                if counter1 != 1:
                    counter1 += 1
                    continue
                else:
                    if criteria_word in review_word:
                        print(imp_words[0])
                        print(criteria_word)








#y = []
#for x in imp_words:
#    y.append(re.findall(r'^.*(ing|ly|ed|ious|ies|ive|es|s|ment)$', x))

#print(y)




