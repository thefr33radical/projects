import csv
with open('feature.csv', 'rb') as f:
    reader = csv.reader(f)
    your_list = list(reader)

feature = []
label = []
for data in your_list:
	feature.append(data[0:12])
	label.append(data[12])

print feature
print label
	
