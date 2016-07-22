#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 3 (decision tree) mini-project.

    Use a Decision Tree to identify emails from the Enron corpus by author:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
from sklearn.metrics import accuracy_score


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
def classify(features_train, labels_train):   
    from sklearn import tree
    clf = tree.DecisionTreeClassifier(min_samples_split = 40)
    #features_train = features_train[:len(features_train)/100] 
    #labels_train = labels_train[:len(labels_train)/100] 
    return clf.fit(features_train, labels_train)

#train classifier
t0 = time()
clf = classify(features_train, labels_train)
print "training time:", round(time()-t0, 3), "s"

#predict outcome
t0 = time()
pred = clf.predict(features_test)
print "prediction time:", round(time()-t0, 3), "s"

#check accuracy
accuracy = accuracy_score(labels_test, pred)
print accuracy
print len(features_train[0])


#########################################################


