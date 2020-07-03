import csv
with open('C:/semi/Application&Data.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    results = []
    for data in spamreader:
        results.append(data)    
print(results)
        #print(', '.join(row))

# import csv

# with open('C:/semi/Application&Data.csv', newline='') as csvfile:
#     spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
#     for row in spamreader:
#         print(', '.join(row))



