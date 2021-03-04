from math import sqrt
from random import seed
from random import randrange
import csv
import pandas as pd 
import collections
from csv import reader



"""
A wrapping function that is the primary way of interacting with your code. It takes as parameters, a training dataframe, 
a value of k and some input data to be classified. It returns the classification for the input data
"""

def k_nearest_neighbors(train, test, neighbors_num):
    predictions = list()
    for row in test:
        output = predict_classification(train, row, neighbors_num)
        predictions.append(output)
    return(predictions)




"""
A function that returns the Euclidean distance between a row in the intput data to be classified.
"""
def predict_classification(train, test_row, neighbors_num):
    neighbors = sorted_neighbors(train, test_row, neighbors_num)
    
    resulted_values = [row[0][-1] for row in neighbors[0:neighbors_num]]

    prediction = max(set(resulted_values), key=resulted_values.count)
    return prediction





"""
A function that returns the list of sorted Euclidean distances between the input data and all rows in the dataframe.
"""
def sorted_neighbors(train, test_row, neighbors_num):
    distance = list()
    for train_row in train:
        dist = eucliden_distance(test_row, train_row)
        distance.append((train_row, dist))
        distance.sort(key=lambda tup: tup[1])
#         print("This is the current distance:", distances)
    return distance


# In[9]:


"""
A function that returns the class prediction based on the list of sorted Euclidean distances
"""
def eucliden_distance(row1, row2):
    distance = 0.0
    for i in range(len(row1)-1):
        distance += (row1[i] - row2[i])**2
    return sqrt(distance)



"""
A wrapping function that helps the user decide on what k to use.
This function takes as parameters, a training dataframe, a testing dataframe and a list of values of k to try. 
It returns a dictionary with k as the keys and the training accuracy of the test set. 
Accuracy is measured by percentage of classifications that were correct for that value of k.
"""
def find_optimum_k(train, test, k_value_set): 
    accuracy_storage = collections.defaultdict()

    for k in k_value_set: 
        predicted_results = k_nearest_neighbors(train, test, k)
        total_measurement = len(predicted_results)
   

        expected_results = [] 
        for each_set in test:
            expected_results.append(each_set[2])

        correct_measurement = 0 
        for i in range(len(predicted_results)): 
            if predicted_results[i] == expected_results[i]: 
                correct_measurement += 1 
        total_accuracy = correct_measurement/total_measurement 
        accuracy_storage[k] = total_accuracy 
        

    inverse = [(value, key) for key, value in accuracy_storage.items()]
    print(max(inverse)[1])