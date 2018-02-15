import csv
import sys

#Naive Bayes classifier. We expect input in the form of a csv file formatted as so:
#example_id, feature0, feature1, ..., featuren, class_label
#where features are numeric.

if len(sys.argv) < 2:
    exit("Usage: python hw1.py data_file.csv")

#rows are features, columns are examples
data = [[]]

with open(sys.argv1) as datafile:
    datareader = csv.reader(datafile, delimiter = ',', quotechar = '"')
    for row in survey_reader:
        counter = 0
        for item in row[1:]:
            data[counter].append(item)
            counter = counter + 1


classes = set(data[-1])

#actually, I have to do this by class anyway
means = []
stddevs = []
#I'm pretty sure I can and should do this with a lambda instead
for feature in data:
    means.append(mean(feature))
    stddevs.append(stdev(feature))


