# -*- coding: utf-8 -*-
"""
Created on Wed May 03 21:03:23 2017

@author: Shah Faisal Mazhar
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

test=np.loadtxt("spectrum.txt")

#Cutting the photopeak
cut=[]
for i in range (0,19999):
    if test[i]>35000:
        if test[i]<43000:
            cut=np.append(cut,test[i])

#Graphing the histogram
num_bins = 100
a_range = (min(cut),max(cut))
y_values, bin_edges, _ = plt.hist(cut,bins=num_bins, range=a_range, color= "gray", label="Data")
#_ = plt.xlim(35000,43000)
_ = plt.xlabel('ADC Counts')
_ = plt.ylabel('Counts')


#Inputting the error bar
_ = bincenters = 0.5*(bin_edges[1:]+bin_edges[:-1])
_ = menStd=np.sqrt(y_values)
_ = width = 0.05
_ = plt.ylim(0,130)
_ = plt.bar(bincenters, y_values, width=width, color='r', yerr=menStd, label ="Error",linewidth=1000.0)
_ = plt.suptitle("CsI 137 Photopeak",fontsize=15)


#Fitting the curve
x_values=np.linspace(min(cut),max(cut),100)

def gaus(x,a,x0,sigma):
    return a*np.exp(-(x-x0)**2/(2*sigma**2))

guesses=[1,3.291e04,8.79e2]
popt,pcov = curve_fit(gaus,x_values,y_values,p0=guesses)
mean_err=np.sqrt(popt[1])
#Finding the mean and the standard deviation along with uncertainty
print popt
print mean_err
std_err=np.sqrt(popt[2])
print std_err
#Plotting the fit
plt.plot(x_values,gaus(x_values,*popt),'k+',label='fit')
plt.text(35000, 120, "mu=3.90e+4 +/- 1.97e+2 ADC Counts") 
plt.text(35000,110, "sigma=1.40e+3 +/- 3.75e+1 ADC Counts")
plt.legend()
plt.show()
print popt
