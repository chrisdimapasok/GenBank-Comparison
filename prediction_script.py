#!/usr/local/bin/python3

import jinja2
import re

#This line tells the template loader where to search for template files
templateLoader= jinja2.FileSystemLoader( searchpath= "./templates")
env= jinja2.Environment(loader=templateLoader)

#Create your environment and loads a specific template
template=env.get_template('prediction.html')


prediction= list()
pred=dict()

count=0  	#define variable count to count number of predictions
for line in open("run1.predict"):
    if "orf" in line:
    pred=dict()
    pred_5= (line.split()[1])
    pred_3= (line.split()[2])

    #Write to dictionary and make this list to input into html
    pred["Pred_5"] = pred_5
    pred["Pred_3"] = pred_3
    prediction.append(pred)

#Output into template
print("Content_Type: text/html\n\n")
print(template.render(prediction=prediction))












