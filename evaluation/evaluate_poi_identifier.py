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
print "test_size",test_size
### your code goes here 
true_positives=0

for actual,predict in zip(labels_test,pred):
    if actual==1 and predict==1:
        true_positives+=1

print "true_positives",true_positives
print "precision score",precision_score(pred,labels_test)
print "recall score",recall_score(pred,labels_test)

predicted=[0,1,1,0,0,0,1,0,1,0,0,1,0,0,1,1,0,1,0,1]
actual   =[0,0,0,0,0,0,1,0,1,1,0,1,0,1,1,1,0,1,0,0]

def cal_precision_recall(actual=[],predicted=[]):
    
    true_positive=0
    false_positive=0
    false_negative=0
    true_negatives=0
    for a,p in zip(actual,predicted):
        if a==1 and p==1:
            true_positive+=1
        elif a==0 and p==1:
            false_positive+=1
        elif a==1 and p==0:
            false_negative+=1
        else:
            true_negatives+=1
    print 'true_positive',true_positive,'true_negative',true_negatives,'false positives',false_positive,'false_negatives',false_negative
    print 'precision score',true_positive*1.0/(true_positive+false_positive)
    print 'recall score',true_positive*1.0/(true_positive+false_negative)
    
cal_precision_recall(actual,predicted)
