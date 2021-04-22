# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 13:44:25 2021

@author: jhbmu
"""


# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 03:20:34 2021

@author: jhbmu
"""
import pandas as pd
import snscrape.modules.twitter as sntwitter
import itertools
from datetime import date,timedelta
import pickle
from utils import clean_tweets
import matplotlib.pyplot as plt
import numpy as np
from creds import CONSUMER_KEY,CONSUMER_SECRET,access_token,access_token_secret
import tweepy
model = pickle.load(open(r'D:\Project\Twitter_depression_detector\src\model.pkl', 'rb'))
tv=pickle.load(open(r'D:\Project\Twitter_depression_detector\src\tv.pkl', 'rb'))
from datetime import datetime

 
# authorization of consumer key and consumer secret
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET) 
# set access to user's access key and access secret 
auth.set_access_token(access_token, access_token_secret)  
# calling the api 
api = tweepy.API(auth)  


def scraper(username,count):
        
    # fetching the statuses
    statuses = api.user_timeline(screen_name,tweet_mode = 'extended',count=25)
    
    json_data = [s._json for s in statuses]
    
    df = pd.io.json.json_normalize(json_data)
    start_date=df.iloc[0,0]
    start_date = datetime.strftime(datetime.strptime(start_date,'%a %b %d %H:%M:%S +0000 %Y'), '%d-%m-%y')
    end_date=df.iloc[-1,0]
    end_date = datetime.strftime(datetime.strptime(end_date,'%a %b %d %H:%M:%S +0000 %Y'), '%d-%m-%y')
    
    df=df.loc[:,['full_text']]
    return df,start_date,end_date



def predict(data,tv,model):  
    test_array = tv.transform(clean_tweets(data['full_text'])).toarray()
    prediction = model.predict(test_array)
    
    data['prediction']=prediction
    return data

def plot(data,start_date,end_date):
    plt.style.use('seaborn-white')
    fig = plt.figure(figsize=(10, 5)) 
    gs = gridspec.GridSpec(1, 2, width_ratios=[3, 1]) 
    ax0 = plt.subplot(gs[0])
    ax1 = plt.subplot(gs[1])
    x=list(range(1, len(data)+1))    
    
    # plot line plot
    ax0.plot(x,data['prediction'],color='blue')
    ax0.set_yticks(range(0,2))
    # Finding the best position for legends and putting it   
    ax0.legend(loc='best')
    ax0.set_xlabel('Tweet Count')
    ax0.set_ylabel('Tweet Nature')
    ax0.set_title('Tweet Nature in the timeperiod: {} to {}'.format(start_date,end_date))
    
    
    labels = 'Depressive','Non Depressive'
    sizes = [100*data['prediction'].tolist().count(1)/len(data), 100*data['prediction'].tolist().count(0)/len(data)]
    colors = ["Red", "Blue"]
    # plot pie chart
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    ax1.set_title('Ratio')
    plt.show()

data,start_date,end_date=scraper('imlonelyandsadd',25)  

data=predict(data,tv,model)    

plot(data,start_date,end_date)
