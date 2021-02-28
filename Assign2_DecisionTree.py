#-------------------------------------------------------------------------
# AUTHOR: Dante Martinez
# FILENAME: Assign2_DecisionTree.py
# SPECIFICATION: Create 3 decision trees using different training data and test their accuracy with a test set
# FOR: CS 4200- Assignment #2
# TIME SPENT: 20 minutes
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard vectors and arrays

#importing some Python libraries
from sklearn import tree
import csv

dataSets = ['contact_lens_training_1.csv', 'contact_lens_training_2.csv', 'contact_lens_training_3.csv']

for ds in dataSets:

    dbTraining = []
    X = []
    Y = []

    #reading the training data in a csv file
    with open(ds, 'r') as csvfile:
         reader = csv.reader(csvfile)
         for i, row in enumerate(reader):
             if i > 0: #skipping the header
                dbTraining.append (row)

    #transform the original training features to numbers and add to the 4D array X. For instance Young = 1, Prepresbyopic = 2, Presbyopic = 3, so X = [[1, 1, 1, 1], [2, 2, 2, 2], ...]]
    #--> add your Python code here
    # X =
    for j in dbTraining:
        #print(j)
        if j[0] == "Young":
            a = 1
        elif j[0] == "Presbyopic":
            a = 2
        elif j[0] == "Prepresbyopic":
            a = 3
        if j[1] == "Myope":
            b = 1
        elif j[1] == "Hypermetrope":
            b = 2
        if j[2] == "Yes":
            c = 1
        elif j[2] == "No":
            c = 2
        if j[3] == "Normal":
            d = 1
        elif j[3] == "Reduced":
            d = 2
        X.append((a, b, c, d))

    #transform the original training classes to numbers and add to the vector Y. For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
    #--> add your Python code here
    # Y =
    for j in dbTraining:
        if j[4] == "Yes":
            Y.append(1)
        elif j[4] == "No":
            Y.append(2)
    #loop your training and test tasks 10 times here
    accuracy = []
    for i in range (10):

        #fitting the decision tree to the data setting max_depth=3
        clf = tree.DecisionTreeClassifier(criterion = 'entropy', max_depth=3)
        clf = clf.fit(X, Y)

        #read the test data and add this data to dbTest
        #--> add your Python code here
        dbTest = []
        with open('contact_lens_test.csv', 'r') as csvfile:
           reader = csv.reader(csvfile)
           for l, row in enumerate(reader):
               if l > 0:  # skipping the header
                   dbTest.append(row)
        TrueCounter = 0
        counter = 0
        for data in dbTest:
            #transform the features of the test instances to numbers following the same strategy done during training, and then use the decision tree to make the class prediction. For instance:
            #class_predicted = clf.predict([[3, 1, 2, 1]])[0]           -> [0] is used to get an integer as the predicted class label so that you can compare it with the true label
            #--> add your Python code here
            #print(data)
            if data[0] == "Young":
                a = 1
            elif data[0] == "Presbyopic":
                a = 2
            elif data[0] == "Prepresbyopic":
                a = 3
            if data[1] == "Myope":
                b = 1
            elif data[1] == "Hypermetrope":
                b = 2
            if data[2] == "Yes":
                c = 1
            elif data[2] == "No":
                c = 2
            if data[3] == "Normal":
                d = 1
            elif data[3] == "Reduced":
                d = 2
            class_predicted = clf.predict([[a, b, c, d]])[0]
            #compare the prediction with the true label (located at data[4]) of the test instance to start calculating the accuracy.
            #--> add your Python code here
            if data[4] == "Yes":
                value = 1
            elif data[4] == "No":
                value = 2
            if class_predicted == value:
                TrueCounter = TrueCounter+1
            counter = counter+1
        accuracy.append(TrueCounter/counter)
        #find the lowest accuracy of this model during the 10 runs (training and test set)
        #--> add your Python code here
    leastError = 2
    for k in accuracy:
        if leastError > k:
            leastError = k
    #print the lowest accuracy of this model during the 10 runs (training and test set).
    #your output should be something like that:
         #final accuracy when training on contact_lens_training_1.csv: 0.2
         #final accuracy when training on contact_lens_training_2.csv: 0.3
         #final accuracy when training on contact_lens_training_3.csv: 0.4
    #--> add your Python code here
    print('final accuracy when training on', ds, ':', leastError)



