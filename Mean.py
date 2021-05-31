import csv

with open('SOCR-HeightWeight.csv', newline='') as f:
   reader = csv.reader(f)
   df = list(reader)

df.pop(0)
Data=[]

for i in range(len(df)):
   n_num = df[i][1]
   Data.append(float(n_num))

n = len(Data)
total =0

for x in Data:
   total += x
 
mean = total / n

print("Mean of the data is: " + str(mean))
