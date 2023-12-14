#! /usr/bin/env python3
import csv
import json

# How many NEOs are in the neos.csv data set?
neos = []
with open('data/neos.csv') as fin: 
    reader = csv.DictReader(fin)
    for elem in reader:
        neos.append(elem)
print('NEOs count:',len(neos))


# What is the primary designation of the first Near Earth Object in the
# neos.csv data set?
print('Primary destination of first element:',neos[0]['pdes'])


# What is the diameter (in kilometers) of the NEO whose name is "Apollo"?
print('Diameter of Apollo:',*[row['diameter'] for row in neos \
                              if row['name'] == 'Apollo'])


# How many NEOs have IAU names in the data set?
named_neos = [row for row in neos if row['name']!='']
print('Named NEOs count:',len(named_neos))


# How many NEOs have diameters in the data set?
measured_neos = [row for row in neos if row['diameter']!='']
print('Measured NEOs count:',len(measured_neos))


# How many close approaches are in the cad.json data set?
with open('data/cad.json','r') as fin:
    cad = json.load(fin) #signature,count,fields,data
print('Close approach count:',cad['count'])


# On January 1st, 2000, how close did the NEO whose primary designation is
# "2015 CL" pass by Earth?
pos = cad['fields'].index('dist')
print('Distance:',*[row[pos] for row in cad['data'] \
                    if row[0]=='2015 CL' and row[3][:11]=='2000-Jan-01'])
