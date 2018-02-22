# -*- coding: utf-8 -*-
"""
Created on Tue May 02 17:19:49 2017

@author: Shah Faisal Mazhar
"""
#Keep this .py file with the data file to get the result
import matplotlib.pyplot as plt
import numpy as np
#Loading the 1003rd waveform
waveform=np.loadtxt("1003.txt")
#Plotting the waveform 
plt.plot(waveform)
#Ploting the integration window
plt.axvline(x=0.0, color="k", label = "Integration window")
plt.axvline(x=2000, color="k")
#Labeling
plt.suptitle("Waveform 1003")
plt.xlabel("ADC Samples")
plt.ylabel("ADC Counts")
#Limiting x-axis and y-axis
plt.xlim([-100,4500])
plt.ylim([2175,2220])
plt.legend()
plt.show()