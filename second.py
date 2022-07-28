import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('StudentsPerformance.csv')

with_edc = len(df[df['parental level of education']!='some college'])

print('Кол-во абитурентов с высшим образованием:',with_edc)



female = len(df[(df['gender']=='female')& (df['math score']>=60)])
male = len(df[(df['gender']=='male')& (df['math score']>=60)])
data = [female,male]
data_info = [f'Males {round(male*100/(male+female))}%', f'Females {round(female*100/(male+female))}%']


female1 = len(df[(df['gender']=='female')& (df['reading score']>=60)])
male1 = len(df[(df['gender']=='male')& (df['reading score']>=60)])
data1 = [female1,male1]
data_info1 = [f'Males {round(male*100/(male1+female1))}%', f'Females {round(female1*100/(male1+female1))}%']


fix, (ax1, ax2) = plt.subplots(1,2)
ax1.pie(data)
ax2.pie(data1)

ax1.legend(data_info)
ax2.legend(data_info1)

plt.show()