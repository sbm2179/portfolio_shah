# -*- coding: utf-8 -*-
"""
Created on Wed May 03 15:30:29 2017

@author: Shah Faisal Mazhar
"""
#Keep this .py file with the data file to get the result
import numpy as np
#creating an empty array for integration data
a=[]
#Loop to load each of the files
for j in range (1,20000):
    x=np.loadtxt(str(j)+".txt")
#Calculating Base
    y=[]
    for i in range (0,4096):
        for x[i] in range (2174,2181):
            y=np.append(y,x[i])
    base=np.mean(y)
#Calculating integration
    x2=np.loadtxt(str(j)+".txt")
    inte=np.sum(x2-base)
    a=np.append(a,inte)
#Saving the spectrum text file
np.savetxt('spectrum.txt', a)