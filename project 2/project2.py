# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 15:17:40 2017

@author: patrickbowden
Project 2
"""
#imports
import nltk
import json
import csv

star_avg={}
count={}
lem=nltk.stem.WordNetLemmatizer()
wordlist = set(nltk.corpus.words.words())
stop = set(nltk.corpus.stopwords.words('english'))

#creating csv template
with open('data/output.csv','w') as csvfile:
    writer = csv.writer(csvfile,delimiter=',',quotechar='"',lineterminator='\n')
    writer.writerow(['Word','AVG'])

#opening json file
with open('data/yelp_academic_dataset_review_small.json') as data:
    jsondata=json.load(data)
    
    for i in range(0,len(jsondata)):
        
        #lemmatizing, tokenizing, and removing the stop words
        words=[lem.lemmatize(word.lower()) for word
            in nltk.word_tokenize(jsondata[i]['text'])
            if word.isalpha()
            and word not in stop
            and word in wordlist]        
        
        #calculating star avg
        for w in words:
            if w in star_avg:
                star_avg[w]+=jsondata[i]['stars']
                count[w]+=1
            elif w not in star_avg:
                star_avg[w]=jsondata[i]['stars']
                count[w]=1
                     
            if count[w] <=10:
                pass
            elif count[w] > 10:
                try:
                    
                    star_avg[w]= star_avg[w] / count[w]
                
                except:
                    pass
        
#writing to csv
with open('data/output.csv','a') as csvfile:
    writer = csv.writer(csvfile,delimiter=',',quotechar='"',lineterminator='\n')
    sort=sorted(star_avg.items(), key=lambda a:a[1], reverse=False)
    
    #grabbing least values
    for l in range(0,500):

        try:
                
            writer.writerow([sort[l][0],sort[l][1]])
            
        except:
            pass
        
    #grabbing greatest values
    for k in range(len(sort)-500,len(sort)):
            
        try:
            writer.writerow([sort[k][0],sort[k][1]])
        
        except:
            pass