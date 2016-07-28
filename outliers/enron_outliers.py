#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit
import numpy as np


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
features = ["salary", "bonus"]
data_dict.pop('TOTAL', 0)
data = featureFormat(data_dict, features)



### your code below
# identifying outliers - total
#max_salary = np.amax(data, 0)[0]
#print [k for k, v in data_dict.iteritems() if v['salary'] == max_salary]

# identifying outliers - people who made a lot more
out_salary = 1000000
out_bonus = 5000000
print [k for k, v in data_dict.iteritems() 
	if v['salary'] > out_salary and
	v['bonus'] >= out_bonus and
	v['salary'] != 'NaN']



for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()


