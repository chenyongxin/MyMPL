"""
Set up legend.

@author: CHEN Yongxin
"""

import os
from matplotlib import font_manager as fm
from matplotlib import rcParams

def legend(ax, location='best', frameon=False, fontsize=12, 
           fontPath=os.path.join(rcParams["datapath"], "fonts/ttf/Helvetica.ttf")):
    """
    Set legend properties
    
    Parameters
    ----------
    ax: object
        Axes of the figure. Fetched by plt.gca()
    """
    prop = fm.FontProperties(fname=fontPath, size=fontsize)
    ax.legend(loc=location, frameon=frameon, prop=prop)
