import csv

with open('SOCR-HeightWeight.csv', newline='') as f:
   reader = csv.reader(f)
   file = list(reader)

file.pop(0)

data=[]

for i in range(len(file)):
   n_num = file[i][1]
   data.append(n_num)

n = len(data)
data.sort()

if (n % 2 == 0):
   median1 = float(data[n//2])
   median2 = float(data[n//2 - 1])
   median = (median1 + median2)/2
else:
   median = data[n//2]

print("Median of the data is: " + str(median))
