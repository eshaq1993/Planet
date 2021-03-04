from random import seed
from math import sqrt
from random import randrange
import csv
from csv import reader
import pandas as pd 
from collections import defaultdict

from knn import k_nearest_neighbors, predict_classification, eucliden_distance, sorted_neighbors

def test_eucliden_distance(row1,row2):
    euclidean_distance = euclidean_distance(row1, row2)
    distance = np.linalg.norm(row2 - row1)
    assert math.isclose(euclidean_distance, distance), "if it returning unexpected distance"
    return 
                            

def test_predict_classification():
    train = [[3,9,2], [1,4,1]]
    test = [1,2,1]
    num_neighbors =1
    result = predict_classification(train, test, neighbors_num)
    assert result == 2, "Unexpected Result"
    return


def test_k_nearest_neighbors():
    data = pd.read_csv("atomradii.csv")
    data.drop('Atom', inplace=True ,axis=1)
    data['Type'] = data['Type'].map({'PT':0 , 'TM': 1 , "Alk": 2})
    dataset = data.reset_index(drop =True)
    dataset = dataset.values.tolist()
    if not isinstance(dataset, list):
        raise TypeError("Expected input is not of type List")
    return

def test_sorted_neighbors():
    train = [[1,0,1], [0,1,2]]
    test = [0,0,2]
    num_neighbors = 1
    result = get_neighbors(train, test, num_neighbors)
    assert result == [([1, 0, 1], 1.0), ([0, 1, 2], 1.0)], "Unexpected Result"
    return


     
