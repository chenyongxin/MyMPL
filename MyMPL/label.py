"""
Set up x and y label.

@author: CHEN Yongxin
"""

import os
from matplotlib import font_manager as fm
from matplotlib import rcParams

def xlabel(ax, text, fontPath=os.path.join(rcParams["datapath"], "fonts/ttf/Helvetica.ttf"),
          fontSize=12):
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
    """
    prop = fm.FontProperties(fname=fontPath)
    ax.set_xlabel(text, fontProperties=prop, fontsize=fontSize)

def ylabel(ax, text, fontPath=os.path.join(rcParams["datapath"], "fonts/ttf/Helvetica.ttf"),
          fontSize=12):
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
    """
    prop = fm.FontProperties(fname=fontPath)
    ax.set_ylabel(text, fontProperties=prop, fontsize=fontSize)