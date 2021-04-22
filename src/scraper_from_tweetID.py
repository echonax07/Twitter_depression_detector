# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 00:06:53 2021

@author: jhbmu
"""


#This code creates the dataset from Corpus.csv which is downloadable from the
#internet well known dataset which is labeled manually by hand. But for the text
#of tweets you need to fetch them with their IDs.
import tweepy

# Twitter Developer keys here
# It is CENSORED
consumer_key = 'u9L8y92xb1S0OrqydndNzM3Al'
consumer_key_secret = 'UD0Rt625HHjnMwWKc5PH0YPLO2JE8aOzuGq39vLfVBU9zYWlm4'
access_token = '1308707110281195521-kYVJKftHmUlBEGNPIDzgH6iBuVBaxH'
access_token_secret = 'VuvHmZ52CSTleeiFAnUXnF00rK9LmToi0zZRQiZRkuDGQ'

auth = tweepy.OAuthHandler(consumer_key, consumer_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# This method creates the training set



# Code starts here
# This is corpus dataset
corpusFile = "D:\Project\Twitter_depression_detector\data\Depression_Annotated_Data (1)\Depression_Annotated_Data\DND_U_Id_Class.tsv"
# This is my target file
targetResultFile = "D:\Project\Twitter_depression_detector\data\Depression_Annotated_Data (1)\Depression_Annotated_Data\final_tweets_text.csv"

import csv
import time
import pandas as pd

counter = 0
corpus = []

corpus=pd.read_csv(corpusFile,sep='\t', header = None,names=['UserID','TweetID','Depressed','NonDepressed'])

corpus=corpus[corpus['Depressed']==1]

sleepTime = 2
trainingDataSet = []
corpus['text']=''
for i in range(len(corpus)):
    try:
        tweetFetched = api.get_status(corpus.iloc[i][1],tweet_mode="extended")
        print("Tweet fetched: " + str(i))
        print('Tweet: ',tweetFetched.full_text)
        corpus.loc[i,"text"] = tweetFetched.full_text
        time.sleep(sleepTime)
        
        
    except Exception as e:
            print(e)
            print("Inside the exception - no:2 ",i)          
            continue
   
with open(targetResultFile, 'w',encoding="UTF-8") as csvfile:
    linewriter = csv.writer(csvfile, delimiter='\t', quotechar="\"")
    for tweet in trainingDataSet:
        try:
            linewriter.writerow([tweet["tweet_id" ], tweet["text"], tweet["label"], tweet["topic"]])
        except Exception as e:
            print(e)

corpus.to_csv('corpus.csv',index=False)

corpus=pd.read_csv('corpus.csv')
corpus=corpus.dropna()
corpus.to_csv('corpus.csv',index=False)
# Code starts here
# This is corpus dataset
corpusFile = r"D:\Project\Twitter_depression_detector\data\Depression_Annotated_Data (1)\Depression_Annotated_Data\depressive_tweet_id.csv"
