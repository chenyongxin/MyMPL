"""
An example of customized plot.

@author: CHEN Yongxin
"""

import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(0, 2*np.pi, 200)
y = np.sin(x)

plt.plot(x, y, label='Sin')
plt.legend(frameon=False)


import MyMPL.axis
import MyMPL.label
import MyMPL.legend
ax = plt.gca()
MyMPL.axis.tick_direction(ax, direction='in')
MyMPL.axis.spines(ax)
MyMPL.axis.xytick(ax)
MyMPL.axis.ytick_formatter(ax)
MyMPL.label.xlabel(ax, r"$\Phi$")
MyMPL.label.ylabel(ax, r"Sin($\mathcal{\Phi}$)")
MyMPL.legend.legend(ax, fontsize=12)
