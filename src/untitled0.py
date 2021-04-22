# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 05:34:17 2021

@author: jhbmu
"""


import pandas as pd
import snscrape.modules.twitter as sntwitter
import itertools
    
id=1010966742653460000
df = pd.DataFrame(itertools.islice(sntwitter.TwitterSearchScraper(
        'since_id:{} max_id:{} -filter:safe'.format(id-1,id)).get_items(),10))
