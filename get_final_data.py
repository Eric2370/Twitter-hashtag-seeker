import csv

ascii_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

dictionary = {}
csvFile = open("result.csv", 'r')
csvreader = csv.reader(csvFile)
count = 0
boolean = False
for row in csvreader:
    count += 1
    word = ''
    for item in row[1]:
        if item not in ascii_letters and boolean == True:
            if word.lower() in dictionary:
                dictionary[word.lower()] += 1
            else:
                dictionary[word.lower()] = 1
            boolean = False
            word = ''
        if item == '#':
            boolean = True
        if boolean == True:
            word += item




dictionary['#education'] = count

#del dictionary['#']
#del dictionary['b']

sorted_x = sorted(dictionary.items(), key=lambda kv: kv[1])

with open('final_data.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(sorted_x[-10:])
csvFile.close()




