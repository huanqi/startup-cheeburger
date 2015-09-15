import pandas as pd
#import numpy as np
#import csv as csv

data = pd.io.excel.read_excel("Cheeburger.xlsx", header = 0)

#print data['Id'].size

data['Gender'] = data['What is your gender?']
data['Age'] = data['What is your age?']
data['Service'] = data['How would you rate our customer service?']
data['Timely'] = data['Was your meal delivered in a timely manner?']
data['Worthy'] = data['Do you feel the quality of the food was worth the price?']
data['Cleanliness'] = data['Please rate the cleanliness of the restaurant during your recent visit.']
data['Distance'] = data['How far away do you live from a Cheeburger location?']
data['Return'] = data['Will you come back to us again?']
data['Refer'] = data['How likely are you to refer a friend to eat at a Cheeburger restaurant?']

# convert all the values into integar

# convert male/female to 1/0
data.loc[ data.Gender.isnull(), 'Gender'] = 'Male'
data['Gender'] = data['Gender'].map( {'Female':0, 'Male':1}).astype(int)


# convert Age  18 to 25:	20
#			   26 to 34:	30
#			   35 to 49:	45
#			   50 to 64:	60
#			   65 and over:	70
data.loc[ data.Age.isnull(), 'Age'] = '18  to 25'
data['Age'] = data['Age'].map( {'18  to 25':20, '26 to 34':30, '35 to 49':45, '50 to 64':60, '65 and over':70}).astype(int)


# convert service: Excellent/Good/Fair/Poor/Terrible to 2/1/0/-1/-2 
data.loc[ data.Service.isnull(), 'Service'] = 'Fair'
data['Service'] = data['Service'].map( {'Excellent':2, 'Good':1, 'Poor':0, 'Fair':-1, 'Terrible':-2}).astype(int)


# convert timely to 1/0
train = data['Timely'].values


# convert worthy to 1/0
train = data['Worthy'].values


# convert cleanliness: Extremely clean/Very clean/Somewhat clean/A little clean/Not at all clean to 2/1/0/-1/-2
data.loc[ data.Cleanliness.isnull(), 'Cleanliness'] = 'Somewhat clean'
data['Cleanliness'] = data['Cleanliness'].map( {'Extremely clean':2, 'Very clean':1, 'Somewhat clean':0, 'A little clean':-1, 'Not at all clean':-2}).astype(int)


# convert distance  Less than 5 miles:	0
#					5-10 miles:		1
#					10-20 miles: 	2
#					More than 20 miles: 	3
#					I'm not sure:	4
data.loc[ data.Distance.isnull(), 'Distance'] = 'Less than 5 miles'
data['Distance'] = data['Distance'].map( {'Less than 5 miles':0, '5 - 10 miles ':1, '10 - 20 miles ':2, 'More than 20 miles':3, 'I\'m not sure':4}).astype(int)


# convert return to 1/0
data.loc[ data.Return.isnull(), 'Return' ] = '0'


# convert refer
data.loc[ data.Refer.isnull(), 'Refer' ] = '0'

# calculate the gender ratio of the return customer
count_Male = 0
count_Return = 0
count_Total = data['Id'].size
data_Gender = data['Gender'].values
data_Return = data['Return'].values
for i in range(0, data['Id'].size):
  if( data_Return[i] == 1):
    count_Male += data_Gender[i]
    count_Return += 1

print 'count_Total = ', count_Total	
print 'count_Return = ', count_Return
print 'return percentage', count_Return/(count_Total * 1.0)
print 'Male percentage from return group ', count_Male/(count_Return*1.0)
print 'Female percentage from return group ', 1 - count_Male/(count_Return*1.0)

count_Male_Non = 0
for i in range(0, data['Id'].size):
  if( data_Return[i] == 0):
    count_Male_Non += data_Gender[i]
count_Return_Non = count_Total - count_Return
print 'Male percentage from non-return group ', count_Male_Non/(count_Return_Non*1.0)
print 'Female percentage from non-return group', 1 - count_Male_Non/(count_Return_Non*1.0)


# calculate the feedback of custormer service from the return customer
count_Male = 0
count_Return = 0
count_Total = data['Id'].size
data_Gender = data['Gender'].values
data_Return = data['Return'].values
for i in range(0, data['Id'].size):
  if( data_Return[i] == 1):
    count_Male += data_Gender[i]
    count_Return += 1

print 'count_Total = ', count_Total	
print 'count_Return = ', count_Return
print 'return percentage', count_Return/(count_Total * 1.0)
print 'Male percentage from return group ', count_Male/(count_Return*1.0)
print 'Female percentage from return group ', 1 - count_Male/(count_Return*1.0)


# calculate the age population
count_20 = 0
count_30 = 0
count_45 = 0
count_60 = 0
count_70 = 0
data_Age = data['Age'].values
for i in range(0, data['Id'].size):
  if( data_Age[i] == 20):
    count_20 += 1
  elif( data_Age[i] == 30):
    count_30 += 1
  elif( data_Age[i] == 45):
    count_45 += 1
  elif( data_Age[i] == 60):
    count_60 += 1
  else:
    count_70 += 1
	
print 'Age 18 to 25 is ', count_20
print 'Age 26 to 34 is ', count_30
print 'Age 35 to 45 is ', count_45
print 'Age 50 to 64 is ', count_60
print 'Age is 65 and over is ', count_70


# calculate non-return customer distribution
return_20 = 0
return_30 = 0
return_45 = 0
return_60 = 0
return_70 = 0
data_Age = data['Age'].values
for i in range(0, data['Id'].size):
  if( data_Age[i] == 20):
    return_20 += 1*data_Return[i]
  elif( data_Age[i] == 30):
    return_30 += 1*data_Return[i]
  elif( data_Age[i] == 45):
    return_45 += 1
#    return_45 += 1*data_Return[i]
  elif( data_Age[i] == 60):
    return_60 += 1*data_Return[i]
  else:
    return_70 += 1*data_Return[i]
	
print 'non return from age 18 to 25 is ', count_20 - return_20
print 'non return from age 26 to 34 is ', count_30 - return_30
print 'non return from age 35 to 45 is ', count_45 - return_45
print 'non return from age 50 to 64 is ', count_60 - return_60
print 'non return from age is 65 and over is ', count_70 - return_70