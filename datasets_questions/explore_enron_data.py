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
pprint.pprint(enron_data)
pprint.pprint(len(enron_data))
pprint.pprint(len(enron_data["SKILLING JEFFREY K"]))
num0=1
salary_num=0
email_num=0
for key,value in enron_data.items():
    if enron_data[key]['poi']==True:
        num0+=1
        print key
    if enron_data[key]['salary']!='NaN':
        salary_num+=1
    if enron_data[key]['email_address']!='NaN':
        email_num+=1

print 'salary_num is ',salary_num,'email_num is',email_num
print enron_data['PRENTICE JAMES']['total_stock_value']
print 'jeff skiling stock',enron_data['SKILLING JEFFREY K']['exercised_stock_options']
print 'Wesley Colwell',enron_data['COLWELL WESLEY']['from_this_person_to_poi']


print 'lay',enron_data['LAY KENNETH L']['total_payments']
print 'skilling',enron_data['SKILLING JEFFREY K']['total_payments']
print 'Fastow',enron_data['FASTOW ANDREW S']['total_payments']
