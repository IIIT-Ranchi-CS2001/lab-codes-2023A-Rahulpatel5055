import pandas as pt
import numpy as np
data=pt.read_csv("C:\\Users\\dell\\Downloads\\AQI_Data.csv")
#the first five rows
print(data.head())
print("the last 6 rows is:")
#the last five rows
print(data.tail())
#the sumarry of staticts
print(data.describe())
print("the mean of aqi:")
c=[data.loc[:,'AQI']]
print(np.mean(c))
print("the mean of pm2.5:")
d=[data.loc[:,'PM2.5']]
print(np.mean(d))
print("the mean of pm10")
e=[data.loc[:,'PM10']]
print(np.mean(e))
print("the program end:")
# set 2 A PART
print(data.isnull())#check for the null

numeric_cols = data.select_dtypes(include=['int64', 'float64']).columns
data[numeric_cols] = data[numeric_cols].fillna(data[numeric_cols].mean())
print(data)



# set-2 b part
a=[data.loc[:,'AQI']]#extract the data and store in array (numpy)
print(np.mean(a))
print(np.std(a))
print(np.median(a))
