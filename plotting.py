import csv

import numpy as np
import matplotlib.pyplot as plt

csvFile = open("final_data_edtech.csv", 'r')
csvreader = csv.reader(csvFile)

Numbers = []
Titles = []
for i in csvreader:
    Numbers.append(int(i[1]))
    Titles.append(i[0])



xs = [1,2,3,4,5,6,7,8,9,10]

plt.barh(xs,Numbers)

# tell pyplot which labels correspond to which x values
plt.yticks(xs,Titles)

plt.show()
