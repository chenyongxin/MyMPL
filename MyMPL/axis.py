"""
Set up x and y axeses.

@author: CHEN Yongxin
"""

import os
from matplotlib import font_manager as fm
from matplotlib import rcParams
from matplotlib.ticker import FormatStrFormatter

def tick_direction(ax, direction='out', which='both'):
    """
    Set up tick direction
    
    Parameters
    ----------
    ax: object
        Axes of the figure. Fetched by plt.gca()

    direction: string, optional
	Direction of ticks with 'out', 'in' and 'inout'.

    which: string, optional
    	Which tick is specified with 'both', 'major' and 'minor'.
    """
    ax.tick_params(which='both', direction=direction)
    

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
    prop = fm.FontProperties(fname=fontPath, size=fontSize)
    #ax.set_xticklabels(ax.get_xticks(), fontProperties=prop)              # this option replaces the location of ticks with number
    for label in ax.get_xticklabels(): label.set_fontproperties(prop)      # this option modify the tick object with properties
    
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
    prop = fm.FontProperties(fname=fontPath, size=fontSize)
    for label in ax.get_yticklabels(): label.set_fontproperties(prop)
    
def ztick(ax, fontPath=os.path.join(rcParams["datapath"], "fonts/ttf/Helvetica.ttf"),
          fontSize=12):
    """
    Set up fonts for z axis ticks 
    
    Parameters
    ----------
    ax: object
        Axes of the figure. Fetched by plt.gca()
    
    fontPath: string
        Full path of font.
        
    fontSize: integer
        Specify font size.
    """
    prop = fm.FontProperties(fname=fontPath, size=fontSize)
    for label in ax.get_zticklabels(): label.set_fontproperties(prop)
    
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
    xtick(ax, fontPath=fontPath, fontSize=fontSize)
    ytick(ax, fontPath=fontPath, fontSize=fontSize)
    
def xyztick(ax, fontPath=os.path.join(rcParams["datapath"], "fonts/ttf/Helvetica.ttf"),
          fontSize=12):
    """
    Set up fonts for x, y and z axis ticks together 
    
    Parameters
    ----------
    ax: object
        Axes of the figure. Fetched by plt.gca()
    
    fontPath: string
        Full path of font.
        
    fontSize: integer
        Specify font size.
    """
    xytick(ax, fontPath=fontPath, fontSize=fontSize)
    ztick(ax, fontPath=fontPath, fontSize=fontSize)
    
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
    
def ztick_formatter(ax, form='%.2f'):
    """
    Set up z-axis tick formats.
    
    Parameters
    ----------
    ax: object
        Axes of the figure.
    
    form: string
        Decimal or exponential format.
    """
    ax.zaxis.set_major_formatter(FormatStrFormatter(form))

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
    
    
    


    
