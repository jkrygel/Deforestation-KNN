# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 13:21:17 2019

@author: Julian
"""

import math

class Knn(object):
    
    def __init__(self, k=3):
        self.k = k
    
    def DistEuclid(self,x1,x2):
        s = 0.0
        for i in range(len(x1)):
            s += math.sqrt((float([x1]) - float([x2])) ** 2)
            return s
    
    def fit(self,x,y):
        self.x = x
        self.y = y
    
    def predict(self,test):
        dist = []
        for i in range(len(self.x)):
            dist.append(self.DistEuclid(self.x[i],test))
        result = []
        for i in range(len(self.k)):
            result.append(self.y[dist.index(min(dist))])
            dist.pop(dist.index(min(dist)))
        return max(set(result), key=result.count)