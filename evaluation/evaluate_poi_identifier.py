#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
import numpy as np
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit
from sklearn.metrics import accuracy_score,precision_score,recall_score
from sklearn.cross_validation import train_test_split
data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)

from sklearn.tree import DecisionTreeClassifier
features_train,features_test,labels_train,labels_test=train_test_split(features, labels, random_state=42, test_size=0.3)
clf=DecisionTreeClassifier()
clf.fit(features_train,labels_train)
pred=clf.predict(features_test)
print clf.score(features_test,labels_test)

values,counts=np.unique(pred,return_counts=True)
test_size=len(features_test)
print "predicted of POIDS",zip(values,counts)
### your code goes here 


