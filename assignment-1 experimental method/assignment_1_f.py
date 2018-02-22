#Keep this .py file with the data file to get the result
import numpy as np
import matplotlib.pyplot as plt
#Loding the file "stopping_powers_xe"
xe=np.loadtxt("stopping_powers_xe.txt")
#Seperating Energy values from the loaded file
x_xe=xe[0:50,0]
#Seperating Stopping powers from the loaded file
y_xe=xe[:,1]
#Seperating Uncertainty values for loaded file
z_xe=xe[0:50,2]
#Plotting the Stopping powers vs Energy for Xe
plt.errorbar(x_xe, y_xe, yerr=z_xe, label="data")
#Putting the "log" scales 
plt.xscale('log')
plt.yscale('log')
#Limiting the y axis from 0 to 1000
plt.ylim([1,1000])
#Adding title and labels of x axis and y axis
plt.suptitle('Stopping Power- Xe')
plt.xlabel('Energy [MeV]')
plt.ylabel("Stopping Power/Density[MeV.cm^2.g^-1]")

#getting the fitting data
y_xe_e=np.array((941.68/x_xe)*(np.log((5.48e-4*x_xe)*(3727.3/(3727.3-(2*x_xe))))-(5.37e-4*x_xe)+7.49))
#Plotting the fit graph
plt.plot(x_xe,y_xe_e,label="Best fit")
#Limiting the y axis from 0 to 1000
plt.ylim([1,1000])
#Adding levels of x axis and y axis
plt.xscale('log')
plt.yscale('log')
#Add legend
plt.legend()
#Save figure
plt.savefig('Xe_1.png')
#Loding the file "stopping_powers_pb"
pb=np.loadtxt("stopping_powers_pb.txt")
#Seperating Energy values from the loaded file
x_pb=pb[0:50,0]
#Seperating Stopping powers values from the loaded file
y_pb=pb[0:50,1]
#Seperating Uncertainty values from the loaded file
z_pb=pb[0:50,2]
#Plotting the Stopping powers vs Energy for Xe
plt.errorbar(x_pb, y_pb, yerr=z_pb,label="Data")
#Putting the "log" scales 
plt.xscale('log')
plt.yscale('log')
#Limiting the y axis from 0 to 1000
plt.ylim([1,1000])
#Adding title and labels of x axis and y axis
plt.suptitle('Stopping Power- Pb')
plt.xlabel('Energy [MeV]')
plt.ylabel("Stopping Power/Densiy[MeV.cm^2.g^-1]")

#getting the fitting data
y_pb_e=np.array((1813.16/x_pb)*(np.log((5.48e-4*x_pb)*(3727.3/(3727.3-(2*x_pb))))-(5.37e-4*x_pb)+7.49))
print(y_pb_e)
#Plotting the fit graph
plt.plot(x_pb,y_pb_e,label="Best fit")
#Limiting the y axis from 0 to 1000
plt.ylim([1,1000])
#Adding levels of x axis and y axis
plt.xscale('log')
plt.yscale('log')
#Add legend
plt.legend()
#Save figure
plt.savefig('Pb_1.png')

