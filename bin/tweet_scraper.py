# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 12:44:56 2021

@author: jhbmu
"""

import os

os.chdir('D:\\Study\\4.1\\BPT-Depression\\tweet_trend')


import pandas as pd
from datetime import datetime
import time
# get a list of dates
date_list=pd.date_range(start="2020-03-01",end="2021-1-09").tolist()
date_list=[datetime.strptime(str(date), '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d') for date in date_list]
tweet_count=[]

for i in range(10):
    start= time.time()
    os.system('snscrape --jsonl --progress --max-results 20000 twitter-search "depression since:{} until:{}" > depression_tweets_{}.json'.format(date_list[i],date_list[i+1],date_list[i]))
    tweets_df = pd.read_json('depression_tweets_{}.json'.format(date_list[i]), lines=True)
    tweets_df.to_csv('depression_tweets_{}.csv'.format(date_list[i]))
    tweet_count.append(len(tweets_df))
    del(tweets_df)
    end=time.time()
    print('Time elapsed: ',end-start)
    
tweets_df=pd.read_json('depression_tweets.json', lines=True)

df = pd.DataFrame(list(zip(date_list, tweet_count)), 
               columns =['Date', 'Tweet_count']) 

df.to_csv('trend.csv')
