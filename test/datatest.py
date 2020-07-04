import csv

with open('C:/Application&Data.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    results = []
    for data in spamreader:
        results.append(data)    

print(results)
        #print(', '.join(row))