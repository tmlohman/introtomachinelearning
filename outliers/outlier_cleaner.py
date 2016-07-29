#!/usr/bin/python

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

