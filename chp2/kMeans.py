__author__ = 'I322233'
from numpy import *
import time
import matplotlib.pyplot as plt

def euclDistance(vector1,vector2):
    return sqrt(sum(power(vector1-vector2,2)))
# init centroids with random samples
def initCentroids(dataSet, k):
    # dataSet 为 numSamples 行,dim 列的矩阵
    numSamples, dim = dataSet.shape
    # k行 dim列的矩阵
    centroids = zeros((k, dim))

    for i in range(k):
        # random.uniform >=0 <=numSamples的随机浮点数
        index = int(random.uniform(0, numSamples))
        #随机从dateset中选一个点
        centroids[i, :] = dataSet[index, :]
    return centroids
# k-means cluster
def kmeans(dataSet, k):

    ## 读取矩阵的长度 shape[0]表示第一维的长度
    numSamples = dataSet.shape[0]
    # first column stores which cluster this sample belongs to,
    # second column stores the error between this sample and its centroid
    # numSamples 行,2列 的0 矩阵, 记录每个点最近的中心点的index及距离的平方
    clusterAssment = mat(zeros((numSamples, 2)))
    clusterChanged = True

    ## step 1: init centroids
    centroids = initCentroids(dataSet, k)

    while clusterChanged:
        clusterChanged = False
        ## for each sample
        #xrange 生成一个对象，性能比range高，range生成的是一个list,在数量较大时尽量使用xrange
        for i in xrange(numSamples):
            minDist  = 100000.0
            minIndex = 0
            ## for each centroid
            ## step 2: find the centroid who is closest
            for j in range(k):
                distance = euclDistance(centroids[j, :], dataSet[i, :])
                if distance < minDist:
                    minDist  = distance
                    minIndex = j

            ## step 3: update its cluster
            if clusterAssment[i, 0] != minIndex:
                clusterChanged = True
                clusterAssment[i, :] = minIndex, minDist**2

        ## step 4: update centroids,更新k个中心点，根据每个中心点的集群，取集群内所有点的x,y坐标的平均
        for j in range(k):
            pointsInCluster = dataSet[nonzero(clusterAssment[:, 0].A == j)[0]]
            centroids[j, :] = mean(pointsInCluster, axis = 0)

    print 'Congratulations, cluster complete!'
    return centroids, clusterAssment

# show your cluster only available with 2-D data
def showCluster(dataSet, k, centroids, clusterAssment):
    numSamples, dim = dataSet.shape
    if dim != 2:
        print "Sorry! I can not draw because the dimension of your data is not 2!"
        return 1

    mark = ['or', 'ob', 'og', 'ok', '^r', '+r', 'sr', 'dr', '<r', 'pr']
    if k > len(mark):
        print "Sorry! Your k is too large! please contact Zouxy"
        return 1

    # draw all samples
    for i in xrange(numSamples):
        markIndex = int(clusterAssment[i, 0])
        plt.plot(dataSet[i, 0], dataSet[i, 1], mark[markIndex])

    mark = ['Dr', 'Db', 'Dg', 'Dk', '^b', '+b', 'sb', 'db', '<b', 'pb']
    # draw the centroids
    for i in range(k):
        plt.plot(centroids[i, 0], centroids[i, 1], mark[i], markersize = 12)

    plt.show()
