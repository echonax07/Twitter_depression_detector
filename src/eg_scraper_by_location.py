# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 17:50:03 2021

@author: jhbmu
"""


import pandas as pd
import snscrape.modules.twitter as sntwitter
import itertools



# place id of india is b850c1bfd38f30e0

df_city = pd.DataFrame(itertools.islice(sntwitter.TwitterSearchScraper(
    'depression place:b850c1bfd38f30e0 since:2020-06-01 until:2020-06-30').get_items(), 100))

df_city['user_location'] =  df_city['user'].apply(lambda x: x['location'])



