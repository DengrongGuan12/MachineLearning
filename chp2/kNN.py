__author__ = 'I322233'
from numpy import *
import operator
import matplotlib
import matplotlib.pyplot as plt
def createDataSet():
    group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels = ['A','A','B','B']
    return group, labels
def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    diffMat = tile(inX,(dataSetSize,1)) - dataSet;
    sqDiffMat = diffMat**2
    sqDiffDist = sqDiffMat.sum(axis=1)
    diffDist = sqDiffDist**0.5
    sortedDist = diffDist.argsort()
    classCount = {}
    for i in range(k):
        voteLabel = labels[sortedDist[i]]
        classCount[voteLabel] = classCount.get(voteLabel,0)+1
    sortedClassCount = sorted(classCount.iteritems(),key = operator.itemgetter(1),reverse = True)
    return sortedClassCount[0][0]
def file2matrix(filename):
    fr = open(filename)
    numberOfLines = len(fr.readlines())
    returnMat = zeros((numberOfLines,3))
    classLabelVector = []
    fr = open(filename)
    index = 0
    for line in fr.readlines():
        line = line.strip()
        listFromLine = line.split('\t')
        returnMat[index,:] = listFromLine[0:3]
        classLabelVector.append(int(listFromLine[-1]))
        index+=1
    return returnMat, classLabelVector
def autoNorm(dataSet):
    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)
    ranges = maxVals -minVals
    normalSet = zeros(shape(dataSet))
    m = dataSet.shape[0]
    normalSet = dataSet - tile(minVals,(m,1))
    normalSet = normalSet/(normalSet-tile(ranges,(m,1)))


# group, labels = createDataSet()
# print classify0([0,1],group,labels,2)
mat, classLabelVector = file2matrix("datingTestSet2.txt")
fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(mat[:,1],mat[:,2],15.0*array(classLabelVector),15.0*array(classLabelVector))
plt.show()
# print mat