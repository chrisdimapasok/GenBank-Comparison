#!/usr/local/bin/python3

import cgi
import jinja2
import re

#Template Loader
templateLoader=jinja2.FileSystemLoader(searchpath="./templates")
env= jinja2.Environment(loader=templateLoader)

#Create environment and load template
template=env.get_template('Comparison_Template.html')


#Parse Genbank File

num= 0
entries= list()
entry= dict()

for line in open("sequence.gb"):
    if "CDS " in line:
        entry= dict()
        num += 1

        if num == 1:
            s= line.split(",")
            s_split= s[1].split("..")
            entry["Ref_5"] = s_split[0]
            entry["Ref_3"]= s_split[1].replace(")", "").strip() #Remove quotes and add new line

        #Else statement for another condition

        else:
            if "complement" in line: #Handle exception where there is compliment on CDS line
                s= line.split("(")
                s_split= s[1].split("..")
                entry["Ref_5"] = s_split[0]
                entry["Ref_3"]= s_split[1].replace(")","").strip()

            #If no compliment just get coordinates normally
            else:
                s= line.split("..")
                entry["Ref_5"] = s[0].replace(" ","").replace("CDS","").strip().replace("<","") #Remove all spaces and CDS
                entry["Ref_3"]= s[1].strip().replace("<","")


        if "/protein_id" in line:
            s= line.split("=")
            entry["REF_ID"]= s[1].strip()
            entries.append(entry)


#Parsing prediction file

for line in open("run1.predict"):
    if "orf" in line:
        pred_5= (line.split()[1])
        pred_3= (line.split()[2])

        #Write to Dictionary and List and input into html

        if count < len(entries):
            entries[count]["Pred_5"] = pred_5
            entries[count]["Pred_3"]= pred_3

        #Set Counter Variable
        count+=1

#Variable for lengths of each ref and pred

len_ref= len(entries)
len_pred= count
data=dict()
data["Count_Of_Ref"]= len_ref
data["Count_Of_Pred"]= len_pred
data["entries"]= entries

#Output into template
print("Content_Type: text/html\n\n")
print(template.render(data=data))
    
