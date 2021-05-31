#Importing.

import csv
from collections import Counter

#Opening and Reading the file

with open('SOCR-HeightWeight.csv', newline='') as f:
   reader = csv.reader(f)
   df = list(reader)

df.pop(0)
data=[]

for i in range(len(df)):
   n_num = df[i][1]
   data.append(float(n_num))

n = len(data)
total =0

#Finding Mean.

for x in data:
   total += x
 
mean = total / n

# Meadian of the data.

data.sort()

if (n % 2 == 0):
   median1 = float(data[n//2])
   median2 = float(data[n//2 - 1])
   median = (median1 + median2)/2
else:
   median = data[n//2]

#Mode of the data.

data = Counter(data)

mode_data_for_range = {
    "50-60": 0,
    "60-70": 0,
    "70-80": 0
}
for height, occurence in data.items():
    if 50 < float(height) < 60:
        mode_data_for_range["50-60"] += occurence
    elif 60 < float(height) < 70:
        mode_data_for_range["60-70"] += occurence
    elif 70 < float(height) < 80:
        mode_data_for_range["70-80"] += occurence

mode_range, mode_occurence = 0, 0
for range, occurence in mode_data_for_range.items():
    if occurence > mode_occurence:
        mode_range, mode_occurence = [
            int(range.split("-")[0]), int(range.split("-")[1])], occurence
mode = float((mode_range[0] + mode_range[1]) / 2)

#Printing.

print("Mean of the data is: " + str(mean))
print("Median of the data is: " + str(median))
print(f"Mode is -> {mode:2f}")