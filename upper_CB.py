# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 01:13:00 2017

@author: ARSHABH SEMWAL
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from math import sqrt , log

dataset  = pd.read_csv('Ads_CTR_Optimisation.csv')

# implementing UCB
N=10000
d=10
ads_selected = []
numbers_of_selection = [0]*d
sums_of_reward=[0]*d
total_reward=0
for n in range(0,N):
    ad=0
    maximum_ucb=0
    for i in range(0,d):
        if( numbers_of_selection[i]>0):
            averages_of_reward = sums_of_reward[i]/numbers_of_selection[i]
            delta_ucb = math.sqrt(3/2 * math.log(n + 1) / numbers_of_selection[i])
            ucb = averages_of_reward + delta_ucb
        else:
            ucb = 1e400
        if ucb>maximum_ucb:
            maximum_ucb = ucb
            ad=i 
    ads_selected.append(ad)            
    numbers_of_selection[ad] +=1
    sums_of_reward[ad] =sums_of_reward[ad] + dataset.values[n,ad]
    total_reward+=dataset.values[n,ad] 


# Visualising the results
plt.hist(ads_selected)
plt.title('Histogram of ads selections')
plt.xlabel('Ads')
plt.ylabel('Number of times each ad was selected')
plt.show()