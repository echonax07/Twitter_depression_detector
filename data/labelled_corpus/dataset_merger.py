# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 15:42:48 2021

@author: jhbmu
"""


import pandas as pd


df=pd.read_csv(r'D:\Project\Twitter_depression_detector\data\labelled_corpus\corpus.csv')
df=df.loc[:,['text','Depressed']]
df=df.rename(columns = {'text':'renderedContent','Depressed':'Depressive'})

df_2=pd.read_excel(r'D:\Project\Twitter_depression_detector\data\labelled_corpus\part_0.xlsx')
df_2=df_2[df_2['Depressive']==1]

df_3=pd.read_csv(r'D:\Project\Twitter_depression_detector\data\labelled_corpus\part_3.tsv',sep='\t')
df_3=df_3[df_3['Depressive']==1]


df=df.append(df_2).append(df_3)

df.to_csv(r'D:\Project\Twitter_depression_detector\data\labelled_corpus\Depression_merged_v1.tsv',sep='\t',index=False)
