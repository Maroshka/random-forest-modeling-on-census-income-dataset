import pandas as pd 
import numpy as np 
from math import *
from patsy import *

def prep(filename,ratio):

	df = pd.read_csv(filename)
	#removing missing values
	del df['education_num']
	del df['fnlwgt']
	del df['Capital_gain']
	del df['Capital_loss']
	df['GT50k'] = df['GT50k'] == '>50K'
	df['GT50k'] = df.GT50k.astype(int)
	# del df['Relationship']
	df = df.dropna(how='any')
	#deviding the dataset into training and testing datasets
	n = int(floor(len(df)*ratio))
	dftrain = df[:n]
	dftest = df[n:]
	# formula = "GT50k ~ Sex + Age + Native_country + education + Race + Marital_status + WorkClass + hpw + Occupation"
	formula = 'GT50k ~ Age + WorkClass + education + Marital_status + Occupation + Sex + hpw'
	y_train,x_train = dmatrices(formula, data=dftrain,return_type='dataframe')
	y_test, x_test = dmatrices(formula, data=dftest,return_type='dataframe')
	l = [x_train.columns[i] for i in range(0, len(x_train.columns)) if x_train.columns[i] not in x_test.columns]
	if len(l)==0:
	    pass
	else:
	    for i in l:
	        x_test[i] = [0]*len(x_test)
	
	return y_train, x_train, y_test, x_test