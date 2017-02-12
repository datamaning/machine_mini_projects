#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###

#features_train=features_train[0:len(features_train)/100]
#labels_train=labels_train[0:len(labels_train)/100]
print len(features_train),len(labels_train)

from sklearn import svm
clf=svm.SVC(kernel='rbf',C=10000.0)

t1=time()
clf.fit(features_train,labels_train)
print 'train time consuming',round(time()-t1,3),'s'

t0=time()
pred=clf.predict(features_test)
num0=0
num1=0
for i in range(len(pred)):
    if pred[i]==0:
        num0+=1
    elif pred[i]==1:
        num1+=1
print num0,num1
print "time consuming",round(time()-t0,3),'s'


from sklearn.metrics import accuracy_score
score=accuracy_score(pred,labels_test)
score=clf.score(features_test,labels_test)

print "Answer is ",score
#########################################################


