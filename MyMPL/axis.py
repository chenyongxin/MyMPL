"""
Set up x and y axeses.

@author: CHEN Yongxin
"""

import os
from matplotlib import font_manager as fm
from matplotlib import rcParams
from matplotlib.ticker import FormatStrFormatter

def tick_direction(ax, direction='out'):
    """
    Set up tick direction, with 'out', 'in' and 'inout'.
    """
    ax.tick_params(direction=direction)
    

def xtick(ax, fontPath=os.path.join(rcParams["datapath"], "fonts/ttf/Helvetica.ttf"),
          fontSize=12):
    """
    Set up fonts for x axis ticks 
    
    Parameters
    ----------
    ax: object
        Axes of the figure. Fetched by plt.gca()
    
    fontPath: string
        Full path of font.
        
    fontSize: integer
        Specify font size.
    """
    prop = fm.FontProperties(fname=fontPath)
    ax.set_xticklabels(ax.get_xticks(), fontProperties=prop, size=fontSize)
    
    
def ytick(ax, fontPath=os.path.join(rcParams["datapath"], "fonts/ttf/Helvetica.ttf"),
          fontSize=12):
    """
    Set up fonts for x axis ticks 
    
    Parameters
    ----------
    ax: object
        Axes of the figure. Fetched by plt.gca()
    
    fontPath: string
        Full path of font.
        
    fontSize: integer
        Specify font size.
    """
    prop = fm.FontProperties(fname=fontPath)
    ax.set_yticklabels(ax.get_yticks(), fontProperties=prop, size=fontSize)
    
    
def xytick(ax, fontPath=os.path.join(rcParams["datapath"], "fonts/ttf/Helvetica.ttf"),
          fontSize=12):
    """
    Set up fonts for x and y axis ticks together 
    
    Parameters
    ----------
    ax: object
        Axes of the figure. Fetched by plt.gca()
    
    fontPath: string
        Full path of font.
        
    fontSize: integer
        Specify font size.
    """
    xtick(ax, fontPath=os.path.join(rcParams["datapath"], "fonts/ttf/Helvetica.ttf"),
          fontSize=12)
    ytick(ax, fontPath=os.path.join(rcParams["datapath"], "fonts/ttf/Helvetica.ttf"),
          fontSize=12)
    
    
def xtick_formatter(ax, form='%.2f'):
    """
    Set up x-axis tick formats.
    
    Parameters
    ----------
    ax: object
        Axes of the figure.
    
    form: string
        Decimal or exponential format.
    """
    ax.xaxis.set_major_formatter(FormatStrFormatter(form))
    
    
def ytick_formatter(ax, form='%.2f'):
    """
    Set up y-axis tick formats.
    
    Parameters
    ----------
    ax: object
        Axes of the figure.
    
    form: string
        Decimal or exponential format.
    """
    ax.yaxis.set_major_formatter(FormatStrFormatter(form))

def spines(ax, visible={'left', 'bottom'}):
    """
    Set up visibility of axis.
    
    Parameters
    ----------
    ax: object
        Axes of the figure.
    
    visible: set
        Set of string which denotes visible. e.g. visible = {'left', 'bottom'}
    """
    full = {'left', 'right', 'bottom', 'top'}
    invisible = full - visible
    
    # Hide the invisible ones
    for i in invisible:
        ax.spines[i].set_visible(False)
    
    
    


    