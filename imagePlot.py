#!/usr/bin/env python
# coding: utf-8

# # Making an Example Image Plot

# In[1]:


import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm


# In[4]:


fig = plt.figure(figsize = (7,7))
ax = fig.add_subplot(111)
x = np.linspace(0, 1 * np.pi, 200)
y = np.linspace(0, 2 * np.pi, 200)
x,y = np.meshgrid(x,y)
z = -np.sin(x) * np.sin(y)
ax = plt.imshow(z, cmap=cm.turbo, origin = "lower")
cbar = fig.colorbar(ax)
cbar.ax.get_yaxis().labelpad = 15
cbar.ax.set_ylabel("Z Value", rotation = 270)
plt.xlabel("X Label")
plt.ylabel("Y Label")
plt.savefig("imagePlot.png", bbox_inches = "tight", facecolor = "white")


# In[ ]:




