#-------------------------------------------------------------------------
# AUTHOR: Dante Martinez
# FILENAME: Assign2_NaiveBayes.py
# SPECIFICATION: Use Naive Bayes strategy to classify a test set
# FOR: CS 4200- Assignment #2
# TIME SPENT: 35 minutes
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard vectors and arrays

#importing some Python libraries
from sklearn.naive_bayes import GaussianNB
import csv
#reading the training data
#--> add your Python code here
dbTraining = []
with open('weather_training.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for i, row in enumerate(reader):
        if i > 0: #skipping the header
            dbTraining.append (row)
#transform the original training features to numbers and add to the 4D array X. For instance Sunny = 1, Overcast = 2, Rain = 3, so X = [[3, 1, 1, 2], [1, 3, 2, 2], ...]]
#--> add your Python code here
X = []
for j in dbTraining:
    if j[1] == "Sunny":
        a = 1
    elif j[1] == "Overcast":
        a = 2
    elif j[1] == "Rain":
        a = 3
    if j[2] == "Cool":
        b = 1
    elif j[2] == "Mild":
        b = 2
    elif j[2] == "Hot":
        b = 3
    if j[3] == "Normal":
        c = 1
    elif j[3] == "High":
        c = 2
    if j[4] == "Weak":
        d = 1
    elif j[4] == "Strong":
        d = 2
    X.append((a, b, c, d))

#transform the original training classes to numbers and add to the vector Y. For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
#--> add your Python code here
Y = []

for j in dbTraining:
    if j[5] == "No":
        Y.append(1)
    elif j[5] == "Yes":
        Y.append(2)

#fitting the naive bayes to the data
clf = GaussianNB()
clf.fit(X, Y)

#reading the data in a csv file
#--> add your Python code here
dbTest = []
with open('weather_test.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for i, row in enumerate(reader):
        if i > 0: #skipping the header
            dbTest.append (row)
#printing the header os the solution
print ("Day".ljust(15) + "Outlook".ljust(15) + "Temperature".ljust(15) + "Humidity".ljust(15) + "Wind".ljust(15) + "PlayTennis".ljust(15) + "Confidence".ljust(15))

#use your test samples to make probabilistic predictions.
#--> add your Python code here
#-->predicted = clf.predict_proba([[3, 1, 2, 1]])[0]
for k in dbTest:
    if k[1] == "Sunny":
        a = 1
    elif k[1] == "Overcast":
        a = 2
    elif k[1] == "Rain":
        a = 3
    if k[2] == "Cool":
        b = 1
    elif k[2] == "Mild":
        b = 2
    elif k[2] == "Hot":
        b = 3
    if k[3] == "Normal":
        c = 1
    elif k[3] == "High":
        c = 2
    if k[4] == "Weak":
        d = 1
    elif k[4] == "Strong":
        d = 2
    predicted = clf.predict_proba([[a, b, c, d]])[0]
    if predicted[0] >= .75:
        print(str(k[0]).ljust(15) + str(k[1]).ljust(15) + str(k[2]).ljust(15) + str(k[3]).ljust(15) + str(k[4]).ljust(15) + str("No").ljust(15) + str(round(predicted[0], 2)).ljust(15))
    elif predicted[1] >= .75:
        print(str(k[0]).ljust(15) + str(k[1]).ljust(15) + str(k[2]).ljust(15) + str(k[3]).ljust(15) + str(k[4]).ljust(15) + "Yes".ljust(15) + str(round(predicted[1], 2)).ljust(15))

