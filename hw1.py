import csv
import sys

#Naive Bayes classifier. We expect input in the form of a csv file formatted as so:
#example_id, feature0, feature1, ..., featuren, class_label
#where features are numeric.

if len(sys.argv) < 2:
    exit("Usage: python hw1.py data_file.csv")

#rows are features, columns are examples
data = {}
with open(sys.argv1) as datafile:
    datareader = csv.reader(datafile, delimiter = ',', quotechar = '"')
    for row in survey_reader:
        counter = 0
        for item in row[1:]:
            label = item[-1]
            if counter in data:
                if label in data[counter]:
                    data[counter].append(item)
                else:
                    data[counter][label] = [item]
            else:
                data[counter] = {class:[item]}
            counter = counter + 1

stats = {}
#I'm pretty sure I can and should do this with a lambda instead
for feature, class_dict in data:
    means.append(mean(feature))
    stddevs.append(stdev(feature))


