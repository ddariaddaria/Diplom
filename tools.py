from pprint import pprint
import pandas as pd
import nltk
import regex as re
import pymorphy2
#?
morph = pymorphy2.MorphAnalyzer()

#splitting skills, whick like 'c/c++'
def split_skills(skills_list, not_to_split):
    skills_list_new = []
    for skill in skills_list:
        skill = skill.lower()
        res = [el for el in not_to_split if(el in skill)]
        if bool(res) == False:
            if re.search('[/\,(]', skill) == None:
                skills_list_new.append(skill)
            else:
                splited_skill = re.split('[/\,(]', skill)
                for skill in splited_skill:
                    skills_list_new.append(skill)
        else:
            skills_list_new.append(skill)
    return skills_list_new

#deleting irrelivant characters
def clean_text(skill, not_to_split):
    skill = skill.lower()
    skill = re.sub(r'1c', r'1с', skill)
    skill = re.sub(r'1[\s][сc]', r'1с', skill)
    skill = re.sub('quot', '', skill)
    skill = re.sub('c++', 'c+', skill)
    if re.search('1с', skill) == None:
        skill = re.sub(r'[0-9]', '', skill)
    else:
        skill = re.sub('0|[2-9]', '', skill)
    res = [el for el in not_to_split if(el in skill)]
    if bool(res) == False:
        skill = re.sub(r'[^\w\s+]', ' ', skill).strip()
    skill = re.sub(r'\s+', ' ', skill)
    return skill

#deleting irrelivant characters in text - возомжно не нужно
def clean_text_2(text, not_to_split):
    text_cleaned = []
    if type(text) == str:
        t_list = list()
        t_list.append(text)
        text = t_list
    for elem in text:
        elem = elem.lower()
        elem = re.sub(r'1c', r'1с', elem)
        elem = re.sub(r'1[\s][сc]', r'1с', elem)
        elem = re.sub('quot', '', elem)
        if re.search('1с', elem) == None:
            elem = re.sub(r'[0-9]', '', elem)
        else:
            #elem = re.sub('[0]', '', elem)
            elem = re.sub('0|[2-9]', '', elem)
        res = [el for el in not_to_split if(el in elem)]
        if bool(res) == False:
            elem = re.sub(r'[^\w\s+]', ' ', elem).strip()
        elem = re.sub(r'\s+', ' ', elem)
        text_cleaned.append(elem)
    return text_cleaned

#lemmatization
def lemmatization(word_list):
    lemm_word_list = []
    for word in word_list:
        lemm_word_list.append(morph.parse(word)[0].normal_form)
    return lemm_word_list

#?
from nltk.stem import SnowballStemmer
snowball = SnowballStemmer(language='russian')
#stemming
def stemming(word_list):
    stemmed = []
    for word in word_list:
        stemmed.append(snowball.stem(word))
    return stemmed

#stop-words removing
def remove_stop_words(tokens, stopwords):
    tokens = [word for word in tokens if word not in stopwords]
    return tokens


#creating a list of the most frequent n-grams
from operator import itemgetter

def most_frequent_ngrams(ngrams_column, frequency):
    ngrams_list = ngrams_column.to_list()
    ngrams = []
    for row in ngrams_list:
        for ngram in row:
            ngrams.append(ngram)
    freqDist = nltk.FreqDist(ngrams)
    most_common = []
    for elem in freqDist.items():
        if elem[1] >= frequency:
            most_common.append(elem)
    most_common = sorted(most_common, key = itemgetter(1), reverse = True)
    return most_common     
