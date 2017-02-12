#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""
import pprint
import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

pprint.pprint(len(enron_data))
pprint.pprint(len(enron_data["SKILLING JEFFREY K"]))
num0=1
for key,value in enron_data.items():
    if enron_data[key]['poi']==True:
        num0+=1
        print key
print num0

print enron_data['JAMES PRENTICE']['bonus']
