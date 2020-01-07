import csv
import math

path=r'C:\Users\Salmaaaan\Desktop\AI PROJECT\Book1.csv'
list = []
input = ["avengers", 5,6]
count = 0
with open(path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        count=count+1
        if(count>1):
            sum = pow((int(row[1])-int(input[1])),2) + pow((int(row[2])-int(input[2])),2)
            distance = math.sqrt(sum)
            list.append((distance,row[0]))
list.sort()
print(list)

        




