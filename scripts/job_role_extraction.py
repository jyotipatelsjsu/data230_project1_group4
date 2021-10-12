#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 15:36:51 2021

@author: sruthimallarapu
"""
import pandas as pd
import os
os.chdir("/Users/sruthimallarapu/Documents/Sruthi/Sem2/Data230/Project-1-dataset")
##Reading data
data= pd.read_csv("alldata.csv")
###Understanding about data
##reading colimns
data.columns
data.describe()

##subset the data
data['position']=data['position'].apply(lambda x: str(x))
data['position']=data['position'].apply(lambda x: x.lower())
#data_2 =data.loc[data['position'].str.contains(r'data|statistic|machine learning|business analyst|ai ',na=False,regex=True)]

####Cleaning the position title
positions=['data analyst','data scientist','decision scientist',]
#data['position2']=data['position'].apply(lambda x: 'data scientist' if any( y in x for y in ['scientist','data science','datascience']) else 'research analyst' if 'research' in x else 'data analyst' if any(y in x for y in ['data analyst','data analysis']) else 'business analyst' if 'business analyst' in x else 'machine learning engineer' if any(y in x for y in['machine learning','ai ']) else 'data engineer' if 'data engineer' in x else 'Statistical Analyst' if 'statistic' in x else 'Data Visualization Engineer' if 'visualization' in x else 'quantitative analyst'  if 'quantitative analyst ' in x else 'software engineer' if any (y in x for y in ['software engineer','software developer','software development'])  else x)
data['position2']=data['position'].apply(lambda x: 'data scientist' if any( y in x for y in ['scientist','data science','datascience']) else 'research analyst' 
                                         if 'research' in x  else 'business analyst'
                                         if any(y in x for  y in ['business analyst','business intelligence'])else 'machine learning engineer' 
                                         if any(y in x for y in['machine learning','ai ']) else 'data engineer' 
                                         if 'data engineer' in x else 'Statistical Analyst' 
                                         if 'statistic' in x else 'Data Visualization Engineer'
                                         if 'visualization' in x else 'quantitative analyst'  if 'quantitative' in x else 'data analyst' 
                                         if any(y in x for y in ['data analyst','data analysis','data']) else 'others')
###extracting skills
data['description']=data['description'].apply(lambda x: str(x))
data['description']=data['description'].apply(lambda x: x.lower())

data['python']=data['description'].apply(lambda x: 1 if any(y in x for y in ['python']) else 0)
data['sql']=data['description'].apply(lambda x: 1 if any(y in x for y in ['sql','sql/','sql,']) else 0)
data['R']=data['description'].apply(lambda x: 1 if any(y in x for y in [' r ','r/','r, ']) else 0)
data['tableau']=data['description'].apply(lambda x: 1 if any(y in x for y in ['tableau']) else 0)
data['statistics']=data['description'].apply(lambda x: 1 if any(y in x for y in ['statistic','stats/']) else 0)
data['machinelearning']=data['description'].apply(lambda x: 1 if any(y in x for y in ['machine learning','machinelearning','ml/','regression','random forest']) else 0)
data['SAS']=data['description'].apply(lambda x: 1 if any(y in x for y in ['sas']) else 0)
data['Scala']=data['description'].apply(lambda x: 1 if any(y in x for y in ['scala']) else 0)
data['java']=data['description'].apply(lambda x: 1 if any(y in x for y in ['java']) else 0)

data.to_csv('project_230.csv',index=False)