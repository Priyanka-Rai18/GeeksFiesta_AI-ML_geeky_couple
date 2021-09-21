# -*- coding: utf-8 -*-
"""datapreprocess.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11WwrIYlYxKhvY9xTp2LrvuaODlovQRKq

#**Day 3**

##Importing libraries and dataset
"""

#importing libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import MinMaxScaler
import pickle

def prediction(year,month,day,hour,temperature,pressure,rain,wind_direction,wind_speed):
  E=0
  ENE=0
  ESE=0
  N=0
  NE=0
  NNE=0
  NNW=0
  NW=0
  S=0
  SE=0
  SSE=0
  SSW=0
  SW=0
  W=0
  WNW=0
  WSW = 0
  if wind_direction =='E':
    E=1
  if wind_direction=='ENE':
    ENE=1
  if wind_direction=='ESE':
    ESE=1
  if wind_direction=='NE':
    NE=1
  if wind_direction=='NNE':
    NNE=1
  if wind_direction=='NNW':
    NNW=1
  if wind_direction=='NW':
    NW=1
  if wind_direction=='S':
    S=1
  if wind_direction=='SE':
    SE=1
  if wind_direction=='SE':
    SE=1
  if wind_direction=='SSE':
    SSE=1
  if wind_direction=='SSW':
    SSW=1
  if wind_direction=='SW':
    SW=1
  if wind_direction=='W':
    W=1
  if wind_direction=='WNW':
    WNW=1
  if wind_direction=='WSW':
    WSW=1

  x=[year,	month,	hour,	temperature	,pressure,	rain,	wind_speed,	E,	ENE	,ESE,	N,	NE,	NNE,	NNW,	NW,	S	,SE,	SSE,	SSW	,SW	,W	,WNW,WSW]
  x[0]=(x[0]-ym)/yr
  x[1]=(x[1]-mm)/mr
  x[2]=(x[2]-hm)/hr
  x[4]=(x[4]-pmin)/pr

  pm2 = reg.predict([x])
  return pm2

#importing dataset
df=pd.read_csv("new-dataset-geeky_couple (1).csv")
   
 
df=df.fillna(method="bfill")

dummies = pd.get_dummies(df['wind_direction'])
df = df.drop('wind_direction',axis=1)
df = pd.concat([df, dummies], axis=1)


df=df.fillna(method="bfill")


from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
# scaling = MinMaxScaler()#StandardScaler()#MinMaxScaler()
# scaling.fit(df[['year','month','hour','pressure']])

# df[['year','month','hour','pressure']]=scaling.fit_transform(df[['year','month','hour','pressure']])
sy=MinMaxScaler()
sm=MinMaxScaler()
sh=MinMaxScaler()
sp=MinMaxScaler()
df[['year']] = sy.fit_transform(df[['year']])
ym=sy.data_min_
yr=sy.data_range_
df[['month']] = sm.fit_transform(df[['month']])
mm=sm.data_min_
mr=sm.data_range_
df[['hour']] = sh.fit_transform(df[['hour']])
hm=sh.data_min_
hr=sh.data_range_
df[['pressure']] = sp.fit_transform(df[['pressure']])
pmin=sp.data_min_
pr=sp.data_range_
#print(np.where(df['wind_speed']>-60))
#replacing lower outlier
median = df.loc[df['wind_speed']>-60, 'wind_speed'].median()
df.loc[df.wind_speed<-60, 'wind_speed'] = np.nan
df.fillna(median,inplace=True)
#replacing upper outlier
#print(np.where(df['wind_speed']>4))
median1 = df.loc[df['wind_speed']>4, 'wind_speed'].median()
df.loc[df.wind_speed>4, 'wind_speed'] = np.nan
df.fillna(median1,inplace=True)


#REPLACING OUTLIER IN rain COLUMN BY MEDIAN METHOD
# Position of the Outlier
#print(np.where(df['rain']>0))
median2 = df.loc[df['rain']>0, 'rain'].median()
df.loc[df.rain>0, 'rain'] = np.nan
df.fillna(median2,inplace=True)
df.boxplot(['rain'])


df=df.drop(['day'],axis=1)


df= df.loc[:, ~df.columns.str.contains('^Unnamed')]


x = df.drop(['PM2.5'],axis=1)
y = df[['PM2.5']]


from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import accuracy_score
reg = RandomForestRegressor(n_estimators=13, random_state=0)
#training the dataset
reg.fit(x,y.values.ravel())
#year,month,day,hour,temperature,pressure,rain,wind_direction,wind_speed
# print(prediction(year,month,day,hour,temperature,pressure,rain,wind_direction,wind_speed))

# pickle.dump(reg, open('model.pkl','wb'))

# model = pickle.load(open('model.pkl','rb'))

