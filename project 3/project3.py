# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 18:24:15 2017

@author: pat
"""
#imports
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

#setting pyplot style
matplotlib.style.use('ggplot')

#importing data
try:
    file = np.loadtxt('data/trades.txt')
  
except:
    print('Could not find data to import')
    raise
    
#math
bchan=(file[:,2]-file[:,1])*file[:,3]

#scatter plot
#creates a scatter plot using the length of the data and the cumulative sum of the balance change
plt.scatter(range(len(file)), bchan.cumsum(),c=bchan,cmap=plt.cm.autumn)
plt.plot(range(len(file)), bchan.cumsum())
plt.title('Account')
plt.xlabel('Day')
plt.ylabel('Balance')
plt.colorbar()
plt.savefig('data/scatter.png',dpi=200)
plt.close()

#pie
wedges=['Positive','Negitive','Zero']
plt.title('Results')
#counts how many positive numbers, negitive numbers and zeros there are
p = len(np.where(bchan>0)[0])
n = len(np.where(bchan<0)[0])
z = len(np.where(bchan==0)[0])
plt.pie([p,n,z], labels=wedges)
plt.savefig('data/pie.png',dpi=200)
plt.close()

#Hist
plt.hist(bchan,bins=25)
plt.title('Distribution')
plt.xlabel('Gains and Losses')
plt.ylabel('Gains and Losses #')
plt.savefig('data/hist.png',dpi=200)
plt.close()

