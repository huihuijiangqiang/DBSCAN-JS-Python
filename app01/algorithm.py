#-*- coding:utf-8 -*-
# @Author : storm eason
# @Time : 2020/11/13 9:24
from sklearn import datasets
from sklearn.datasets import make_moons
import numpy as np
import random
import matplotlib.pyplot as plt
import time
import copy


# def loadDataSet(fileName, splitChar='\t'):
#     dataSet = []
#     with open(fileName) as fr:
#         for line in fr.readlines():
#             curline = line.strip().split(splitChar)
#             fltline = list(map(float, curline))
#             dataSet.append(fltline)
#     return dataSet

def find_neighbor(j, x, eps):
    N = list()  #
    for i in range(x.shape[0]):
        temp = np.sqrt(np.sum(np.square(x[j] - x[i])))  # 计算欧式距离
        if temp <= eps:
            N.append(i)
    return set(N)


def DBSCAN(X, eps, min_Pts):
    k = -1
    neighbor_list = []  # 用来保存每个数据的邻域
    omega_list = []  # 核心对象集合
    gama = set([x for x in range(len(X))])  # 初始时将所有点标记为未访问
    cluster = [-1 for _ in range(len(X))]  # 聚类
    for i in range(len(X)):
        neighbor_list.append(find_neighbor(i, X, eps))  #传入每一个i和整个集合X，其半径范围eps，将find_neighbor中得到的数据集加入到 neighbor_list来确定邻域
        if len(neighbor_list[-1]) >= min_Pts:       # 从 -1开始计算（本程序所有都是从-1开始）若其范围内集合个数（即长度）大于min_pts
            omega_list.append(i)  # 将样本加入核心对象集合
    print(len(neighbor_list))
    print(len(omega_list))
    omega_list = set(omega_list)  # 转化为集合便于操作
    while len(omega_list) > 0:      # 在核心对象集合不为空时
        gama_old = copy.deepcopy(gama)  #深复制，即将被复制对象完全再复制一遍作为独立的新个体单独存在。所以改变原有被复制对象不会对已经复制出来的新对象产生影响。
        j = random.choice(list(omega_list))  # 随机选取一个核心对象

        Q = list()
        Q.append(j) #将随机选出的核心对象j加入到Q集合中
        gama.remove(j)  #将其从初始的点中删除
        while len(Q) > 0:   #当q的长度大于零时
            q = Q[0]    #取出其首个样本来
            Q.remove(q)
            if len(neighbor_list[q]) >= min_Pts:    #如果这个样本其邻域大于min_Pts
                delta = neighbor_list[q] & gama     #若其仍然在未访问的样本中存在
                # print(delta)
                deltalist = list(delta)             #将所有的都放入到一个集合中
                for i in range(len(delta)):
                    Q.append(deltalist[i])
                    gama = gama - delta

        Ck = gama_old - gama        #原来的减去已经是密度相邻的
        Cklist = list(Ck)
        k = k + 1
        for i in range(len(Ck)):        #得到已经聚合为一类的某一个类  在所有的都没有完成之间对k+1在进行聚类
            cluster[Cklist[i]] = k
        omega_list = omega_list - Ck
    return cluster
X1, y1 = make_moons(n_samples=100, noise=0.1)
X2, y2 = make_moons(n_samples=100, noise=0.1)
X = np.concatenate((X1,X2))
y = np.concatenate((y1,y2))
# plt.show()

# X1, y1 = datasets.make_circles(n_samples=2000, factor=.6, noise=.02)
# X2, y2 = datasets.make_blobs(n_samples=400, n_features=2, centers=[[1.2, 1.2]], cluster_std=[[.1]], random_state=9)
X = np.concatenate((X1, X2))
# dataSet = loadDataSet('1.txt', splitChar=',')
eps = 0.2
min_Pts = 4
# begin = time.time()
C = DBSCAN(X, eps, min_Pts)
# # end = time.time()
plt.figure()

plt.scatter(X[:, 0], X[:, 1], c=C)
plt.show()
