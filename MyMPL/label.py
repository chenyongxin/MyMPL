"""
Set up x and y label.

@author: CHEN Yongxin
"""

import os
from matplotlib import font_manager as fm
from matplotlib import rcParams

def xlabel(ax, text, fontPath=os.path.join(rcParams["datapath"], "fonts/ttf/Helvetica.ttf"),
          fontSize=12, color='k', alpha=1.0):
    """
    Set xlabel
    
    Parameters
    ----------
    ax: object
        Axes of the figure. Fetched by plt.gca()
    
    text: string
        Text of x-axis label.    
    
    fontPath: string
        Full path of font.
        
    fontSize: integer
        Specify font size.

    color: string
	Color of label. Black is the defalut.

    alpha: float
	Transparency of label. 1 is default.
    """
    prop = fm.FontProperties(fname=fontPath)
    ax.set_xlabel(text, fontProperties=prop, fontsize=fontSize, color=color, alpha=alpha)

def ylabel(ax, text, fontPath=os.path.join(rcParams["datapath"], "fonts/ttf/Helvetica.ttf"),
          fontSize=12, color='k', alpha=1.0):
    """
    Set ylabel
    
    Parameters
    ----------
    ax: object
        Axes of the figure. Fetched by plt.gca()
    
    text: string
        Text of x-axis label.    
    
    fontPath: string
        Full path of font.
        
    fontSize: integer
        Specify font size.

    color: string
	Color of label. Black is the defalut.

    alpha: float
	Transparency of label. 1 is default.
    """
    prop = fm.FontProperties(fname=fontPath)
    ax.set_ylabel(text, fontProperties=prop, fontsize=fontSize, color=color, alpha=alpha)
