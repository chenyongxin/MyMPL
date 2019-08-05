"""
An example of customized plot.

@author: CHEN Yongxin
"""

import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(0, 2*np.pi, 200)
y = np.sin(x)
y2 = np.sin(x+np.pi/6)
y3 = np.sin(x+np.pi/3)


plt.plot(x, y,  label=r"sin($\mathcal{\phi}$)")
plt.plot(x, y2, 'k', label=r"sin($\mathcal{\phi+\pi/6}$)")
plt.plot(x, y3, 'k', alpha=0.3, label=r"sin($\mathcal{\phi+\pi/3}$)")
plt.legend(frameon=False)


import MyMPL.axis
import MyMPL.label
import MyMPL.legend
ax = plt.gca()
MyMPL.axis.tick_direction(ax, direction='in')
MyMPL.axis.spines(ax)
MyMPL.axis.xytick(ax, fontSize=12)
MyMPL.axis.ytick_formatter(ax)
MyMPL.label.xlabel(ax, r"$\mathcal{\phi}$", fontSize=12)
MyMPL.label.ylabel(ax, r"Sin($\mathcal{\phi}$)", fontSize=12)
MyMPL.legend.legend(ax, fontsize=12)
