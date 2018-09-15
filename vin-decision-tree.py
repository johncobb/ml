
import sklearn
from sklearn import tree
from collections import Count

# features
numeric = 0
alpha_num = 1
len_17 = 2
checksum = 3

# labels
vin = 0
year = 1
make = 2
model = 3
age = 4
# imput to the classifier
#features = [[17, alpha_num, checksum], [17, alpha_num, checksum], [17, alpha_num, checksum]]

features = [[17, alpha_num, checksum], 
            [4, numeric, 0], 
            [5, alpha_num, 0]]

# output we want
# vin, year, model
labels = [0, 1, 3]


clf = tree.DecisionTreeClassifier()

# find patterns in training data
# FIT synonym for finding patterns in data
clf = clf.fit(features, labels)

# predict outcome
# length, is_alphanumeric, valid_checksum
print clf.predict([[17, alpha_num, checksum]])
print clf.predict([[4, numeric, 0]])
print clf.predict([[2, alpha_num, 0]])




