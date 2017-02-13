#!/usr/bin/python

from pprint import pprint
def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []

    ### your code goes here
    for i in range(len(predictions)):
        error=(predictions[i]-net_worths[i])*(predictions[i]-net_worths[i])
        data=(ages[i],net_worths[i],error)
        cleaned_data.append(data)
    cleaned_data=sorted(cleaned_data,key=lambda x:x[2])
    num=int(len(predictions)*0.9)
    cleaned_data=cleaned_data[0:num]
    print(cleaned_data),len(cleaned_data)
    return cleaned_data

