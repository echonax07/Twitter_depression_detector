# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 12:23:13 2021

@author: jhbmu
"""


import pandas as pd
import os


os.chdir('D:\\Study\\4.1\\BPT-Depression\\tweet_trend')

# Reads the json generated from the CLI commands above and creates a pandas dataframe
tweets_df = pd.read_csv('depression_tweets_2020-03-01.csv')
tweets_df=tweets_df.drop_duplicates(subset=['conversationId'])
tweets_df=tweets_df.drop(columns=['Unnamed: 0'],axis=1)
tweets_df['hashtags']=tweets_df.content.str.findall(r'#.*?(?=\s|$)')


tweets_df.hashtags.value_counts().head(20)
medical_terms = ["#mentalhealth", "#health", "#happiness", "#mentalillness", "#happy", "#joy", "#wellbeing"]
mask1 = tweets_df.hashtags.apply(lambda x: any(item for item in medical_terms if item in x))
tweets_df[mask1].content.tail()
tweets_df[mask1==False].content.head(10)
tweets_df=tweets_df[mask1==False]

mask2 = tweets_df.hashtags.apply(lambda x: len(x) < 4)
tweets_df=tweets_df[mask2]
tweets_df.hashtags.value_counts().head(20)
tweets_df.hashtags.value_counts().head(20)

tweets_df.content.tail(20)

mask5 = tweets_df.urls.apply(lambda x: len(x) < 5)

