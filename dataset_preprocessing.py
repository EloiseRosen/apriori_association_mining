import sys
import re
import csv

file = open('C:/Users/Mohammad Khorasani/Desktop/MCSDS/CS 498 CCA/Project/Dataset/Online Retail.csv')
data = file.readlines()

#Parsing each tuple and delimiting
for i in range(0,len(data)):
    data[i] = data[i].replace('\n','')
    data[i] = data[i].replace('"','')
    data[i] = data[i].replace("'",'')
    data[i] = data[i].replace('.','')
    data[i] = data[i].replace('-','')
    data[i] = re.split(',', data[i])


#Creating trasnactions dataset by appending unique invoices together
td = []
temp = data[0][1]

for i in range(0,len(data)-1):
    
    if data[i][0] == data[i+1][0]:
        length = len(data[i+1])
        for j in range(1, length):
            temp += ';'
            temp += data[i+1][j]
        
    if data[i][0] != data[i+1][0]:
        td.append(temp)
        length = len(data[i+1])
        for k in range(1, length):
            temp = data[i+1][k]

#Removing certain characters from transaction dataset
for i in range(0,len(td)):
    td[i] = td[i].replace('"','')
    td[i] = re.split(';', td[i])

#Removing whitespaces from transaction dataset
for i in range(0,len(td)):
    if ' ' in td[i]:
        td[i].remove(' ')

#Converting transactions dataset into a list of lists
tdf = []

for i in range(0,len(td)):
    temp = ''
    for j in range(0,len(td[i])):
        temp += ';'
        temp += td[i][j]
        temp = temp.lower()
    tdf.append(temp[1:])

for i in range(0,len(tdf)):
    if tdf[i] == ';':
        tdf[i] = ''

#Removing null entries from transactions dataset
tdf = filter(None, tdf)

#Creating text file of transactions dataset      
with open('C:/Users/Mohammad Khorasani/Desktop/MCSDS/CS 498 CCA/Project/dataset.txt', 'w') as f:
    for item in tdf:
        f.write("%s\n" % item)
        

    

        
    
