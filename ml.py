import os
import numpy as pn
from collections import Counter
from sklearn.naive_bayes import MultinomialNB, GaussianNB, BernoulliNB
from sklearn.svm import SVC, NuSVC, LinearSVC
import csv
import pandas
import sys



from sklearn.tree import *
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import HashingVectorizer

from sklearn.calibration import *
from sklearn.linear_model import *
from sklearn.multiclass import *
from sklearn.svm import *

from util import ValidateVIN

def export_vin(filePath):

    data = csv.reader(open(filePath), delimiter='\t')

    #file_out = open("training/output.dat", "w")

    i = 0
    
    # vins = [r[0].upper() for r in data]
    #results = ValidateVIN(vins, many=True)
    # invalidVins = [r for r in ValidateVIN(vins, many=True) if not r[0]]

    # for v in invalidVins:
    #     print "%s\t%s\t%s" % v

    validFile = open("validVins.txt", "w")
    invalidFile = open("invalidVins.txt", "w")

    for row in data:
        # all records
        # recordData = "{0}\t{1}\t{2}\t{3}\t{4}\t{5}".format(row[0], row[1], row[2], row[3], row[4], row[5])
        # vin make
        recordData = "{0}\t{1}".format(row[0], row[4])
        vinResult = ValidateVIN(row[0].upper())
        if vinResult[0]:
            validFile.write(recordData + "\n")
        else:
            invalidFile.write(recordData + "\t" + vinResult[2] + "\n")

        # print "%s\t%s\t%s" % vinResult

        # print "%s\t%s\n" % (row[0], valid[1])

    validFile.flush()
    validFile.close()
    invalidFile.flush()
    invalidFile.close()


def export_vin_make(self):
    pass

def export_vin_model(self):
    pass

# cat vinValidation.txt | grep False > invalidVins.txt
# cat vinValidation.txt | grep True > validVins.txt
# python ml.py > vinValidation.txt


if __name__ == "__main__": 
    # print "Hello World"

    #test_output()
    #export_vin(sys.argv[1])


    #data = csv.reader(open('training/AI_VehicleInfo_Joined_Lexus.txt'), delimiter='\t')

    data = pandas.read_csv('validVins.txt', delimiter='\t')

    print data.head()
    print data.describe()
    learn = data[:261673]
    test = data[261673:]

    classifier = DecisionTreeClassifier()
    vectorizer = CountVectorizer()
    # vect_count = CountVectorizer()
    # vect_tfid = TfidfVectorizer()
    # vect_hash = HashingVectorizer()

    count_train = vectorizer.fit(learn)
    bag_of_words = vectorizer.transform(learn)

    print("Every feature:\n{}".format(vectorizer.get_feature_names()))
    print("\nEvery 3rd feature:\n{}".format(vectorizer.get_feature_names()[::3]))
    # classifier.fit(vect_text, learn.v1)
 
