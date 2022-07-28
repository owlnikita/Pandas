import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('StudentsPerformance.csv')
df1 = pd.read_csv('countries of the world.csv')




with_edc = len(df[df['parental level of education']!='some college'])

print('Кол-во абитурентов с высшим образованием:',with_edc)

female = len(df[df['gender']=='female'])
print('Кол-во девочек:',female)
male = len(df[df['gender']=='male'])
print('Кол-во мальчиков:',male)

print('Кол-во учеников относящихся к группе A:',len(df[df['race/ethnicity']=='group A']))
print('Кол-во учеников относящихся к группе B:',len(df[df['race/ethnicity']=='group B']))
print('Кол-во учеников относящихся к группе C:',len(df[df['race/ethnicity']=='group C']))
print('Кол-во учеников относящихся к группе D:',len(df[df['race/ethnicity']=='group D']))
print('Кол-во учеников относящихся к группе E:',len(df[df['race/ethnicity']=='group E']))

#--------------------------------------------------------------------------------------




print('\n \nОбщее кол-во стран:',len(df1['Country']))
print('Средний уровень ВВП всех стран:', int(df1['GDP ($ per capita)'].mean()) )

