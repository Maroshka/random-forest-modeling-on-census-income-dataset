import pandas as pd 
import numpy as np 
import statsmodels.discrete.discrete_model as st 
from patsy import *
import pylab as plt 
import statsmodels.api as st
from sklearn.metrics import classification_report
from clean import prep
from sklearn import tree
from math import *
import sklearn.ensemble as sk

y_train, x_train, y_test, x_test = prep('newCensus.csv', 0.7)
""" Decision Tree Model"""
model = DecisionTreeClassifier()
res = model.fit(x_train, y_train)
y_pred = res.predict(x_test)
print pd.crosstab(y_test.GT50k, y_pred, colnames=['Predicted'], rownames=['Actual'])
print '\n \n'
print classification_report(y_test.GT50k,y_pred)

#decision tree models don't hold up well when there are many variables and a large dataset. This is
#where ensemble models, such as random forest, come to rescue.

"""Random Forest """
#A random forest basically creates many decision trees on the dataset and then
#averages out the results.
clf = sk.RandomForestClassifier(n_estimators = 100, oob_score = True, min_samples_leaf = 2,min_samples_split = 5)
res = clf.fit(x_train, y_train.GT50k)
rank = pd.Series(res.feature_importances_,index=x_train.columns, ).sort(ascending=False, inplace=False)
y_pred = res.predict(x_test)
print pd.crosstab(y_test.GT50k, y_pred, colnames=['Predicted'], rownames=['Actual'])
print '\n \n'
print classification_report(y_test.GT50k,y_pred)

rank.index.name = 'Features'
top_features = rank.iloc[:].sort(ascending=True,inplace=False)
plt.figure(figsize=(20,12))
ax = top_features.plot(kind='barh')
a = ax.set_title("Features")
a = ax.set_xlabel('Importance')
a = ax.set_yticklabels(top_features.index, fontsize=8)



