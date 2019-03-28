import sys
import re
from apyori import apriori
import time

start_time = time.time()

#Importing dataset
file = open('C:/Users/Mohammad Khorasani/Desktop/MCSDS/CS 498 CCA/Project/dataset_1.txt','r')
data = file.readlines()
#data = data[0:1000]

#Parsing and delimiting dataset
for i in range(0,len(data)):
    data[i] = data[i].replace('\n','')
    
for i in range(0,len(data)):
    data[i] = re.split(';', data[i])

#Executing association mining using the apriori toolkit
min_support = 0.005
association_results = apriori(data, min_support = 0.005)
results = list(association_results)

#Creating a list of lists of the support, itemsets
final_results = [[0 for x in range(2)] for y in range(len(results))]

for i in range(0,len(results)):
    final_results[i][0] = int((results[i][1])*len(data))
    final_results[i][1] = ', '.join(list(results[i][0]))

#Sorting list of lists in descending order
final_results.sort(reverse = True)

#Saving association mining results to text file
with open('C:/Users/Mohammad Khorasani/Desktop/MCSDS/CS 498 CCA/Project/results_min_support_%s.txt' % (min_support), 'w') as f:
    for item in final_results:
        f.write("%s\n" % item)

end_time =  time.time()
execution_time = (end_time - start_time)
print(execution_time)
