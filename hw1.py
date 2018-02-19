import csv
from math import pi, exp, pow, log, sqrt
from statistics import mean, stdev
import sys

#Naive Bayes classifier. We expect input in the form of a csv file formatted as so:
#example_id, feature0, feature1, ..., featuren, class_label
#where features are numeric.

if len(sys.argv) < 2:
    exit("Usage: python hw1.py data_file.csv folds")

def get_stats(data):
    features = {}
    class_priors = {}
    
    for example in data:
        counter = 0
        label = int(example[-1])
        if label in class_priors:
            class_priors[label] = class_priors[label] + 1
        else:
            class_priors[label] = 1
            
        for item in example[:-1]:
            if counter in features:
                if label in features[counter]:
                    features[counter][label].append(float(item))
                else:
                    features[counter][label] = [float(item)]
            else:
                features[counter] = {label:[float(item)]}
            counter = counter + 1
            
    means = {}
    stddevs = {}
    for feature, class_dict in features.items():
        means[feature] = {n: mean(class_dict[n]) for n in class_dict.keys()}
        stddevs[feature] = {n: stdev(class_dict[n]) for n in class_dict.keys()}

    size = sum(class_priors.values())
    class_priors = {n: float(class_priors[n])/float(size) for n in class_priors.keys()}
    return(means, stddevs, class_priors)


def pdf(x, mean, stddev):
    first = 1 / (sqrt(2 * pi) * stddev)
    second =  exp(-(pow(x - mean,2)/(2*pow(stddev,2))))
    return first * second


training_data = []
with open(sys.argv[1]) as datafile:
    datareader = csv.reader(datafile, delimiter = ',', quotechar = '"')
    for row in datareader:
        training_data.append(row[1:])


folds = int(sys.argv[2])
size = len(training_data)
fold_size = size/folds
last_fold_size = (size % folds) + fold_size
wrong_count = 0
total_count = 0
for i in range(folds):
    val_set_start =int( fold_size * (i)) 
    val_set_end = int(val_set_start + fold_size) - 1
    if i == (folds - 1):
        val_set_end = int(val_set_start + last_fold_size)

    print("for fold " + str(i))
    print(val_set_start)
    print(val_set_end)
    #construct training & validation set
    training_set = []
    validation_set = training_data[val_set_start:val_set_end]
    if i == 0:
        #special case
        if folds == 1:
            training_set = training_data
        else:
            training_set = training_data[val_set_end + 1:] #is this right?
    else:
        training_set = training_data[:val_set_start -1] + training_data[val_set_end + 1:]

    (training_means, training_stddevs, training_class_priors) = get_stats(training_data)
    
    print(training_class_priors)
    print(training_means)
    print(training_stddevs)
    print(" ")

    for example in validation_set:
        probs = {}
        pred = (0,0.0) #label, probability
        for label, prior in training_class_priors.items():
            prob = log(prior)
            counter = 0
            for feature in example[:-1]:
                prob = prob + log(pdf(float(feature), training_means[counter][label], training_stddevs[counter][label]))
                counter = counter + 1

            probs[label] = prob
            if prob >= pred[1]:
                if prob > pred[1] or label > pred[0]:
                    pred = (label, prob)

     #   print(pred)
     #   print(example[-1])
        total_count = total_count + 1
        if int(pred[0]) != example[-1]:
            wrong_count = wrong_count + 1

print("training error: " + str(float(wrong_count)/float(total_count)))
        
