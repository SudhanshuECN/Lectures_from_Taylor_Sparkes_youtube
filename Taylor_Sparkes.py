# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 20:37:46 2022

@author: Sudhanshu
"""
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size" : 14})

x_data = np.arange(0,101,10)
y_data = x_data**2
noise = np.random.randint(-10,10,11)
y_data = np.add(y_data,noise)

fig = plt.figure(1, figsize = (5,5))
plt.semilogy(x_data,y_data, marker = 'o',markersize = 10, mfc ="white",
         linestyle = '-.', alpha = 0.8, label = '$y = x^2$')
fig = plt.figure(1, figsize = (5,5))

plt.semilogy(x_data,y_data+500, marker = 's',markersize = 10, mfc ="white",
         linestyle = '-.', alpha = 0.8, label = '$y = x^2+500$')
plt.xlabel(' x varibale')
plt.ylabel(' y varibale')
plt.legend(loc = 'lower right' )
plt.show()

# %%
rings  = ({'elves' : 3, 'men' : 9,'dwarves' : 7, 'sauron' : 1})

fig = plt.figure(2, figsize = (5,5))

lists = sorted(rings.items(), key= lambda item : item[1])

x,y = zip(*lists)
# plt.bar(x,y)
# plt.barh(x,y)

explode = (0,0.1,0,0)
plt.pie(y, labels= x, explode = explode)

# %%

x_data = np.arange(0,50,1)
y_data = np.arange(0,50,1)
colors = np.arange(0,50,1)
area = np.random.rand(50)**2*1000

fig = plt.figure(3, figsize = (5,5))
plt.scatter(x_data, y_data, c = colors,s =area,alpha=0.8)

# %%

import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm

N_POINTS = 41
DOMIAN_SIZE = 1.0
N_ITERATIONS = 500
TIME_STEP_LENGTH = 0.001
KINEMATIC_VISCOSITY = 0.1
DENSITY = 1.0
HORIZONTAL_VELOCITY_TOP = 1.0

N_PRESSURE_POISSION_ITERATION = 50

