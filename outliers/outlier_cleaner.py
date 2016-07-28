#!/usr/bin/python

p = [0, 2,4,6,8,10, 12,14,16,18]
a = [0,1,2,3,4,5,6,7,8,9]
nw = [0.1, 2, 4, 6, 7.5, 10.1, 12, 14, 16.3, 18]
def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    import numpy as np
    cleaned_data = []

    ### your code goes here
    errors = []
    for n in range(0, 89):
		d = abs(net_worths[n] - predictions[n])
		errors.append(d)
		
    cut = np.percentile(errors, 90)
    for n in range(0, 89):
		if errors[n] <= cut:
			cleaned_data.append((ages[n], net_worths[n], errors[n]))
		
    return cleaned_data

#print len(outlierCleaner(p, a, nw))
#print len(p)
