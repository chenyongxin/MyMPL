"""
Example of making contour plot

@author: CHEN Yongxin
"""

import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 2*np.pi, 100)
y = x.copy()
xx, yy = np.meshgrid(x, y, indexing='ij')
zz = np.sin(xx*yy)
draw = plt.contourf(xx, yy, zz, 100, cmap='bwr')



import MyMPL.axis
import MyMPL.label
import MyMPL.legend
import MyMPL.colorbar
ax = plt.gca()
MyMPL.axis.tick_direction(ax, direction='in')
MyMPL.axis.spines(ax)
MyMPL.axis.xytick(ax, fontSize=12)
MyMPL.axis.xtick_formatter(ax, form='%.0f')
MyMPL.axis.ytick_formatter(ax, form='%.0f')
MyMPL.label.xlabel(ax, r"$\mathbf{x}$", fontSize=12)
MyMPL.label.ylabel(ax, r"$\mathbf{y}$", fontSize=12)
cbar = ax.figure.colorbar(draw, orientation='horizontal', ticks=[-1,-0.5,0,0.5,1], shrink=0.8)
#cbar.ax.set_xticklabels(['a','b','c','d','e'])     # modify the names if needed
MyMPL.colorbar.horizontal(cbar, fontSize=12, direction='in')
MyMPL.colorbar.label(cbar, r'sin($\mathit{xy}$)')
