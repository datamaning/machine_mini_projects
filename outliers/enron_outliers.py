#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
features = ["salary", "bonus"]
data = featureFormat(data_dict, features)


### your code below

from sklearn import linear_model

clf=linear_model.LinearRegression()
print data
print data[:,0]
print len(data[:,0]),len(data[:,1])
clf.fit(data,[0])
print clf.coef_

