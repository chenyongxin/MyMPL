"""
Set up x and y label.

@author: CHEN Yongxin
"""

import os
from matplotlib import font_manager as fm
from matplotlib import rcParams
import matplotlib.pyplot as plt

def xlabel(ax, text, fontPath=os.path.join(rcParams["datapath"], "fonts/ttf/Helvetica.ttf"),
          fontSize=12, color='k', alpha=1.0, **kwargs):
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
    ax.set_xlabel(text, fontProperties=prop, fontsize=fontSize, color=color, alpha=alpha, **kwargs)

def ylabel(ax, text, fontPath=os.path.join(rcParams["datapath"], "fonts/ttf/Helvetica.ttf"),
          fontSize=12, color='k', alpha=1.0, **kwargs):
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
    ax.set_ylabel(text, fontProperties=prop, fontsize=fontSize, color=color, alpha=alpha, **kwargs)
    
def zlabel(ax, text, fontPath=os.path.join(rcParams["datapath"], "fonts/ttf/Helvetica.ttf"),
          fontSize=12, color='k', alpha=1.0, **kwargs):
    """
    Set zlabel
    
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
    ax.set_zlabel(text, fontProperties=prop, fontsize=fontSize, color=color, alpha=alpha, **kwargs)
    
def title(ax, text, fontPath=os.path.join(rcParams["datapath"], "fonts/ttf/Helvetica.ttf"),
          fontSize=12, color='k', alpha=1.0, **kwargs):
    prop = fm.FontProperties(fname=fontPath)
    ax.set_title(text, fontProperties=prop, color=color, alpha=alpha, fontsize=fontSize, **kwargs)