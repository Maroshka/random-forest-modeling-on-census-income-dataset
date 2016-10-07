import pandas as pd 
import pylab as plt

data = pd.read_csv('newCensus.csv')
"""preparing the data """
del data['education_num']
del data['fnlwgt']
del data['Capital_gain']
del data['Capital_loss']
df = data.dropna(how='any')
df['GT50k'] = df['GT50k'] == '>50K'

"""Hypothesis 1: People who are older earn more"""
hist = plt.hist(df[df['GT50k'].values == True].Age.values,10, color='green',alpha=0.8 )
plt.title('Age distribution of above 50k earners')
plt.xlabel("Age")
plt.ylabel("Frequency")

hist2 = plt.hist(df[df['GT50k'] == False].Age.values, 10, color='green', alpha=0.8)
plt.title('Age ditribution of below 50k earners')
plt.xlabel('Age')
plt.ylabel('Frequency')

conclusion = "We can see that people who earn above $50K are mostly aged between theirlate 30s and mid 50s,\n whereas people who earn less than $50K are primarily aged between 20 and 30."
print conclusion

"""Hypothesis 2: Income bias based on working class"""
stuff = pd.concat([df[df['GT50k'] == True].groupby('WorkClass').WorkClass.count(),df[df['GT50k'] == False].groupby('WorkClass').WorkClass.count()],axis=1)
stuff.columns = ['WkClassGT50k', 'WkClassLT50k']
final = stuff.WkClassGT50k / (stuff.WkClassGT50k + stuff.WkClassLT50k)
final.sort(ascending=False)
ax = final.plot(kind = 'bar', color = 'r', y='Percentage')
ax.set_xticklabels(final.index, rotation=30,fontsize=8, ha='right')
ax.set_xlabel('Working Class')
ax.set_ylabel('Percentage of People')

conclusion2 = "We see that people who are self-employed and have a company have got the maximum share of people who earn more than $50K. The second most well-offgroup in terms of earning are federal government employees."
print conclusion

"""Hypothesis 3: People with more education earn more"""
edu = pd.concat([df[df.GT50k == True].groupby('education').education.count(), df[df.GT50k == False].groupby('education').education.count()], axis=1)
edu.columns = ['EduGT50k', 'EduLT50k']
final = edu.EduGT50k / (edu.EduGT50k + edu.EduLT50k)
final.sort(ascending=False)
ax = final.plot(kind='bar', color='blue', y='Percentage')
ax.set_xticklabels(final.index, rotation=30,fontsize=8, ha='right')
ax.set_xlabel('Education')
ax.set_ylabel('Percentage of People')

conclusion3 = "We can see that the more the person is educated, the greater the number of people in their group who earn more than $50K.
print conclusion

"""Hypothesis 4: Married People tend to earn more"""
mar = pd.concat([df[df.GT50k == True].groupby('Marital_status').Marital_status.count(), df[df.GT50k == False].groupby('Marital_status').Marital_status.count()], axis=1)
mar.columns = ['MarGT50k', 'MarLT50k']
final = mar.MarGT50k / (mar.MarGT50k + mar.MarLT50k)
final.sort(ascending=False)
ax = final.plot(kind='bar', color='green', y='Percentage')
ax.set_xticklabels(final.index, rotation=30,fontsize=8, ha='right')
ax.set_xlabel('Education')
ax.set_ylabel('Percentage of People')

conclusion4 = "We can see that people who are married earn better as compared to people who are single."
print conclusion4

"""Hypothesis 5: There's a bias income based on race"""
rac = pd.concat([df[df.GT50k == True].groupby('Race').Race.count(), df[df.GT50k == False].groupby('Race').Race.count()], axis=1)
rac.columns = ['RacGT50k', 'RacLT50k']
final = rac.RacGT50k / (rac.RacGT50k + rac.RacLT50k)
final.sort(ascending=False)
ax = final.plot(kind='bar', color='y', y='Percentage')
ax.set_xticklabels(final.index, rotation=30,fontsize=8, ha='right')
ax.set_xlabel('Education')
ax.set_ylabel('Percentage of People')

conclusion5 = "Asian Pacific people and Whites have the highest earning power."
print conclusion5

"""Hypothesis 6: Men earn more"""
sex = pd.concat([df[df.GT50k == True].groupby('Sex').Sex.count(), df[df.GT50k == False].groupby('Sex').Sex.count()], axis=1)
sex.columns = ['SexGT50k', 'SexLT50k']
final = sex.SexGT50k / (sex.SexGT50k + sex.SexLT50k)
final.sort(ascending=False)
ax = final.plot(kind='bar', color='r', y='Percentage')
ax.set_xticklabels(final.index, rotation=30,fontsize=8, ha='right')
ax.set_xlabel('Education')
ax.set_ylabel('Percentage of People')

conclusion6 = "Men earn more."
print conclusion6

"""Hypothesis 7: People who clock in more hours earn more"""
hist = plt.hist(df[df['GT50k'].values == True].hpw.values,10, color='r',alpha=0.8 )
plt.title('Hpw distribution of above 50k earners')
plt.xlabel("HPW")
plt.ylabel("Frequency")

hist2 = plt.hist(df[df['GT50k'] == False].hpw.values, 10, color='green', alpha=0.8)
plt.title('HPW ditribution of below 50k earners')
plt.xlabel('HPW')
plt.ylabel('Frequency')

