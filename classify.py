# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 12:42:49 2019

@author: Julian
"""

import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from Knn import Knn
from img.data import x,y

def main():
    knn = Knn(7)
    
    knn.fit(x,y)
    
    img = mpimg.imread(sys.argv[1])
    
    for j in range(img.shape[0]/50+1):
        for i in range(img.shape[1]/50+1):
            h, b = np.histogram(img[j*50:(j*50)+50,i*50:(i*50)+50])
            if (knn.predict(h) == 1):
                img[j*50:(j*50)+50,i*50:(i*50)+50,1] = 0
        
    plt.imshow(img)
    plt.show()

if __name__ == "__main__":
    
    if len(sys.argv) < 2:
        print("Enter image path")
        exit()
    
    main()