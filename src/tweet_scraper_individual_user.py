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

model = pickle.load(open(r'D:\Project\Twitter_depression_detector\src\model.pkl', 'rb'))
tv=pickle.load(open(r'D:\Project\Twitter_depression_detector\src\tv.pkl', 'rb'))

# def scraper(username,since,until):
#     # place id of india is b850c1bfd38f30e0

#     # df = pd.DataFrame(itertools.islice(sntwitter.TwitterSearchScraper(
#     #     'from:{}'.format(username)).get_items(), no_of_tweets))
#     # df = df.loc[:, ['date', 'content']]
#     # return df
#     df = pd.DataFrame(itertools.islice(sntwitter.TwitterSearchScraper(
#         'from:{} since:{} until:{}'.format(username,since,until)).get_items(), 10000))
#     df = df.loc[:, ['date', 'renderedContent']]
#     return df


def predict(data,tv,model):  
    test_array = tv.transform(clean_tweets(data['renderedContent'])).toarray()
    prediction = model.predict(test_array)
    
    data['prediction']=prediction
    data['date']=data['date'].dt.strftime("%y-%m-%d")
    data=data.sort_values(by=['date'])
    return data

def plot(data):    
    
    dates=data['date'].unique()
    count_depressive = dict.fromkeys(dates, 0)
    count_non_depressive=dict.fromkeys(dates, 0)
    
    for i in range(len(data)):
        if data.loc[i,'prediction']==1:
            count_depressive[data.loc[i,'date']]+=1
        else:
            count_non_depressive[data.loc[i,'date']]+=1
    
    # Numbers of pairs of bars you want
    N =2
    # Data on X-axis
    # Specify the values of blue bars (height)
    blue_bar = list(count_non_depressive.values())
    # Specify the values of orange bars (height)
    orange_bar = list(count_depressive.values())
    max1=max(blue_bar)
    max2=max(orange_bar)
    max_overall=max(max1,max2)
    # Position of bars on x-axis
    ind = np.arange(len(blue_bar))
    
    fig, ax = plt.subplots(figsize=(10, 5))
    # Figure size
    
    
    # Width of a bar 
    width = 0.3       
    
    # Plotting
    ax.bar(ind-width/2, blue_bar , width, label='Non Depressive Tweets',zorder=100)
    ax.bar(ind+width/2, orange_bar, width, label='Depressive Tweets',zorder=100)
    
    ax.set_xlabel('Date')
    ax.set_ylabel('Count')
    ax.set_title('Tweet Nature over time')
    
    # xticks()
    # First argument - A list of positions at which ticks should be placed
    # Second argument -  A list of labels to place at the given locations
    ax.set_xticks(ind + width)
    ax.set_xticklabels((list(count_non_depressive.keys())))
    ax.set_yticks(range(0,max_overall+1))
    # Finding the best position for legends and putting it
    ax.legend(loc='best')
    ax.grid(zorder=2)
    fig.show()


data=scraper('imlonelyandsadd','2021-03-20','2021-03-30')  
data=predict(data,tv,model)    
plot(data)
