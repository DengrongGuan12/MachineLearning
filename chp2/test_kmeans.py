__author__ = 'I322233'
from numpy import *
import time
import matplotlib.pyplot as plt
import kMeans as km

## step 1: load data
print "step 1: load data..."
dataSet = []
## read file
fileIn = open('kmeans_test_set.txt')
for line in fileIn.readlines():
    lineArr = line.strip().split(' ')
    dataSet.append([float(lineArr[0]), float(lineArr[1])])

## step 2: clustering...
print "step 2: clustering..."

## change array to matrix
dataSet = mat(dataSet)
k = 4
centroids, clusterAssment = km.kmeans(dataSet, k)

## step 3: show the result
print "step 3: show the result..."
km.showCluster(dataSet, k, centroids, clusterAssment)