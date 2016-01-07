__author__ = 'I322233'
from numpy import *
import operator
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
group, labels = createDataSet()
print classify0([0,1],group,labels,2)